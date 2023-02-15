#! -*- coding:utf-8 -*-
#先运行creat_graph .py

from py2neo import Graph
from neo_db.config import graph, CA_LIST
import codecs
import os
import json

data = graph.run(
    "match(p)-[r]->(n:Entity) return p.Name,r.relation,n.Name,p.cate,n.cate"
).data()

data = list(data)


# print(data)
#
def get_json_data(data):
    json_data = {'data': [], "links": []}
    d = []

    for i in data:
        # print(i["p.Name"], i["r.relation"], i["n.Name"], i["p.cate"], i["n.cate"])
        d.append(i['p.Name'] + "$$" + i['p.cate'])
        d.append(i['n.Name'] + "$$" + i['n.cate'])
        d = list(set(d))
    name_dict = {}
    count = 0
    for j in d:
        # print(j)
        # print(jk)
        j_array = j.split("$$")
        # print("j_array:", j_array)
        # print(pp)
        data_item = {}
        name_dict[j_array[0]] = count
        count += 1
        data_item['name'] = j_array[0]
        data_item['category'] = CA_LIST[j_array[1]]
        json_data['data'].append(data_item)
    for i in data:
        link_item = {}
        link_item['source'] = name_dict[i['p.Name']]
        link_item['target'] = name_dict[i['n.Name']]
        link_item['value'] = i['r.relation']
        json_data['links'].append(link_item)

    #
    return json_data

json_data = get_json_data(data)

f = codecs.open(r'fangji.json', 'w', 'utf-8')
f.write(json.dumps(json_data, ensure_ascii=False))
