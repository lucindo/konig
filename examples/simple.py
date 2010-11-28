#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R. Lucindo (lucindo@gmail.com)

import konig

def simple_test():
    graph = konig.Graph()
    node = graph.node("1")
    node['name'] = 'Lucindo'

    print node['name']
    print node

    node = graph.node("test")
    print node

    edge = graph.edge("1", "test")
    edge['color'] = 'red'
    print edge

    print "before del"

    print graph.node("1")
    print graph.node("test")

    graph.del_edge("1", "test")

    print "after del"

    print graph.node("1")
    print graph.node("test")

    edge = graph.edge("test", "1")

    print "added edge"

    print graph.node("1")
    print graph.node("test")

    print "removed node 1"

    graph.del_node("1")

    print graph.node("test")

if __name__ == '__main__':
    konig.config(["localhost:6379"])
    simple_test()
