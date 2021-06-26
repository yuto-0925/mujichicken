# coding:utf-8
import os
import csv

# htmlからのデータをcsvファイルに記録
def write_csv(data):
    datas = [data]
    with open(os.getcwd()+'/insta/application/'+'data.csv','a') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(datas)