import pandas as pd
import joblib
import csv
import sys
from sklearn.metrics import accuracy_score,recall_score,precision_score,f1_score,roc_auc_score
import collections


class Result:
    accuracy = 0
    recall = 0
    precision = 0
    fMeasure = 0
    rocArea = 0

params = {}
params['model'] = r'D:\py-program\phm_zhoucheng\model\best_2\LGB_ne400_md10_nl1023_ff0.8(IF0.0001).model'
params['test'] = r'D:\py-program\phm_zhoucheng\test_set_1\upload_test_feature.csv'
params['opath'] = r'D:\py-program\phm_zhoucheng\test_set_1\upload_test_result.csv'
argvs = sys.argv

def diagnose(model_path, input_file, output_file):
    clf = joblib.load(model_path)
    csv_file = csv.reader(open(input_file))
    feature = []
    cnt = 0
    for content in csv_file:
        cnt += 1
        if(cnt>1):
            content = list(map(float, content))
            if len(content) != 0:
                feature.append(content)
    label_pred = clf.predict(feature)
    label_pred.sort()
    label_pred[:] = collections.Counter(label_pred).most_common(1)[0][0]
    predict_df = pd.DataFrame(label_pred)
    predict_df.columns = ['predict']
    predict_df.to_csv(output_file,index=False)
try:
    for i in range(len(argvs)):
        if i < 1:
            continue
        if argvs[i].split('=')[1] == 'None':
            params[argvs[i].split('=')[0]] = None
        else:
            Type = type(params[argvs[i].split('=')[0]])
            params[argvs[i].split('=')[0]] = Type(argvs[i].split('=')[1])
    diagnose(params['model'],params['test'],params['opath'])
except Exception as e:
    print(e)

