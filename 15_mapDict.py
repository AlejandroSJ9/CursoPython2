items = [
  {
    'product': 'camisa',
    'price': 100,
  },
  {
    'product': 'pantalones',
    'price': 300
  },
  {
    'product': 'pantalones 2',
    'price': 200
  }
]

new = list(map(lambda x: x['price'],items))
print(new)

def change(item):
  item['taxes'] = item['price'] * .19
  return item
new_item = list(map(change,items))
items = list(map(change,items))
#print(items)
