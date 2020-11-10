from argparse import ArgumentParser


def main():
    parser = ArgumentParser(prog="DB Insert")
    parser.add_argument('schema', help="数据生成器")
    parser.add_argument('-d', '--driver', choices=['mysql', 'mongodb'], default='mysql', help="连接数据库类型，默认：mysql")
    parser.add_argument('-n', '--number', dest='number', type=int, default=1, help="生成数据量（万），默认：1 万")
    args = parser.parse_args()
    print('driver:', args.driver)
    print('schema:', args.schema)
    print('number:', args.number)


if __name__ == '__main__':
    main()
