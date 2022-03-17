#!/usr/bin/python3.8.7
# -*- coding: utf-8 -*-

"""
@author: Wang Hao
@project: flask_mock
@file: config.py
@time: 2022-3-2 16:00
"""
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

DATA_PATH = os.path.join(BASE_DIR, 'data')

LOGIN_PATH = os.path.join(BASE_DIR, 'data', 'login_response.yaml')

CAPTCHA_PATH = os.path.join(BASE_DIR, 'data', 'captcha_response.json')