#Python 3.7.4

from tkinter import *
import json
import datetime
import turtle
import urllib.request
import random

def reset():
    pass
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
    t.pensize(1) 
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
    
def plot():

    if month.get()=='select month':
        print('Please select month')
        return
    if cur.get()=='select':
        print('Please select currency')
        return
    if len(year_entry.get())>4 or int(year_entry.get())<2009:
        print('year is not valid')
        return
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December']
    try:
        yy=year_entry.get()
        mm=months.index(month.get())+1
        if int(mm)<10:
            mm=str('0'+str(mm))
        ss='1'
        if int(mm)==2:
            ee='26'
        if int(mm)%2!=0 or int(mm)==1:
            ee=('31')
        if int(mm)%2==0 and int(mm)!=2:
            ee=('30')
        startdate=(str(yy)+'-'+str(mm)+'-'+ss)
        enddate=(str(yy)+'-'+str(mm)+'-'+ee)

        
        info['text']='Please wait fetching data from site....'
        url='https://api.exchangeratesapi.io/history?start_at='+str(startdate)+'&end_at='+str(enddate)
        try:
            print('Please wait fetching data from site....')
            x = urllib.request.urlopen(url)
            print('Data Revecied successfully')
            info['text']='Data Revecied successfully'
            data = json.loads(x.read())
        except:
            data=json.load(open('data.json'))
        d={}

        d1=1

        dates=[]

        rupees=[]

        while d1<10:

            for k,v in data.items():

                for k1 in v:

                    if k1==str(yy)+'-'+str(mm)+'-0'+str(d1):
                        
                        dates.append(k1)

                        d=v[k1]

                        for (k2,v2) in d.items():

                            if k2==str(cur.get()):

                                rupees.append(v2)


            d1+=1





        while d1<32:

            for p_id, p_info in data.items():

                for key in p_info:

                    if key==str(yy)+'-'+str(mm)+'-'+str(d1):
                        dates.append(key)

                        d=p_info[key]

                        for (k,v) in d.items():

                            if k==str(cur.get()):

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
        
        print(date)
        print(xs)
        try:
            turtle.reset()
        except:
            pass
        try:
            turtle.clear()
        except:
            pass
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
        tess.color("green")


        m=max(xs)
        tess.left(90)


        tess.backward(3)
        tess.write('   x,y')
        tess.forward(3)
        tess.forward(m+3)
        tess.write(cur.get()+' exchange rate against EUR')
        tess.backward(m+3)


        tess.right(90)
        tess.backward(20)
        tess.forward(20)
        tess.forward((len(xs)*39)+30)
        tess.right(90)
        tess.color('white')
        tess.forward(3)
        tess.color('green')
        tess.write('Date',align='right')
        tess.color('white')
        tess.backward(3)
        tess.color('green')

        tess.left(90)
        tess.forward(40)
        tess.backward((len(xs)*39)+70)
        tess.forward(((len(xs)*39)-100)/2)
        tess.right(90)
        tess.color("white")
        tess.forward(5)
        tess.color("blue")
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December']
        mm=months.index(month.get())+1
        if int(mm)<10:
            mm=str('0'+str(mm))
        ss='1'
        if int(mm)==2:
            ee='26'
        if int(mm)%2!=0 or int(mm)==1:
            ee=('31')
        if int(mm)%2==0 and int(mm)!=2:
            ee=('30')
        tess.write(" 1 "+month.get()+" "+year_entry.get()+" to "+ee+ " " +month.get()+" "+year_entry.get(),font=('Arial',10,'normal'))
        tess.color("white")
        tess.backward(5)
        tess.color("green")
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
        info['text']='Ops! Try Again (Check internet connection/No data found'




app = Tk()

app.title('Stats')
app.geometry('900x550')
info = Label(app, text='Data source (https://api.exchangeratesapi.io)', font=('bold', 10),pady=20)
info.grid(row=50, column=2)
start_txt = StringVar()
year_txt = StringVar()
year_label = Label(app, text='Year', font=('bold', 12),pady=20)
year_label.grid(row=0, column=1)
year_label1 = Label(app, text='(above 2008)', font=('Arial', 8),pady=20)
year_label1.grid(row=0, column=3)
year_entry =Entry(app,textvariable =year_txt)
year_entry.grid(row =0 ,column=2)

month = StringVar()
month.set('select month')
month_list = OptionMenu(app ,month, 'January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December')
month_list.grid(row =0 ,column=0)

select_label = Label(app, text=' Select currency : ', font=('bold', 12),pady=20)
select_label.grid(row=10 , column=0)
cur = StringVar()
cur.set('select')
cur_list = OptionMenu(app ,cur, 'CAD','HKD','ISK','PHP','DKD','HUF','CZK','AUD','RON','SEK','IDR','INR','BRL','RUB','HRK','JPY','THB','CHF','SGD','PLN','BGN','TRY','CNY','NOK','NZD','ZAR','USD','MXN','ILS','GBP','KRW','MYR')
cur_list.grid(row =10 ,column=1)
submit_btn = Button(app, text='Submit',width = 12,command =plot)
submit_btn.grid(row=10,column=2)
reset_btn = Button(app, text='Reset',width = 12,command =reset)
reset_btn.grid(row=10,column=3)
app.mainloop()