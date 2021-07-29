
position = [1,2,3,4,5,6]

f = open('testfile.txt','w',encoding='utf-8')
f.writelines(str(position))
#print(position, file = f)
f.close() # save