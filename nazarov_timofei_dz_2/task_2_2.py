lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(lst)

for idx in range(len(lst)):
    if lst[idx].isdigit():
        lst[idx] = f'{int(lst[idx]):02d}'
    elif lst[idx].startswith('+'):
        lst[idx] = f'+{int(lst[idx][1:]):02d}'
print('2 - ', lst)

new_list = []
for v in lst:
    if v.isdigit() or v.startswith('+'):
        new_list.append('"')
        new_list.append(v)
        new_list.append('"')
    else:
        new_list.append(v)
print(new_list)

message = []
for i in range(len(new_list)):
    if new_list[i].startswith('+') or new_list[i].isdigit() and new_list[i-1].startswith('"') and new_list[i+1].startswith('"'):
        message_part = [new_list[i - 1], new_list[i], new_list[i + 1]]
        message_part = ''.join(message_part)
        message.append(message_part)
    elif not new_list[i].startswith('"'):
        message.append(new_list[i])
print(message)

message = ' '.join(message)
print(message)