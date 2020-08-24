import os
import pandas as pd
from pandas import Series, DataFrame
from pandas.errors import EmptyDataError
from sklearn.preprocessing import OneHotEncoder

from data_collect.data_struct import data
import csv
import numpy as np

path = 'AI/'
workspaces = os.walk(path)
allfiles = []
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

product_list = {

'A11887':	1,
'A121151':	2,
'A314222':	3,
'A330530':	4,
'A35776':	5,
'A369919':	6,
'A37248':	7,
'A393450':	8,
'A46872':	9,
'A47143':	10,
'A511193':	11,
'A538130':	12,
'A555894':	13,
'A620395':	14,
'A65195':	15,
'A714858':	16,
'A726846':	17,
'A747317':	18,
'A775826':	19,
'A778989':	20,
'A794147':	21,
'A79630':	22,
'A834782':	23,
'A84462':	24,
'A85484':	25,
'A859833':	26,
'A87907589':27,
'A9017':	28,
'A913844':	29,
'A927695':	30

}

class main(data):

    # 將檔案載入allfiles
    def load_file(self) -> DataFrame:
        datas = [[0 for i in range(7)] for j in range(5000)]
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
                            tempture2 = float(temptures[i][j + 12])

                            final_tempture = 0
                            slope = 1
                            for h in range (j+36,100):
                                if (temptures[i][h]==temptures[i][h+1]):
                                    hold_tempture =  float(temptures[i][h+1])
                                    hold_time = len(temptures[i])-h
                                    #slope = (final_tempture - init_tempture)
                            if hold_tempture > 0 :
                                self.f = file
                                self.group = file[3: file.find("\\", 3)]
                                self.product = keys[0]
                                self.pt = temptures[i][0]
                                self.init_temp = init_tempture
                                self.slope = slope
                                datas[k][0] = file[3: file.find("\\", 3)] #Group
                                datas[k][1] = keys[0] # Product
                                datas[k][2] = temptures[i][0] #熱偶線
                                datas[k][3] = init_tempture #初始溫度
                                datas[k][4] = (tempture2-init_tempture)/12  #2 小時後溫度
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
        out.to_csv("./param.csv", index=False, header=["Group", "Product", "Pt", "Init_tempture","Tempture2 ","Hold_tempture","Hold_time"])

        print('OK')

    def __str__(self):
        return (super().__str__())


if __name__ == '__main__':
    m = main()
    m.load_file()