#! -*- coding:utf-8 -*-
from py2neo import Graph

"""
#旧版Connection profiles示例 2020.1.1
from py2neo import Graph
graph = Graph('http://localhost:7474/', username='neo4j', password='111111')

#py2neo 2021.2.3 版本的Connection profiles示例
from py2neo import Graph
graph = Graph("http://localhost:7474", auth=("neo4j", "111111"))
"""

graph = Graph("http://localhost:7474", auth=("neo4j", "111111"))

CA_LIST = {"处方": 0, "中药": 1}
