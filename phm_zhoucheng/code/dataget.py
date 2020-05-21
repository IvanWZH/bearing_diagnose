import pandas as pd
import os

def dataget(input_path, out_path,label):
    # 读取机组文件夹下各数据组文件夹的路径并按文件名排序，保证整合时
    # 数据组文件夹读取的顺序固定，使接下来的读取以a-e或1-5的顺序进行
    dirs_bearing = os.listdir(input_path)  # 获取数据组文件夹目录（B,IR,OR,NORMAL）
    print('开始整合数据')
    dirs_bearing.sort()  # 将子文件夹排序
    datafile_path = [os.path.join(input_path, name) for name in dirs_bearing]  # 得到数据组文件夹路径的列表
    # 建立输入数据的dataframe对象
    df_bearing = pd.DataFrame()
    df = []
    # 建立循环，对机组内数据组从a-e或1-5依次进行读取，进行数据整合
    for j in range(0, len(datafile_path)):
        df_temp = pd.read_csv(datafile_path[j])
        df.append(df_temp)

    df_bearing = pd.concat(df)
    df_bearing['label'] = label
    df_bearing.to_csv(out_path, index=False)

dataget(r'D:\py-program\phm_zhoucheng\dataset\B', r'D:\py-program\phm_zhoucheng\dataset\data_expend\B_data.csv',1)
dataget(r'D:\py-program\phm_zhoucheng\dataset\IR', r'D:\py-program\phm_zhoucheng\dataset\data_expend\IR_data.csv',3)
dataget(r'D:\py-program\phm_zhoucheng\dataset\OR', r'D:\py-program\phm_zhoucheng\dataset\data_expend\OR_data.csv',2)
dataget(r'D:\py-program\phm_zhoucheng\dataset\NORMAL', r'D:\py-program\phm_zhoucheng\dataset\data_expend\NORMAL_data.csv',0)