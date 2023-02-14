items = []
while True:
    item = input("enter input. if no input put nothing")
    if item == '':
        break
    items.append(item)
print(items)
count=0
for i in items:
    i =int(i)
    count=count+i
print(count)