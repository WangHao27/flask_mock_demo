#!/usr/bin/python3.8.7
# -*- coding: utf-8 -*-

"""
@author: Wang Hao
@project: jy-test
@file: fileUtils.py
@time: 2021-11-19 11:07
"""
import csv
import json
import os
from json import JSONDecodeError
import yaml
from yaml.parser import ParserError
from yaml.scanner import ScannerError
from yamlinclude.constructor import YamlIncludeConstructor


# 用于yaml文件嵌套
YamlIncludeConstructor.add_to_loader_class(loader_class=yaml.FullLoader)
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

class FileUtils:
    """
    文件读取与写入工具类，处理一些解析异常
    """
    def __init__(self, filePath):
        """
        文件路径初始化
        """
        if os.path.isfile(PATH(filePath)):
            self.file = PATH(filePath)
        else:
            raise FileNotFoundError("文件不存在")


    def read(self):
        """
        读取yaml文件数据
        :return:
        """
        try:
            with open(self.file, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
                f.close()
            return data
        except (ScannerError, ParserError) as error:
            print("yaml文件格式存在问题，请检查：{}：{}".format(type(error), error))


    def write(self, message):
        """
        数据写入yaml文件
        :param message:
        :return:
        """
        if type(message) == dict:
            # 此模式为追加模式,若想直接重写则将open函数中的模式'a+'改为'w'
            with open(self.file, "a+", encoding="utf-8") as f:
                yaml.dump(message, f)
            f.close()
        else:
            print("请输入字典类型的数据！")


    def json_read(self):
        """
        读取json文件数据
        :return:
        """
        try:
            with open(self.file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                f.close()
            return data
        except JSONDecodeError as error:
            print("json文件格式存在问题，请检查：{}：{}".format(type(error), error))


    def json_write(self, message):
        """
        json文件的数据写入
        :param message:
        :return:
        """
        if type(message) in (str, dict, list):
            with open(self.file, 'w', encoding="utf-8") as j:
                json.dump(message, j, ensure_ascii=False)
        else:
            print("请传入字典或列表类型的数据！")


    def csv_write(self, headers, rows):
        """
        数据格式：
        表头(列表)[key1, key2, ...]，
        行(列表嵌套字典)[{'key1': 'val1', 'key2': 'val2'}，{...}, ...]
        :param headers:
        :param rows:
        :return:
        """
        if type(headers) and type(rows) in (str, list):
            with open(self.file, "w", encoding='utf-8', newline="") as w:
                writer = csv.DictWriter(w, headers)
                writer.writeheader()
                writer.writerows(rows)
                w.close()
        else:
            print("请传入列表类型数据！")


# if __name__ == '__main__':
#     path = setting.TEST_METHOD_JSON
#     info = FileUtils(path).json_read()
#     headers = ['key1', 'key']
#     rows = [{'key': 'value', 'key1': ['q', 'sad', 'asd']}, {'key': 'v5464', 'key1':  'asd'}]
#     FileUtils("D:/PycharmProject/jy-test/utils/test.csv").csv_write(headers, rows)
#     print(info)