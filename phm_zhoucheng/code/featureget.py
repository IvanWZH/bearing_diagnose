import pandas as pd
import numpy as np
import os
from scipy import stats
from scipy import signal
from pywt import wavedec
#列名定义
df_out_columns = ['time_mean','time_std','time_ptp','time_median','time_skew','time_kurtosis','time_var','time_amp',
                  'time_rms','time_smr','time_max','time_min','time_wavefactor','time_peakfactor','time_pulse','time_margin',
                  'freq_1X','freq_2X','freq_3X','freq_1XRatio','freq_2XRatio','freq_3XRatio','freq_mean','freq_std',
                  'freq_max','freq_min','freq_rms','freq_median',
                  'ratio_cA5','ratio_cD1','ratio_cD2','ratio_cD3','ratio_cD4','ratio_cD5']
DE_columns = ['DE_' + i for i in df_out_columns]
FE_columns = ['FE_' + i for i in df_out_columns]
full_columns = DE_columns + FE_columns
def print_label(inputfile,label):
    df = pd.read_csv(inputfile)
    df['label'] = label
    df.to_csv(inputfile,index=False)

def feature_get(inputfile,outputfile,win_len,label):
    result_out = []
    df_data = pd.read_csv(inputfile)
    if label == None:
        df_data=df_data.iloc[:,:-1]
    else:
        df_data = df_data.iloc[:,:-2]
    result_out.append(full_columns)
    sum = len(df_data)

    for i in range(0,sum,win_len):
        df = df_data[i:i+win_len]
        result_list = []
        for j in df.columns:
            #时域特征
            time_mean = df[j].mean()
            time_std = df[j].std()
            time_ptp = np.asarray(df[j]).ptp()
            time_median = np.median(df[j])
            time_skew = stats.skew(df[j])
            time_kurtosis = stats.kurtosis(df[j])
            time_var = np.var(df[j])
            time_amp = np.abs(df[j]).mean()
            time_rms = np.sqrt(np.square(df[j]).mean())
            time_smr = np.square(np.sqrt(np.abs(df[j])).mean())
            time_max = df[j].max()
            time_min = df[j].min()
            time_wavefactor = time_rms / time_amp
            time_peakfactor = time_max / time_rms
            time_pulse = time_max / time_amp
            time_margin = time_max / time_smr
            # 频域特征
            plist_raw = np.fft.fft(list(df[j]), n=1024)  # 做1024点快速傅里叶变换
            plist = np.abs(plist_raw)  # 取绝对值
            plist_energy = (np.square(plist)).sum()  # 频域信号的总能量
            freq_1X = plist[32]
            freq_2X = plist[64]
            freq_3X = plist[96]
            freq_1XRatio = np.square(plist[32]) / plist_energy
            freq_2XRatio = np.square(plist[64]) / plist_energy
            freq_3XRatio = np.square(plist[96]) / plist_energy
            freq_mean = plist.mean()
            freq_std = plist.std()
            freq_max = plist.max()
            freq_min = plist.min()
            freq_rms = np.sqrt(np.square(plist).mean())
            freq_median = np.median(plist)
            # 5级小波变换，最后输出6个能量特征和其归一化能量特征
            cA5, cD5, cD4, cD3, cD2, cD1 = wavedec(df[j], 'db10', level=5)
            ener_cA5 = np.square(cA5).sum()
            ener_cD5 = np.square(cD5).sum()
            ener_cD4 = np.square(cD4).sum()
            ener_cD3 = np.square(cD3).sum()
            ener_cD2 = np.square(cD2).sum()
            ener_cD1 = np.square(cD1).sum()
            ener = ener_cA5 + ener_cD1 + ener_cD2 + ener_cD3 + ener_cD4 + ener_cD5
            ratio_cA5 = ener_cA5 / ener
            ratio_cD5 = ener_cD5 / ener
            ratio_cD4 = ener_cD4 / ener
            ratio_cD3 = ener_cD3 / ener
            ratio_cD2 = ener_cD2 / ener
            ratio_cD1 = ener_cD1 / ener

           
            list_para = [time_mean,time_std,time_ptp,time_median,time_skew,time_kurtosis,time_var,time_amp,time_rms,time_smr,time_max,
                         time_min,time_wavefactor,time_peakfactor,time_pulse,time_margin,freq_1X,freq_2X,freq_3X,freq_1XRatio,
                         freq_2XRatio,freq_3XRatio,freq_mean,freq_std,freq_max,freq_min,freq_rms,freq_median,
                         ratio_cA5,ratio_cD1,ratio_cD2,ratio_cD3,ratio_cD4,ratio_cD5]
            result_list.extend(list_para)
        result_out.append(result_list)

    df_out = pd.DataFrame(result_out)
    df_out.to_csv(outputfile,index=False,header=None)
    if label != None:
        print_label(outputfile,label)

feature_get(r'D:\py-program\phm_zhoucheng\train_set\B_train.csv',r'D:\py-program\phm_zhoucheng\featureset\B_feature.csv',400,1)
feature_get(r'D:\py-program\phm_zhoucheng\train_set\IR_train.csv',r'D:\py-program\phm_zhoucheng\featureset\IR_feature.csv',400,3)
feature_get(r'D:\py-program\phm_zhoucheng\train_set\NORMAL_train.csv',r'D:\py-program\phm_zhoucheng\featureset\NORMAL_feature.csv',400,0)
feature_get(r'D:\py-program\phm_zhoucheng\train_set\OR_train.csv',r'D:\py-program\phm_zhoucheng\featureset\OR_feature.csv',400,2)