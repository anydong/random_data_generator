import time
from multiprocessing import Pool
from argparse import ArgumentParser
from drivers.mongodb import MongoDBDriver


def run(driver, name):
    driver.run(name)


def error_callback(res):
    print(res)


if __name__ == '__main__':
    parser = ArgumentParser(prog="DB Insert")
    parser.add_argument('schema', help="数据生成器")
    parser.add_argument('-d', '--driver', choices=['mysql', 'mongodb'], default='mysql', help="连接数据库类型，默认：mysql")
    parser.add_argument('-n', '--number', dest='number', type=int, default=1, help="生成数据量（万），默认：1 万")
    args = parser.parse_args()
    print('schema:', args.schema)
    print('number:', args.number)

    # driver = __import__(''.join(['drivers', '.', args.driver]), fromlist=[args.driver])
    driver = MongoDBDriver(args.schema)

    main_process_start_time = time.time()
    pool = Pool()

    for i in range(args.number):
        print(i)
        pool.apply_async(run, (driver, args.schema,), error_callback=error_callback)

    pool.close()
    pool.join()

    print('总耗时：', time.time() - main_process_start_time)
