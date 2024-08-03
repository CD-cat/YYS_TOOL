from adb import *


if __name__ == '__main__':
    # print('请输入数字以选择需要种植的作物（0.亚麻、1.藜麦、2.熊瓜、3。圣女果）：')
    n = 0
    zuowu = ['yama','limai','xiong','shengnv']
    zhong = zuowu[n]
    shou = 'm'+zuowu[n]
    print(shou , zhong)
    while True:
        while True:
            point = match('blank', 0.9)
            print('finding blank')
            if point is None:
                print('blank not found')
                break
            print('blank founded')
            click(*point)
            wait(0.5)
            try:
                swipe(*match('yama'), 950, 515, 750)
            except:
                break
            wait(0.5)
    
        # wait(12*60+20)
    
        while True:
            point = match('myama9', 0.6)
            print('finding myama')
            if point is None:
                print('myama was not founded')
                break
            print('myama was founded',point[1],type(point))
            wait(0.2)
            click(*point)
            wait(1)
            swipe(820, 460, 1100, 700, 800)
            wait(0.2)
