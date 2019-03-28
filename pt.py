#! /opt/abilisoft.com/thirdparty/python27/bin/python
c=input()
start=1
pasc=[]
list=[]
prevlist=[]
nexlist[]

def nextlist(prevlist):
    list=[]
    prev=0
    for row in prevlist:
        lst=row+prev
        prev=row
	list=append(lst)

    list.append(start)
    return list

for i in range(1, c + 1)
    list=[]
    if i== 1:
        list.append(start)
	pasc.append(list)
    elif i == 2:
	list.append(start)
	list.append(start)
	pasc.append(list)
   else:
        nexlist=nextlist(prevlist)
        pasc.append(nexlist)
	prevlist=nexlist

buff=''
count=0
for item in reversed(pasc):
    count= count + 1
    for it in item:
	buff= buff + ' ' + str(it)
    print buff
    buff=''
    for k in range(0, count):
        buff = buff + ' '

