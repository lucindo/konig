#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R. Lucindo (lucindo@gmail.com)

# hashring code bowrred from gleicon:
# https://github.com/gleicon/txredisapi/blob/master/txredisapi/hashring.py

import redis
import zlib
import bisect

from exceptions import KonigError

servers = []

def config(server_list):
    global servers
    for server in server_list:
        servers.append((server.split(":")[0], int(server.split(":")[1])))

class ShardRedis(redis.Redis):
    def __init__(self, db = 0, replicas = 160):
        self.redis = []
        self.ring = {}
        self.sorted_keys = []
        self.replicas = replicas

        for server in servers:
            node = redis.Redis(host=server[0], port=server[1], db=db)
            self.redis.append(node)
            for x in xrange(self.replicas):
                crckey = zlib.crc32("%s:%d:%d" % (server[0], server[1], x))
                self.ring[crckey] = node
                self.sorted_keys.append(crckey)
                
        self.sorted_keys.sort()

    def _get_node_pos(self, key):
        if len(self.ring) == 0:
            return [None, None]
        crc = zlib.crc32(key)
        idx = bisect.bisect(self.sorted_keys, crc)
        idx = min(idx, (self.replicas * len(self.redis)) - 1) # prevents out of range index
        return [self.ring[self.sorted_keys[idx]], idx]

    def _get_redis(self, key):
        node, i = self._get_node_pos(key)
        if node is None: raise KonigError("Internal error: cant find server for key %s" % key)
        return node

    def hgetall(self, key):
        redis = self._get_redis(key)
        return redis.hgetall(key)

    def smembers(self, key):
        redis = self._get_redis(key)
        return redis.smembers(key)

    def hset(self, name, key, value):
        redis = self._get_redis(name)
        return redis.hset(name, key, value)

    def hdel(self, name, key):
        redis = self._get_redis(name)
        return redis.hdel(name, key)

    def sadd(self, key, value):
        redis = self._get_redis(key)
        return redis.sadd(key, value)

    def srem(self, key, value):
        redis = self._get_redis(key)
        return redis.srem(key, value)

    def delete(self, *names):
        for key in names:
            redis = self._get_redis(key)
            redis.delete(key)

if __name__ == '__main__':
    pass
