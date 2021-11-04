matrix_size=5
command_count=4
command=[]
for i in range(0,command_count):
    way=input("enter way:")
    command.append(way)
print(command)
def myfunction(m,com):
    i=0
    p=0
    while i<len(com):
        if com[i]=="right":
            p=p+1
        elif com[i]=="down":
            p=p+matrix_size
        elif com[i]=="up":
            if p<4:
                print("cannot move up")
            else:
                p=p-matrix_size
        elif com[i]=="left":
            if p==0:
                print("cannot go left")
            else:
                p=p-1
        i=i+1
    return p
print(myfunction(matrix_size,command))



