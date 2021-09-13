import pandas
import os
import re
spainish_chinese_xls = pandas.read_excel("1_merge_wordlist.xlsx",header=None)
if os.path.exists("3_chinese_spainish_deleteNoChinese.xlsx"):
    os.remove("3_chinese_spainish_deleteNoChinese.xlsx")
chinese_spainish = pandas.DataFrame(columns=[ 'chinese', 'spainish'])
for dataFrameIndex, row in spainish_chinese_xls.iterrows():
    spainish = row[0]
    pattern = re.compile(r'[^\u4e00-\u9fa5]')
    chinese = re.sub(pattern, '', str(row[1]))
    if chinese != "":
        chinese_spainish = chinese_spainish.append({
            'chinese': chinese,
            'spainish': spainish
        },
            ignore_index=True)
chinese_spainish.to_excel("3_chinese_spainish_deleteNoChinese.xlsx", index=False, header=False)
