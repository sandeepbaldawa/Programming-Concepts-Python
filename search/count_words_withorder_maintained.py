from collections import OrderedDict
n = int(raw_input())

dict = OrderedDict()
for i in range (0,n):
    str = raw_input().rstrip("\r")
    if str in dict:
        dict[str] += 1
    else:
        dict[str] = 1
print len(dict)        
print ' '.join([`value` for key, value in dict.items()])    
        
