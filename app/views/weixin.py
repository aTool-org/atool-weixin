# -*- coding: utf-8 -*-
'''
Created on 2016年10月19日

@author: hustcc
'''
from app import app, weixin
from app.utils import OtherUtil

app.add_url_rule('/wx/weixin.html', view_func=weixin.view_func)


@weixin.register(type='event', event='subscribe')
def send_welcome(**kwargs):
    username = kwargs.get('sender')
    sender = kwargs.get('receiver')
    return weixin.reply(username, sender=sender, content=u'感谢关注 在线工具 公众号！')


@weixin.register(type='event', event='CLICK')
def restart_im(**kwargs):
    username = kwargs.get('sender')
    sender = kwargs.get('receiver')
    
    event_key = kwargs.get('event_key')
    if event_key == 'restart_im':
        OtherUtil.restart_im()
    
    return weixin.reply(username, sender=sender, content=u'感谢关注！')


@weixin.register('*')
def reply(**kwargs):
    username = kwargs.get('sender')
    sender = kwargs.get('receiver')
    content = kwargs.get('content')
    
    return weixin.reply(username, sender=sender, content=u'建设中...')