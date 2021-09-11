import pandas
import os
directory = "wordlist"
english_xlsx = pandas.DataFrame(columns=['Item'])


def getLastIntOfFileName(fileName):
    res = int(fileName.split("_")[-1].split(".")[0])
    print(res)
    return res
fileNames =  os.listdir(directory)
fileNamesSorted = sorted(fileNames, reverse=True, key=getLastIntOfFileName)

for filename in fileNamesSorted:
    wordlist = pandas.read_excel(os.path.join(directory, filename), header=3)[:-1][['Item']]
    english_xlsx = english_xlsx.append(wordlist)
english_xlsx.to_excel("english.xlsx", index=False, header=False)
pass