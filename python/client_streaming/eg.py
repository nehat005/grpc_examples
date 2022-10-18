import os
import sys
import time

import grpc
import logging
import argparse
import client_streaming_pb2
import client_streaming_pb2_grpc
import queue

import_root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
sys.path.insert(0, import_root_path)

from scripts.diarizer import grpc_diarizer

sys.path.remove(import_root_path)


class SendData:
    """
    Producer class in a separate thread for real-time diarization.
    """

    def __init__(self, audio_source, diarizer):
        super(SendData, self).__init__()
        self.diarizer = diarizer
        self.audio_source = audio_source
        self.data_queue = queue.Queue(maxsize=100)

    def StreamData(self):
        try:
            while True:
                if self.audio_source:
                    audio_samples_int16 = self.audio_source.read()
                    if audio_samples_int16.shape[0] == 0:
                        break
                    data = self.diarizer.process(audio_samples_int16=audio_samples_int16)
                    scores = None
                    name = None
                    for item in data[1]:
                        if scores is None:
                            scores = [item[0]]
                            name = item[1]
                        else:
                            if item[0] > scores[0]:
                                scores[0] = item[0]
                                name = item[1]

                    yield [float(data[0]), scores[0], name]
        except KeyboardInterrupt:
            logging.info('KeyboardInterrupt')


def create_message(message):
    return client_streaming_pb2.SendRequest(queues=client_streaming_pb2.Queue(
        data=client_streaming_pb2.Queue.TimeData(timestamp=list(message)[0], speaker_score=list(message)[1],
                                                 speaker_name=list(message)[2])))


def message_iterator(message_list):
    for message in message_list:
        print('message: ', message)
        yield create_message(message)


def run(args):
    logging.basicConfig()
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('--audio-file', help='Path to audio file', required=False)
    parser.add_argument('--database-file', help='Path to database file', required=False)
    parser.add_argument('--diarizer-type',
                        help='Specify which diarizer to use: demo mockup diarizer or real-time enhanced baseline diarizer',
                        default='mockup_diarizer', choices=['LiveDiarizer', 'MockupDiarizer'], required=False)
    args = parser.parse_args(args)

    sampling_rate = 16000

    default_ivector_model_dir = \
        os.path.join(import_root_path, 'res', 'WSJ_aliDIT_1kH_25001_dit2_cov')

    if args.audio_file:
        audio_source = visualizer_for_grpc.AudioFileInput(audio_file_path=args.audio_file)
    else:
        audio_source = visualizer_for_grpc.MicrophoneInput(sampling_rate=sampling_rate)

    if args.database_file:
        behavior_type = visualizer_for_grpc.SpeakerKnowledgeBehaviorType.CLASSIFY_ONLY
    else:
        behavior_type = visualizer_for_grpc.SpeakerKnowledgeBehaviorType.CLASSIFY_AND_UPDATE

    diarizer = visualizer_for_grpc.EnhancedBaselineLiveDiarizer(behavior_type=behavior_type,
                                                                sampling_frequency_hz=sampling_rate,
                                                                database_file_path=args.database_file,
                                                                ivector_model_dir=default_ivector_model_dir)

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = client_streaming_pb2_grpc.SendDataStub(channel)

        s = SendData(audio_source=audio_source, diarizer=diarizer)
        list_of_requests = s.StreamData()
        response = stub.StreamData(message_iterator([x for x in list(list_of_requests)]))

        print("Server response: ", response.message)


if __name__ == '__main__':
    run(sys.argv[1:])
