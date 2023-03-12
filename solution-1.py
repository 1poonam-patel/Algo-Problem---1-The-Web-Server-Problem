inputList=[]

smInput = open('TWSP_small.txt')
lines = smInput.readlines()
for i in range(1,len(lines)):
    records=lines[i].split(" ")
    li=[i for i in records if i!='']
    li[2]=li[2].replace('\n','')
    inputList.append((li[0],li[1],li[2]))
    

inputList.sort()

answer=[]
di = {}

# to collect same no. of text content in records
for i in range(len(inputList)):
    if(inputList[i][0] not in di.keys()):
        di[inputList[i][0]]=[]
        di[inputList[i][0]].append(inputList[i])
    else:
        di[inputList[i][0]].append(inputList[i])


# Bubble sort for sort the image content
for k in di.keys():
    for i in range(len(di[k])):
        for j in range(len(di[k])-1):
            if(di[k][j]<di[k][j+1]):
                temp=di[k][j]
                di[k][j]=di[k][j+1]
                di[k][j+1]=temp


# make list of answer
for i in di.values():
    for j in i:
        answer.append(j)

# write output in file
    
with open("small_output.txt","w") as out:
    for a,b,c in answer:
        out.write(a+','+b+','+c+'\n')