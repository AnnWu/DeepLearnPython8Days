#-*- coding:utf-8 -*-
import re
from collections import Counter
FileSource="./abc.txt"
def getMostCommonWord(fileSource):
    pattern = r'''[A-Za-z]+|\$?\d+%?$'''
    #+ 加号出现一次或多次
    with open(fileSource) as f :
        r = re.findall(pattern,f.read())
        return Counter(r).most_common()

if __name__ == "__main__":
    print getMostCommonWord(FileSource)