#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R. Lucindo (lucindo@gmail.com)

import graph
import shardredis
import base64

rnodes = None
redges = None

def config(server, port):
    shardredis.config(server, port)
    rnodes = ShardRedis(0)
    redges = ShardRedis(1)

def load_node(node):
    assert isinstance(node, Node)
    node_id = node['id']
    properties = rnodes.hgetall(node_id)
    for key, value in properties.items():
        node[key] = value
    node._eout = node._eout.union(rnodes.smembers("%s:o" % node_id))
    node._ein = node._ein.union(rnodes.smembers("%s:i" % node_id))
    return node

def update_node_property(node, key, value):
    assert isinstance(node, Node)
    rnodes.hset(node['id'], key, value)

def remove_node_property(node, key):
    assert isinstance(node, Node)
    rnodes.hdel(node['id'], key, value)

def del_node(node):
    out_edges = rnodes.smembers("%s:o" % node['id'])
    for n in out_edges:
        del_edge(Edge(node['id'], n))
    rnodes.delete(node['id'], "%s:o" % node['id'], "%s:i" % node['id'])

def load_edge(edge):
    pass

def update_edge_property(edge, key, value):
    pass

def remove_edge_property(edge, key):
    pass

def del_edge(edge):
    pass

if __name__ == '__main__':
    pass
