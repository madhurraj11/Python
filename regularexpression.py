
import urllib.request as rq
import re
f = rq.urlopen('https://www.iimtindia.net/contact-us.php')
data = f.read()

# print(data)
# print(type(data))
data = str(data)
# print(type(data))
p = r'\w+[.]?\w*@\w+[.]\w+[.]?\w*|[+]91[-]?\d{10}'
res = re.findall(p, data)
print(res)
print(len(res))
r = set(res)
print(r)
print(len(r))

# s = '''madhur +91 7292459429 2394800808 madhur@gmail.com riet.jaipur@gmail.co.in basfggdh cetpa1123@outlook.com
#      gwugrujskd +91 0917478689 cetpa.infotech +91 9291667661'''
# p = r'\w+[.]?\w*@\w+[.]\w+[.]?\w*|[+]91 \d{10}'
# res = re.findall(p, s)
# print(s)
# print(res)