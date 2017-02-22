# -*- coding: utf-8 -*-
'''
Created on 2016年6月15日

@author: hustcc
'''
import sys


def do_nothing():
    return 'nothing done.'


# 定义一些操作
operator = {
}

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ('argv length is not equal 2.')
    else:
        print (operator.get(sys.argv[1], do_nothing)())
