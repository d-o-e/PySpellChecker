# Deniz Erisgen ©
from pymongo import MongoClient

from my_utils import make_list_from_file_for_db as make_list


def get_database(name):
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    connection_string = \
        "mongodb://YOUR_USER_NAME:YOUR_PASSWORD@127.0.0.1:27017/?authMechanism=DEFAULT"

    client = MongoClient(connection_string)
    return client[name]


def main():
    database_name = "Dictionary"
    collection_name = "spell"
    db = get_database(database_name)
    collection = db[collection_name]
    data_list = make_list("words")
    print(data_list)
    collection.insert_many(data_list)


if __name__ == '__main__':
    main()
