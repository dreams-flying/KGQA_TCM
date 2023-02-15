#! -*- coding:utf-8 -*-
from neo_db.config import graph, CA_LIST
from spider.show_profile import get_profile
import codecs
import os
import json
import base64

def query(name):
    data = graph.run(
    "match(p )-[r]->(n:Entity{Name:'%s'}) return  p.Name,r.relation,n.Name,p.cate,n.cate\
        Union all\
    match(p:Entity {Name:'%s'}) -[r]->(n) return p.Name, r.relation, n.Name, p.cate, n.cate" % (name,name)
    )
    data = list(data)
    return get_json_data(data)

def get_json_data(data):
    json_data={'data':[],"links":[]}
    d=[]
    for i in data:
        # print(i["p.Name"], i["r.relation"], i["n.Name"], i["p.cate"], i["n.cate"])
        d.append(i['p.Name']+"_"+i['p.cate'])
        d.append(i['n.Name']+"_"+i['n.cate'])
        d=list(set(d))
    name_dict={}
    count=0
    for j in d:
        j_array=j.split("_")
    
        data_item={}
        name_dict[j_array[0]]=count
        count+=1
        data_item['name']=j_array[0]
        data_item['category']=CA_LIST[j_array[1]]
        json_data['data'].append(data_item)
    for i in data:
   
        link_item = {}
        
        link_item['source'] = name_dict[i['p.Name']]
        
        link_item['target'] = name_dict[i['n.Name']]
        link_item['value'] = i['r.relation']
        json_data['links'].append(link_item)

    return json_data


def get_KGQA_answer(array):
    # array = ['CIH病毒', '外文名', '的']
    data_array=[]
    for i in range(len(array)-2):
        if i==0:
            name=array[0]
        else:
            name=data_array[-1]['p.Name']
        # print("name:", name)
        # print("array:", array)
        # print("similar_words[array[1]]:", similar_words[array[1]])
        data = graph.run(
            "match(p)-[r:%s{relation: '%s'}]->(n:Entity{Name:'%s'}) return  p.Name,n.Name,r.relation,p.cate,n.cate" % (
                array[1], array[1], name)
        )
        # print("data：", data)
        data = list(data)
        data_array.extend(data)
        
        print("==="*36)
    #打开图片
    print("data_array:", data_array)  #data_array[-1]显示最后一个组成的中药
    with open("E:/demo/KGQA_TCM/spider/images/"+"%s.jpg" % (str(data_array[-1]['p.Name'].split("&&")[0])), "rb") as image:
            base64_data = base64.b64encode(image.read())
            b=str(base64_data)
          
    return [get_json_data(data_array), get_profile(str(data_array[-1]['p.Name'].split("&&")[0])), b.split("'")[1]]
    # return [get_json_data(data_array)]

def get_answer_profile(name):
    with open("./spider/images/"+"%s.jpg" % (str(name)), "rb") as image:
        base64_data = base64.b64encode(image.read())
        b = str(base64_data)
    return [get_profile(str(name)), b.split("'")[1]]

if __name__ == '__main__':
    # json_data=query("白术")
    # print(json_data)##补脾人参散

    KGQA = get_KGQA_answer(['补脾白术散', '组成', '的'])
    print(KGQA)

        



