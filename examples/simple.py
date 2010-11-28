#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R. Lucindo (lucindo@gmail.com)

import konig

def simple_test():
    graph = konig.Graph()
    node = graph.node("1")
    node['name'] = 'Lucindo'

if __name__ == '__main__':
    konig.config("localhost", 6379)
    simple_test()
