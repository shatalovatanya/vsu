message = input('Введите текст на русском языке для зашифровки: ').lower()
key = input('Введите слово-ключ: ')
alph = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о',
      'п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
newMesRange = []
newMes = ''
for i in message:
    if i not in alph:
             newMesRange.append(i)
    else:
        newMesRange.append(alph[(alph.index(i) + len(key)) % len(alph)])
for i in range(len(newMesRange)):
    newMes += newMesRange[i]
print('Зашифрованное сообщение: ', newMes)