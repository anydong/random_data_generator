#!/usr/bin/python3
from multiprocessing import Pool
import pymongo
import time

schema = __import__(''.join(['schemas', '.', 'mongo_user']), fromlist=['schema'])

client = pymongo.MongoClient(schema.url())
db = client.get_default_database()


def run(name):
    child_process_start_time = time.time()

    for _ in range(10):
        documents = []
        for _ in range(1000):
            documents.append(schema.generator())
        db.get_collection("user").insert_many(documents)

    print(name, '耗时：', time.time() - child_process_start_time)


def error_callback(res):
    print(res)


def main():
    main_process_start_time = time.time()
    pool = Pool()

    for i in range(10):
        print(i)
        pool.apply_async(run, (str(i),), error_callback=error_callback)

    pool.close()
    pool.join()

    print('总耗时：', time.time() - main_process_start_time)


if __name__ == "__main__":
    main()
