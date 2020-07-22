#Python 3.7.4
import turtle
import json
import random

swtich=0
FLOAT_FORMAT = "0.2f"
def datacurrent(latestcrn):
    latest=json.load(open('latest-rates.json'))
    rates = latest['rates']
    value = rates[latestcrn]
    return value
def countList(lst1, lst2): 
	return [sub[item] for item in range(len(lst2)) 
					for sub in [lst1, lst2]] 
	
def data(crn):
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

                        if k2==crn:

                            rupees.append(v2)


        d1+=1

    while d1<32:

        for p_id, p_info in data.items():

            for key in p_info:

                if key=='2019-01-'+str(d1):
                    dates.append(key)

                    d=p_info[key]

                    for (k,v) in d.items():

                        if k==crn:

                            rupees.append(v)


        d1+=1

    date1=[]

    for x in dates:

        a=x.split('-')

        y=a[0]

        m=a[1]

        dates=a[2]

        date1.append(int(dates))
    x=date1
    y=rupees
    return x,y      
def drawBar(t, height,old,date):
    """ Get turtle t to draw one bar, of height. """
    global swtich
    t.begin_fill()
    t.right(180)
    t.backward(12)
    t.color('black')
    t.left(90)
    t.color('lightgreen')
    t.forward(3)
    t.color('black')
    if(swtich==1):
        t.write(date ,font=("Arial", 8, "normal"),align='right')
    if(swtich==0):
        t.write('' ,font=("Arial", 8, "normal"),align='right')
    t.color('lightgreen')
    t.backward(3)
    t.color('black')
    t.right(90)
    t.color('black')
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
    t.color("white")
    t.forward(13)
    t.color('blue')
    t.write(format(height,FLOAT_FORMAT), font=("Arial", 6, "normal"),align='center')
    t.color('blue')
    t.forward(13)
    
    t.color('black')
    t.right(90)
    t.forward((height))
    t.left(90)
    if swtich==0:
        t.color('lightblue')
        swtich=1
    else:
        t.color('orange')
        swtich=0
    t.end_fill()
if __name__ == "__main__":
    try:

     
        a,b=data('INR')
        c,d=data('GBP')


        date=countList(a, c) 
        xs=countList(b, d)
        maxheight = max(xs)
        numbars = len(xs)
        border = 10

        wn = turtle.Screen()             # Set up the window and its attributes
        wn.setworldcoordinates(0-border, 0-border, 40*numbars+border, maxheight+border)
        wn.bgcolor("lightgreen")

        tess = turtle.Turtle()
        tess.speed('fastest') 

        turtle.colormode(255)
        tess.pensize(3)


        tess.sety(-0.0125)
        tess.color("black")


        m=max(xs)
        tess.left(90)


        tess.backward(6)
        tess.write('   x,y')
        tess.forward(6)
        
        tess.forward(m+5)
        
        tess.right(90)
        tess.write(' INR(LIGHT_BLUE) and GBP(ORANGE) exchange rate against EUR')
        tess.color('lightgreen')
        tess.forward((len(xs)*30)-10)
        tess.color('blue')
        tess.write('    Latest rates INR: '+str(datacurrent('INR')))
        tess.color('lightgreen')
        tess.right(90)
        tess.forward(3)
        tess.color('black')
        tess.write('    Latest rates GBP: '+str(datacurrent('GBP')))
        tess.color('lightgreen')
        tess.backward(3)
        
        tess.left(90)
        tess.backward((len(xs)*30)-10)
        tess.left(90)
        tess.color('black')
        tess.backward(m+5)


        tess.right(90)
        tess.backward(20)
        tess.forward(20)
        tess.forward((len(xs)*39)+30)
        tess.right(90)
        tess.color('lightgreen')
        tess.forward(6)
        tess.color('black')
        tess.write('day',align='right')
        tess.color('lightgreen')
        tess.backward(6)
        tess.color('black')

        tess.left(90)
        tess.forward(40)
        tess.backward((len(xs)*39)+70)
        tess.forward(((len(xs)*39)-100)/2)
        tess.right(90)
        tess.color("lightgreen")
        tess.forward(8)
        tess.color("blue")
        tess.write(" 1 Jan 2019 to 31 Jan 2019 (T3)",font=('Arial',10,'normal'))
        tess.color("lightgreen")
        tess.backward(8)
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
