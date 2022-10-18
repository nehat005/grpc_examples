import grpc

import user_search_pb2_grpc
from utils import create_message, message_iterator


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = user_search_pb2_grpc.UserSearchStub(channel)
        # response = stub.ListUsers(create_message("Sam"))
        # print("Single Request Single Response", response.users)
        output_list = []
        # response_iterator = stub.ListUsersSingleRequestStreamResponse(
        #     create_message("John")
        # )
        # for response in response_iterator:
        #     output_list.extend(response.users)
        # print("Single Request Stream Response", output_list)

        response = stub.ListUsersStreamRequestSingleResponse.future(
            message_iterator(["John", "james"])
        )
        print("Stream Request Single Response", response.result())

        # output_list = []
        # response_iterator = stub.ListUsersStreamRequestStreamResponse(
        #     message_iterator(["John", "james"])
        # )
        # for response in response_iterator:
        #     output_list.extend(response.users)
        # print("Stream Request Stream Response", output_list)


if __name__ == "__main__":
    run()