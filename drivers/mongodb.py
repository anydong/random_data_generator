import pymongo
import time


def error_callback(res):
    print(res)


class MongoDBDriver:
    def __init__(self, schema_name: str):
        self.schema = __import__(''.join(['schemas', '.', schema_name]), fromlist=['schema'])
        client = pymongo.MongoClient(self.schema.url())
        self.db = client.get_default_database()

    def run(self, name):
        child_process_start_time = time.time()

        for _ in range(10):
            documents = []
            for _ in range(1000):
                documents.append(self.schema.generator())
            self.db.get_collection("user").insert_many(documents)

        print(name, '耗时：', time.time() - child_process_start_time)
