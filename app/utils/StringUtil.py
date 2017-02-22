# -*- coding: utf-8 -*-
'''
Created on 2015年6月16日

@author: hustcc
'''

import hashlib
import binascii
import uuid
import base64


def is_empty(s):
    '''string is empty ?'''
    if s is None or s == '':
        return True
    return False


def is_true(s):
    '''string is true'''
    if s is True:
        return True
    if s == 'true':
        return True
    return False


def md5_salt(s, salt="atool_weixin"):
    '''
    md5 + 盐：即便两个用户使用了同一个密码，由于系统为它们生成的salt值不同，他们的散列值也是不同的。
    '''
    if s:
        return md5(s + salt)
    else:
        return ''


def md5(s):
    '''
    md5
    '''
    m = hashlib.md5()
    m.update(s)
    return m.hexdigest()


def crc32_hash(v):
    """
    Generates the crc32 hash of the v.
    @return: str, the str value for the crc32 of the v (crc32b)
    """
    return '%x' % (binascii.crc32(v) & 0xffffffff)  # 取crc32的八位数据 %x返回16进制


def md5_token():
    return hashlib.md5(str(uuid.uuid1()).encode('utf-8')).hexdigest()  # md5 32bit


# 获取一个新的token，保证完全唯一
def crc32_token():
    return crc32_hash(str(uuid.uuid1()).encode('utf-8'))


# 判断是否为数字
def is_num(num):
    try:
        int(num)
        return True
    except:
        return False


def base64_encode(s):
    return base64.encodestring(str(s))


def base64_decode(s):
    return base64.decodestring(str(s))
