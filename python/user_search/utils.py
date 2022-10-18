import user_search_pb2

resource_db = [
    {
        "user_id": 1,
        "first_name": "John",
        "last_name": "Snow",
        "address": {"city": "NYC", "country": "US"},
    },
    {
        "user_id": 2,
        "first_name": "Sam",
        "last_name": "Johmson",
        "address": {"city": "Mountain View", "country": "US"},
    },
    {
        "user_id": 3,
        "first_name": "James",
        "last_name": "Bond",
        "address": {"city": "NYC", "country": "US"},
    },
]


def create_message(message):
    return user_search_pb2.SearchRequest(query=message)


def message_iterator(message_list):
    for message in message_list:
        yield create_message(message)


def get_user(query: str, resource_db: list):
    for user in resource_db:
        if (
                query.lower() in user["first_name"].lower()
                or query.lower() in user["last_name"].lower()
        ):
            print(query, user['first_name'], user['last_name'])
            yield user