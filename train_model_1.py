from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score

# 載入X,Y 資料
df = pd.read_csv("param.csv")
tempture_datas = pd.DataFrame(df.to_numpy(),columns=["Group", "Pt","Product",  "Init_tempture","Tempture2 ","Hold_tempture","Hold_time"])
 #分為
X_train,X_test,Y_label_train,Y_label_test = train_test_split(
     tempture_datas[["Product", "Pt",  "Init_tempture","Tempture2 ","Hold_tempture","Hold_time"]],tempture_datas[["Group"]]
    ,test_size=0.2,random_state=0)

# 初始溫度
#=====================================================================
sc = StandardScaler()

sc.fit(X_train.to_numpy()[:,2:3])
X_train_std = sc.transform(X_train.to_numpy()[:,2:3])
X_test_std  = sc.transform(X_test.to_numpy()[:,2:3])
svm = SVC(kernel='rbf',verbose=False)
y_train = Y_label_train.to_numpy().ravel()
y_test = Y_label_test.to_numpy().ravel()
svm.fit(X_train_std,y_train)
X_test_predict = svm.predict(X_test_std)
score = accuracy_score(y_test,X_test_predict)
print(f"初始溫度 ==>估算熱偶線 accuracy_score:{score}")
#===============================================================
#
# #初始溫度+6小時斜率
# #=====================================================================
sc = StandardScaler()
sc.fit(X_train.to_numpy()[:,2:4])
X_train_std = sc.transform(X_train.to_numpy()[:,2:4])
X_test_std  = sc.transform(X_test.to_numpy()[:,2:4])
svm = SVC(kernel='rbf',verbose=False)
y_train = Y_label_train.to_numpy().ravel()
y_test = Y_label_test.to_numpy().ravel()
svm.fit(X_train_std,y_train)
X_test_predict = svm.predict(X_test_std)
score = accuracy_score(y_test,X_test_predict)
print(f"初始溫度+6小時斜率 ==> 估算熱偶線 accuracy_score:{score}")

# #=====================================================================
# #
# # #初始溫度+6小時斜率+持溫
# #==================================================================
sc = StandardScaler()
sc.fit(X_train.to_numpy()[:,2:5])
X_train_std = sc.transform(X_train.to_numpy()[:,2:5])
X_test_std  = sc.transform(X_test.to_numpy()[:,2:5])
svm = SVC(kernel='rbf',verbose=False)
y_train = Y_label_train.to_numpy().ravel()
y_test = Y_label_test.to_numpy().ravel()
svm.fit(X_train_std,y_train)
X_test_predict = svm.predict(X_test_std)
score = accuracy_score(y_test,X_test_predict)
print(f"初始溫度+6小時斜率+持溫 ==> 估算熱偶線 accuracy_score:{score}")
#
#
sc = StandardScaler()
sc.fit(X_train.to_numpy()[:,3:7])
X_train_std = sc.transform(X_train.to_numpy()[:,3:7])
X_test_std  = sc.transform(X_test.to_numpy()[:,3:7])
svm = SVC(kernel='rbf',verbose=False)
y_train = Y_label_train.to_numpy().ravel()
y_test = Y_label_test.to_numpy().ravel()
svm.fit(X_train_std,y_train)
X_test_predict = svm.predict(X_test_std)
score = accuracy_score(y_test,X_test_predict)
print(f"初始溫度+6小時斜率+持溫+持溫時間 ==> 估算熱偶線 accuracy_score:{score}")
#
# svm.fit(X_train_std,Y_train_PT)
# X_test_predict = svm.predict(X_test_std)
# score = accuracy_score(Y_test_PT,X_test_predict)
# print(f"初始溫度+6小時斜率+持溫+持溫時間 估算熱偶線 accuracy_score:{score}")

# print(f"初始溫度+6小時斜率+持溫溫度+持溫時間 ：accuracy_score:{score}")
# test_series = pd.Series(Y_test)
# predict_series = pd.Series(X_test_predict)
# df1 = pd.DataFrame({'test':test_series,'predict_series':predict_series})
# df1.to_csv('result.csv',index=False)
