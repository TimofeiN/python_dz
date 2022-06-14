import urllib.request

url = 'https://gbcdn.mrgcdn.ru/uploads/asset/2729331/attachment/e84f9ad49c706008fba3b58e2a1e5b09.txt'

ip_data = []

with urllib.request.urlopen(url) as response:
    for line in response:
        line = line.decode('utf-8')
        idx = line.find(' - ')
        ip = line[:idx]
        ip_data.append(ip)

# print(ip_data)

