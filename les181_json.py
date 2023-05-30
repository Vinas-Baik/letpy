import json

MY_NAME_FILE = 'test.json'

catalog = {}
lines = ''

#  чтение из файла 
try:
    with open(MY_NAME_FILE) as f:
        lines = f.readlines()
    catalog = json.loads(''.join([line for line in lines]))
    #  вывод на экран содержимого файла 

    print('Из файла прочитано следующее:')
    print(''.join([cat_key + ':' + str(cat_val) + ';\t' for cat_key, cat_val in catalog.items()]))
except FileNotFoundError:
    print('нет файла', MY_NAME_FILE)

for i in range(3):
    user_in1 = input('Товар: ')
    user_in2 = int(input('Количество: '))
    if user_in1 in catalog.keys():
        catalog[user_in1] += user_in2
    else:
        catalog[user_in1] = user_in2

# print(catalog)
catalog = dict(sorted(catalog.items()))
# print(catalog)

with open(MY_NAME_FILE, 'w') as f:
    f.write(json.dumps(catalog))

print('\nВ файл записано следующее:')
print(''.join([cat_key + ':' + str(cat_val) + ';\t' for cat_key, cat_val in catalog.items()]))
