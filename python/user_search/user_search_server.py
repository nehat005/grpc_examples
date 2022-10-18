from concurrent import futures

import grpc

import user_search_pb2
import user_search_pb2_grpc
from utils import get_user, resource_db


class UserSearchService(user_search_pb2_grpc.UserSearchServicer):
    def ListUsers(self, request, context):
        query = request.query
        output = [
            user_search_pb2.User(
                first_name=user["first_name"],
                last_name=user["last_name"],
                user_id=user["user_id"],
                address=user_search_pb2.User.Address(
                    city=user["address"]["city"], country=user["address"]["country"]
                ),
            )
            for user in get_user(query, resource_db)
        ]
        return user_search_pb2.SearchResponse(page_num=1, users=output)

    def ListUsersStreamRequestSingleResponse(self, request_iterator, context):
        output_list = []
        for request in request_iterator:
            output = self.ListUsers(request, context=None)
            output_list.extend(output.users)
        return user_search_pb2.SearchResponse(page_num=1, users=output_list)

    # def ListUsersSingleRequestStreamResponse(self, request, context):
    #     for user in get_user(request.query, resource_db):
    #         yield user_search_pb2.SearchResponse(
    #             page_num=1,
    #             users=[
    #                 user_search_pb2.User(
    #                     first_name=user["first_name"],
    #                     last_name=user["last_name"],
    #                     user_id=user["user_id"],
    #                     address=user_search_pb2.User.Address(
    #                         city=user["address"]["city"],
    #                         country=user["address"]["country"],
    #                     ),
    #                 )
    #             ],
    #         )
    #
    # def ListUsersStreamRequestStreamResponse(self, request_iterator, context):
    #     for request in request_iterator:
    #         for user in get_user(request.query, resource_db):
    #             yield user_search_pb2.SearchResponse(
    #                 page_num=1,
    #                 users=[
    #                     user_search_pb2.User(
    #                         first_name=user["first_name"],
    #                         last_name=user["last_name"],
    #                         user_id=user["user_id"],
    #                         address=user_search_pb2.User.Address(
    #                             city=user["address"]["city"],
    #                             country=user["address"]["country"],
    #                         ),
    #                     )
    #                 ],
    #             )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_search_pb2_grpc.add_UserSearchServicer_to_server(UserSearchService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
