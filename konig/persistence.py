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
    assert isinstance(edge, Edge)
    properties = redges.hgetall(edge['id'])
    for key, value in properties.items():
        edge[key] = value
    return edge

def update_edge_property(edge, key, value):
    assert isinstance(edge, Edge)
    redges.hset(edge['id'], key, value)

def remove_edge_property(edge, key):
    assert isinstance(edge, Edge)
    redges.hdel(edge['id'], key, value)

def del_edge(edge):
    assert isinstance(edge, Edge)
    in_node = edge.in_node_id()
    out_node = edge.out_node_id()
    rnodes.srem("%s:o" % out_node, in_node)
    rnodes.srem("%s:i" % in_node, out_node)
    redges.delete(edge['id'])

if __name__ == '__main__':
    pass
