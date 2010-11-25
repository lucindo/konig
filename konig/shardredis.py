#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R. Lucindo (lucindo@gmail.com)

import redis

__server__ = None
__port__ = None

def config(server, port):
    __server__ = server
    __port__ = port

class ShardRedis(redis.Redis):
    def __init__(self):
        redis.Redis.__init__(self, host=__server__, port=__port__)

if __name__ == '__main__':
    pass
