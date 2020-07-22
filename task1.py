
""""
Python 3.7.4
--------------------------
tkinter.TkVersion 8.6
--------------------------
"""
import turtle
import json
import random

c = (0,0,0)
def drawBar(t, height,old,date):
    """ Get turtle t to draw one bar, of height. """
    global c
    try:
        if c[0]<220 and c[1]<220 and c[2]<220:
            r, g, b = c
            r += 30 
            g += 30
            b += 30
            c = (r, g, b)
        else:
            try:
               
                c = (random.randint(0,220),random.randint(0,220),random.randint(0,220))
            except:
                pass
    except:
        pass
    # start drawing this shape
    
    
    t.begin_fill()
    t.right(180)
    t.backward(12)
    t.color('black')
    t.write(date,font=("Arial", 8, "normal"),align='left')
    
    t.color(c)
    t.forward(10)
    t.left(90)
    t.backward(0)
    t.left(90)
    t.left(90)
    t.color("black")

    
    t.forward((old))
    t.color('black')
    t.forward(((height-old)))

 
    
    t.right(90)
    t.color('blue')
    tess.pensize(1) 
    t.forward(13)
    t.color("red")
    t.forward(13)
    t.color('blue')
    t.write(format(height), font=("Arial", 6, "normal"),align='center')
    t.color('blue')
    t.forward(13)
    
    t.color(c)
    t.right(90)
    t.forward((height))
    t.left(90)

if __name__ == "__main__":
    try:
        data=json.load(open('data.json'))

        d={}

        d1=1

        dates=[]

        rupees=[]

        while d1<10:

            for k,v in data.items():

                for k1 in v:

                    if k1=='2019-01-0'+str(d1):
                        
                        dates.append(k1)

                        d=v[k1]

                        for (k2,v2) in d.items():

                            if k2=="INR":

                                rupees.append(v2)


            d1+=1





        while d1<32:

            for p_id, p_info in data.items():

                for key in p_info:

                    if key=='2019-01-'+str(d1):
                        dates.append(key)

                        d=p_info[key]

                        for (k,v) in d.items():

                            if k=="INR":

                                rupees.append(v)


            d1+=1







        date1=[]

        for x in dates:

            a=x.split('-')

            y=a[0]

            m=a[1]

            dates=a[2]

            date1.append(int(dates))



        date=date1

        xs=rupees
        xs = [79.9855, 79.608, 79.4315, 79.6895, 80.245, 80.6365, 81.2005, 81.3475, 81.2195, 81.231, 81.0055, 80.9765, 81.0875, 80.9335, 81.046, 81.0535, 80.656, 80.634, 81.232, 81.306, 81.351, 81.686]
        maxheight = max(xs)
        numbars = len(xs)
        border = 10

        wn = turtle.Screen()             # Set up the window and its attributes
        wn.setworldcoordinates(0-border, 0-border, 40*numbars+border, maxheight+border)
        wn.bgcolor("white")

        tess = turtle.Turtle()
        tess.speed('fastest') 

        turtle.colormode(255)
        tess.pensize(3)


        tess.sety(-0.0125)
        tess.color("black")


        m=max(xs)
        tess.left(90)


        tess.backward(3)
        tess.write('   x,y')
        tess.forward(3)
        tess.forward(m+3)
        tess.write('INR exchange rate against EUR')
        tess.backward(m+3)


        tess.right(90)
        tess.backward(20)
        tess.forward(20)
        tess.forward((len(xs)*39)+30)
        tess.right(90)
        tess.color('white')
        tess.forward(3)
        tess.color('black')
        tess.write('Date',align='right')
        tess.color('white')
        tess.backward(3)
        tess.color('black')

        tess.left(90)
        tess.forward(40)
        tess.backward((len(xs)*39)+70)
        tess.forward(((len(xs)*39)-100)/2)
        tess.right(90)
        tess.color("white")
        tess.forward(5)
        tess.color("blue")
        tess.write(" 1 Jan 2019 to 31 Jan 2019 (T1)",font=('Arial',10,'normal'))
        tess.color("white")
        tess.backward(5)
        tess.color("black")
        tess.left(90)
        tess.backward(((len(xs)*39)-100)/2)

        old=0
        i=0
        for a in xs:

           drawBar(tess, a,old,str(date[i]))
           old=a
           i+=1


           

        wn.exitonclick()
    except Exception as e:
        print(e)
