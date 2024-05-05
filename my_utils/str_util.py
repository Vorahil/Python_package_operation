def str_reverse(s):#反向输出
    return str(s)[::-1]

def str_check(s,n):#输出指定位置
    return str(s)[n]

def str_replace(s,a,b):#在指定位置替换
    return str(s).replace(str(a),str(b))

def str_input_every_s(s):
    for i in str(s):
        print(i)



if __name__ == '__main__':
    print(str_reverse(123456))
    print(str_check(123456,1))
    print(str_replace(123456,3,0))
    print(str_input_every_s(123456))

