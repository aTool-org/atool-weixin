# -*- coding: utf-8 -*-
'''
Created on 2016年3月15日

'''

import platform


def get_server_name():
    '''
    获取系统的名称，不同的名称选择不同的配置
    '''
    return platform.node()


if __name__ == '__main__':
    print(platform.machine())
    print(platform.node())
    print(platform.platform(True))
    print(platform.system())
    print(platform.uname())
    print(platform.architecture())
    print(platform.platform() + ' ' + platform.architecture()[0])
