'''
使用Redis进行用户数进行统计,不用在数据库进行标记，更加节省资源占用。
当数据量达到一定值时，Redis比数据库select统计更快。
'''
import redis
r = redis.Redis(host='127.0.0.1',port=6379,decode_responses=True)
tag = True
count = 100
num = 0
while tag:
    username = input("username:")
    if username == 'E':
        tag = False
    elif username == 'P':
        # 统计当前在线人数
        for key in r.keys():
            #查找对应位置比特位是否为1，为1则表示登录用户
            if r.getbit(key, int(key)) == 1:
                num += 1
        print("num:", num)
    else:
        count += 1
        #将用户编号和用户名存入Redis
        r.set(count,username)
        #将用户名编号处的比特位置一，用来标记登录用户
        r.setbit(count,count,1)
