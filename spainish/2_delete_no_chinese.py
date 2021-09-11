import pandas
import os
import re
spainish_chinese_xls = pandas.read_excel("spainish_chinese_75203_1211104300.xlsx",header=None)
if os.path.exists("chinese_spainish.xlsx"):
    os.remove("chinese_spainish.xlsx")
chinese_spainish = pandas.DataFrame(columns=[ 'chinese', 'spainish'])
for dataFrameIndex, row in spainish_chinese_xls.iterrows():
    spainish = row[0]
    pattern = re.compile(r'[^\u4e00-\u9fa5]')
    chinese = re.sub(pattern, '', row[1])
    if chinese != "":
        chinese_spainish = chinese_spainish.append({
            'chinese': chinese,
            'spainish': spainish
        },
            ignore_index=True)
chinese_spainish.to_excel("chinese_spainish.xlsx", index=False, header=False)
