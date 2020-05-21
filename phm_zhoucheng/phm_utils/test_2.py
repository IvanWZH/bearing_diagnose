import pandas as pd
import joblib
from phm_utils import pre_processing,feature_processing
import csv
import os
import collections


clf = joblib.load(r'D:\py-program\phm_zhoucheng\model\final\(90.84)LGB_ne400_md10_nl1023_ff0.8(IF0.0005-0.0001).model')#加载训练好的模型

#原始测试集路径下各个文件的文件名
dirs_test = os.listdir(r'D:\py-program\phm_zhoucheng\test_set_2\test')
dirs_test.sort(key=lambda x: int(x.split('T')[2][:-4]))
#各个原始测试文件的路径列表
inputfile_path = [os.path.join(r'D:\py-program\phm_zhoucheng\test_set_2\test', name) for name in dirs_test]
#数据对齐后的文件保存路径列表
dimctrl_path = [os.path.join(r'D:\py-program\phm_zhoucheng\test_set_2\test_dimctrl', name) for name in dirs_test]
#数据清洗后的文件保存路径列表
cleandata_path = [os.path.join(r'D:\py-program\phm_zhoucheng\test_set_2\test_cleaned',name) for name in dirs_test]
#提取特征后的文件保存路径列表
feature_path  = [os.path.join(r'D:\py-program\phm_zhoucheng\test_set_2\test_feature',name) for name in dirs_test]
#筛选特征后的文件保存路径列表
finalfeature_path = [os.path.join(r'D:\py-program\phm_zhoucheng\test_set_2\test_finalfeature',name) for name in dirs_test]
label = ['label']
filename = ['filename']
for i in range(0,142):
    pre_processing.dim_ctrl(inputfile_path[i], dimctrl_path[i])#数据对齐
    pre_processing.datacleaning_if(dimctrl_path[i], cleandata_path[i],0.0001)#数据清洗
    feature_processing.feature_get_new(cleandata_path[i],feature_path[i],400,None)#特征提取
    feature_processing.feature_select_new(feature_path[i],finalfeature_path[i])#特征筛选

    feature = []
    csv_file = csv.reader(open(finalfeature_path[i]))
    for content in csv_file:
        content = list(map(float, content))
        if len(content) != 0:
            feature.append(content)

    print("测试文件",i+1,'的预测结果如下')
    label_pred = clf.predict(feature)
    print(label_pred)
    label_pred.sort()
    label_pred[:] = collections.Counter(label_pred).most_common(1)[0][0]
    print(label_pred)
    label.extend(label_pred)
    for j in range(0,len(label_pred)):
        filename.append(str(dirs_test[i]).split('.')[0])
label = pd.DataFrame(label)
filename = pd.DataFrame(filename)
result_df = [label,filename]
result_df = pd.concat(result_df,axis=1)
result_df.to_csv(r'D:\py-program\phm_zhoucheng\final_result\0424_LGB_ne400_md10_nl1023_ff0.8(IF0.0005-0.0001)(new).csv',index=None,header=None)



