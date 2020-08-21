import os
import pandas as pd
from pandas import Series, DataFrame
from pandas.errors import EmptyDataError
from data_collect.data_struct import data
import csv
import numpy as np

path = 'AI/'
workspaces = os.walk(path)
allfiles = []


class main(data):

    # 將檔案載入allfiles
    def load_file(self) -> DataFrame:
        datas = [[0 for i in range(6)] for j in range(2251)]
        with open("output.csv", "w") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["file", "Group", "Product", "PT", "Init_tempture", "Slope", "Group_num"])
            print("file", "Group", "Product", "PT", "Init_tempture", "Slope", "Group_num")
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
                        #      i = 0
                        # temptures = []
                        temptures.append(df.get(key).array)  #
                        for j in range(2, len(temptures[i])):
                            if (temptures[i][j + 1]) > (temptures[i][j]):
                                # pos = file.find("\\",3)
                                # print(pos)
                                init_tempture = float(temptures[i][j + 1])
                                final_tempture = float(temptures[i][j+36])
                                highest_tempture = df[df.get(key)].max()
                                slope = (final_tempture- init_tempture)/36


                                if slope > 0:
                                    self.f = file
                                    self.group = file[3: file.find("\\", 3)]
                                    self.product = keys[0]
                                    self.pt = temptures[i][0]
                                    self.init_temp = init_tempture
                                    self.slope = slope
                                    datas[k][0] = file[3: file.find("\\", 3)]
                                    datas[k][1] = keys[0]
                                    datas[k][2] = temptures[i][0]
                                    datas[k][3] = init_tempture
                                    datas[k][4] = highest_tempture
                                    datas[k][5] = slope
                                    # writer.writerow({self})
                                    print(self)
                                    k = k + 1
                                break
                        i += 1
            except EmptyDataError:
                print(file)
            except file :
                print(file)
        out = pd.DataFrame(np.array(datas))
        out.to_csv("param.csv", index=False, header=["Group", "Product", "Pt", "Init_tempture", "Final_tempture", "Slope"])

        print('OK')

    def __str__(self):
        return (super().__str__())


if __name__ == '__main__':
    m = main()
    m.load_file()