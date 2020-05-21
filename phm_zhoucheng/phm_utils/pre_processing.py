import pandas as pd
from sklearn.ensemble import IsolationForest
import numpy as np
import sys
import csv

def dim_ctrl(inputfile,outputfile):
    df = pd.read_csv(inputfile)
    df = df.loc[:,['DE_time','FE_time','RPM']]
    #df = df.loc[:,['DE_time','FE_time','RPM','label']]
    df.to_csv(outputfile,index=False)

def datacleaning_if(input_file,output_file,contamination):
    params = {}
    params['n_estimators'] = 100
    params['max_samples'] = 'auto'
    params['contamination'] = contamination
    params['max_features'] = 1.0
    params['path'] = input_file
    params['opath'] = output_file
    try:
        with open(params['path'], 'r') as f:
        # 1.创建阅读器对象
            reader = csv.reader(f)
        # 2.读取文件第一行数据
            head_row = next(reader)
        data_attribute = []
        for item in head_row:
            data_attribute.append(item)
    # 读取数据
        tn = pd.read_csv(params['path'])
        tn.dropna(inplace=True)
        train = np.array(tn)
        train_x = train[:, :-1] #输出评估结果时使用
        #train_x = train[:, :-2] #测试评估效果时使用
    # 对所有数据行进行异常检测
        train_x = np.array(train_x)
        clf = IsolationForest(n_estimators=params['n_estimators'],
                              max_samples=params['max_samples'],
                              contamination=params['contamination'],
                              max_features=params['max_features'],
                              bootstrap=False, n_jobs=1, random_state=None,
                              verbose=0).fit(train_x)
    # pred存入的是每一行数据的预测值，是1或者-1
        pred = clf.predict(train_x)
        normal = train_x[pred == 1]
        abnormal = train_x[pred == -1]
    # 删除pred为-1的行数据
        df = pd.DataFrame(pd.read_csv(params['path']))[0:pred.
            size]
        df['pred'] = pred
    # data2=data1[-data1.sorce.isin([61])]
        df2 = df[-df.pred.isin([-1])]
        df2 = df2.drop(['pred'], axis=1)
    # 将清洗之后的数据存入csv文件
        data_out = df2.iloc[:, :].values
        csvfile2 = open(params['opath'], 'w', newline='')
        writer = csv.writer(csvfile2)
        writer.writerow(data_attribute)  # 存属性
        m = len(data_out)
        for i in range(m):
            writer.writerow(data_out[i])
    except Exception as e:
        print(e)
def none_clean(inputfile,outputfile):
    df = pd.read_csv(inputfile)
    df.to_csv(outputfile,index=False)
