import pandas as pd
df_out_columns = ['time_mean','time_std','time_max','time_min','time_rms','time_ptp','time_median','time_iqr','time_pr','time_skew','time_kurtosis','time_var','time_amp',
                    'time_smr','time_wavefactor','time_peakfactor','time_pulse','time_margin','freq_mean','freq_std','freq_max','freq_min','freq_rms','freq_median',
                    'freq_iqr','freq_pr','freq_f2','freq_f3','freq_f4','freq_f5','freq_f6','freq_f7','freq_f8','ener_cA5','ener_cD1','ener_cD2','ener_cD3','ener_cD4',
                    'ener_cD5','ratio_cA5','ratio_cD1','ratio_cD2','ratio_cD3','ratio_cD4','ratio_cD5']
DE_columns = ['DE_' + i for i in df_out_columns]
FE_columns = ['FE_' + i for i in df_out_columns]
full_columns = DE_columns + FE_columns+['label']

df1 = pd.read_csv(r'D:\py-program\phm_zhoucheng\featureset\B_feature.csv')
df2 = pd.read_csv(r'D:\py-program\phm_zhoucheng\featureset\IR_feature.csv')
df3 = pd.read_csv(r'D:\py-program\phm_zhoucheng\featureset\NORMAL_feature.csv')
df4 = pd.read_csv(r'D:\py-program\phm_zhoucheng\featureset\OR_feature.csv')
df_temp = [df1,df2,df3,df4]
df = pd.concat(df_temp)
feature_selected_list = ['DE_time_mean','DE_time_std','DE_time_rms','DE_time_ptp','DE_time_median',
                         'DE_time_wavefactor','DE_time_peakfactor','DE_time_pulse','DE_time_margin','DE_freq_mean','DE_freq_std',
                         'DE_freq_f2','DE_freq_f3','DE_freq_f4','DE_freq_f5','DE_freq_f6','DE_freq_f7','DE_freq_f8',
                         'DE_ener_cA5','DE_ener_cD1','DE_ener_cD2','DE_ener_cD3','DE_ener_cD4','DE_ener_cD5',
                         'DE_ratio_cA5','DE_ratio_cD1','DE_ratio_cD2','DE_ratio_cD3','DE_ratio_cD4','DE_ratio_cD5',
                         'FE_time_mean','FE_time_std','FE_time_rms','FE_time_ptp','FE_time_median',
                         'FE_time_wavefactor','FE_time_peakfactor','FE_time_pulse','FE_time_margin','FE_freq_mean','FE_freq_std',
                         'FE_freq_f2','FE_freq_f3','FE_freq_f4','FE_freq_f5','FE_freq_f6','FE_freq_f7','FE_freq_f8',
                         'FE_ener_cA5','FE_ener_cD1','FE_ener_cD2','FE_ener_cD3','FE_ener_cD4','FE_ener_cD5',
                         'FE_ratio_cA5','FE_ratio_cD1','FE_ratio_cD2','FE_ratio_cD3','FE_ratio_cD4','FE_ratio_cD5','label']
feature_selected = df[full_columns]
# 筛选后特征保存
feature_selected.to_csv(r'D:\py-program\phm_zhoucheng\featureset\feature_selected.csv',index=False,header=None)
