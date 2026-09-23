#!/usr/bin/env python3

import configparser

conf = configparser.ConfigParser()

conf.read('my.conf')

print("I expect to see 4 lines of output after this: data1, data2, data3, data4")

print(conf["cat1"]["key1"])
print(conf["cat1"]["key2"])
print(conf["cat2"]["key2"]) # demonstrate that keys are namespaced by categories
print(conf["cat2"]["key3"])

