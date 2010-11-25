#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R. Lucindo (lucindo@gmail.com)

import persistence

class Node:
    def __init__(self, id):
        self._id = id
        self._properties = dict()
        self._eout = set()
        self._ein = set()

    def out_edges(self):
        return self._eout

    def in_edges(self):
        return self._ein

    def __getitem__(self, key):
        return self._properties[key]

    def __setitem__(self, key, value):
        self._properties[key] = value
        persistence.update_node_property(self, key, value)

    def __delitem__(self, key):
        del self._properties[key]
        persistence.remove_node_property(self, key)

class Edge:
    def __init__(self, nin, nout):
        self._nin = nin
        self._nout = nout
        self._properties = dict()

    def in_node_id(self):
        return self._nin

    def out_node_id(self):
        return self._nout

    def __getitem__(self, key):
        return self._properties[key]

    def __setitem__(self, key, value):
        self._properties[key] = value
        persistence.update_edge_property(self, key, value)

    def __delitem__(self, key):
        del self._properties[key]
        persistence.remove_edge_property(self, key)


class Graph:
    def node(self, id):
        node = Node(id)
        persistence.load_node(node)
        return node

    def edge(self, uid, vid):
        edge = Edge(uid, vid)
        persistence.load_edge(edge)
        return edge

    def del_node(self, id):
        node = Node(id)
        persistence.del_node(node)

    def del_edge(self, uid, vid):
        edge = Edge(uid, vid)
        persistence.del_edge(edge)

if __name__ == '__main__':
    pass
