konig
=====

**konig** is a *very simple* distributed graph (actually digraph) database, result of my NIH syndrome.

Dependencies & Installation
---------------------------

**konig** depends on:

* [Python 2.6] [1]
* [Redis 2.0.x] [2]
* [redis-py] [3]

there's no *closed* version by now, but you can do:

    $ git clone https://github.com/lucindo/konig.git
	$ cd konig
	$ sudo python setup.py install

I'll try my best to push only working code to master.

Features
--------

* Distributed
* Nodes and Edges Properties

Working on (following this order):

* Traversal API
* Error handling (read-only flag)
* Add/Remove servers on the fly
* Caching system
* Change notification (pubsub)

Usage
-----

    >>> import konig
    >>> konig.config(["localhost:6379"])
	>>> graph = konig.graph()
	>>> node1 = graph.node("1")
	>>> node2 = graph.node("2")
	>>> edge = graph.edge("1", "2")
	>>> edge["color"] = "red"
	>>> node1["name"] = "konig-test"

API Reference
-------------

### konig.config(server_list)
  Configure the system with a list of *fixed* redis servers. Each list element a string
  "server:port". Example: konig.config(["localhost:6379", "localhost:8080"])

### konig.Graph()
  General graph class

### konig.Graph.node(id)
  Loads a node or creates one. The id must be a string. Returns a Node class instance.

### konig.Graph.edge(uid, vid)
  Loads or created a edge from node uid, vid. The parameters uid and vid can be strings (node's id)
  or Nodes instances. Returns an Edge instance. Note: all edges are directed.

### konig.Graph.del_edge(uid, vid)
  Removes an edge from the system.

### konig.Graph.del_node(id)
  Removes a node from the system. This method has one known issue: #1

Future
------

* Non-blocking API (using [txredisapi] [5])
* Indexing
* Namespaces (named graphs)
* Support for proper graphs (not only digraphs)

Copyright and License
---------------------

[BOLA - Buena Onda License Agreement (v1.1)] [4]

<pre>
I don't like licenses, because I don't like having to worry about all this
legal stuff just for a simple piece of software I don't really mind anyone
using. But I also believe that it's important that people share and give back;
so I'm placing this work under the following license.


BOLA - Buena Onda License Agreement (v1.1)
------------------------------------------

This work is provided 'as-is', without any express or implied warranty. In no
event will the authors be held liable for any damages arising from the use of
this work.

To all effects and purposes, this work is to be considered Public Domain.


However, if you want to be "buena onda", you should:

1. Not take credit for it, and give proper recognition to the authors.
2. Share your modifications, so everybody benefits from them.
3. Do something nice for the authors.
4. Help someone who needs it: sign up for some volunteer work or help your
   neighbour paint the house.
5. Don't waste. Anything, but specially energy that comes from natural
   non-renewable resources. Extra points if you discover or invent something
   to replace them.
6. Be tolerant. Everything that's good in nature comes from cooperation.
</pre>

  [1]: http://www.python.org/                      "Python"
  [2]: http://code.google.com/p/redis/             "Redis"
  [3]: http://github.com/andymccurdy/redis-py/     "redis-py"
  [4]: http://blitiri.com.ar/p/bola/               "BOLA - Buena Onda License Agreement (v1.1)"
  [5]: https://github.com/gleicon/txredisapi       "redis client for twisted"
