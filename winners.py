import json
from datetime import datetime
import pandas as pd
import re
with open('competitors2.json', 'r', encoding='utf-8') as file1, open('results_RUN.txt') as file2:
  competitors = json.load(file1)
  result = {}

  for i in file2.readlines():
    
    i = i.replace('п»ї', '').split()
    result.setdefault(i[0], []).extend(i[1:])


  for key, val in result.items():
    z = datetime.strptime(val[3], '%H:%M:%S,%f') - datetime.strptime(val[1], '%H:%M:%S,%f')
    val.clear()
    val.append(z)

  k = [(i[0], str(*i[1])[2:10].replace('.', ',')) for i in sorted(result.items(), key=lambda item: item[1])[:4]]

  counter = 1
  df = pd.DataFrame()
  for i in k:
    new_df = pd.DataFrame([{'Занятое место': counter, 'Нагрудный номер': i[0], 'Имя': competitors[i[0]]['Surname'], 'Фамилия': competitors[i[0]]['Name'], 'Результат': i[1]}])
    df = pd.concat([df, new_df], axis=0, ignore_index=True)
    counter += 1
print(df)  
