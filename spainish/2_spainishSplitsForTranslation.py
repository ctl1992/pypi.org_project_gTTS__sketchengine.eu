import pandas
import os

spainish_xlsx = pandas.read_excel("1_merge_wordlist.xlsx", header=None)
for i in range (9,10):
    index_start = (i-1)*10000+1
    index_end = i * 10000
    spainish_xlsx[index_start - 1:index_end][0].to_excel("2_spainishSplits/spainish_" + str(index_start) + "_" + str(index_end) + ".xlsx"
                                                      , index=False, header=False)
