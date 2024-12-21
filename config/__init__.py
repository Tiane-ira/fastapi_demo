import configparser

CONF = configparser.ConfigParser()
with open('config.ini', 'r', encoding='utf-8') as c:
    CONF.read_file(c)
