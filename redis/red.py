import redis  # импортируем библиотеку
import json

red = redis.Redis(
    host='localhost',
    # ваш хост, если вы поставили Редис к себе на локальную машину, то у вас это будет localhost. Если же вы находитесь на Windows, то воспользуйтесь полем host из вашей облачной БД, которую мы создавали в скринкасте.
    port=6379)
converted_dict =
dict = {}
nam = input('Имя ')
phon = input("телефон ")
dict[nam] = phon

red.set('dict', json.dumps(dict))  # с помощью функции dumps() из модуля json превратим наш словарь в строчку
converted_dict = json.loads(red.get('dict'))  # с помощью знакомой нам функции превращаем данные, полученные из кеша обратно в словарь
nams = input('name for phon search ')

print(type(converted_dict))  # убеждаемся, что мы получили действительно словарь
print(converted_dict[nams])  # ну и выводим его содержание