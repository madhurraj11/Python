s=input('Enter any string:')
res_str=''
next=True
for e in s:
    code=ord(e)
    if next:
        if code>=97 and code<=122:
            code-=32
    else:
        if code>=65 and code<=90:
            code+=32
    e=chr(code)
    res_str+=e
    next=e in " ;:,.'!?/|"
print(res_str)