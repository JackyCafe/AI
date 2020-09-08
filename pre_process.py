import  os
import pandas as pd

path = 'AI/'
workspaces = os.walk(path)
allfiles = []

for root, dirs, files in workspaces:
    for file in files:
        allfiles.append(f'{root}/{file}')

try:
        for file in allfiles:
            df = pd.read_csv(file)
            df.dropna(how='all').to_csv(file,index=False)
except :
    print(file)

print('OK')
#


