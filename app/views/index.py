# -*- coding: utf-8 -*-
'''
Created on 2016年10月1日

@author: CXM
'''

from app import app


@app.route('/index.html', methods=['GET'])
@app.route('/', methods=['GET'])
def index_page_html():
    return 'weixin for www.atool.org, 微信号：atool-org（在线工具）'
