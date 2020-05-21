import pandas as pd
import numpy as np
import os
from scipy import stats,signal,fftpack
from pywt import wavedec
import math


def print_label(inputfile,label):
    df = pd.read_csv(inputfile)
    df['label'] = label
    df.to_csv(inputfile,index=False)

def feature_get(inputfile,outputfile,win_len,label):
    df_out_columns = ['time_mean', 'time_std', 'time_ptp', 'time_median', 'time_skew', 'time_kurtosis', 'time_var',
                      'time_amp',
                      'time_rms', 'time_smr', 'time_max', 'time_min', 'time_wavefactor', 'time_peakfactor',
                      'time_pulse', 'time_margin',
                      'freq_1X', 'freq_2X', 'freq_3X', 'freq_1XRatio', 'freq_2XRatio', 'freq_3XRatio', 'freq_mean',
                      'freq_std',
                      'freq_max', 'freq_min', 'freq_rms', 'freq_median',
                      'ratio_cA5', 'ratio_cD1', 'ratio_cD2', 'ratio_cD3', 'ratio_cD4', 'ratio_cD5']
    DE_columns = ['DE_' + i for i in df_out_columns]
    FE_columns = ['FE_' + i for i in df_out_columns]
    full_columns = DE_columns + FE_columns

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
    df_out = df_out.dropna(axis=0, how='any', inplace=False)
    df_out.to_csv(outputfile,index=False,header=None)

    if label != None:
        print_label(outputfile,label)

def feature_select(inputfile,outputfile):
    df = pd.read_csv(inputfile)
    feature_selected_list = ['DE_freq_1XRatio', 'DE_freq_2XRatio', 'DE_freq_3XRatio',
                             'FE_freq_1XRatio', 'FE_freq_2XRatio', 'FE_freq_3XRatio',
                             'DE_freq_1X', 'DE_freq_2X', 'DE_freq_3X',
                             'FE_freq_1X', 'FE_freq_2X', 'FE_freq_3X',
                             'DE_time_ptp', 'FE_time_ptp']
    df_out_columns = ['time_mean', 'time_std', 'time_ptp', 'time_median', 'time_skew', 'time_kurtosis', 'time_var',
                      'time_amp',
                      'time_rms', 'time_smr', 'time_max', 'time_min', 'time_wavefactor', 'time_peakfactor',
                      'time_pulse', 'time_margin',
                      'freq_1X', 'freq_2X', 'freq_3X', 'freq_1XRatio', 'freq_2XRatio', 'freq_3XRatio', 'freq_mean',
                      'freq_std',
                      'freq_max', 'freq_min', 'freq_rms', 'freq_median',
                      'ratio_cA5', 'ratio_cD1', 'ratio_cD2', 'ratio_cD3', 'ratio_cD4', 'ratio_cD5']
    DE_columns = ['DE_' + i for i in df_out_columns]
    FE_columns = ['FE_' + i for i in df_out_columns]
    full_columns = DE_columns + FE_columns #输出分类结果时使用
    #full_columns = DE_columns + FE_columns+['label'] #评估分类效果时使用
    feature_selected = df[full_columns]
    # 筛选后特征保存
    feature_selected.to_csv(outputfile, index=False, header=None)
    #feature_selected.to_csv(outputfile, index=False) # 评估效果时使用



def feature_get_new(inputfile, outputfile, win_len, label):
    # 列名定义
    df_out_columns = ['time_mean', 'time_std', 'time_max', 'time_min', 'time_rms', 'time_ptp', 'time_median',
                      'time_iqr', 'time_pr', 'time_skew', 'time_kurtosis', 'time_var', 'time_amp',
                      'time_smr', 'time_wavefactor', 'time_peakfactor', 'time_pulse', 'time_margin', 'freq_mean',
                      'freq_std', 'freq_max', 'freq_min', 'freq_rms', 'freq_median',
                      'freq_iqr', 'freq_pr', 'freq_f2', 'freq_f3', 'freq_f4', 'freq_f5', 'freq_f6', 'freq_f7',
                      'freq_f8', 'ener_cA5', 'ener_cD1', 'ener_cD2', 'ener_cD3', 'ener_cD4',
                      'ener_cD5', 'ratio_cA5', 'ratio_cD1', 'ratio_cD2', 'ratio_cD3', 'ratio_cD4', 'ratio_cD5']
    DE_columns = ['DE_' + i for i in df_out_columns]
    FE_columns = ['FE_' + i for i in df_out_columns]
    full_columns = DE_columns + FE_columns

    result_out = []
    df_data = pd.read_csv(inputfile)
    if label == None:
        df_data = df_data.iloc[:, :-1]
    else:
        df_data = df_data.iloc[:, :-2]
    result_out.append(full_columns)
    sum = len(df_data)

    for j in range(0, sum, win_len):
        df = df_data[j:j + win_len]
        result_list = []
        for i in df.columns:
            # ----------  time-domain feature,18
            # 依次为均值，标准差，最大值，最小值，均方根，峰峰值，中位数，四分位差，百分位差，偏度，峰度，方差，整流平均值，方根幅值，波形因子，峰值因子，脉冲值，裕度
            df_line = df[i]
            time_mean = df_line.mean()
            time_std = df_line.std()
            time_max = df_line.max()
            time_min = df_line.min()
            time_rms = np.sqrt(np.square(df_line).mean())
            time_ptp = df_line.ptp()
            time_median = np.median(df_line)
            time_iqr = np.percentile(df_line, 75) - np.percentile(df_line, 25)
            time_pr = np.percentile(df_line, 90) - np.percentile(df_line, 10)
            time_skew = stats.skew(df_line)
            time_kurtosis = stats.kurtosis(df_line)
            time_var = np.var(df_line)
            time_amp = np.abs(df_line).mean()
            time_smr = np.square(np.sqrt(np.abs(df_line)).mean())
            # 下面四个特征需要注意分母为0或接近0问题，可能会发生报错
            time_wavefactor = time_rms / time_amp
            time_peakfactor = time_max / time_rms
            time_pulse = time_max / time_amp
            time_margin = time_max / time_smr
            # ----------  freq-domain feature,15
            # 采样频率25600Hz
            df_fftline = fftpack.fft(df[i])
            freq_fftline = fftpack.fftfreq(len(df[i]), 1 / 25600)
            df_fftline = abs(df_fftline[freq_fftline >= 0])
            freq_fftline = freq_fftline[freq_fftline >= 0]
            # 基本特征,依次为均值，标准差，最大值，最小值，均方根，中位数，四分位差，百分位差
            freq_mean = df_fftline.mean()
            freq_std = df_fftline.std()
            freq_max = df_fftline.max()
            freq_min = df_fftline.min()
            freq_rms = np.sqrt(np.square(df_fftline).mean())
            freq_median = np.median(df_fftline)
            freq_iqr = np.percentile(df_fftline, 75) - np.percentile(df_fftline, 25)
            freq_pr = np.percentile(df_fftline, 90) - np.percentile(df_fftline, 10)
            # f2 f3 f4反映频谱集中程度
            freq_f2 = np.square((df_fftline - freq_mean)).sum() / (len(df_fftline) - 1)
            freq_f3 = pow((df_fftline - freq_mean), 3).sum() / (len(df_fftline) * pow(freq_f2, 1.5))
            freq_f4 = pow((df_fftline - freq_mean), 4).sum() / (len(df_fftline) * pow(freq_f2, 2))
            # f5 f6 f7 f8反映主频带位置
            freq_f5 = np.multiply(freq_fftline, df_fftline).sum() / df_fftline.sum()
            freq_f6 = np.sqrt(np.multiply(np.square(freq_fftline), df_fftline).sum()) / df_fftline.sum()
            freq_f7 = np.sqrt(np.multiply(pow(freq_fftline, 4), df_fftline).sum()) / np.multiply(
                np.square(freq_fftline), df_fftline).sum()
            freq_f8 = np.multiply(np.square(freq_fftline), df_fftline).sum() / np.sqrt(
                np.multiply(pow(freq_fftline, 4), df_fftline).sum() * df_fftline.sum())
            # ----------  timefreq-domain feature,12
            # 5级小波变换，最后输出6个能量特征和其归一化能量特征
            cA5, cD5, cD4, cD3, cD2, cD1 = wavedec(df[i], 'db10', level=5)
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

            list_para = [time_mean,time_std,time_max,time_min,time_rms,time_ptp,time_median,time_iqr,time_pr,time_skew,time_kurtosis,time_var,time_amp,
                                 time_smr,time_wavefactor,time_peakfactor,time_pulse,time_margin,freq_mean,freq_std,freq_max,freq_min,freq_rms,freq_median,
                                 freq_iqr,freq_pr,freq_f2,freq_f3,freq_f4,freq_f5,freq_f6,freq_f7,freq_f8,ener_cA5,ener_cD1,ener_cD2,ener_cD3,ener_cD4,ener_cD5,
                                 ratio_cA5,ratio_cD1,ratio_cD2,ratio_cD3,ratio_cD4,ratio_cD5]
            result_list.extend(list_para)
        result_out.append(result_list)

    df_out = pd.DataFrame(result_out)
    df_out = df_out.dropna(axis=0, how='any', inplace=False)
    df_out.to_csv(outputfile, index=False, header=None)
    if label != None:
        print_label(outputfile, label)

def feature_select_new(inputfile,outputfile):
    df = pd.read_csv(inputfile)
    feature_selected_list = ['DE_time_mean','DE_time_std','DE_time_rms','DE_time_ptp','DE_time_median',
                         'DE_time_wavefactor','DE_time_peakfactor','DE_time_pulse','DE_time_margin','DE_freq_mean','DE_freq_std',
                         'DE_freq_f2','DE_freq_f3','DE_freq_f4','DE_freq_f5','DE_freq_f6','DE_freq_f7','DE_freq_f8',
                         'DE_ener_cA5','DE_ener_cD1','DE_ener_cD2','DE_ener_cD3','DE_ener_cD4','DE_ener_cD5',
                         'DE_ratio_cA5','DE_ratio_cD1','DE_ratio_cD2','DE_ratio_cD3','DE_ratio_cD4','DE_ratio_cD5',
                         'FE_time_mean','FE_time_std','FE_time_rms','FE_time_ptp','FE_time_median',
                         'FE_time_wavefactor','FE_time_peakfactor','FE_time_pulse','FE_time_margin','FE_freq_mean','FE_freq_std',
                         'FE_freq_f2','FE_freq_f3','FE_freq_f4','FE_freq_f5','FE_freq_f6','FE_freq_f7','FE_freq_f8',
                         'FE_ener_cA5','FE_ener_cD1','FE_ener_cD2','FE_ener_cD3','FE_ener_cD4','FE_ener_cD5',
                         'FE_ratio_cA5','FE_ratio_cD1','FE_ratio_cD2','FE_ratio_cD3','FE_ratio_cD4','FE_ratio_cD5']
    df_out_columns = ['time_mean','time_std','time_max','time_min','time_rms','time_ptp','time_median','time_iqr','time_pr','time_skew','time_kurtosis','time_var','time_amp',
                    'time_smr','time_wavefactor','time_peakfactor','time_pulse','time_margin','freq_mean','freq_std','freq_max','freq_min','freq_rms','freq_median',
                    'freq_iqr','freq_pr','freq_f2','freq_f3','freq_f4','freq_f5','freq_f6','freq_f7','freq_f8','ener_cA5','ener_cD1','ener_cD2','ener_cD3','ener_cD4',
                    'ener_cD5','ratio_cA5','ratio_cD1','ratio_cD2','ratio_cD3','ratio_cD4','ratio_cD5']
    DE_columns = ['DE_' + i for i in df_out_columns]
    FE_columns = ['FE_' + i for i in df_out_columns]
    full_columns = DE_columns + FE_columns #输出分类结果时使用
    feature_selected = df[full_columns]
    # 筛选后特征保存
    feature_selected.to_csv(outputfile, index=False, header=None)



