import os
import pandas as pd
from pandas import Series, DataFrame
from pandas.errors import EmptyDataError
from sklearn.preprocessing import OneHotEncoder

from data_collect.data_struct import data
import csv
import numpy as np

from data_process.setup import group_list, pt_list

path = '../AI/'
workspaces = os.walk(path)
allfiles = []


class main(data):

    # 將檔案載入allfiles
    def load_file(self) -> DataFrame:
        datas = [[0 for i in range(7)] for j in range(2190)]
        for root, dirs, files in workspaces:
            for file in files:
                allfiles.append(f'{root}/{file}')



        try:
            # 先以read_csv 讀為dataframe
            k = 0
            temptures = []
            i = 0
            for file in allfiles:
                df = pd.read_csv(file)
                # 將dataframe 的資料轉換成array
                keys = df.keys()

                for key in keys:
                    temptures.append(df.get(key).array)  #
                    for j in range(2, len(temptures[i])):
                        if (temptures[i][j + 1]) > (temptures[i][j]):
                            init_tempture = float(temptures[i][j + 1])
                            tempture2 = float(temptures[i][j + 24])

                            final_tempture = 0
                            slope = 1
                            for h in range (j+36,100):
                                if (temptures[i][h]==temptures[i][h+1]):
                                    hold_tempture =  float(temptures[i][h+1])
                                    hold_time = len(temptures[i])-h
                                    #slope = (final_tempture - init_tempture)
                            if hold_tempture > 0 :
                                self.f = file
                                self.group = file[6: file.find("\\", 3)]
                                self.product = keys[0]
                                self.pt = temptures[i][0]
                                self.init_temp = init_tempture
                                self.slope = slope
                                #---------------------------------------------------------------
                                #-----  熱偶線 分產品用
                                #-----  群組、PTC要編碼
                                #--------------------------------------------------------------
                                datas[k][0] = group_list.get(file[6: file.find("\\", 3)]) #Group
                                datas[k][1] = keys[0] # Product
                                datas[k][2] = pt_list.get(temptures[i][0]) #熱偶線
                                datas[k][3] = init_tempture #初始溫度
                                datas[k][4] = round(tempture2-init_tempture,2)  #2 小時後溫度
                                datas[k][5] = hold_tempture # 持溫溫度
                                datas[k][6] = hold_time #持溫時間
                                print(self)
                                k = k + 1
                            break
                    i += 1
        except EmptyDataError:
            print(file)
        except Exception as e:
            print(e)


        out = pd.DataFrame(np.array(datas))
        out.to_csv("../csv/param/ptc2product.csv", index=False, header=["Group", "Product", "Pt", "Init_tempture","Tempture2","Hold_tempture","Hold_time"])

        print('OK')

    def __str__(self):
        return (super().__str__())


if __name__ == '__main__':
    m = main()
    m.load_file()