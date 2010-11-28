#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R. Lucindo (lucindo@gmail.com)

import graph
import shardredis
import base64

rnodes = None
redges = None

def config(server_list):
    global rnodes, redges
    shardredis.config(server_list)
    rnodes = shardredis.ShardRedis(0)
    redges = shardredis.ShardRedis(1)

def load_node(node):
    assert isinstance(node, graph.Node)
    node_id = node['id']
    properties = rnodes.hgetall(node_id)
    for key, value in properties.items():
        node[key] = value
    node._eout = node._eout.union(rnodes.smembers("%s:o" % node_id))
    node._ein = node._ein.union(rnodes.smembers("%s:i" % node_id))
    return node

def update_node_property(node, key, value):
    assert isinstance(node, graph.Node)
    rnodes.hset(node['id'], key, value)

def remove_node_property(node, key):
    assert isinstance(node, graph.Node)
    rnodes.hdel(node['id'], key)

def del_node(node):
    for oe in rnodes.smembers("%s:o" % node['id']):
        del_edge(graph.Edge(node['id'], oe))
    for ie in rnodes.smembers("%s:i" % node['id']):
        del_edge(graph.Edge(ie, node['id']))
    rnodes.delete(node['id'], "%s:o" % node['id'], "%s:i" % node['id'])

def load_edge(edge):
    assert isinstance(edge, graph.Edge)
    properties = redges.hgetall(edge['id'])
    for key, value in properties.items():
        edge[key] = value
    return edge

def update_edge_property(edge, key, value):
    assert isinstance(edge, graph.Edge)
    redges.hset(edge['id'], key, value)

def remove_edge_property(edge, key):
    assert isinstance(edge, graph.Edge)
    redges.hdel(edge['id'], key)

def del_edge(edge):
    assert isinstance(edge, graph.Edge)
    uid = edge.uid()
    vid = edge.vid()
    rnodes.srem("%s:o" % uid, vid)
    rnodes.srem("%s:i" % vid, uid)
    redges.delete(edge['id'])

def add_edge_to_nodes(uid, vid):
    rnodes.sadd("%s:o" % uid, vid)
    rnodes.sadd("%s:i" % vid, uid)

if __name__ == '__main__':
    pass
