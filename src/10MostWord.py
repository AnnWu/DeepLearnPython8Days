#-*- coding:utf-8 -*-
# 最重要的词（出现频次最高的词）
import os,re

from collections import Counter

FilePath='./count'
def getCounter(fileSource):
    pattern = r'''[A-Za-z]+|\$?\d+%?$'''
    with open(fileSource) as f :
        r = re.findall(pattern,f.read())
        return Counter(r)
#过滤词
stop_word = ['the','In','of','and','has','that','s','Is','are','a']
def run(fileSource):
    #切换到目标文件目录
    os.chdir(FilePath)
    total_counter = Counter()
    for i in os.listdir(os.getcwd()):
        if os.path.splitext(i)[1] == '.txt':
            total_counter += getCounter(i)

    for i in stop_word:
        total_counter[i]=0
    print total_counter.most_common()[0][0]
if __name__ == "__main__":
    run(FilePath)