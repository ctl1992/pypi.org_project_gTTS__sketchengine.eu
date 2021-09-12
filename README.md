# 使用gTTS合成单词表的配套mp3

WARNING 调用谷歌接口有频率限制，会被认为对谷歌进行ddos攻击，被封主机和ip

# 词汇来源：https://app.sketchengine.eu/#corpus?tab=advanced&cat=all&sketches=0&lang=&lang2=&query=&showOld=0

登录后选择不同语言的语料库（corpus）

免费账户每次只能下载1000个单词，可以限制词频得到第1001-第2000的单词，

循环往复可获得15000词甚至更多

# 使用http://translate.google.com 翻译excel

chrome网页不要关闭，网页会顺序调用谷歌翻译接口，直到全部翻译完成，

大概每次翻译14000行，然后ip被封，可能第二天会好，若超出可分割多个excel翻译

## 不要使用使用google sheets翻译excel，每次打开excel都会再翻译一次，结果不全
https://www.mamababymandarin.com/automatically-translate-english-to-chinese-with-google-sheets/

无拖拽填充公式到整列auto

https://spreadsheetpoint.com/apply-formula-to-entire-column-google-sheets/

ARRAYFORMULA不支持GOOGLETRANSLATE

https://webapps.stackexchange.com/questions/129762/how-can-i-use-arrayformula-or-something-similar-with-googletranslate
