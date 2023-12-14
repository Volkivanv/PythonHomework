# Задача 44: В ячейке ниже представлен код генерирующий DataFrame,
# которая состоит всего из 1 столбца. Ваша задача перевести его в
# one hot вид. Сможете ли вы это сделать без get_dummies?
import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

#без get_dummies
res = data.copy()
res.loc[res['whoAmI'] == 'robot', 'robot'] = 'True'
res.loc[res['whoAmI'] != 'robot', 'robot'] = 'False'
res.loc[res['whoAmI'] == 'human', 'human'] = 'True'
res.loc[res['whoAmI'] != 'human', 'human'] = 'False'

res.drop('whoAmI', axis=1, inplace=True)

print("Вывод перевода в one hot вид без get_dummies")
print(res)

#с get_dummies
print("Вывод перевода в one hot вид с помощью get_dummies")
print(pd.get_dummies(data['whoAmI']))
