# -*- coding: utf-8 -*-
'''
Created on 2016年2月19日

@author: hustcc
'''
import flask
from app.utils import RequestUtil, JsonUtil


def standard_response(success, data):
    '''接口的标准json返回值，统一使用同一个方法，便于统一修改
    '''
    rst = {}
    rst['success'] = success
    rst['data'] = data
    return JsonUtil.object_2_json(rst)


# 重写 render_template 写入固定的一些参数
def render_template(*args, **kwargs):
    kwargs['t'] = 't'
    return flask.render_template(*args, **kwargs)
