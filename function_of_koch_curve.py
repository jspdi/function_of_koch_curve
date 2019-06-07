import turtle
def koch(t, length):
    if length <= 3:
        t.fd(length)
    t.fd(length)
    t.lt(60)
    t.fd(length)
    t.rt(120)
    t.fd(length)
    t.lt(60)
    t.fd(length)
def snowflake(t, length):
    t.lt(60)
    koch(t, length)
    t.rt(120)
    koch(t, length)
    t.rt(120)
    koch(t, length)

def fundament(t, length,length_given,n,m):
    '''fundament function used to draw one of the three side of the snowflake based on the fucntion koch
       length is the total length of each three side of the snow
       length_given is the shortest base line segment that consists the whole snowflake
       n used to count the times the line was divided by 3
       m used to set the times the lind was permited to divided by 3'''
    length = length/3
    if length < 3:
        t.fd(length)
        t.lt(60)
        t.fd(length)
        t.rt(120)
        t.fd(length)
        t.lt(60)
        t.fd(length)
    if  length != length_given:#第一步画出koch曲线4条组成线段中的第一条
        fundament(t, length,length_given,n+1,m)#如果此时koch曲线4条组成线段的长度不等于最小的我们设置的想要的长度length_given则
        #通过recursion来call这个函数以便继续对线段进行处以3的操作，直到等于我们设置的想要的长度length_given。
    t.lt(60)#第二步左转60度以便画出koch曲线4条组成线段中的第二条
    if  length != length_given:#画出koch曲线4条组成线段中的第二条
        fundament(t, length,length_given,n+1,m)
    t.rt(120)
    if  length != length_given:
        fundament(t, length,length_given,n+1,m)
    t.lt(60)
    if  length != length_given:
        fundament(t, length,length_given,n+1,m)
    if length == length_given:
        koch(t, length)
        t.lt(60)
        koch(t, length)
        t.rt(120)
        koch(t, length)
        t.lt(60)
        koch(t, length)
    
def koch_curve(t, length,n,m):
    '''koch_curve function used to draw a snowflake type koch curve
       t used to present the turtle
       length used to present the length of each of the three sides
       n used to be set as a argument in fundament function
       m used to be set as a arguemnt in fundament function'''
    length_given = length/3**m
    t.lt(60)
    fundament(t, length, length_given,n,m)
    t.rt(120)
    fundament(t, length, length_given,n,m)
    t.rt(120)
    fundament(t, length, length_given,n,m)
    t.hideturtle()
#below is the code to test this function to see whether it will operate successfully.
bob = turtle.Turtle()
#koch(bob,30)
#snowflake(bob, 30)
koch_curve(bob,90,0,4)
