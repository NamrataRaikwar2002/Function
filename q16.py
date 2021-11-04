# def table(num):
#     for i in range(1,11):
#         print(num,"x",i,"=",num*i)
# number=int(input("enter number to print its table:"))
# table(number)


num = 1
def func():
    global num
    num = num + 3
    print(num)
func()
print(num)