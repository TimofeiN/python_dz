import urllib.request

url = 'https://gbcdn.mrgcdn.ru/uploads/asset/2729331/attachment/e84f9ad49c706008fba3b58e2a1e5b09.txt'

tmp = set()
result = {}

with urllib.request.urlopen(url) as response:
    for line in response:
        line = line.decode('utf-8')
        idx = line.find(' - ')
        ip = line[:idx]
        if ip not in tmp:
            ip_dic = {ip: 1}
            result.update(ip_dic)
        else:
            count = result.get(ip) + 1
            result[ip] = count
        tmp.add(ip)

spammer = ''
for k, v in result.items():
    if v == max(result.values()):
        spammer = f'{k} - {v}'
print('spammer', spammer)

# spammer 216.46.173.126
