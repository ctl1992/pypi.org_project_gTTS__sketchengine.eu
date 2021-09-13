import re
from time import sleep

from num2words import num2words
import pandas
from gtts import gTTS
import os
chinese_spainish_xlsx = pandas.read_excel("4_chinese_spainish_deleteNoChinese.xlsx", header=None)
xlsxIndex_start = 1 # xlsx_index==dataFrameIndex+1
xlsxIndex_end = 14000
f = None
def index2ChineseChars(xlsxIndex):
    res = ""
    for char in list(str(xlsxIndex)):
        if char == "1":
            res = res + "一"
        if char == "2":
            res = res + "二"
        if char == "3":
            res = res + "三"
        if char == "4":
            res = res + "四"
        if char == "5":
            res = res + "五"
        if char == "6":
            res = res + "六"
        if char == "7":
            res = res + "七"
        if char == "8":
            res = res + "八"
        if char == "9":
            res = res + "九"
        if char == "0":
            res = res + "零"
    return res
for dataFrameIndex, row in chinese_spainish_xlsx.iterrows():
    xlsxIndex = dataFrameIndex + 1
    if xlsxIndex>=xlsxIndex_start and xlsxIndex<=xlsxIndex_end:
        indexChinese = index2ChineseChars(xlsxIndex)
        chinese = row[0]
        spainish = row[1]
        print(indexChinese, chinese, spainish)
        if (dataFrameIndex % 1000) == 0:
            if f is not None:
                f.close()
            mp3Path = "4_mp3/indexChinese_chinese_spainish_" + str(xlsxIndex) + "_" + str(xlsxIndex + 999) + ".4_mp3"
            if os.path.exists(mp3Path):
                os.remove(mp3Path)
            f = open(mp3Path, 'wb')
        try:
            gTTS(indexChinese + "。" + chinese, lang="zh-TW").write_to_fp(f)  # a1mp3 1
            sleep(2)
            gTTS(spainish + ".", lang="es").write_to_fp(f)  # 西班牙文
            sleep(2)
        except:
            pass
f.close()