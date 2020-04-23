# 打印9*9 乘法口诀表(注意格式)
def table():
    for i in range(1,10):
        for j in range(1,i+1):
            s1=str(j)+"*"+str(i)+"="+str(j*i)
            print('%-10s'%s1,end="")
        print(""),
if __name__ == '__main__':
    table()