import pandas
import os
directory = "english"

english_xlsx = pandas.read_excel("english.xlsx", header=None)
for i in range (1,6):
    index_start = (i-1)*10000+1
    index_end = i * 10000
    english_xlsx[index_start-1:index_end].to_excel("englishSplits/english_"+str(index_start)+"_"+str(index_end)+".xlsx"
                                                     , index=False, header=False)
