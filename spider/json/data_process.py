#! -*- coding:utf-8 -*-
import json

fw = open('data.json', 'w', encoding='utf-8')
tempDict = {}
with open('../../raw_data/zhongyao_spo.txt', encoding='utf-8') as f:
    for line in f:
        arrays = line.replace("\n", "").split("&&")
        if arrays[0] not in tempDict:
            tempDict[arrays[0]] = len(tempDict)

tempDict2 = {}
for k, v in tempDict.items():
    # print(k)
    with open('../../raw_data/zhongyao_spo.txt', encoding='utf-8') as f:
        tempDict1 = {}
        tempDict1["中药"] = k
        for line in f:
            arrays1 = line.replace("\n", "").split("&&")
            if k == arrays1[0]:
                tempDict1[arrays1[1]] = arrays1[2]
        tempDict2[k] = tempDict1
l1 = json.dumps(tempDict2, ensure_ascii=False)
fw.write(l1)