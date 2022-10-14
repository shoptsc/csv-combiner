import pandas as pd
import sys

def csvCombiner(files):

    dataframe = pd.DataFrame()
    fileName = []
    fileNameList = []
            
    for i in range(1, len(files)):
        data = pd.read_csv(files[i])
        fileName.append(list(len(data) * (files[i].replace("./fixtures/", ""),)))
        dataframe  = pd.concat([dataframe, data])

    for i in fileName:
        fileNameList.extend(i)

    dataframe['filename'] = fileNameList
    return (dataframe.to_csv(index = False, lineterminator='\r'))
   
print(csvCombiner(sys.argv))
