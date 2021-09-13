import pandas
import os
import re
english_chinese_xls = pandas.read_excel("1_merge_wordlist.xlsx", header=None)
if os.path.exists("3_chinese_english_deleteNoChinese.xlsx"):
    os.remove("3_chinese_english_deleteNoChinese.xlsx")
chinese_english = pandas.DataFrame(columns=['chinese', 'english'])
for dataFrameIndex, row in english_chinese_xls.iterrows():
    try:
        english = row[0]
        pattern = re.compile(r'[^\u4e00-\u9fa5]')
        chinese = re.sub(pattern, '', str(row[1]))
        if chinese != "":
            print(chinese, english)
            chinese_english = chinese_english.append({
                'chinese': chinese,
                'english': english
            },
                ignore_index=True)
    except:
        pass
chinese_english.to_excel("3_chinese_english_deleteNoChinese.xlsx", index=False, header=False)
