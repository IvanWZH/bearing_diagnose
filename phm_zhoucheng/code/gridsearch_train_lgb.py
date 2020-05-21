import lightgbm as lgb
import csv
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import joblib
from sklearn.model_selection import GridSearchCV

data=[]
feature=[]
target=[]
csv_file = csv.reader(open(r'D:\py-program\phm_zhoucheng\featureset\feature_selected.csv'))
for content in csv_file:
    content=list(map(float,content))
    if len(content)!=0:
        data.append(content)
        feature.append(content[0:-1])
        target.append(content[-1])

feature_train, feature_test, target_train, target_test = train_test_split(feature, target, test_size=0.2,random_state=0)
print(type(feature_test))
print(len(feature_test[0]))

clf = lgb.LGBMClassifier(n_estimators=400,max_depth=10,num_leaves=1023,feature_fraction=0.8)

clf.fit(feature_train, target_train)

joblib.dump(clf,r'D:\py-program\phm_zhoucheng\model\final\temp.model')

predict_results = clf.predict(feature_test)

conf_mat = confusion_matrix(target_test, predict_results)

print(conf_mat)

print(classification_report(target_test, predict_results))
