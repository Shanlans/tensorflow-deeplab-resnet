# -*- coding: utf-8 -*-

import os 


def get_list(path):
    j=0
    f = open('cemianTrain.txt','w')
    for i in os.listdir(path):
        print(i)        
        f.write(os.path.join('/',i))        
        j+=1
        if j%2 == 0:
            f.write('\n')
        else:
            f.write(' ')
    f.close()
    
    
def get_list1(path):
    f = open('holderTrain.txt','w')
    for i in os.listdir(path):
        if i.split('_')[-1] == 'label.png':
            pass
        else:
            f.write(os.path.join('/',i))        
            f.write(' ')
            f.write(os.path.join('/',i.split('.')[0]+'_label.png'))
            f.write('\n')
    f.close()
        
        
get_list1('holder/')