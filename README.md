# 基于知识图谱的中药方剂可视化及问答系统<br>

# 项目目录
1)  app.py是整个系统的主入口<br>
2)  templates文件夹是HTML的页面<br>
     &emsp;|——index.html 欢迎界面<br> 
     &emsp;|——search.html 搜索处方关系页面<br>
     &emsp;|——all_relation.html 所有处方关系页面<br>
     &emsp;|——KGQA.html 处方问答页面<br>
3)  static文件夹存放css和js，是页面的样式和效果的文件<br>
4)  raw_data文件夹是存在数据处理后的三元组文件<br>
5)  neo_db文件夹是知识图谱构建模块<br>
     &emsp;|——config.py 配置参数<br>
     &emsp;|——create_graph.py 创建知识图谱，图数据库的建立<br>
     &emsp;|——query_graph.py 知识图谱的查询<br>
6)  KGQA文件夹是问答系统模块<br>
     &emsp;|——ltp.py 分词、词性标注、命名实体识别<br>
7)  spider文件夹是爬虫模块<br>
     &emsp;|——get_*.py 是之前爬取人物资料的代码，已经产生好images和json 可以不用再执行<br>
     &emsp;|——show_profile.py 是调用处方资料和图谱展示在前端的代码
<hr>

# 部署步骤：<br>
* 0.安装所需的库 执行pip install -r requirement.txt<br>
* 1.先下载好neo4j图数据库，并配好环境。修改neo_db目录下的配置文件config.py,设置图数据库的账号和密码。<br>
* 2.切换到neo_db目录下，执行python  create_graph.py 建立知识图谱<br>
* 3.在spider目录下，运行data_process.py(已处理好)<br>
* 4.在static目录下，运行neo2json.py(已处理好)<br>
* 5.去[这里](http://pyltp.readthedocs.io/zh_CN/latest/api.html#id2)下载好ltp模型。[ltp简介](http://ltp.ai/)<br>
* 6.在KGQA目录下，修改ltp.py里的ltp模型文件的存放目录<br>
* 7.运行python app.py,浏览器打开localhost:5000即可查看<br>

# 网站示例:<br>
欢迎界面
![image](https://github.com/dreams-flying/KGQA_TCM/blob/master/images/index.png)
索引界面
![image](https://github.com/dreams-flying/KGQA_TCM/blob/master/images/search.png)
问答界面
![image](https://github.com/dreams-flying/KGQA_TCM/blob/master/images/KGQA.png)
# 参考
https://github.com/chizhu/KGQA_HLM
