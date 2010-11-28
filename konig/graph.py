#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R. Lucindo (lucindo@gmail.com)

import persistence
from exceptions import KonigError

class Node:
    def __init__(self, idx):
        self._id = idx
        self._properties = {"id": idx}
        self._eout = set()
        self._ein = set()

    def out_edges(self):
        return self._eout

    def in_edges(self):
        return self._ein

    def __getitem__(self, key):
        return self._properties[key]

    def __setitem__(self, key, value):
        if key == 'id': raise KonigError("cannot set id")
        self._properties[key] = value
        persistence.update_node_property(self, key, value)

    def __delitem__(self, key):
        del self._properties[key]
        persistence.remove_node_property(self, key)

    def __str__(self):
        return "id: %s | out_edges: %s | in_edges: %s | properties: %s" % (self._id, str(self._eout), str(self._ein), str(self._properties))

class Edge:
    def __init__(self, uid, vid):
        self._uid = uid
        self._vid = vid
        self._id = "%s:%s" % (uid, vid) 
        self._properties = {"id" : self._id }

    def uid(self):
        return self._uid

    def vid(self):
        return self._vid

    def __getitem__(self, key):
        return self._properties[key]

    def __setitem__(self, key, value):
        if key == 'id': raise KonigError("cannot set id")
        self._properties[key] = value
        persistence.update_edge_property(self, key, value)

    def __delitem__(self, key):
        del self._properties[key]
        persistence.remove_edge_property(self, key)

    def __str__(self):
        return "id: %s | uid: %s | vid: %s | properties: %s" % (self._id, self._uid, self._vid, str(self._properties))

class Graph:
    def _get_node(self, idx):
        if isinstance(idx, Node): idx = idx['id']
        node = Node(idx)
        return node
    
    def _get_edge(self, uid, vid):
        if isinstance(uid, Node): uid = uid["id"]
        if isinstance(vid, Node): vid = vid["id"]
        edge = Edge(uid, vid)
        return edge

    def node(self, idx):
        node = self._get_node(idx)
        node = persistence.load_node(node)
        return node

    def edge(self, uid, vid):
        edge = self._get_edge(uid, vid)
        persistence.add_edge_to_nodes(edge.uid(), edge.vid())
        edge = persistence.load_edge(edge)
        return edge

    def del_node(self, idx):
        persistence.del_node(self._get_node(idx))

    def del_edge(self, uid, vid):
        persistence.del_edge(self._get_edge(uid, vid))

class Traversal:
    def __init__(self, start_node):
        self._graph = Graph()
        self._start_node = self._graph.node(start_node)
        self._visited = set()

    def __iter__(self):
        pass

if __name__ == '__main__':
    pass
