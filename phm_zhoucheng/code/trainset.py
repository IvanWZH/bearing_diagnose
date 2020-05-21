import pandas as pd

df1 = pd.read_csv(r'D:\py-program\phm_zhoucheng\datacleaned\B_cleandata.csv')
df2 = pd.read_csv(r'D:\py-program\phm_zhoucheng\datacleaned\IR_cleandata.csv')
df3 = pd.read_csv(r'D:\py-program\phm_zhoucheng\datacleaned\NORMAL_cleandata.csv')
df4 = pd.read_csv(r'D:\py-program\phm_zhoucheng\datacleaned\OR_cleandata.csv')


df1 = df1.loc[:,['DE_time','FE_time','RPM','label']]
df2 = df2.loc[:,['DE_time','FE_time','RPM','label']]
df3 = df3.loc[:,['DE_time','FE_time','RPM','label']]
df4 = df4.loc[:,['DE_time','FE_time','RPM','label']]

df1.to_csv(r'D:\py-program\phm_zhoucheng\train_set\B_train.csv',index=False)
df2.to_csv(r'D:\py-program\phm_zhoucheng\train_set\IR_train.csv',index=False)
df3.to_csv(r'D:\py-program\phm_zhoucheng\train_set\NORMAL_train.csv',index=False)
df4.to_csv(r'D:\py-program\phm_zhoucheng\train_set\OR_train.csv',index=False)
df_temp = [df1,df2,df3,df4]
df_result = pd.concat(df_temp)
df_result.to_csv(r'D:\py-program\phm_zhoucheng\train_set\train.csv',index=False,header=None)

