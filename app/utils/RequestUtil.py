# -*- coding: utf-8 -*-
'''
Created on 2015年8月21日

@author: hustcc
'''

from flask.globals import request, session

# 获得参数，post或者get
def get_parameter(key, default=None):
    '''
    info:获得请求参数，包括get和post，其他类型的访问不管
    '''
    # post参数
    if request.method == 'POST':
        param = request.form.get(key, default)
    # get
    elif request.method == 'GET':
        param = request.args.get(key, default)
    else:
        return default

    return param


def is_on_server():
    if '127.0.0.1' in request.url_root or 'localhost' in request.url_root:
        return True
    return False
