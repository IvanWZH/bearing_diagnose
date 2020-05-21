#导入作图相关库matplotlib和数据处理包pandas
import matplotlib.pyplot as plt
import pandas as pd
#训练数据的读取
df1 = pd.read_csv(r'D:\py-program\phm_zhoucheng\test_set\test\TEST01.csv')
df2 = pd.read_csv(r'D:\py-program\phm_zhoucheng\test_set\test\TEST02.csv')
df3 = pd.read_csv(r'D:\py-program\phm_zhoucheng\test_set\test\TEST03.csv')
df4 = pd.read_csv(r'D:\py-program\phm_zhoucheng\test_set\test\TEST04.csv')

##训练数据可视化
#设置画布大小
plt.figure(figsize=(20, 6))
for i in range(0,4):
    plt.subplot(1,4,i+1)
    plt.plot(df1.iloc[:, i])

plt.figure(figsize=(20, 6))
for i in range(0,4):
    plt.subplot(1,4,i+1)
    plt.plot(df2.iloc[:, i])

plt.figure(figsize=(20, 6))
for i in range(0,2):
    plt.subplot(1,2,i+1)
    plt.plot(df3.iloc[:, i])

plt.figure(figsize=(20,6))
for i in range(0,4):
    plt.subplot(1,4,i+1)
    plt.plot(df4.iloc[:, i])


plt.show()
