from matplotlib.colors import ListedColormap
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
group_list = {'G01_715':1,
'G02_715':2,
'G11-3_930':3,
'G11-5_715':4,
'G13_715':5,
'G13-B_715':6,
'G15_1230':7,
'G21_1230':8,
'G49_1030':9,
 }

pt_list ={
    'PTC1':1,
    'PTC2':2,
    'PTC3': 3,
    'PTC4': 4,
    'PTC5': 5,
    'PTC6': 6,
    'PTC7': 7,
    'PTC8': 8,
    'PTC9': 9,
    'PTC10': 10,
    'PTC11': 11,
    'PTC12': 12,
    'PTC13': 13,
    'PTC14': 14,
    'PTC15': 15,
    'PTC16': 16,
    'PTC17': 17,
    'PTC18': 18,
    'PTC19': 19,
    'PTC20': 20,
    'PTC21': 21,
    'PTC22': 22,
    'PTC23': 23,
    'PTC24': 24,
    'PTC25': 25,
    'PTC26': 26,
    'PTC27': 27,
    'PTC28': 28,
    'PTC29': 29,
    'PTC30': 30,
    'PTC31': 31,
    'PTC32': 32,
    'PTC33': 33,
    'PTC34': 34,
    'PTC35': 35,
    'PTC36': 36,
    'PTC37': 37,
    'PTC38': 38,
    'PTC39': 39,
    'PTC40': 40
}

def get_key(dict, value):
    for k, v in dict.items():
        if v == value:
            return k


# 載入X,Y 資料
df = pd.read_csv("..\\csv\\param\\ptc2product.csv")
# #將X,Y 資料合併

tempture_datas =  pd.DataFrame(df,columns=["Group", "Product", "Pt", "Init_tempture","Tempture2","Hold_tempture","Hold_time"])

#分為
X_train,X_test,Y_base_train,Y_base_test = train_test_split(
     tempture_datas[["Group","Pt",  "Init_tempture","Tempture2","Hold_tempture","Hold_time"]],tempture_datas[['Product']]
    ,test_size=0.2,random_state=0)

Y_train = np.array(Y_base_train).ravel()
Y_test  = np.array(Y_base_test).ravel()
#
# #StrandardScaler
sc = StandardScaler()

# #  Input Param :
# 1、Group
# 2、Pt、
# 3、Init_temp
#  Predict -->Product
sc.fit(X_train.to_numpy()[:,0:3])
X_train_std = sc.transform(X_train.to_numpy()[:,0:3])
X_test_std  = sc.transform(X_test.to_numpy()[:,0:3])

# # #
svm = SVC(kernel='rbf',verbose=False)
svm.fit(X_train_std,Y_train)
#
X_test_predict = svm.predict(X_test_std)
score = accuracy_score(Y_test,X_test_predict)
print(f"初始溫度 ==>熱偶線 ：accuracy_score:{score}")

group_array = []
groups = X_test.get('Group').to_numpy()
for group in groups:
    group_array.append(get_key(group_list,group))

pt_array = []
pts = X_test.get('Pt')
for pt in pts:
    pt_array.append(get_key(pt_list,pt))

group_series = pd.Series(group_array).to_numpy()
pt_series = pd.Series(pt_array).to_numpy()
init_tempture = pd.Series(X_test.get('Init_tempture').to_numpy())
test_series = pd.Series(Y_test)
predict_series = pd.Series(X_test_predict)

df1 = pd.DataFrame({'Group':group_series,'PTC': pt_series
                       ,'init_tempture':init_tempture ,'predict_series':predict_series
                       ,'actual':test_series})
df1.to_csv('..\\csv\\result\\ptc_init_temp2product.csv',index=False)


# #  Input Param :
# 1、Group
# 2、Pt、
# 3、Init_temp、
# 4、Slope
#  Predict -->Product
sc.fit(X_train.to_numpy()[:,0:4])
X_train_std = sc.transform(X_train.to_numpy()[:,0:4])
X_test_std  = sc.transform(X_test.to_numpy()[:,0:4])
# #
svm = SVC(kernel='rbf',verbose=False)
svm.fit(X_train_std,Y_train)
X_test_predict = svm.predict(X_test_std)
score = accuracy_score(Y_test,X_test_predict)
print(f"初始溫度+6小時斜率 ==>熱偶線：accuracy_score:{score}")
#
group_array = []
groups = X_test.get('Group').to_numpy()
for group in groups:
    group_array.append(get_key(group_list,group))

pt_array = []
pts = X_test.get('Pt')
for pt in pts:
    pt_array.append(get_key(pt_list,pt))

group_series = pd.Series(group_array).to_numpy()
pt_series = pd.Series(pt_array).to_numpy()
init_tempture = pd.Series(X_test.get('Init_tempture').to_numpy())
slope = pd.Series(X_test.get('Tempture2').to_numpy())
test_series = pd.Series(Y_test)
predict_series = pd.Series(X_test_predict)
df2 = pd.DataFrame({'Group':group_series,'PTC': pt_series
                       ,'init_tempture':init_tempture
                       ,'slope': slope
                       ,'predict_series':predict_series,'actual':test_series})
df2.to_csv('..\\csv\\result\\ptc_slope2product.csv',index=False)
