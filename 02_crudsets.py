set_countries = {'col','mex','bol'}
size = len(set_countries)
print(size)
#add
print('col' in set_countries)
print('pe' in set_countries)
set_countries.add('pe')
print(set_countries)

#update
set_countries.update({'arg'})
print(set_countries)

#remove

#set_countries.remove('arg')
set_countries.discard('ar')
print(set_countries)
set_countries.clear()
print(len(set_countries))