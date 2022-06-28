import re
import urllib.request
RE_DATA = re.compile(r'^([\d.]+)[\s-]+([\S\w\s]+[]])\W+(\w+)\s(\S+)\s\S+\s(\d+)\s(\d+)')

url = 'https://gbcdn.mrgcdn.ru/uploads/asset/2729331/attachment/e84f9ad49c706008fba3b58e2a1e5b09.txt'
with urllib.request.urlopen(url) as response:
    for line in response:
        line = str(line).strip("b'")[:-3]
        print(line)
        parsed_line = RE_DATA.findall(line)
        print(*parsed_line)
