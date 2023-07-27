import turtle
import time
import math
import turtle as tur
turtle.screensize(1080,1080)
tur.title("INITIAL")

tur.write("               SPECIALLY FOR U KANNALU!!!!        ", align="left",font=("Verdana",10,"bold" ))

turtle.penup()

turtle.left(90)

turtle.fd(200)

turtle.pendown()

turtle.right(90)

# flower base

turtle.fillcolor("red")

turtle.begin_fill()

turtle.circle(10, 180)

turtle.circle(25, 110)

turtle.left(50)

turtle.circle(60, 45)

turtle.circle(20, 170)

turtle.right(24)

turtle.fd(30)

turtle.left(10)

turtle.circle(30, 110)

turtle.fd(20)

turtle.left(40)

turtle.circle(90, 70)

turtle.circle(30, 150)

turtle.right(30)

turtle.fd(15)

turtle.circle(80, 90)

turtle.left(15)

turtle.fd(45)

turtle.right(165)

turtle.fd(20)

turtle.left(155)

turtle.circle(150, 80)

turtle.left(50)

turtle.circle(150, 90)

turtle.end_fill()

# Petal 1

turtle.left(150)

turtle.circle(-90, 70)

turtle.left(20)

turtle.circle(75, 105)

turtle.setheading(60)

turtle.circle(80, 98)

turtle.circle(-90, 40)

# Petal 2

turtle.left(180)

turtle.circle(90, 40)

turtle.circle(-80, 98)

turtle.setheading(-83)

# Leaves 1

turtle.fd(30)

turtle.left(90)

turtle.fd(25)

turtle.left(45)

turtle.fillcolor("green")

turtle.begin_fill()

turtle.circle(-80, 90)

turtle.right(90)

turtle.circle(-80, 90)

turtle.end_fill()

turtle.right(135)

turtle.fd(60)

turtle.left(180)

turtle.fd(85)

turtle.left(90)

turtle.fd(80)

# Leaves 2

turtle.right(90)

turtle.right(45)

turtle.fillcolor("green")

turtle.begin_fill()

turtle.circle(80, 90)

turtle.left(90)

turtle.circle(80, 90)

turtle.end_fill()

turtle.left(135)

turtle.fd(60)

turtle.left(180)

turtle.fd(60)

turtle.right(90)

turtle.circle(226, 60)

# heart

turtle.pensize(4)

turtle.color("red")

turtle.left(50)

turtle.forward(200)

turtle.circle(70, 200)

turtle.right(140)

turtle.circle(70, 200)

turtle.forward(200)

turtle.clear()
turtle.resetscreen()
turtle.title("LETTER")

Para="AYE BUJJILU\n NAKU EE LETTER RAYADAM TELIDHU\n..MA .. CHINNAPATI NUNDI I HAVENT WRITTEN A SINGLE LETTER UNLESS ITS FOR SOME " \
     "SCHOOLPURPOSE OR LEAVEFORM THIS IS THE FIRST TIME IM WRITING A LETTER KANI CHEPTUNNA KANNA EE LETTER NI CHADAVADANIKI NAKI TELSI NUVVU CHALA NE KASHTAPADI..UNTAV KADA.." \
     "PARLE KONCHAM OPIKA RAVALI ANI CHESNA NENU EEE LETTER RAYADANIKI KARANAM EDO PEDDADE CHEPTADU ANUKUNTUNNAV KADA BONGEM KADU" \
     " JUST NUV ROOM NO 106(SAVOURY) LO LEV ANDUKE BORE KOTTI RASTUNNA NIKU LETTER.. IDI LETTER KAADU EDO NA MATALU ANTHE" \
     "LOPALA NUNDI NIKU IPPUDU CHEPPALEKAPOTUNNA KABATTI ILA RASTUNNA INKA SODHI API MATTER LOKI VELDAMA . CINEMATIC GA UNTE TITTAKU" \
     "AND....MOSTLY NAVVAKU.... IPPPUDU RIGHT NOW NII FINGERS NI ENTHA MISS AYTUNNA TELSA GUITAR KI UNNA STRINGS LA UNTAY KANNA Nii...FINGERS" \
     " AA TEYYATI CHETULU NA CHEST MIDA VESINAPUDU SKIN LOPALKI VELLI NA HEART TOUCH AYNTATU UNTADI AND WHEN YOU SLEEP ON ME I MYSELF FEEL" \
     " LIKE A NEST WHERE PARROT SLEEPS WARM AND.. AA CHIINNA PILLA LA ADUGTAV CHUDU EMANNA KAVALI ANTE INKA DANI GURINCHI EM CHEPTAM LE " \
     "AA CUTENESS THO ADIGITEY NENU ALIVE GA UNDADANIKI REASON EDAYNA ICHESTA I KNOW IKKADA HEART PEDTEY TANTAV ANDUKE AH LINE SARELE INKA CHALU IDI CHADIVATANIKE PAPAM LATE AYUNTUNDI OPIKA " \
     " TECHUKONI CHADIVI UNTAV NOW FINAL ANIMATION FOR YOU ITLU...YOURS..KANNA"
list_words=list(Para.split(" "))
for x in list_words:
     turtle.pendown()
     turtle.hideturtle()
     turtle.write(x,font=("Verdana",10,"bold"),align="right")
     time.sleep(0.5)
     turtle.clear()
turtle.resetscreen()
from turtle import*
def hearta(k):
    return 15*math.sin(k)**3
def heartb(k):
    return 12*math.cos(k)-5*\
    math.cos(2*k)-2*\
    math.cos(3*k)-\
    math.cos(4*k)
speed (0)
bgcolor("black")
for i in range(6000):
    goto(hearta(i)*20,heartb(i)*20)
    for j in range(5):
        color("red")
    goto(0,0)
done()
