from concurrent import futures
from typing import Tuple

import grpc
import client_streaming_pb2
import client_streaming_pb2_grpc

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import queue


class VisualizeApp:
    def __init__(self):
        self.tasks = []
        self.server = self.setup_grpc()
        self.data_queue = queue.Queue(maxsize=100)
        self.time_index_from_queue = 0.0
        colors_ = ['r', 'g', 'y', 'k', 'b', 'c', 'pink', 'purple', 'brown', 'gray', 'm']
        self.speaker_id_data = np.zeros((11, 1))
        self.time_data = [self.time_index_from_queue]
        # self.speaker_id_scores_list_from_queue = []
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlabel('Time (in seconds)')
        self.ax.set_ylabel('Most Active Speaker Scores')
        self.ax.set_ylim(0.0, 1.1)
        self.ax.title.set_text('Active Speakers using Multi-Threading')
        line, = self.ax.plot([], [], lw=2)
        self.scores = np.zeros((11, 1))  # UNK speaker + 10 speakers
        self.map_speaker_id_to_speaker_num = {-1: 0, 0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10,
                                              10: 11}
        self.lines_object = []
        for i in range(self.speaker_id_data.shape[0]):
            lobj = self.ax.plot([], [], '--', lw=2, color=colors_[i])[0]
            # self.lines_object.append(self.ax.plot(self.time_data, self.speaker_id_data[i], '--', color=colors_[i])[0])
            self.lines_object.append(lobj)
        self.anim = FuncAnimation(self.fig, func=self.update, frames=self.run, interval=0.05)

    def setup_grpc(self):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        return server

    def run(self):
        while True:
            if not self.data_queue.empty():
                item = self.data_queue.get()
                print('*********************************************************************************: ')
                self.time_index_from_queue = float(item.data.timestamp)
                # logging.debug('Getting ' + str(item) + ' : ' + str(self.data_queue.qsize()) + ' items in queue')
                self.scores = np.zeros((11, 1))
                # for r in item['1']:
                speaker_name = int(item.data.speaker_name.split('_')[1])
                mapped_spkr_name = self.map_speaker_id_to_speaker_num[speaker_name]
                self.scores[mapped_spkr_name] = float(item.data.speaker_score)
                print('------------------------------SCORES-----------------------', self.scores)
                yield self.time_index_from_queue, self.scores

    def update(self, frame: Tuple):
        timestamp = frame[0]

        self.ax.set_xlim(timestamp - 10, timestamp)
        n_time_indices = (timestamp - self.time_data[-1]) * 100
        for i in range(int(n_time_indices) - 1):
            self.time_data.append(self.time_data[-1] + 0.01)  # increment time at frame rate of 10 milliseconds
            self.speaker_id_data = np.append(self.speaker_id_data, frame[1], axis=1)

        self.time_data.append(timestamp)
        self.speaker_id_data = np.append(self.speaker_id_data, frame[1], axis=1)
        self.time_data = self.time_data[-1000:]
        self.speaker_id_data = self.speaker_id_data[:, -1000:]
        for lnum, line in enumerate(self.lines_object):
            line.set_data(self.time_data, self.speaker_id_data[lnum])
            if lnum == 0:
                line.set_label('speaker %s' % 'UNK')
            if lnum > 0:
                line.set_label('speaker %s' % (lnum - 1))
        legend = plt.legend()

    def StreamData(self, request_iterator, context):
        for request in request_iterator:
            tuple_data = request.queues
            self.data_queue.put(tuple_data)
        return client_streaming_pb2.SendResponse(message='Data added to queue')


if __name__ == "__main__":
    app = VisualizeApp()
    client_streaming_pb2_grpc.add_SendDataServicer_to_server(app, app.server)
    app.server.add_insecure_port('[::]:50051')
    app.server.start()
    plt.show()
