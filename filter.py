# -*- coding: utf8 -*- 
#import opencc
import re
from langconv import *
import string
import jieba
#cc = opencc.OpenCC('t2s')
import sys  
#reload(sys)  
import time
start_time = time.clock()
print 'load data...'
fp = open("data.txt","rb")
print 'standardlize ing...'
data = []
#标准化格式

for line in fp:
    line = line.decode('utf-8')
    match = re.search("(?<=人工审核)(政治类|违法诈骗|商业广告类|涉黄|涉黑)".decode('utf-8'),line)
    line = re.sub("人工审核(政治类|违法诈骗|商业广告类|涉黄|涉黑)短信".decode('utf-8'),"".decode('utf-8'),line)
    line = line.encode('utf-8')
    try:    
        line = "人工审核"+ match.group(0).encode('utf-8') + "短信\t" + line
        data.append(line)
    except Exception as e:
        print(str(e))
fp.close()

stop_lists = []#停用词读取
with open("stop_words.txt","rb") as f:
    for line in f:
        line = re.sub("\n","",line)
        stop_lists.append(line.strip())
f.close()

try:
    fn = open('filter_data.txt','w+')#写入到新文件中
except Exception as e:
    print(str(e))
    exit(0)

#fs = open('cut_message.txt','wb+')
print 'regularize ing...'

for line in data:
    line = " ".join(jieba.cut(line))
    line = line.encode('utf-8')
    fs.write(line)
ddd
record = set()
num = 0
for line in data:
    line = line.decode('utf-8')
    line = re.sub("(http:\/\/|https:\/\/){0,1}(((\w+)(\.))(((\w+)(\.){0,1}){0,})\/{0,1}){1,}".decode('utf-8'),"网址".decode('utf-8'),line)#标记网址
    new_line =""
    for char in line:
        if char >= u'\u4e00' and char <= u'\u9fa5':
            new_line = new_line + char
    line = new_line
    #line = re.sub("[^\u4e00-\u9fa5]","".decode('utf-8'),line)#去除非中文字符
    #line = re.sub("[\s+\.\-\!\/_,:$%^*()?+\"\'[\]<>=;{}]+".decode('utf-8'),"".decode('utf-8'),line)#非中文字符处理
    #line = re.sub("[0-9a-zA-Z０-９]+".decode('utf-8'),"".decode('utf-8'),line)
    #line = re.sub("[+——！，。？、：；．~@#￥%……&*“”（）【】║|《》〝〞「」‘’〖〗『』～＝｛｝]+".decode('utf-8'),"".decode('utf-8'),line)
    #line = re.sub("[▉◆◎★☆□○◇▼╳↓→Ё╰╯╭╮┌└]".decode('utf-8'),"".decode('utf-8'),line)
    #line = re.sub("[％]".decode('utf-8'),"".decode('utf-8'),line)
    #line = re.sub("[〤⒌おぅ]".decode('utf-8'),"".decode('utf-8'),line)
    #print("正在过滤第" + str(n) + "条")
    #print(line)
    line = line.encode('utf-8')
    string = line.split("短信",1)
    if len(string) > 1:    
        line = string[0] + "短信" + '\t' + string[1]
    
    for i in range(len(stop_lists)):#停用词处理
        line = re.sub(stop_lists[i],"",line)
    
    line = Converter('zh-hans').convert(line.decode('utf-8'))#繁体字转为简体字
    line = line.encode('utf-8')
    strings = line.split('\t',1)
    if len(strings) < 1:
        print("空数据")
        continue
    if line not in record:
        fn.write(line + '\n')
        record.add(line)
    #print(line)
    num += 1
fn.close()

end_time = time.clock()
print '执行时间总长为 %f s'%(end_time - start_time) 