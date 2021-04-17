# try:
#     print(num)
# except (NameError,IndexError) as msg:
#     print(msg)
#
# try:
#     print(1)
# except Exception as result:
#     print(result)
# else:
#     print('w我是else,是没有异常的时候执行的代码')
#
# try:
#     f=open('test.txt','r')
# except Exception as result:
#     f=open('test.txt','w')
# else:
#     print('m没有异常')
# finally:
#     f.close()


import time

try:
    f = open('test.txt')

    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    except:
        # 如果在读取⽂文件的过程中，产⽣生了了异常，那么就会捕获到
        # ⽐比如 按下了了 ctrl+c
        print('意外终⽌止了了读取数据')
    finally:
        f.close()
        print('关闭⽂文件')
except:
    print("没有这个⽂文件")