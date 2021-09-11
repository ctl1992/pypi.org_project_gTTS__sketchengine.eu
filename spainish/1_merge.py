import pandas
import os
directory = "wordlist"
spainish_xlsx = pandas.DataFrame(columns=['Item'])
for filename in os.listdir(directory):
    wordlist = pandas.read_excel(os.path.join(directory, filename), header=3)[:-1][['Item']]
    spainish_xlsx = spainish_xlsx.append(wordlist)
spainish_xlsx.to_excel("spainish.xlsx", index=False, header=False)
pass