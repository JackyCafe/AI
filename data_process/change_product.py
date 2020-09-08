import os
import pandas as pd

from data_collect.data_struct import data

path = '../AI/Training/'
workspaces = os.walk(path)
allfiles = {}
datas = [[0 for i in range(2)] for j in range(522)]


class main(data):

    def load_file(self):
        j = 0
        for root, dirs, files in workspaces:
            for file in files:
                datas[j][0] = file
                datas[j][1] = root
                print(j,datas[j][0],datas[j][1])
                j = j + 1


        for i in range(0,len(datas)):
            file = datas[i][0]
            path = datas[i][1]
            folderpath = "../out" + path
            if not os.path.isdir(folderpath):
                os.makedirs(folderpath)
            df = pd.read_csv(f'{path}/{file}')
            # print(f'{path}/{file}')
            df1 = pd.DataFrame(df.to_numpy())
            df1.to_csv(f'{folderpath}/{file}', index=False,header=False)
            print(f'{folderpath}/{file}')

        print('OK')




    def __str__(self):
        return (super().__str__())


#
if __name__ == '__main__':
    m = main()
    m.load_file()

