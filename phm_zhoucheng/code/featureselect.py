import pandas as pd
df_out_columns = ['time_mean','time_std','time_ptp','time_median','time_skew','time_kurtosis','time_var','time_amp',
                  'time_rms','time_smr','time_max','time_min','time_wavefactor','time_peakfactor','time_pulse','time_margin',
                  'freq_1X','freq_2X','freq_3X','freq_1XRatio','freq_2XRatio','freq_3XRatio','freq_mean','freq_std',
                  'freq_max','freq_min','freq_rms','freq_median',
                  'ratio_cA5','ratio_cD1','ratio_cD2','ratio_cD3','ratio_cD4','ratio_cD5']
DE_columns = ['DE_' + i for i in df_out_columns]
FE_columns = ['FE_' + i for i in df_out_columns]
full_columns = DE_columns + FE_columns+['label']

df1 = pd.read_csv(r'D:\py-program\phm_zhoucheng\featureset\B_feature.csv')
df2 = pd.read_csv(r'D:\py-program\phm_zhoucheng\featureset\IR_feature.csv')
df3 = pd.read_csv(r'D:\py-program\phm_zhoucheng\featureset\NORMAL_feature.csv')
df4 = pd.read_csv(r'D:\py-program\phm_zhoucheng\featureset\OR_feature.csv')
df_temp = [df1,df2,df3,df4]
df = pd.concat(df_temp)
feature_selected_list = ['DE_freq_1XRatio', 'DE_freq_2XRatio', 'DE_freq_3XRatio',
                             'FE_freq_1XRatio', 'FE_freq_2XRatio', 'FE_freq_3XRatio',
                             'DE_freq_1X', 'DE_freq_2X', 'DE_freq_3X',
                             'FE_freq_1X', 'FE_freq_2X', 'FE_freq_3X',
                             'DE_time_ptp', 'FE_time_ptp','label']
feature_selected = df[full_columns]
# 筛选后特征保存
feature_selected.to_csv(r'D:\py-program\phm_zhoucheng\featureset\feature_selected.csv',index=False,header=None)
