import codecs

#/home/lrq/桌面/文件/知识图谱/KGQA_HLM-master/raw_data/relation.txt
def get_character():
    f = codecs.open('/home/lrq/桌面/文件/知识图谱/KGQA_HLM-master/raw_data/relation.txt','r','utf-8')
    data = []
    for line in f.readlines():
        array = line.strip("\n").split(",")
        arr = [array[0],array[1]]
        data.extend(arr)
    
    return data

