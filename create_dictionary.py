# -*- coding: utf-8 -*-
import time
start_time = time.clock()
dicts = {}
record = set()
with open('cut_message.txt','rb') as fi:
    for line in fi:
        words = line.split(' ')
        for word in words:
            if word not in dicts:
                dicts[word] = 1
            else:
                dicts[word] += 1
fi.close()
print 'loop search ...'
with open('low_frequence_words.txt','w+') as fo:
    for key , value in dicts.items():
        if int(value) <= 5:
            fo.write(key)
            fo.write('\n')
fo.close()
end_time = time.clock()
print '总用时 %f s'%(end_time - start_time)
