#! -*- coding:utf-8 -*-
#将数据导入到neo4j中
#先启动neo4j,运行完creat_graph.py，然后才能运行neo2json.py
#标签名，关系名中不要有括号以及英文句号

"""
#旧版Connection profiles示例 2020.1.1
from py2neo import Graph
graph = Graph('http://localhost:7474/', username='neo4j', password='111111')

#py2neo 2021.2.3 版本的Connection profiles示例
from py2neo import Graph
graph = Graph("http://localhost:7474", auth=("neo4j", "111111"))
"""
from py2neo import Graph, Node, Relationship#,NodeSelector
from config import graph


count = 0
with open("../import/fangji_spo.txt", encoding='utf-8') as f:
    graph.run('MATCH (n) DETACH DELETE n')  #删除图数据库中数据
    for line in f.readlines():
        count += 1
        if count <= 1000000:
            rela_array=line.strip("\n").split("||")
            print(count)
            graph.run("MERGE(p: Entity{cate:'%s',Name: '%s'})"% (rela_array[3], rela_array[0]))
            graph.run("MERGE(p: Entity{cate:'%s',Name: '%s'})" % (rela_array[4], rela_array[2]))
            graph.run(
                "MATCH(e: Entity), (cc: Entity) \
                WHERE e.Name='%s' AND cc.Name='%s'\
                CREATE(e)-[r:%s{relation: '%s'}]->(cc)\
                RETURN r" % (rela_array[2], rela_array[0], rela_array[1],rela_array[1])
            )
        
