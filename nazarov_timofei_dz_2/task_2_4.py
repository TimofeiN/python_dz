position_name = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
                 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in range(len(position_name)):
    position_name[i] = position_name[i].split(' ')
    name = position_name[i][-1].capitalize()
    print(f'Привет, {name}!')
