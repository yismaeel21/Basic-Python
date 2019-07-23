
statement = 'four score and sixty five years in the past'
count = {}
for x in statement:
    count.setdefault(x,0)
    count[x]+=1
print(count)