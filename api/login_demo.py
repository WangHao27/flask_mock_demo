#!/usr/bin/python3.8.7
# -*- coding: utf-8 -*-

"""
@author: Wang Hao
@project: flask_mock
@file: login_demo.py
@time: 2022-3-2 15:06
"""
from flask import Flask, request
from utils import config
from utils.fileUtils import FileUtils
from flask_cors import cross_origin,CORS

# app实例化
app = Flask(__name__)
# 解决跨域请求中的OPTIONS预检操作
CORS(app, supports_credentials=True, resources=r'/*')
# @cross_origin()


# 登录接口的mock实例
# 设置路由地址和请求方式
@app.route('/accountLogin', methods=['POST'])
def loign():
    """
    登录接口请求实例：http://192.168.2.130:8080/accountLogin?loginName=wanghao&password=123456789&captcha=XXXX&captchaKey=11111
    启动APP后，使用postman请求即可看到响应结果
    captchaKey可作为接口多参测试
    :return:
    """
    # 读取响应文件
    res = FileUtils(config.LOGIN_PATH).read()


    # 错误的用户名
    if request.args.get('loginName') != 'wanghao':
        return res['fail']

    # 错误的密码
    if request.args.get('password') != '123456789':
        return res['fail']

    # 错误的验证码
    if request.args.get('captcha') != 'XXXX':
        return res['vcode_error']

    return res['success']


# 登录页面验证码请求接口
@app.route('/captcha', methods=['GET'])
def captcha():

    # 获取需要的响应值
    res = FileUtils(config.CAPTCHA_PATH).json_read()

    return res


if __name__ == '__main__':
    # 设置应用的域名和端口，然后启动即可
    app.run(host='192.168.2.130', port=8080, debug=True)