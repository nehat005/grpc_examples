# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import user_search_pb2 as user__search__pb2


class UserSearchStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListUsersStreamRequestSingleResponse = channel.stream_unary(
                '/UserSearch/ListUsersStreamRequestSingleResponse',
                request_serializer=user__search__pb2.SearchRequest.SerializeToString,
                response_deserializer=user__search__pb2.SearchResponse.FromString,
                )


class UserSearchServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ListUsersStreamRequestSingleResponse(self, request_iterator, context):
        """rpc ListUsers(SearchRequest) returns (SearchResponse) {}
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserSearchServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListUsersStreamRequestSingleResponse': grpc.stream_unary_rpc_method_handler(
                    servicer.ListUsersStreamRequestSingleResponse,
                    request_deserializer=user__search__pb2.SearchRequest.FromString,
                    response_serializer=user__search__pb2.SearchResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'UserSearch', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UserSearch(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListUsersStreamRequestSingleResponse(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/UserSearch/ListUsersStreamRequestSingleResponse',
            user__search__pb2.SearchRequest.SerializeToString,
            user__search__pb2.SearchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
