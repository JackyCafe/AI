from matplotlib.colors import ListedColormap
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score



def get_key(dict, value):
    for k, v in dict.items():
        if v == value:
            return k


# 載入X,Y 資料
df = pd.read_csv("../csv/param/tempture2group.csv")
tempture_datas =  pd.DataFrame(df,columns=["Group", "Product", "Pt", "Init_tempture","Tempture2"])

#分為
X_train,X_test,Y_base_train,Y_base_test = train_test_split(
     tempture_datas[["Product",  "Init_tempture","Tempture2"]],tempture_datas[['Group']]
    ,test_size=0.2,random_state=2)

Y_train = np.array(Y_base_train).ravel()
Y_test  = np.array(Y_base_test).ravel()
#
# #StrandardScaler
sc = StandardScaler()
print(X_train.to_numpy()[:,0:2])
# # 初始溫度
sc.fit(X_train.to_numpy()[:,0:2])
X_train_std = sc.transform(X_train.to_numpy()[:,0:2])
X_test_std  = sc.transform(X_test.to_numpy()[:,0:2])


# # #
svm = SVC(kernel='rbf',verbose=False)
svm.fit(X_train_std,Y_train)
#
X_test_predict = svm.predict(X_test_std)
score = accuracy_score(Y_test,X_test_predict)
print(f"初始溫度 ==>群組 ：accuracy_score:{score}")
#
# #初始溫度+6小時斜率
sc.fit(X_train.to_numpy()[:,0:3])
X_train_std = sc.transform(X_train.to_numpy()[:,0:3])
X_test_std  = sc.transform(X_test.to_numpy()[:,0:3])
# #
svm = SVC(kernel='rbf',verbose=False)
svm.fit(X_train_std,Y_train)
X_test_predict = svm.predict(X_test_std)
score = accuracy_score(Y_test,X_test_predict)
print(f"初始溫度+6小時斜率 ==>熱偶線：accuracy_score:{score}")
