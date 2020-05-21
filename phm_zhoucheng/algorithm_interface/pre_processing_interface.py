import pandas as pd
from sklearn.ensemble import IsolationForest
import numpy as np
import sys
import csv


#数据清洗
def datacleaning_if(input_file, output_file):
    with open(input_file, 'r') as f:
    # 1.创建阅读器对象
        reader = csv.reader(f)
    # 2.读取文件第一行数据
        head_row = next(reader)
    data_attribute = []
    for item in head_row:
        data_attribute.append(item)
    # 读取数据
    tn = pd.read_csv(input_file)
    tn.dropna(inplace=True)
    train = np.array(tn)
    train_x = train[:, :-1] #输出评估结果时使用
    # 对所有数据行进行异常检测
    train_x = np.array(train_x)
    clf = IsolationForest(n_estimators=100,
                            max_samples='auto',
                            contamination=0.0001,
                            max_features=1.0,
                            bootstrap=False, n_jobs=1, random_state=None,
                            verbose=0).fit(train_x)
    # pred存入的是每一行数据的预测值，是1或者-1
    pred = clf.predict(train_x)
    normal = train_x[pred == 1]
    abnormal = train_x[pred == -1]
    # 删除pred为-1的行数据
    df = pd.DataFrame(pd.read_csv(input_file))[0:pred.
            size]
    df['pred'] = pred
    # data2=data1[-data1.sorce.isin([61])]
    df2 = df[-df.pred.isin([-1])]
    df2 = df2.drop(['pred'], axis=1)
    # 将清洗之后的数据存入csv文件
    data_out = df2.iloc[:, :].values
    csvfile2 = open(output_file, 'w', newline='')
    writer = csv.writer(csvfile2)
    writer.writerow(data_attribute)  # 存属性
    m = len(data_out)
    for i in range(m):
        writer.writerow(data_out[i])


params = {}
params['path'] = r'D:\py-program\phm_zhoucheng\test_set_1\test\TEST01.csv'
params['opath'] = r'D:\py-program\phm_zhoucheng\test_set_1\upload_test_clean.csv'
argvs = sys.argv


try:
    for i in range(len(argvs)):
        if i < 1:
            continue
        if argvs[i].split('=')[1] == 'None':
            params[argvs[i].split('=')[0]] = None
        else:
            Type = type(params[argvs[i].split('=')[0]])
            params[argvs[i].split('=')[0]] = Type(argvs[i].split('=')[1])

    datacleaning_if(params['path'], params['opath'])

except Exception as e:
    print(e)