import numpy as np
import pygame as pg
import matplotlib.pyplot as plt

def approkEXDeriv(x,h):
    return (np.e**(x+h)-np.e**x)/h

def oppgave1():
    print("Oppgave 1:\nFasit:",np.e**1.5)
    for i in range(2,18):
        y=(np.e**(1.5+10**(-i))-np.e**1.5)/10**(-i)
        print(f"h: {10**(-i)}\t\tApproksimasjon: {y}\t\tFeil: {y-np.e**1.5}")

def oppgave2():
    print("Oppgave 2:\nFasit:",np.e**1.5)
    for i in range(1,18):
        y=(np.e**(1.5+10**(-i))-np.e**(1.5-10**(-i)))/10**(-i)/2
        print(f"h: {10**(-i)}\t\tApproksimasjon: {y}\t\tFeil: {y-np.e**1.5}")

def oppgave3():
    print("Oppgave 3:\nFasit:",np.e**1.5)
    for i in range(1,18):
        h=10**(-i)
        y=(np.e**(1.5-2*h)-8*np.e**(1.5-h)+8*np.e**(1.5+h)-np.e**(1.5+2*h))/h/12
        print(f"h: {10**(-i)}\t\tApproksimasjon: {y}\t\tFeil: {y-np.e**1.5}")

def animateMatrix(m,FPS=60):
    clock = pg.time.Clock()
    WIDTH,HEIGHT=900,600
    WIN = pg.display.set_mode((WIDTH, HEIGHT))
    run=1
    frame=0
    mLength=len(m)
    frameLength=len(m[0])
    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = 0
        WIN.fill((255,255,255))
        for i in range(frameLength):
            pg.draw.circle(WIN,(255,0,0),(50+int(800*i/frameLength),int(300+200*m[frame][i])),1)
        frame+=2
        if frame>=mLength:
            frame=0
        pg.display.update()

def oppgave4():
    k=10**(-4)
    h=0.05
    N=int(1/h+1)
    T=1
    u=np.zeros((int(T/k)+1,N))
    for i in range(1,N-1):
        u[0,i]=np.sin(i*np.pi/(N-1))
    for j in range(int(T/k)):
        for i in range(1,N-1):
            u[j+1,i]=(k/h**2)*((u[j,i+1]+u[j,i-1])-2*u[j,i])+u[j,i]
    animateMatrix(u,200)
    return u

def oppgave5():
    k=10**(-4)
    h=0.05
    N=int(1/h+1)
    T=0.02
    u=np.zeros((int(T/k)+1,N))
    for i in range(1,N-1):
        u[0,i]=np.sin(i*np.pi/(N-1))
    for j in range(int(T/k)):
        for i in range(2,N-2):
            u[j+1,i]=(k**2/h**2*(u[j,i+2]-2*u[j,i+1]+2*u[j,i]-2*u[j,i-1]+u[j,i-2])+u[j,i]*h**2)/(h**2+k)
        u[j+1,1]=(k**2/h**2*(u[j,3]-2*u[j,2]+2*u[j,1]-2*u[j,0]+u[j,0])+u[j,1]*h**2)/(h**2+k)
        u[j+1,N-2]=(k**2/h**2*(u[j,N-1]-2*u[j,N-1]+2*u[j,N-2]-2*u[j,N-3]+u[j,N-4])+u[j,N-2]*h**2)/(h**2+k)
    animateMatrix(u,40)
    return u

def oppgave6():
    k=10**(-4)
    h=0.05
    N=int(1/h+1)
    T=0.02
    u=np.zeros((int(T/k)+1,N))
    for i in range(1,N-1):
        u[0,i]=np.sin(i*np.pi/(N-1))
    for j in range(int(T/k)):
        for i in range(2,N-2):
            u[j+1,i]=(k**2/h**2*(u[j,i+2]-2*u[j,i+1]+2*u[j,i]-2*u[j,i-1]+u[j,i-2])/2+u[j,i]*h**2+k/2*(u[j,i+1]-2*u[j,i]+u[j,i-1]))/(h**2+k)
        u[j+1,1]=(k**2/h**2*(u[j,3]-2*u[j,2]+2*u[j,1]-2*u[j,0]+u[j,0])/2+u[j,1]*h**2+k/2*(u[j,2]-2*u[j,1]+u[j,0]))/(h**2+k)
        u[j+1,N-2]=(k**2/h**2*(u[j,N-1]-2*u[j,N-1]+2*u[j,N-2]-2*u[j,N-3]+u[j,N-4])/2+u[j,N-2]*h**2+k/2*(u[j,N-1]-2*u[j,N-2]+u[j,N-3]))/(h**2+k)
    animateMatrix(u,40)
    return u

def u(t,x=0.5):
    return np.e**(-np.pi**2*t)*np.sin(np.pi*x)

def sammenlikn(m4,m5,m6):
    m4ind=int(np.round(len(m4)/2)-1)
    m5ind=int(np.round(len(m5)/2)-1)
    m6ind=int(np.round(len(m6)/2)-1)
    plt.plot(np.linspace(0,1,len(m4[m4ind])),m4[m4ind],label="Eksplisitt")
    plt.plot(np.linspace(0,1,len(m5[m5ind])),m5[m5ind],label="Implisitt")
    plt.plot(np.linspace(0,1,len(m6[m6ind])),m6[m6ind],label="Crank-Nicholson")
    plt.plot(np.linspace(0,1,200),u(np.linspace(0,1,200)),label="Analytisk")
    plt.legend()
    plt.ylabel("u(0.5,t)")
    plt.xlabel("t")
    plt.show()


# oppgave1()
# oppgave2()
# oppgave3()
m4=np.transpose(oppgave4())
m5=np.transpose(oppgave5())
m6=np.transpose(oppgave6())
sammenlikn(m4,m5,m6)