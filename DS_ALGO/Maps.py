import collections

dict1 = {'day1': 'Mon', 'day2': 'Tue'}
dict2 = {'day3': 'Wed', 'day1': 'Thu'}

res = collections.ChainMap(dict1,dict2)

#Accessing
print(res.maps)
print('Keys = {}'.format(list(res.keys())))
print('Values = {}'.format(list(res.values())))

for key, val in res.items():
   print('{} = {}'.format(key, val))
print()

#Updating
dict2['day4'] = 'Fri'
print(res.maps,'\n') 