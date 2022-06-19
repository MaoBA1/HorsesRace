from random import randrange
from time import sleep
horseList=[['Cisco',3,2,115],['Cash',4,2,40],
           ['Fancy',2,1,50],['Blue',10,3,55],
           ['Gypsy',14,5,120],['Jack',8,2,50],
           ['Spirit',10,4,75],['Lilly',3,5,70],
           ['Rebel',2,5,100],['Black Jack',10,4,40],
           ['Harley',7,1,30],['Prince',11,1,10]]
def HorseRace(r1,r2,dis=500):
    a,b=dis,dis
    while a>=0 and b>=0:
        a,b=a-randrange(10,50),b-randrange(10,50)
        if a<b and a>=0:
            print('{:<10s}[{:^3d}]:{:<10s}[{:^3d}]'.format(r1[0],a,r2[0],b))
        elif b<a and b>=0:
            print('{:<10s}[{:^3d}]:{:<10s}[{:^3d}]'.format(r2[0],b,r1[0],a))
        sleep(0.4)
    if a<b:
        print('{:<10s} finished first!'.format(r1[0]))
        print('{:<10s} finished on the second place'.format(r2[0]))
        return r1
    print('{:<10s} finished first!'.format(r2[0]))
    print('{:<10s} finished on the second place'.format(r1[0]))
    return r2
def ChoiceHorses(lis,c=4):
    l=[lis[randrange(len(lis))]]
    c-=1
    while c!=0:        
        h=lis[randrange(len(lis))]
        f=True
        for i in l:            
            if i==h:
                f=False
        if f:
            l.append(h)
            c-=1
        else:
            c+=1
            l.remove(l[len(l)-1])
    return l
def printList(lis,n=0):
    if n==0 or abs(n)>len(lis):
        for i in range(len(lis)):
            print('{0:>2}.{1:<10}{2:>5}{3:>}{4:>4}'.format(i+1,lis[i][0],lis[i][1],lis[i][2],lis[i][3]))
    elif n>0:
        for i in range(n):
            print('{0:>2}.{1:<10}{2:>5}{3:>4}{4:>4}'.format(i+1,lis[i][0],lis[i][1],lis[i][2],lis[i][3]))
    else:
        n=abs(n)
        for i in range(len(lis)-n,len(lis)):
            print('{0:>2}.{1:<10}{2:>5}{3:>4}{4:>4}'.format(i+1,lis[i][0],lis[i][1],lis[i][2],lis[i][3]))
def HorseRacing(name,lis,dis=500,c=4):
    lis=ChoiceHorses(lis,c)
    print('[',name,']')
    printList(lis)
    while len(lis)>1:
        lis.append(HorseRace(lis.pop(0),lis.pop(0),dis))
        lis[-1][-1]+=5
    lis[-1][-1]+=5
    return lis
def sortHorses(lis,fil='points',order=2):
    hlist=[]
    if order==2:
        if fil=='age':
            while len(lis)!=0:
                Max=0
                h=None
                for i in lis:
                    if i[1]>Max:
                        Max=i[1]
                        h=i
                lis.remove(h)
                hlist.append(h)
        elif fil=='wins':
            while len(lis)!=0:
                Max=0
                h=None
                for i in lis:
                    if i[2]>Max:
                        Max=i[2]
                        h=i
                lis.remove(h)
                hlist.append(h)
        else:
            while len(lis)!=0:
                Max=0
                h=None
                for i in lis:
                    if i[3]>Max:
                        Max=i[3]
                        h=i
                lis.remove(h)
                hlist.append(h)
    else:
        if fil=='age':
            while len(lis)!=0:
                Min=lis[0][1]
                h=lis[0]
                for i in lis:
                    if i[1]<Min:
                        Min=i[1]
                        h=i
                lis.remove(h)
                hlist.append(h)
        elif fil=='wins':
            while len(lis)!=0:
                Min=lis[0][2]
                h=lis[0]
                for i in lis:
                    if i[2]<Min:
                        Min=i[2]
                        h=i
                lis.remove(h)
                hlist.append(h)
        else:
            while len(lis)!=0:
                Min=lis[0][3]
                h=lis[0]
                for i in lis:
                    if i[3]<Min:
                        Min=i[3]
                        h=i
                lis.remove(h)
                hlist.append(h)
    return hlist
def addHorse(lis):
    name,age,win,points=str(input('Enter horse name:')),int(input('Enter horse age:')),int(input('Enter number of wins:')),int(input('Enter horse points:'))
    horse=[name,age,win,points]
    lis.append(horse)    
    lis=sortHorses(lis,fil='points',order=2)
    return lis
def removeHorse(lis):
    h,Min=lis[0],lis[0][3]
    for i in lis:
        if i[3]<Min:
            Min=i[3]
            h=i
    print(h[0],'is removed') 
    lis.remove(h)
    return lis
def menu(lis):
    print('-----------main menu-------------')
    print('[1]Print horses list')
    print('[2]Sort horses list')
    print('[3]Add horse')
    print('[4]Remove horse')
    print('[5]Horse Racing')
    print('[6]Exit')
    ch=None
    while ch!=6:
        ch=int(input('Enter your choice:'))
        if ch==1:
            ch1=int(input('0-all,positive-first,negative-last:')or"0")
            printList(lis,ch1)
        elif ch==2:
            ch1=str(input('[points/wins/age], choice or enter to default:')or"points")
            ch2=int(input('[Ascending/Descending order], choice[1/2] or enter to default:')or"2")
            lis=sortHorses(lis,ch1,ch2)            
        elif ch==3:
            lis=addHorse(lis)
        elif ch==4:
            lis=removeHorse(lis)
        elif ch==5:
            ch1=str(input('Enter horse racing name:')or"Race")
            ch2=int(input('Enter number of horses:')or"4")
            ch3=int(input('Enter distance:')or"500")
            HorseRacing(ch1,lis,ch3,ch2)
        elif ch==6:
            input()
        else:
            print('Bad choice try again!')
menu(horseList)
                
            
            
    




        

