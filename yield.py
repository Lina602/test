
def produce():
    print("starting....")
    for i in range(1, 11):
        c.send(i)
        print("生产者：", str(i))

def consumer():
    while True:
        res = yield
        print("消费者：",res)

c = consumer()
next(c)
produce()