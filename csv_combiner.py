import pandas as pd
import sys

def csvCombiner(files):

    # Create an empty dataframe.
    dataframe = pd.DataFrame()
    
    # Create an empty list to add the file names.
    fileName = []
    fileNameList = []
            
    for i in range(1, len(files)):
        data = pd.read_csv(files[i])
        # append the file names to the empty list
        fileName.append(list(len(data) * (files[i].replace("./fixtures/", ""),)))
        dataframe  = pd.concat([dataframe, data])

    # Spread the nested array into one single list.
    for i in fileName:
        fileNameList.extend(i)

    # Add the file name as extra column with header filename and convert to csv.
    dataframe['filename'] = fileNameList
    return (dataframe.to_csv(index = False, lineterminator='\r'))
   
print(csvCombiner(sys.argv))
