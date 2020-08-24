from matplotlib.colors import ListedColormap
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

# 載入X,Y 資料
df = pd.read_csv("param.csv")
X =  pd.DataFrame(df.to_numpy()[:,1:7],columns=["Product", "Pt", "Init_tempture","Tempture2 ","Hold_tempture","Hold_time"])
Y =  pd.DataFrame(df.to_numpy()[:,0:1],columns=["Group"])
#Y =  pd.DataFrame(df.to_numpy()[:,5:6],columns=["Group_num"])
#將X,Y 資料合併
tempture_datas =  pd.concat([X,Y],axis = 1)

#分為
X_train,X_test,Y_base_train,Y_base_test = train_test_split(
     tempture_datas[["Product", "Pt", "Init_tempture","Tempture2 ","Hold_tempture","Hold_time"]],tempture_datas[['Group']]
    ,test_size=0.2,random_state=0)

Y_train = np.array(Y_base_train).ravel()
Y_test  = np.array(Y_base_test).ravel()

#StrandardScaler
sc = StandardScaler()
# 初始溫度
sc.fit(X_train.to_numpy()[:,2:3])
X_train_std = sc.transform(X_train.to_numpy()[:,2:3])
X_test_std  = sc.transform(X_test.to_numpy()[:,2:3])
# #
svm = SVC(kernel='rbf',verbose=False)
svm.fit(X_train_std,Y_train)

X_test_predict = svm.predict(X_test_std)
score = accuracy_score(Y_test,X_test_predict)
print(f"初始溫度 ：accuracy_score:{score}")

#初始溫度+6小時斜率
sc.fit(X_train.to_numpy()[:,2:4])
X_train_std = sc.transform(X_train.to_numpy()[:,2:4])
X_test_std  = sc.transform(X_test.to_numpy()[:,2:4])
# #
svm = SVC(kernel='rbf',verbose=False)
svm.fit(X_train_std,Y_train)
X_test_predict = svm.predict(X_test_std)
score = accuracy_score(Y_test,X_test_predict)
print(f"初始溫度+6小時斜率 ：accuracy_score:{score}")

#初始溫度+6小時斜率＋持溫溫度
sc.fit(X_train.to_numpy()[:,2:5])
X_train_std = sc.transform(X_train.to_numpy()[:,2:5])
X_test_std  = sc.transform(X_test.to_numpy()[:,2:5])
# #
svm = SVC(kernel='rbf',verbose=False)
svm.fit(X_train_std,Y_train)
X_test_predict = svm.predict(X_test_std)
score = accuracy_score(Y_test,X_test_predict)
print(f"初始溫度+6小時斜率+持溫溫度 ：accuracy_score:{score}")


#初始溫度+6小時斜率＋持溫溫度＋持溫時間
sc.fit(X_train.to_numpy()[:,2:6])
X_train_std = sc.transform(X_train.to_numpy()[:,2:6])
X_test_std  = sc.transform(X_test.to_numpy()[:,2:6])
# #
svm = SVC(kernel='rbf',verbose=False)
svm.fit(X_train_std,Y_train)
X_test_predict = svm.predict(X_test_std)
score = accuracy_score(Y_test,X_test_predict)
print(f"初始溫度+6小時斜率+持溫溫度+持溫時間 ：accuracy_score:{score}")
test_series = pd.Series(Y_test)
predict_series = pd.Series(X_test_predict)
df1 = pd.DataFrame({'test':test_series,'predict_series':predict_series})
df1.to_csv('result.csv',index=False)



def plot_decision_regions(X,y,resolution=0.02 ):
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])
    x1_min, x1_max = X[:, 0].min() , X[:, 0].max()+1
    x2_min, x2_max = X[:, 1].min() , X[:, 1].max()+1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))

    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())
    for idx, cl in enumerate(np.unique(y)):
        print(cl)
    # for idx, cl in enumerate(np.unique(y)):
    #     print(idx)
    #     plt.scatter(x=X[y == cl, 0],
    #                 y=X[y == cl, 1],
    #                 alpha=0.1,
    #                 c=cmap(idx),
    #                 edgecolor='black',
    #                 marker=markers[idx],
    #                 label=cl)
    # plt.scatter(X[:, 0],
    #             X[:, 1],
    #             c='',
    #             alpha=0.1,
    #             edgecolor='black',
    #             linewidths=1,
    #             marker='o',
    #             s=55, label='test set')
    plt.show()
    return x1_min,x1_max,x2_min, x2_max
#print(X.to_numpy()[:, 2:3])
#x1_min,x1_max,x2_min, x2_max = plot_decision_regions(X.to_numpy()[:, 2:3],Y)
# print(x1_min,x1_max,x2_min, x2_max)