# err_logging.py

import logging


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)  # 通过配置，logging还可以把错误记录到日志文件里，方便事后排查


main()
print('END')
