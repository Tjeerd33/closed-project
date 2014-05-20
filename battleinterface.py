
power=10000
engines=10
canon_batterys1=500
canon_battery1= True
canon_batterys2=500
canon_battery2= True
canon_batterys3=500
canon_battery3= True
canon_batterys4=300 #normal is 500
canon_battery4= True
canon_batterys5=10
canon_battery5= False
canon_batterys6=0
canon_battery6= False
canon_batterys7=0
canon_battery7= False
canon_batterys8=0
canon_battery8= False
canon_batterys9=0
canon_battery9= False
hull=1654 #full is 2000
shieldfront=300 #shields max is 900
shield_front= True
shieldmid=350
shield_mid= True
shieldback=200
shield_back= True
mainweapona=800 #full power is 800
mainweaponb= True
question_answerd=0
ftl_overload=0
import time
import random
enemy_numbers=3
shieldoverdrive=0
cargobay={'nitrogen':400,'drones':40,'metal':50,'hydrogen':500,'electronics':10}
orbit=False
collecting=False
collectiontime=0
engines=300
engine= True
options_active=0
wait=0

#star system info
system='Taurie-48a1'
starsclass='a1'
planets={'Icarus-3a':('gas planet'),'Icarus-3b':('Iron based planet'),'Icarus-3c':('gas planet')}
planetdistance={'Icarus-3a':2352,'Icarus-3b':329905,'Icarus-3c':6568223}
starsystems=['Delta-37g2','Gamma-492b2']

#battle interface
positions=['front','mid','back']
target=0
go=1
classes=['scout','scout','scout','scout','battleship','battleship','battleship','gunship','gunship','transport','transport','commandship']
ftl_cooldown=10
jump=0


#enemy 1
class1=random.choice(classes)
distance1=random.randint(-4000,4000)
if(class1=='scout'):
    enemy_shields1=450
    enemy_hull1=500
    enemy_weapon1=0
    enemy_weapons1= True
    enemy1_damagemin=5
    enemy1_damagemax=50
    speed1=600
elif(class1=='battleship'):
    enemy_shields1=900
    enemy_hull1=1000
    enemy_weapon1=0
    enemy_weapons1= True
    enemy1_damagemin=10
    enemy1_damagemax=100
    speed1=400
elif(class1=='transport'):
    enemy_shields1=1000
    enemy_hull1=1500
    enemy_weapon1=0
    enemy_weapons1= True
    enemy1_damagemin=5
    enemy1_damagemax=50
    speed1=300
elif(class1=='commandship'):
    enemy_shields1=1500
    enemy_hull1=2000
    enemy_weapon1=40
    enemy_weapons1= True
    enemy1_damagemin=50
    enemy1_damagemax=200
    speed1=200
elif(class1=='gunship'):
    enemy_shields1=500
    enemy_hull1=500
    enemy_weapon1=200
    enemy_weapons1= True
    enemy1_damagemin=100
    enemy1_damagemax=100
    speed1=300
#enemy 2
class2=random.choice(classes)
distance2=random.randint(-4000,4000)
if(class2=='scout'):
    enemy_shields2=450
    enemy_hull2=500
    enemy_weapon2=0
    enemy_weapons2= True
    enemy2_damagemin=5
    enemy2_damagemax=50
    speed2=600
elif(class2=='battleship'):
    enemy_shields2=900
    enemy_hull2=1000
    enemy_weapon2=0
    enemy_weapons2= True
    enemy2_damagemin=10
    enemy2_damagemax=100
    speed2=400
elif(class2=='transport'):
    enemy_shields2=1000
    enemy_hull2=1500
    enemy_weapon2=0
    enemy_weapons2= True
    enemy2_damagemin=5
    enemy2_damagemax=50
    speed2=300
elif(class2=='commandship'):
    enemy_shields2=1500
    enemy_hull2=2000
    enemy_weapon2=40
    enemy_weapons2= True
    enemy2_damagemin=50
    enemy2_damagemax=200
    speed2=200
elif(class2=='gunship'):
    enemy_shields2=500
    enemy_hull2=500
    enemy_weapon2=200
    enemy_weapons2= True
    enemy2_damagemin=100
    enemy2_damagemax=100
    speed2=300
#enemy 3
class3=random.choice(classes)
distance3=random.randint(-4000,4000)
if(class3=='scout'):
    enemy_shields3=450
    enemy_hull3=500
    enemy_weapon3=0
    enemy_weapons3= True
    enemy3_damagemin=5
    enemy3_damagemax=50
    speed3=600
elif(class3=='battleship'):
    enemy_shields3=900
    enemy_hull3=1000
    enemy_weapon3=0
    enemy_weapons3= True
    enemy3_damagemin=10
    enemy3_damagemax=100
    speed3=400
elif(class3=='transport'):
    enemy_shields3=1000
    enemy_hull3=1500
    enemy_weapon3=0
    enemy_weapons3= True
    enemy3_damagemin=5
    enemy3_damagemax=50
    speed3=300
elif(class3=='commandship'):
    enemy_shields3=1500
    enemy_hull3=2000
    enemy_weapon3=40
    enemy_weapons3= True
    enemy3_damagemin=50
    enemy3_damagemax=200
    speed3=200
elif(class3=='gunship'):
    enemy_shields3=500
    enemy_hull3=500
    enemy_weapon3=200
    enemy_weapons3= True
    enemy3_damagemin=100
    enemy3_damagemax=100
    speed3=300
#enemy 4
position4=random.choice(positions)
class4=random.choice(classes)
distance4=random.randint(100,5000)
enemy_shields4=0
enemy_hull4=0
enemy_weapons4=0
enemy_weapons4= True
#battle presets
salvage1=0
salvage2=0
salvage3=0
ftl_active=0
repair=0
shield_total=shieldfront+shieldmid+shieldback
course_plot=0
rand=0
scan=0
engines=100
engine= True
options=['jump to ftl','fire weapons','start repairing','transfer power','status    report',
'plot course','scan area','toggle shield overdrive','fire drones','collect raw materials','toggle drone building','salvage','quit']#setting options
while(hull>0)and(ftl_active==0)and(system=='Taurie-48a1'):#loop until ftl jump is made or ship is destroyed
    if(distance1>1500):#positioning enemy's
        position1='back'
    elif(distance1<1500)and(distance1>-1500):
        position1='mid'
    elif(distance1<-1500):
        position1='front'
    if(distance2>1500):
        position2='back'
    elif(distance2<1500)and(distance1>-1500):
        position2='mid'
    elif(distance2<-1500):
        position2='front'
    if(distance3>1500):
        position3='back'
    elif(distance3<1500)and(distance3>-1500):
        position3='mid'
    elif(distance3<-1500):
        position3='front'
    if(options_active==0):
        if(collecting==True)and(collectiontime>0):
            collectiontime=collectiontime-2
        elif(collecting==True)and(collectiontime==0)and(orbit==True):
            print('the probe is back')
            time.sleep(1)
            if(orbita=='Icarus-3a'):
                extrahydrogen=random.randint(30,400)
                cargobay['hydrogen']=cargobay['hydrogen']+extrahydrogen
                print('collected',extrahydrogen,'hydrogen')
                time.sleep(1)
                extranitrogen=random.randint(50,800)
                cargobay['nitrogen']=cargobay['nitrogen']+extranitrogen
                print('collected',extranitrogen,'nitrogen')
                time.sleep(1)
                collecting=False
            elif(orbita=='Icarus-3b'):
                extrametal=random.randint(100,200)
                print('collected',extrametal,'metal')
                cargobay['metal']=cargobay['metal']+extrametal
                time.sleep(1)
                collecting=False
            elif(orbita=='Icarus-3c'):
                extrahydrogen=random.randint(40,800)
                cargobay['hydrogen']=cargobay['hydrogen']+extrahydrogen
                print('collected',extrahydrogen,'hydrogen')
                time.sleep(1)
                extranitrogen=random.randint(900,1000)
                cargobay['nitrogen']=cargobay['nitrogen']+extranitrogen
                print('collected',extranitrogen,'nitrogen')
                time.sleep(1)
                collecting=False
        ftl_cooldown=ftl_cooldown-1#counting down until you can use ftl
        if(ftl_cooldown==0):
            print('ftl drive online')
        if(engines>0)and(engine==True):#calculate distance
            orbit=False
            distance1=distance1+engines
            distance2=distance2+engines
            distance3=distance3+engines
            cargobay['hydrogen']=cargobay['hydrogen']+engines/100#collecting space dust
            planetdistance['Icarus-3a']=planetdistance['Icarus-3a']-engines
            planetdistance['Icarus-3b']=planetdistance['Icarus-3b']-engines
            planetdistance['Icarus-3c']=planetdistance['Icarus-3c']-engines
            if(planetdistance['Icarus-3a']>=-200):
                if(planetdistance['Icarus-3a']<=200):
                    print('planet in orbital range')
                    orbital=input('do you want to orbit?')
                    if(orbital=='yes')or(orbital=='Yes')or(orbital=='ja'):
                        engines=0
                        time.sleep(2)
                        print('we are now in orbit')
                        orbit= True
                        print('start engines to break from orbit')
                        if(planetdistance['Icarus-3a']<=200)and(planetdistance['Icarus-3a']>=-200)and(orbit==True):
                            print('you are in orbit around Icarus-3a')
                            orbita='Icarus-3a'
            if(planetdistance['Icarus-3b']>=-200):
                if(planetdistance['Icarus-3b']<=200):
                    print('planet in orbital range')
                    orbital=input('do you want to orbit?')
                    if(orbital=='yes')or(orbital=='Yes')or(orbital=='ja'):
                        engines=0
                        time.sleep(2)
                        print('we are now in orbit')
                        orbit= True
                        print('start engines to break from orbit')
                        if(planetdistance['Icarus-3b']<=200)and(planetdistance['Icarus-3b']>=-200)and(orbit==True):
                            print('you are in orbit around Icarus-3b')
                            orbita='Icarus-3b'
            elif(planetdistance['Icarus-3c']>=-200):
                if(planetdistance['Icarus-3c']<=200):
                    print('planet in orbital range')
                    orbital=input('do you want to orbit?')
                    if(orbital=='yes')or(orbital=='Yes')or(orbital=='ja'):
                        engines=0
                        time.sleep(2)
                        print('we are now in orbit')
                        orbit= True
                        print('start engines to break from orbit')
                        if(planetdistance['Icarus-3c']<=200)and(planetdistance['Icarus-3c']>=-200)and(orbit==True):
                            print('you are in orbit around Icarus-3c')
                            orbita='Icarus-3c'
        elif(engines<0)and(engine==True):#calculate reversed distance
            orbit=False
            distance1=distance1+engines
            distance2=distance2+engines
            distance3=distance3+engines
            cargobay['hydrogen']=cargobay['hydrogen']-engines/100#collecting space dust
            planetdistance['Icarus-3a']=planetdistance['Icarus-3a']+engines
            planetdistance['Icarus-3b']=planetdistance['Icarus-3b']+engines
            planetdistance['Icarus-3c']=planetdistance['Icarus-3c']+engines
            if(planetdistance['Icarus-3a']>=-200):
                if(planetdistance['Icarus-3a']<=200):
                    print('planet in orbital range')
                    orbital=input('do you want to orbit?')
                    if(orbital=='yes')or(orbital=='Yes')or(orbital=='ja'):
                        engines=0
                        time.sleep(2)
                        print('we are now in orbit')
                        orbit= True
                        print('start engines to break from orbit')
                        if(planetdistance['Icarus-3a']<=200)and(planetdistance['Icarus-3a']>=-200)and(orbit==True):
                            print('you are in orbit around Icarus-3a')
                            orbita='Icarus-3a'
            if(planetdistance['Icarus-3b']>=-200):
                if(planetdistance['Icarus-3b']<=200):
                    print('planet in orbital range')
                    orbital=input('do you want to orbit?')
                    if(orbital=='yes')or(orbital=='Yes')or(orbital=='ja'):
                        engines=0
                        time.sleep(2)
                        print('we are now in orbit')
                        orbit= True
                        print('start engines to break from orbit')
                        if(planetdistance['Icarus-3b']<=200)and(planetdistance['Icarus-3b']>=-200)and(orbit==True):
                            print('you are in orbit around Icarus-3b')
                            orbita='Icarus-3b'
            elif(planetdistance['Icarus-3c']>=-200):
                if(planetdistance['Icarus-3c']<=200):
                    print('planet in orbital range')
                    orbital=input('do you want to orbit?')
                    if(orbital=='yes')or(orbital=='Yes')or(orbital=='ja'):
                        engines=0
                        time.sleep(2)
                        print('we are now in orbit')
                        orbit= True
                        print('start engines to break from orbit')
                        if(planetdistance['Icarus-3c']<=200)and(planetdistance['Icarus-3c']>=-200)and(orbit==True):
                            print('you are in orbit around Icarus-3c')
                            orbita='Icarus-3c'
        if(distance1>1500)or(distance1<-1500)and(enemy_hull1>0):#calculate enemy distance
            if(distance1>0):
                distance1=distance1-speed1
            elif(distance1<0):
                distance1=distance1+speed1
        if(distance2>1500)or(distance2<-1500)and(enemy_hull2>0):
            if(distance2>0):
                distance2=distance2-speed2
            elif(distance2<0):
                distance2=distance2+speed2
        if(distance3>1500)or(distance3<-1500)and(enemy_hull3>0):
            if(distance3>0):
                distance3=distance3-speed3
            elif(distance3<0):
                distance3=distance3+speed3
        repaired= random.randint(0,90)
        #resetting some intergers
        backdamage=0
        frontdamage=0
        middamage=0
        if(enemy_hull1>0):
            number1=1
        elif(enemy_hull1<=0):
            number1=0
        if(enemy_hull2>0):
            number2=1
        elif(enemy_hull2<=0):
            number2=0
        if(enemy_hull3>0):
            number3=1
        elif(enemy_hull3<=0):
            number3=0
        enemy_numbers=number1+number2+number3#update enemy numbers
        if(repaired==1)and(repair==1)and(canon_battery1==False):#checking repair status
            canon_battery1=True
            print('cannon 1 repaired')
        if(repaired==2)and(repair==1)and(canon_battery2==False):
            canon_battery2=True
            print('cannon 2 repaired')
        if(repaired==3)and(repair==1)and(canon_battery3==False):
            canon_battery3=True
            print('cannon 3 repaired')
        if(repaired==4)and(repair==1)and(canon_battery4==False):
            canon_battery4=True
            print('cannon 4 repaired')
        if(repaired==5)and(repair==1)and(canon_battery5==False):
            canon_battery5=True
            print('cannon 5 repaired')
        if(repaired==6)and(repair==1)and(canon_battery6==False):
            canon_battery6=True
            print('cannon 6 repaired')
        if(repaired==7)and(repair==1)and(canon_battery7==False):
            canon_battery7=True
            print('cannon 7 repaired')
        if(repaired==8)and(repair==1)and(canon_battery8==False):
            canon_battery8= True
            print('cannon 8 repaired')
        if(repaired==9)and(repair==1)and(canon_battery9==False):
            canon_battery9=True
            print('cannon 9 repaired')
        if(repaired==10)and(repair==1)and(mainweaponb==False):
            mainweaponb=True
            print('main weapon repaired')
        if(repaired==11)and(repair==1)and(hull<2000):
            hull=hull+20
            print('hull repaired')
            if(hull>2000):
                hull=2000
                print('hull fully repaired')
        if(repaired==12)and(repair==1)and(hull<2000):
            hull=hull+20
            print('hull repaired')
            if(hull>2000):
                hull=2000
                print('hull fully repaired')
        if(repaired==13)and(repair==1)and(hull<2000):
            hull=hull+20
            print('hull repaired')
            if(hull>2000):
                hull=2000
                print('hull fully repaired')
        if(repaired==14)and(repair==1)and(shield_front==False):
            shield_front==True
            print('shield front repaired')
        if(repaired==15)and(repair==1)and(shield_mid==False):
            shield_mid=True
            print('shield mid repaired')
        if(repaired==16)and(repair==1)and(shield_back==False):
            shield_back= True
            print('shield back repaired')
        if(repaired==17)and(repair==1)and(engine==False):
            engine=True
            print('engines repaired')
        if(repaired==18)and(repair==1)and(engine==False):
            engine=True
            print('engines repaired')
        if(repaired==19)and(repair==1)and(engine==False):
            engine=True
            print('engines repaired')
        if(repaired==20)and(repair==1)and(engine==False):
            engine=True
            print('engines repaired')    
        if(hull<100):
            print('warning! hull is critically low')
            time.sleep(1)
        if(shieldfront==0):
            print('warning! front shield is down')
            time.sleep(1)
        if(shieldmid==0):
            print('warning! mid shield is down')
            time.sleep(1)
        if(shieldback==0):
            print('warning! rear shield is down')
            time.sleep(1)
        target=0
        #preset for damage
        damage1=0
        damage2=0
        damage3=0
        damage4=0
        damage5=0
        damage6=0
        damage7=0
        damage8=0
        damage9=0
        damagemain=0
    elif(options_active>0):
        options_active=0
    if(wait<1):
        action=input('input:')#prompt for action

    if(action=='wait'):
        wait=int(input('how many turns?'))
        action='waiting'

    elif(action=='waiting'):
        wait=wait-1

    elif(action=='salvage'):
        if(enemy_hull1==0)and(distance1<=400)and(distance1>=-400)and(salvage1<1):
            print('salveging remains of enemy 1')
            time.sleep(5)
            extraelectronics=random.randint(1,20)
            print('found some electronics parts:',extraelectronics)
            cargobay['electronics']=cargobay['electronics']+extraelectronics
            extrametal=random.randint(1,40)
            print('found some metal:',extrametal)
            cargobay['metal']=cargobay['metal']+extrametal
            salvage1=1
        elif(enemy_hull2==0)and(distance2<=400)and(distance2>=-400)and(salvage2<1):
            print('salveging remains of enemy 2')
            time.sleep(5)
            extraelectronics=random.randint(1,20)
            print('found some electronics parts:',extraelectronics)
            cargobay['electronics']=cargobay['electronics']+extraelectronics
            extrametal=random.randint(1,40)
            print('found some metal:',extrametal)
            cargobay['metal']=cargobay['metal']+extrametal
            salvage2=1
        elif(enemy_hull3==0)and(distance3<=400)and(distance3>=-400)and(salvage3<1):
            print('salveging remains of enemy 3')
            time.sleep(5)
            extraelectronics=random.randint(1,20)
            print('found some electronics parts:',extraelectronics)
            cargobay['electronics']=cargobay['electronics']+extraelectronics
            extrametal=random.randint(1,40)
            print('found some metal:',extrametal)
            cargobay['metal']=cargobay['metal']+extrametal
            salvage3=1
        else:
            print('can olny salvage destroyed enemy ships')
            print('cannot salvage if enemy is out of range(200,-200)')
            print('cannot salvage enemy more than once')

    elif(action=='collect raw materials'):
        if(orbit==False):
            print('you can only do this in orbit')
            time.sleep(2)
        elif(orbit==True):
            time.sleep(1)
            print('launched capsule')
            collectiontime=10
            time.sleep(1)
            print('it will take some time to find materials')
            collecting=True
            time.sleep(1)

    elif(action=='fire drones'):
        while(target!='1')and(target!='2')and(target!='3')and(target!='untracable')and(target!='quit'):
            target=input('target:')
            if(target=='1')and(enemy_hull1<=0):
                print('cannot find target')
                target=0
            elif(target=='2')and(enemy_hull2<=0):
                print('cannot find target')
                target=0
            elif(target=='3')and(enemy_hull3<=0):
                print('cannot find target')
                target=0
            dronenumbers=int(input('numbers:'))
            if(cargobay['drones']-dronenumbers<0):
                print('not enough drones')
            elif(cargobay['drones']-dronenumbers>=0):
                cargobay['drones']=cargobay['drones']-dronenumbers
                if(target=='1'):
                    enemy_hull1=enemy_hull1-(50*dronenumbers)
                    print('drones hit! enemy hull damaged')
                    if(enemy_hull1<=0):
                        enemy_hull1=0
                        print('enemy 1 destroyed')
                if(target=='2'):
                    enemy_hull2=enemy_hull2-(50*dronenumbers)
                    print('drones hit! enemy hull damaged')
                    if(enemy_hull2<=0):
                        enemy_hull2=0
                        print('enemy 2 destroyed')
                if(target=='3'):
                    enemy_hull3=enemy_hull3-(50*dronenumbers)
                    print('drones hit! enemy hull damaged')
                    if(enemy_hull3<=0):
                        enemy_hull3=0
                        print('enemy 3 destroyed')

    elif(action=='toggle shield overdrive'):
        time.sleep(1)
        if(shieldoverdrive==0):
            print('shield overdrive activated')
            shieldoverdrive=1
            time.sleep(1)
        elif(shieldoverdrive==1):
            print('shield overdrive deactivated')
            time.sleep(1)
            shieldoverdrive=0

    elif(action=='scan area'):
        print('scanning area')
        time.sleep(2)
        print("enemy's in this area:")
        time.sleep(3)
        print('    ',enemy_numbers)
        print('enemy postions:')
        time.sleep(3)
        if(enemy_hull1>0):
            print('    ',position1)
        if(enemy_hull2>0):
            print('    ',position2)
        if(enemy_hull3>0):
            print('    ',position3)
        print('enemy shields are at:')
        time.sleep(2)
        if(enemy_hull1>0):
            print('    ',enemy_shields1)
        if(enemy_hull2>0):
            print('    ',enemy_shields2)
        if(enemy_hull3>0):
            print('    ',enemy_shields3)
        print('enemy hull is at')
        time.sleep(2)
        print('    ',enemy_hull1)
        print('    ',enemy_hull2)
        print('    ',enemy_hull3)
        print('density')
        time.sleep(1)
        print('enemy classes are:')
        if(enemy_hull1>0):
            print('    ',class1)
        if(enemy_hull2>0):
            print('    ',class2)
        if(enemy_hull3>0):
            print('    ',class3)
        print('enemy distance:')
        print('enemy 1:')
        print('    ',distance1)
        print('enemy 2:')
        print('    ',distance2)
        print('enemy3:')
        print('    ',distance3)
        print('planets in this system:')
        time.sleep(2)
        print(planets)
        time.sleep(1)
        print('planet distance:')
        print(planetdistance)
        time.sleep(2)
        scan=1
        print('systems nearby:')
        time.sleep(2)
        print(starsystems)
        time.sleep(3)

        

    elif(action=='plot course'):
        if(scan>0):
            print('choose your destination')
            time.sleep(2)
            print(starsystems)
            destination=0
            while(destination!='Gamma-492b2')and(destination!='Delta-37g2'):
                destination=input('destination:')
            time.sleep(1)
            print('plotting course')
            time.sleep(5)
            print('course plotted')
            course_plot=1
        elif(scan==0):
            print('plotting course to nearest star')
            time.sleep(2)
            destination='Gamma-492b2'
            course_plot=1

            
    elif(action=='quit'):
        hull=0
        ftl_active=1

    elif action=='transfer power':
        time.sleep(1)
        print('power levels now:')
        print('shields:')
        print('    front:',shieldfront,'power')
        print('    mid:  ',shieldmid,'power')
        print('    back: ',shieldback,'power')
        shield_total=shieldfront+shieldmid+shieldback
        print('total shield:',shield_total)
        time.sleep(1)
        print('weapons are at')
        time.sleep(1)
        print('    1:',canon_batterys1)
        print('    1:',canon_battery1)
        print('    2:',canon_batterys2)
        print('    2:',canon_battery2)
        print('    3:',canon_batterys3)
        print('    3:',canon_battery3)
        print('    4:',canon_batterys4)
        print('    4:',canon_battery4)
        time.sleep(1)
        print('    5:',canon_batterys5)
        print('    5:',canon_battery5)
        print('    6:',canon_batterys6)
        print('    6:',canon_battery6)
        print('    7:',canon_batterys7)
        print('    7:',canon_battery7)
        print('    8:',canon_batterys8)
        print('    8:',canon_battery8)
        print('    9:',canon_batterys9)
        print('    9:',canon_battery9)
        time.sleep(1)
        print('main weapon:',mainweapona,'status:',mainweaponb)
        print('hull is at',hull,'density')
        print('power:',power)
        print('engines:',engines)
        alter=input('alter:')
        if(alter=='options')or(alter=='?')or(alter=='help'):
            print('weapons, shields or engines')
        elif(alter=='weapons')or(alter=='weapon'):
            newcanon_batterys1=int(input('battery 1:   '))
            newcanon_batterys2=int(input('battery 2:   '))
            newcanon_batterys3=int(input('battery 3:   '))         
            newcanon_batterys4=int(input('battery 4:   '))
            newcanon_batterys5=int(input('battery 5:   '))
            newcanon_batterys6=int(input('battery 6:   '))
            newcanon_batterys7=int(input('battery 7:   '))
            newcanon_batterys8=int(input('battery 8:   '))
            newcanon_batterys9=int(input('battery 9:   '))
            newmainweapona=int(input('main weapon: '))
            if(newcanon_batterys1>500)or(newcanon_batterys2>500)or(newcanon_batterys3>500)or(newcanon_batterys4>500)or(newcanon_batterys5>500)or(newcanon_batterys6>500)or(newcanon_batterys7>500)or(newcanon_batterys8>500)or(newcanon_batterys9>500)or(newmainweapona>800):
                print('cannot maintain more than 500 power in normal weapons and cannot maintain more than 800 power in main weapon')
            elif(newcanon_batterys1<0)or(canon_batterys2<0)or(newcanon_batterys3<0)or(newcanon_batterys4<0)or(newcanon_batterys5<0)or(newcanon_batterys6<0)or(newcanon_batterys7<0)or(newcanon_batterys8<0)or(newcanon_batterys9<0)or(newmainweapona<0):
                print('error, power cannot be lower than 0')
            elif(newcanon_batterys1<=500)or(newcanon_batterys2<=500)or(newcanon_batterys3<=500)or(newcanon_batterys4<=500)or(newcanon_batterys5<=500)or(newcanon_batterys6<=500)or(newcanon_batterys7<=500)or(newcanon_batterys8<=500)or(newcanon_batterys9<=500)or(newmainweapona<=800):
                transport1=newcanon_batterys1-canon_batterys1
                transport2=newcanon_batterys2-canon_batterys2
                transport3=newcanon_batterys3-canon_batterys3
                transport4=newcanon_batterys4-canon_batterys4
                transport5=newcanon_batterys5-canon_batterys5
                transport6=newcanon_batterys6-canon_batterys6
                transport7=newcanon_batterys7-canon_batterys7
                transport8=newcanon_batterys8-canon_batterys8
                transport9=newcanon_batterys9-canon_batterys9
                transport10=newmainweapona-mainweapona
                power=power-transport1
                time.sleep(1)
                if(power<0):
                    power=power+transport1
                    print('transport1 failed: not enough power')
                elif(power>=0):
                    print('transport1 succesfull')
                    canon_batterys1=newcanon_batterys1
                power=power-transport2
                time.sleep(1)
                if(power<0):
                    power=power+transport2
                    print('transport2 failed: not enough power')
                elif(power>=0):
                    print('transport2 succesfull')
                    canon_batterys2=newcanon_batterys2
                power=power-transport3
                time.sleep(1)
                if(power<0):
                    power=power+transport3
                    print('transport3 failed: not enough power')
                elif(power>=0):
                    print('transport3 succesfull')
                    canon_batterys3=newcanon_batterys3
                power=power-transport4
                time.sleep(1)
                if(power<0):
                    power=power+transport4
                    print('transport4 failed: not enough power')
                elif(power>=0):
                    print('transport4 succesfull')
                    canon_batterys4=newcanon_batterys4
                power=power-transport5
                time.sleep(1)
                if(power<0):
                    power=power+transport5
                    print('transport5 failed: not enough power')
                elif(power>=0):
                    print('transport5 succesfull')
                    canon_batterys5=newcanon_batterys5
                power=power-transport6
                time.sleep(1)
                if(power<0):
                    power=power+transport6
                    print('transport6 failed: not enough power')
                elif(power>=0):
                    print('transport6 succesfull')
                    canon_batterys6=newcanon_batterys6
                power=power-transport7
                time.sleep(1)
                if(power<0):
                    power=power+transport7
                    print('transport7 failed: not enough power')
                elif(power>=0):
                    print('transport7 succesfull')
                    canon_batterys7=newcanon_batterys7
                power=power-transport8
                time.sleep(1)
                if(power<0):
                    power=power+transport8
                    print('transport8 failed: not enough power')
                elif(power>=0):
                    print('transport8 succesfull')
                    canon_batterys8=newcanon_batterys8
                power=power-transport9
                time.sleep(1)
                if(power<0):
                    power=power+transport9
                    print('transport9 failed: not enough power')
                elif(power>=0):
                    print('transport9 succesfull')
                    canon_batterys9=newcanon_batterys9
                power=power-transport10
                time.sleep(1)
                if(power<0):
                    power=power+transport10
                    print('transport to mainweapon failed: not enough power')
                elif(power>=0):
                    mainweapona=newmainweapona
                    print('transport to mainweapon succesfull')                
        elif(alter=='shields')or(alter=='shield')or(alter=='Shields')or(alter=='Shield'):
            if(shield_mid== True):
                newshieldmid=int(input('shield mid:   '))
            elif(shield_mid== False):
                print('mid shield offline')
            if(shield_front== True):
                newshieldfront=int(input('shield front: '))
            elif(shield_front==False):
                print('front shield offline')
            if(shield_back== True):
                newshieldback=int(input('shield back:  '))
            elif(shield_back== False):
                print('rear shield offline')
            if(newshieldmid>900)or(newshieldfront>900)or(newshieldback>900):
                print('error shields cannot contain more than 900 power')
            elif(newshieldmid<0)or(newshieldfront<0)or(newshieldback<0):
                print('error shields cannot contain less than 0 power')
            else:
                transport1=newshieldmid-shieldmid
                transport2=newshieldfront-shieldfront
                transport3=newshieldback-shieldback
                power=power-transport1
                time.sleep(1)
                if(power<0):
                    print('error: insufficient power')
                    print('transport 1 failed')
                    power=power+transport1
                elif(power>=0):
                    print('transport 1 succesfull')
                    shieldmid=newshieldmid
                power=power-transport2
                time.sleep(1)
                if(power<0):
                    print('error: insufficient power')
                    print('transport 2 failed')
                    power=power+transport2
                elif(power>=0):
                    print('transport 2 succesfull')
                    shieldfront=newshieldfront
                power=power-transport3
                time.sleep(1)
                if(power<0):
                    print('error: insufficient power')
                    print('transport 3 failed')
                    power=power+transport3
                elif(power>=0):
                    print('transport 3 succesfull')
                    shieldback=newshieldback
                time.sleep(1)
        if(alter=='engines'):
            newengines=int(input('engines:   '))
            power=power-newengines
            if(power<0):
                power=power+newengines
                print('error: insufficient power')
            elif(newengines>400):
                power=power+newengines
                print('error: engines cannot contain more than 400 power')
            elif(newengines<0):
                power=power+newengines
                power=power+newengines
                print('reversed course')
                engines=newengines
            elif(newengines<-400):
                print('error: engines cannot contain more than 400 power')
            else:
                engines=newengines
                print('transfer succesfull')

    elif action=='start repairing':
        time.sleep(1)
        print('started repairs')
        repair=1

    elif action=='fire weapons':
        while(target!='1')and(target!='2')and(target!='3')and(target!='untracable')and(target!='quit')and(target!='x'):
            target=input('target:')
            if((target=='1')and(enemy_hull1<=0))or((target=='1')and(distance1>2500)):
                print('cannot find target')
                target=0
            if((target=='2')and(enemy_hull2<=0))or((target=='2')and(distance2>2500)):
                print('cannot find target')
                target=0
            if((target=='3')and(enemy_hull3<=0))or((target=='3')and(distance3>2500)):
                print('cannot find target')
                target=0
            if((distance1>2500)and(distance2>2500))and(distance3>2500):
                print('no targets in range')
                target='untracable'
        time.sleep(1)
        if(target=='x'):
            target=random.choice('1','2','3')
        if(target!='untracable')or(target=='1')or(target=='2')or(target=='3'):
            print('locking on')
            time.sleep(1)
            print('target locked')
            if(canon_batterys1>0)and(canon_battery1==True):
                damage1=random.randint(10,40)
                canon_batterys1=canon_batterys1-damage1
                print('cannon 1 firing')
                if(canon_batterys1<0):
                    canon_batterys1=0
                time.sleep(1)
            if(canon_batterys2>0)and(canon_battery2==True):
                damage2=random.randint(10,40)
                canon_batterys2=canon_batterys2-damage2
                print('cannon 2 firing')
                if(canon_batterys2<0):
                    canon_batterys2=0
                time.sleep(1)
            if(canon_batterys3>0)and(canon_battery3==True):
                damage3=random.randint(10,40)
                canon_batterys3=canon_batterys3-damage3
                print('cannon 3 firing')
                if(canon_batterys3<0):
                    canon_batterys3=0
                time.sleep(1)
            if(canon_batterys4>0)and(canon_battery4==True):
                damage4=random.randint(10,40)
                canon_batterys4=canon_batterys4-damage4
                print('cannon 4 firing')
                if(canon_batterys4<0):
                    canon_batterys4=0
                time.sleep(1)
            if(canon_batterys5>0)and(canon_battery5==True):
                damage5=random.randint(10,40)
                canon_batterys5=canon_batterys5-damage5
                print('cannon 5 firing')
                if(canon_batterys5<0):
                    canon_batterys5=0
                time.sleep(1)
            if(canon_batterys6>0)and(canon_battery6==True):
                damage6=random.randint(10,40)
                canon_batterys6=canon_batterys6-damage6
                print('cannon 6 firing')
                if(canon_batterys6<0):
                    canon_batterys6=0
                time.sleep(1)
            if(canon_batterys7>0)and(canon_battery7==True):
                damage7=random.randint(10,40)
                canon_batterys7=canon_batterys7-damage7
                print('cannon 7 firing')
                if(canon_batterys7<0):
                    canon_batterys7=0
                time.sleep(1)
            if(canon_batterys8>0)and(canon_battery8==True):
                damage8=random.randint(10,40)
                canon_batterys8=canon_batterys8-damage8
                print('cannon 8 firing')
                if(canon_batterys8<0):
                    canon_batterys8=0
                time.sleep(1)
            if(canon_batterys9>0)and(canon_battery9==True):
                damage9=random.randint(10,40)
                canon_batterys9=canon_batterys9-damage9
                print('cannon 9 firing')
                if(canon_batterys9<0):
                    canon_batterys9=0
                time.sleep(1)
            if(mainweapona>0)and(mainweaponb==True):
                damagemain=random.randint(20,80)
                mainweapona=mainweapona-damagemain
                print('mainweapon  firing')
                if(mainweapona<0):
                    mainweapona=0
                time.sleep(1)
            total_damage=damage1+damage2+damage3+damage4+damage5+damage6+damage7+damage8+damage9+damagemain 
            if(target=='1')and(distance1<2500):
                if(enemy_shields1>0):
                        enemy_shields1=enemy_shields1-total_damage
                        print('youd did',total_damage,"to enemy 1's shields")
                        if(enemy_shields1<0):
                            enemy_hull1=enemy_hull1+enemy_shields1
                            enemy_shields1=0
                elif(enemy_shields1==0):
                    enemy_hull1=enemy_hull1-total_damage
                    print('you did',total_damage,"to enemy 1's hull")
                    if(enemy_hull1<=0):
                        enemy_hull1=0
                        print('enemy 1 destroyed')
                    rand=random.randint(0,20)
                    if(rand==1):
                        enemy_weapons1= False
                        print('enemy weapons disabled')
                    if(rand==2):
                        speed1=0
                        print('enemy engines disabled')
            if(target=='2')and(distance2<2500):
                if(enemy_shields2>0):
                    enemy_shields2=enemy_shields2-total_damage
                    print('youd did',total_damage,"to enemy 2's shields")
                    if(enemy_shields2<0):
                            enemy_hull2=enemy_hull2+enemy_shields2
                            enemy_shields2=0
                            print('enemy shields depleted, hull damaged')
                elif(enemy_shields2==0):
                    enemy_hull2=enemy_hull2-total_damage
                    print('you did',total_damage,"to enemy 2's hull")
                    if(enemy_hull2<=0):
                        enemy_hull2=0
                        print('enemy 2 destroyed')
                    rand=random.randint(0,20)
                    if(rand==1):
                        enemy_weapons2= False
                        print('enemy weapons disabled')
                    if(rand==2):
                        speed2=0
                        print('enemy engines disabled')
            if(target=='3')and(distance3<2500):
                if(enemy_shields3>0):
                    enemy_shields3=enemy_shields3-total_damage
                    print('youd did',total_damage,"to enemy 3's shields")
                    if(enemy_shields3<0):
                            enemy_hull3=enemy_hull3+enemy_shields3
                            enemy_shields3=0
                            print('enemy shields depleted, hull damaged')
                elif(enemy_shields3==0):
                    enemy_hull3=enemy_hull3-total_damage
                    print('you did',total_damage,"to enemy 3's hull")
                    if(enemy_hull3<=0):
                        enemy_hull3=0
                        print('enemy 3 destroyed')
                    rand=random.randint(0,20)
                    if(rand==1):
                        enemy_weapons3= False
                        print('enemy weapons disabled')
                    if(rand==2):
                        speed3=0
                        print('enemy engines disabled')
                
                
    elif action=='options'or action=='?' or action=='help':
        print(options)
        options_active=1
        print('maximum weapon power=500')
        print('maximum main weapon power=800')
        print('maximum shield power=900')
        print('maximum engines power=400')
        print('enemy class explenation:')
        print('scout: low fire power and low defenses they are fast and you cannot outrun them')
        print('battleship: medium fire power and medium defenses. they are as fast as you are  so if you have a head start you can outrun them')
        print('gunship: high fire power but weak shields and hull, they are slightly slower    than you')
        print('transport: low fire power but strong defenses, they are slightly slower than you')
        print('commandship: high fire power and strong defenses, you can easily outrun them')
        print('')
        print('drones: medium damage guided missels: they deal 50 damage per drone directly to the enemy hull. They are very limited but can be build from metal hydrogen and electronics')
        print('tip!: engines can be set to negative')
        print('tip!: if you break from orbit you will not collecet the probe you send before')
        print("tip!: minimum fire distance is 2500 for you and the enemy's")
        print('tip!: drones can be fired from any distance')
        print('tip!: you can recharge at a g2 type star')

    elif action=='status report':#prints the status of all systems
        print('status report:')
        print('shields are at')
        time.sleep(1)
        print('    front:',shieldfront,'power')
        print('    mid:  ',shieldmid,'power')
        print('    back: ',shieldback,'power')
        shield_total=shieldfront+shieldmid+shieldback
        print('total shield:',shield_total)
        time.sleep(3)
        print('weapons are at')
        time.sleep(2)
        print('    1:',canon_batterys1)
        print('    1:',canon_battery1)
        print('    2:',canon_batterys2)
        print('    2:',canon_battery2)
        print('    3:',canon_batterys3)
        print('    3:',canon_battery3)
        print('    4:',canon_batterys4)
        print('    4:',canon_battery4)
        time.sleep(1)
        print('    5:',canon_batterys5)
        print('    5:',canon_battery5)
        print('    6:',canon_batterys6)
        print('    6:',canon_battery6)
        print('    7:',canon_batterys7)
        print('    7:',canon_battery7)
        print('    8:',canon_batterys8)
        print('    8:',canon_battery8)
        print('    9:',canon_batterys9)
        print('    9:',canon_battery9)
        time.sleep(2)
        print('main weapon:',mainweapona,'status:',mainweaponb)
        print('hull is at',hull,'density')
        print('power:',power)
        time.sleep(1)
        print('engines:',engines)
        time.sleep(1)
        print('ftl cooldown:',ftl_cooldown)
        print('if ftl is less than 0 or 0: ftl drive online')
        time.sleep(2)
        print('cargo bay:',cargobay)
        time.sleep(1)
               
    elif action=='jump to ftl':
        if(course_plot<1)and(ftl_cooldown<=0):
            print('calculating path to nearest star')
            destination='Gamma-492b'
            print('if shields are down the ship will be destroyed')
            if(shieldback==0)or(shieldmid==0)or(shieldfront==0):
                print('warning! if you go to ftl with depleted shields the ship will tear apart')
            answer=input('continue?')
            if(answer=='yes'):
                go=1
            elif(answer=='no'):
                go=0
            else:
                print('error unkown command')
                go=0
            time.sleep(2)
            if(enemy_hull1>0)and(distance1<2500)and(distance1>-2500):
                if(enemy_weapon1>0)and(enemy_weapons1==True)and(hull>0):
                    print('enemy 1 is locking on')
                    time.sleep(1)
                    print('enemy 1 is discharging weapons')
                    damage= random.randint(enemy1_damagemin,enemy1_damagemax)
                    enemy_weapon1=enemy_weapon1-damage
                    print('enemy 1 did',damage,'damage')
                    if(position1=='back'):
                        if(shieldback>0):
                            shieldback=shieldback-damage
                            if(shieldback<0):
                                print('rear shields depleted')
                                hull=hull+shieldback
                                shieldback=0
                                print('hull damaged')
                        elif(shieldback==0):
                            hull=hull-damage
                            print('rear shields are down, hull damaged')
                            backdamage=1
                            if(hull<0):
                                hull=0
                                print('signal lost')
                    elif(position1=='mid'):
                        if(shieldmid>0):
                            shieldmid=shieldmid-damage
                            if(shieldmid<0):
                                print('mid shields depleted')
                                hull=hull+shieldmid
                                shieldmid=0
                                print('hull damaged')
                        elif(shieldmid==0):
                            hull=hull-damage
                            print('mid shields are down, hull damaged')
                            middamage=1
                            if(hull<0):
                                hull=0
                    elif(position1=='front'):
                        if(shieldfront>0):
                            shieldfront=shieldfront-damage
                            if(shieldfront<0):
                                print('front shields depleted')
                                hull=hull+shieldfront
                                shieldfront=0
                                print('hull damaged')
                        elif(shieldfront==0):
                            hull=hull-damage
                            print('front shields are down, hull damaged')
                            frontdamage=1
                            if(hull<0):
                                hull=0
                elif(enemy_weapon1<=0):
                    print('enemy 1 is charging weapons')
                    enemy_weapon1=500
            if(enemy_hull2>0)and(distance2<2500):
                if(enemy_weapon2>0)and(enemy_weapons2==True)and(hull>0)and(distance2>-2500):
                    print('enemy 2 is locking on')
                    time.sleep(1)
                    print('enemy 2 is discharging weapons')
                    damage= random.randint(enemy2_damagemin,enemy2_damagemax)
                    enemy_weapon2=enemy_weapon2-damage
                    print('enemy 2 did',damage,'damage')
                    if(position2=='back'):
                        if(shieldback>0):
                            shieldback=shieldback-damage
                            if(shieldback<0):
                                print('rear shields depleted')
                                hull=hull+shieldback
                                shieldback=0
                                print('hull damaged')
                        elif(shieldback==0):
                            hull=hull-damage
                            print('rear shields are down, hull damaged')
                            backdamage=1
                            if(hull<0):
                                hull=0
                                print('signal lost')
                    elif(position2=='mid'):
                        if(shieldmid>0):
                            shieldmid=shieldmid-damage
                            if(shieldmid<0):
                                print('mid shields depleted')
                                hull=hull+shieldmid
                                shieldmid=0
                                print('hull damaged')
                        elif(shieldmid==0):
                            hull=hull-damage
                            print('mid shields are down, hull damaged')
                            middamage=1
                            if(hull<0):
                                hull=0
                    elif(position2=='front'):
                        if(shieldfront>0):
                            shieldfront=shieldfront-damage
                            if(shieldfront<0):
                                print('front shields depleted')
                                hull=hull+shieldfront
                                shieldfront=0
                                print('hull damaged')
                        elif(shieldfront==0):
                            hull=hull-damage
                            print('front shields are down, hull damaged')
                            frontdamage=1
                            if(hull<0):
                                hull=0
                elif(enemy_weapon2<=0):
                    print('enemy 2 is charging weapons')
                    enemy_weapon2=500
            if(enemy_hull3>0)and(distance3<2500):
                if(enemy_weapon3>0)and(enemy_weapons3==True)and(hull>0)and(distance3>-2500):
                    print('enemy 3 is locking on')
                    time.sleep(1)
                    print('enemy 3 is discharging weapons')
                    damage= random.randint(enemy3_damagemin,enemy3_damagemax)
                    enemy_weapon3=enemy_weapon3-damage
                    print('enemy 3 did',damage,'damage')
                    if(position3=='back'):
                        if(shieldback>0):
                            shieldback=shieldback-damage
                            if(shieldback<0):
                                print('rear shields depleted')
                                hull=hull+shieldback
                                shieldback=0
                                print('hull damaged')
                        elif(shieldback==0):
                            hull=hull-damage
                            print('rear shields are down, hull damaged')
                            backdamage=1
                            if(hull<0):
                                hull=0
                                print('signal lost')
                    elif(position3=='mid'):
                        if(shieldmid>0):
                            shieldmid=shieldmid-damage
                            if(shieldmid<0):
                                print('mid shields depleted')
                                hull=hull+shieldmid
                                shieldmid=0
                                print('hull damaged')
                        elif(shieldmid==0):
                            hull=hull-damage
                            print('mid shields are down, hull damaged')
                            middamage=1
                            if(hull<0):
                                hull=0
                    elif(position3=='front'):
                        if(shieldfront>0):
                            shieldfront=shieldfront-damage
                            if(shieldfront<0):
                                print('front shields depleted')
                                hull=hull+shieldfront
                                shieldfront=0
                                print('hull damaged')
                        elif(shieldfront==0):
                            hull=hull-damage
                            print('front shields are down, hull damaged')
                            frontdamage=1
                            if(hull<0):
                                hull=0
                elif(enemy_weapon3<=0):
                    print('enemy 3 is charging weapons')
                    enemy_weapon3=500
            if(enemy_hull4>0)and(distance4<2500)and(distance4>-2500):
                if(enemy_weapon4>0)and(enemy_weapons4==True)and(hull>0):
                    print('enemy 4 is locking on')
                    time.sleep(1)
                    print('enemy 4 is discharging weapons')
                    damage= random.randint(enemy4_damagemin,enemy4_damagemax)
                    enemy_weapon4=enemy_weapon4-damage
                    print('enemy 4 did',damage,'damage')
                    if(position4=='back'):
                        if(shieldback>0):
                            shieldback=shieldback-damage
                            if(shieldback<0):
                                print('rear shields depleted')
                                hull=hull+shieldback
                                shieldback=0
                                print('hull damaged')
                        elif(shieldback==0):
                            hull=hull-damage
                            print('rear shields are down, hull damaged')
                            backdamage=1
                            if(hull<0):
                                hull=0
                                print('signal lost')
                    elif(position4=='mid'):
                        if(shieldmid>0):
                            shieldmid=shieldmid-damage
                            if(shieldmid<0):
                                print('mid shields depleted')
                                hull=hull+shieldmid
                                shieldmid=0
                                print('hull damaged')
                        elif(shieldmid==0):
                            hull=hull-damage
                            print('mid shields are down, hull damaged')
                            middamage=1
                            if(hull<0):
                                hull=0
                    elif(position4=='front'):
                        if(shieldfront>0):
                            shieldfront=shieldfront-damage
                            if(shieldfront<0):
                                print('front shields depleted')
                                hull=hull+shieldfront
                                shieldfront=0
                                print('hull damaged')
                        elif(shieldfront==0):
                            hull=hull-damage
                            print('front shields are down, hull damaged')
                            frontdamage=1
                            if(hull<0):
                                hull=0
                elif(enemy_weapon4<=0):
                    print('enemy 4 is charging weapons')
                    enemy_weapon4=500
            time.sleep(1)
            if(shieldfront==0)and(frontdamage==1):
                rand=random.randint(0,40)
                if(rand==1):
                    canon_battery1= False
                    print('cannon battery 1 offline')
                elif(rand==2):
                    canon_battery2= False
                    print('cannon battery 2 offline')
                elif(rand==3):
                    shield_front= False
                    print('shieldgenerator front offline')
            if(shieldmid==0)and(middamage==1):
                rand=random.randint(0,40)
                if(rand==0):
                    canon_battery3= False
                    print('cannon battery 3 offline')
                elif(rand==1):
                    canon_battery4= False
                    print('cannon battery 4 offline')
                elif(rand==2):
                    canon_battery5= False
                    print('cannon battery 5 offline')
                elif(rand==3):
                    mainweaponb= False
                    print('main weapon offline')
                elif(rand==4):
                    canon_battery6= False
                    print('cannon battery 6 offline')
                elif(rand==5):
                    shield_mid= False
                    print('shieldgenerator mid offline')
            if(shieldback==0)and(backdamage==1):
                rand=random.randint(0,40)
                if(rand==0):
                    canon_battery7= False
                    print('cannon battery 7 offline')
                elif(rand==1):
                    canon_battery8= False
                    print('cannon battery 8 offline')
                elif(rand==2):
                    canon_battery9= False
                    print('cannon battery 9 offline')
                elif(rand==3):
                    shieldback= False
                    print('shieldgenerator back offline')
            if(hull>0)and(go==1)and(ftl_cooldown<=0):
                if(course_plot<1):
                    print('path calculated, prepairing for jump')
                print('jump in 20 seconds')
            time.sleep(7)
            if(enemy_hull1>0)and(distance1<2500)and(distance1>-2500):
                if(enemy_weapon1>0)and(enemy_weapons1==True)and(hull>0):
                    print('enemy 1 is locking on')
                    time.sleep(1)
                    print('enemy 1 is discharging weapons')
                    damage= random.randint(enemy1_damagemin,enemy1_damagemax)
                    enemy_weapon1=enemy_weapon1-damage
                    print('enemy 1 did',damage,'damage')
                    if(position1=='back'):
                        if(shieldback>0):
                            shieldback=shieldback-damage
                            if(shieldback<0):
                                print('rear shields depleted')
                                hull=hull+shieldback
                                shieldback=0
                                print('hull damaged')
                        elif(shieldback==0):
                            hull=hull-damage
                            print('rear shields are down, hull damaged')
                            backdamage=1
                            if(hull<0):
                                hull=0
                                print('signal lost')
                    elif(position1=='mid'):
                        if(shieldmid>0):
                            shieldmid=shieldmid-damage
                            if(shieldmid<0):
                                print('mid shields depleted')
                                hull=hull+shieldmid
                                shieldmid=0
                                print('hull damaged')
                        elif(shieldmid==0):
                            hull=hull-damage
                            print('mid shields are down, hull damaged')
                            middamage=1
                            if(hull<0):
                                hull=0
                    elif(position1=='front'):
                        if(shieldfront>0):
                            shieldfront=shieldfront-damage
                            if(shieldfront<0):
                                print('front shields depleted')
                                hull=hull+shieldfront
                                shieldfront=0
                                print('hull damaged')
                        elif(shieldfront==0):
                            hull=hull-damage
                            print('front shields are down, hull damaged')
                            frontdamage=1
                            if(hull<0):
                                hull=0
                elif(enemy_weapon1<=0):
                    print('enemy 1 is charging weapons')
                    enemy_weapon1=500
            if(enemy_hull2>0)and(distance2<2500)and(distance2>-2500):
                if(enemy_weapon2>0)and(enemy_weapons2==True)and(hull>0):
                    print('enemy 2 is locking on')
                    time.sleep(1)
                    print('enemy 2 is discharging weapons')
                    damage= random.randint(enemy2_damagemin,enemy2_damagemax)
                    enemy_weapon2=enemy_weapon2-damage
                    print('enemy 2 did',damage,'damage')
                    if(position2=='back'):
                        if(shieldback>0):
                            shieldback=shieldback-damage
                            if(shieldback<0):
                                print('rear shields depleted')
                                hull=hull+shieldback
                                shieldback=0
                                print('hull damaged')
                        elif(shieldback==0):
                            hull=hull-damage
                            print('rear shields are down, hull damaged')
                            backdamage=1
                            if(hull<0):
                                hull=0
                                print('signal lost')
                    elif(position2=='mid'):
                        if(shieldmid>0):
                            shieldmid=shieldmid-damage
                            if(shieldmid<0):
                                print('mid shields depleted')
                                hull=hull+shieldmid
                                shieldmid=0
                                print('hull damaged')
                        elif(shieldmid==0):
                            hull=hull-damage
                            print('mid shields are down, hull damaged')
                            middamage=1
                            if(hull<0):
                                hull=0
                    elif(position2=='front'):
                        if(shieldfront>0):
                            shieldfront=shieldfront-damage
                            if(shieldfront<0):
                                print('front shields depleted')
                                hull=hull+shieldfront
                                shieldfront=0
                                print('hull damaged')
                        elif(shieldfront==0):
                            hull=hull-damage
                            print('front shields are down, hull damaged')
                            frontdamage=1
                            if(hull<0):
                                hull=0
                elif(enemy_weapon2<=0):
                    print('enemy 2 is charging weapons')
                    enemy_weapon2=500
            if(enemy_hull3>0)and(distance3<2500)and(distance3>-2500):
                if(enemy_weapon3>0)and(enemy_weapons3==True)and(hull>0):
                    print('enemy 3 is locking on')
                    time.sleep(1)
                    print('enemy 3 is discharging weapons')
                    damage= random.randint(enemy3_damagemin,enemy3_damagemax)
                    enemy_weapon3=enemy_weapon3-damage
                    print('enemy 3 did',damage,'damage')
                    if(position3=='back'):
                        if(shieldback>0):
                            shieldback=shieldback-damage
                            if(shieldback<0):
                                print('rear shields depleted')
                                hull=hull+shieldback
                                shieldback=0
                                print('hull damaged')
                        elif(shieldback==0):
                            hull=hull-damage
                            print('rear shields are down, hull damaged')
                            backdamage=1
                            if(hull<0):
                                hull=0
                                print('signal lost')
                    elif(position3=='mid'):
                        if(shieldmid>0):
                            shieldmid=shieldmid-damage
                            if(shieldmid<0):
                                print('mid shields depleted')
                                hull=hull+shieldmid
                                shieldmid=0
                                print('hull damaged')
                        elif(shieldmid==0):
                            hull=hull-damage
                            print('mid shields are down, hull damaged')
                            middamage=1
                            if(hull<0):
                                hull=0
                    elif(position3=='front'):
                        if(shieldfront>0):
                            shieldfront=shieldfront-damage
                            if(shieldfront<0):
                                print('front shields depleted')
                                hull=hull+shieldfront
                                shieldfront=0
                                print('hull damaged')
                        elif(shieldfront==0):
                            hull=hull-damage
                            print('front shields are down, hull damaged')
                            frontdamage=1
                            if(hull<0):
                                hull=0
                elif(enemy_weapon3<=0):
                    print('enemy 3 is charging weapons')
                    enemy_weapon3=500
            if(enemy_hull4>0)and(distance4<2500)and(distance4>-2500):
                if(enemy_weapon4>0)and(enemy_weapons4==True)and(hull>0):
                    print('enemy 4 is locking on')
                    time.sleep(1)
                    print('enemy 4 is discharging weapons')
                    damage= random.randint(enemy4_damagemin,enemy4_damagemax)
                    enemy_weapon4=enemy_weapon4-damage
                    print('enemy 4 did',damage,'damage')
                    if(position4=='back'):
                        if(shieldback>0):
                            shieldback=shieldback-damage
                            if(shieldback<0):
                                print('rear shields depleted')
                                hull=hull+shieldback
                                shieldback=0
                                print('hull damaged')
                        elif(shieldback==0):
                            hull=hull-damage
                            print('rear shields are down, hull damaged')
                            backdamage=1
                            if(hull<0):
                                hull=0
                                print('signal lost')
                    elif(position4=='mid'):
                        if(shieldmid>0):
                            shieldmid=shieldmid-damage
                            if(shieldmid<0):
                                print('mid shields depleted')
                                hull=hull+shieldmid
                                shieldmid=0
                                print('hull damaged')
                        elif(shieldmid==0):
                            hull=hull-damage
                            print('mid shields are down, hull damaged')
                            middamage=1
                            if(hull<0):
                                hull=0
                    elif(position4=='front'):
                        if(shieldfront>0):
                            shieldfront=shieldfront-damage
                            if(shieldfront<0):
                                print('front shields depleted')
                                hull=hull+shieldfront
                                shieldfront=0
                                print('hull damaged')
                        elif(shieldfront==0):
                            hull=hull-damage
                            print('front shields are down, hull damaged')
                            frontdamage=1
                            if(hull<0):
                                hull=0
                elif(enemy_weapon4<=0):
                    print('enemy 4 is charging weapons')
                    enemy_weapon4=500
            time.sleep(1)
            if(shieldfront==0)and(frontdamage==1):
                rand=random.randint(0,40)
                if(rand==1):
                    canon_battery1= False
                    print('cannon battery 1 offline')
                elif(rand==2):
                    canon_battery2= False
                    print('cannon battery 2 offline')
                elif(rand==3):
                    shield_front= False
                    print('shieldgenerator front offline')
            if(shieldmid==0)and(middamage==1):
                rand=random.randint(0,40)
                if(rand==0):
                    canon_battery3= False
                    print('cannon battery 3 offline')
                elif(rand==1):
                    canon_battery4= False
                    print('cannon battery 4 offline')
                elif(rand==2):
                    canon_battery5= False
                    print('cannon battery 5 offline')
                elif(rand==3):
                    mainweaponb= False
                    print('main weapon offline')
                elif(rand==4):
                    canon_battery6= False
                    print('cannon battery 6 offline')
                elif(rand==5):
                    shield_mid= False
                    print('shieldgenerator mid offline')
            if(shieldback==0)and(backdamage==1):
                rand=random.randint(0,40)
                if(rand==0):
                    canon_battery7= False
                    print('cannon battery 7 offline')
                elif(rand==1):
                    canon_battery8= False
                    print('cannon battery 8 offline')
                elif(rand==2):
                    canon_battery9= False
                    print('cannon battery 9 offline')
                elif(rand==3):
                    shieldback= False
                    print('shieldgenerator back offline')
        if(hull>0)and(go==1)and(ftl_cooldown<=0):
            time.sleep(1)
            print('10')
            time.sleep(1)
            print('9')
            time.sleep(1)
            print('8')
            time.sleep(1)
            print('7')
            time.sleep(1)
            print('6')
            time.sleep(1)
            print('5')
            time.sleep(1)
            print('4')
            time.sleep(1)
            print('3')
            time.sleep(1)
            print('2')
            time.sleep(1)
            print('1')
            time.sleep(2)
            jump=1
        if(hull>0)and(shieldfront>0)and(shieldmid>0)and(shieldback>0)and(go==1)and(jump==1)and(ftl_cooldown<=0):
            print('jump succesful')
            ftl_active=1
        elif(go==0)or(ftl_cooldown<=0)or(shieldfront>0)or(shieldmid>0)or(shieldback>0):
            print('failsafe override')
            print('jump canceld')
        else:
            print('signal lost')
            hull=0

    else:
        print('error: unkown command')
        options_active=1

    if(enemy_hull1>0)and(options_active!=1)and(ftl_active!=1):
            if(enemy_weapon1>0)and(enemy_weapons1==True)and(hull>0)and(distance1<2500)and(distance1>-2500):
                print('enemy 1 is locking on')
                time.sleep(1)
                print('enemy 1 is discharging weapons')
                damage= random.randint(enemy1_damagemin,enemy1_damagemax)
                enemy_weapon1=enemy_weapon1-damage
                print('enemy 1 did',damage,'damage')
                if(position1=='back'):
                    if(shieldback>0)and(shieldoverdrive==1)and(damage<power):
                        power=power-damage
                        print('shield overdrive active')
                        time.sleep(1)
                        print('shields are holding, power is dropping')
                    elif(shieldoverdrive==1)and(damage>power):
                        print('failsave override')
                        time.sleep(1)
                        print('shield overdrive shut down')
                        shieldoverdrive=0
                    if(shieldback>0)and(shieldoverdrive==0):
                        shieldback=shieldback-damage
                        if(shieldback<0):
                            print('rear shields depleted')
                            hull=hull+shieldback
                            shieldback=0
                            print('hull damaged')
                    elif(shieldback==0):
                        hull=hull-damage
                        print('rear shields are down, hull damaged')
                        backdamage=1
                        if(hull<0):
                            hull=0
                            print('signal lost')
                elif(position1=='mid'):
                    if(shieldmid>0)and(shieldoverdrive==1)and(damage<power):
                        power=power-damage
                        print('shield overdrive active')
                        time.sleep(1)
                        print('shields are holding, power is dropping')
                    elif(shieldoverdrive==1)and(damage>power):
                        print('failsave override')
                        time.sleep(1)
                        print('shield overdrive shut down')
                        shieldoverdrive=0
                    if(shieldmid>0)and(shieldoverdrive==0):
                        shieldmid=shieldmid-damage
                        if(shieldmid<0):
                            print('mid shields depleted')
                            hull=hull+shieldmid
                            shieldmid=0
                            print('hull damaged')
                    elif(shieldmid==0):
                        hull=hull-damage
                        print('mid shields are down, hull damaged')
                        middamage=1
                        if(hull<0):
                            hull=0
                elif(position1=='front'):
                    if(shieldfront>0)and(shieldoverdrive==1)and(damage<power):
                        power=power-damage
                        print('shield overdrive active')
                        time.sleep(1)
                        print('shields are holding, power is dropping')
                    elif(shieldoverdrive==1)and(damage>power):
                        print('failsave override')
                        time.sleep(1)
                        print('shield overdrive shut down')
                        shieldoverdrive=0
                    if(shieldfront>0)and(shieldoverdrive==0):
                        shieldfront=shieldfront-damage
                        if(shieldfront<0):
                            print('front shields depleted')
                            hull=hull+shieldfront
                            shieldfront=0
                            print('hull damaged')
                    elif(shieldfront==0):
                        hull=hull-damage
                        print('front shields are down, hull damaged')
                        frontdamage=1
                        if(hull<0):
                            hull=0
            elif(enemy_weapon1<=0):
                print('enemy 1 is charging weapons')
                enemy_weapon1=500
    if(enemy_hull2>0)and(options_active!=1):
            if(enemy_weapon2>0)and(enemy_weapons2==True)and(hull>0)and(distance2<2500)and(distance2>-2500):
                print('enemy 2 is locking on')
                time.sleep(1)
                print('enemy 2 is discharging weapons')
                damage= random.randint(enemy2_damagemin,enemy2_damagemax)
                enemy_weapon2=enemy_weapon2-damage
                print('enemy 2 did',damage,'damage')
                if(position2=='back'):
                    if(shieldback>0)and(shieldoverdrive==1)and(damage<power):
                        power=power-damage
                        print('shield overdrive active')
                        time.sleep(1)
                        print('shields are holding, power is dropping')
                    elif(shieldoverdrive==1)and(damage>power):
                        print('failsave override')
                        time.sleep(1)
                        print('shield overdrive shut down')
                        shieldoverdrive=0
                    if(shieldback>0)and(shieldoverdrive==0):
                        shieldback=shieldback-damage
                        if(shieldback<0):
                            print('rear shields depleted')
                            hull=hull+shieldback
                            shieldback=0
                            print('hull damaged')
                    elif(shieldback==0):
                        hull=hull-damage
                        print('rear shields are down, hull damaged')
                        backdamage=1
                        if(hull<0):
                            hull=0
                            print('signal lost')
                elif(position2=='mid'):
                    if(shieldmid>0)and(shieldoverdrive==1)and(damage<power):
                        power=power-damage
                        print('shield overdrive active')
                        time.sleep(1)
                        print('shields are holding, power is dropping')
                    elif(shieldoverdrive==1)and(damage>power):
                        print('failsave override')
                        time.sleep(1)
                        print('shield overdrive shut down')
                        shieldoverdrive=0
                    if(shieldmid>0)and(shieldoverdrive==0):
                        shieldmid=shieldmid-damage
                        if(shieldmid<0):
                            print('mid shields depleted')
                            hull=hull+shieldmid
                            shieldmid=0
                            print('hull damaged')
                    elif(shieldmid==0):
                        hull=hull-damage
                        print('mid shields are down, hull damaged')
                        middamage=1
                        if(hull<0):
                            hull=0
                elif(position2=='front'):
                    if(shieldfront>0)and(shieldoverdrive==1)and(damage<power):
                        power=power-damage
                        print('shield overdrive active')
                        time.sleep(1)
                        print('shields are holding, power is dropping')
                    elif(shieldoverdrive==1)and(damage>power):
                        print('failsave override')
                        time.sleep(1)
                        print('shield overdrive shut down')
                        shieldoverdrive=0
                    if(shieldfront>0)and(shieldoverdrive==0):
                        shieldfront=shieldfront-damage
                        if(shieldfront<0):
                            print('front shields depleted')
                            hull=hull+shieldfront
                            shieldfront=0
                            print('hull damaged')
                    elif(shieldfront==0):
                        hull=hull-damage
                        print('front shields are down, hull damaged')
                        frontdamage=1
                        if(hull<0):
                            hull=0
            elif(enemy_weapon2<=0):
                print('enemy 2 is charging weapons')
                enemy_weapon2=500
    if(enemy_hull3>0)and(options_active!=1):
            if(enemy_weapon3>0)and(enemy_weapons3==True)and(hull>0)and(distance3<2500)and(distance3>-2500):
                print('enemy 3 is locking on')
                time.sleep(1)
                print('enemy 3 is discharging weapons')
                damage= random.randint(enemy3_damagemin,enemy3_damagemax)
                enemy_weapon3=enemy_weapon3-damage
                print('enemy 3 did',damage,'damage')
                if(position3=='back'):
                    if(shieldback>0)and(shieldoverdrive==1)and(damage<power):
                        power=power-damage
                        print('shield overdrive active')
                        time.sleep(1)
                        print('shields are holding, power is dropping')
                    elif(shieldoverdrive==1)and(damage>power):
                        print('failsave override')
                        time.sleep(1)
                        print('shield overdrive shut down')
                        shieldoverdrive=0
                    if(shieldback>0)and(shieldoverdrive==0):
                        shieldback=shieldback-damage
                        if(shieldback<0):
                            print('rear shields depleted')
                            hull=hull+shieldback
                            shieldback=0
                            print('hull damaged')
                    elif(shieldback==0):
                        hull=hull-damage
                        print('rear shields are down, hull damaged')
                        backdamage=1
                        if(hull<0):
                            hull=0
                            print('signal lost')
                elif(position3=='mid'):
                    if(shieldmid>0)and(shieldoverdrive==1)and(damage<power):
                        power=power-damage
                        print('shield overdrive active')
                        time.sleep(1)
                        print('shields are holding, power is dropping')
                    elif(shieldoverdrive==1)and(damage>power):
                        print('failsave override')
                        time.sleep(1)
                        print('shield overdrive shut down')
                        shieldoverdrive=0
                    if(shieldmid>0)and(shieldoverdrive==0):
                        shieldmid=shieldmid-damage
                        if(shieldmid<0):
                            print('mid shields depleted')
                            hull=hull+shieldmid
                            shieldmid=0
                            print('hull damaged')
                    elif(shieldmid==0):
                        hull=hull-damage
                        print('mid shields are down, hull damaged')
                        middamage=1
                        if(hull<0):
                            hull=0
                elif(position3=='front'):
                    if(shieldfront>0)and(shieldoverdrive==1)and(damage<power):
                        power=power-damage
                        print('shield overdrive active')
                        time.sleep(1)
                        print('shields are holding, power is dropping')
                    elif(shieldoverdrive==1)and(damage>power):
                        print('failsave override')
                        time.sleep(1)
                        print('shield overdrive shut down')
                        shieldoverdrive=0
                    if(shieldfront>0)and(shieldoverdrive==0):
                        shieldfront=shieldfront-damage
                        if(shieldfront<0):
                            print('front shields depleted')
                            hull=hull+shieldfront
                            shieldfront=0
                            print('hull damaged')
                    elif(shieldfront==0):
                        hull=hull-damage
                        print('front shields are down, hull damaged')
                        frontdamage=1
                        if(hull<0):
                            hull=0
            elif(enemy_weapon3<=0):
                print('enemy 3 is charging weapons')
                enemy_weapon3=500
    if(enemy_hull4>0):
            if(enemy_weapon4>0)and(enemy_weapons4==True)and(hull>0)and(distance4<2500)and(distance4>-2500):
                print('enemy 4 is locking on')
                time.sleep(1)
                print('enemy 4 is discharging weapons')
                damage= random.randint(enemy4_damagemin,enemy4_damagemax)
                enemy_weapon4=enemy_weapon4-damage
                print('enemy 4 did',damage,'damage')
                if(position4=='back'):
                    if(shieldmid>0)and(shieldoverdrive==1)and(damage<power):
                        power=power-damage
                        print('shield overdrive active')
                        time.sleep(1)
                        print('shields are holding, power is dropping')
                    elif(shieldoverdrive==1)and(damage>power):
                        print('failsave override')
                        time.sleep(1)
                        print('shield overdrive shut down')
                        shieldoverdrive=0
                    if(shieldback>0)and(shieldoverdrive==0):
                        shieldback=shieldback-damage
                        if(shieldback<0):
                            print('rear shields depleted')
                            hull=hull+shieldback
                            shieldback=0
                            print('hull damaged')
                    elif(shieldback==0):
                        hull=hull-damage
                        print('rear shields are down, hull damaged')
                        backdamage=1
                        if(hull<0):
                            hull=0
                            print('signal lost')
                elif(position4=='mid'):
                    if(shieldmid>0)and(shieldoverdrive==1)and(damage<power):
                        power=power-damage
                        print('shield overdrive active')
                        time.sleep(1)
                        print('shields are holding, power is dropping')
                    elif(shieldoverdrive==1)and(damage>power):
                        print('failsave override')
                        time.sleep(1)
                        print('shield overdrive shut down')
                        shieldoverdrive=0
                    if(shieldmid>0)and(shieldoverdrive==0):
                        shieldmid=shieldmid-damage
                        if(shieldmid<0):
                            print('mid shields depleted')
                            hull=hull+shieldmid
                            shieldmid=0
                            print('hull damaged')
                    elif(shieldmid==0):
                        hull=hull-damage
                        print('mid shields are down, hull damaged')
                        middamage=1
                        if(hull<0):
                            hull=0
                elif(position4=='front'):
                    if(shieldfront>0)and(shieldoverdrive==1)and(damage<power):
                        power=power-damage
                        print('shield overdrive active')
                        time.sleep(1)
                        print('shields are holding, power is dropping')
                    elif(shieldoverdrive==1)and(damage>power):
                        print('failsave override')
                        time.sleep(1)
                        print('shield overdrive shut down')
                        shieldoverdrive=0
                    if(shieldfront>0)and(shieldoverdrive==0):
                        shieldfront=shieldfront-damage
                        if(shieldfront<0):
                            print('front shields depleted')
                            hull=hull+shieldfront
                            shieldfront=0
                            print('hull damaged')
                    elif(shieldfront==0):
                        hull=hull-damage
                        print('front shields are down, hull damaged')
                        frontdamage=1
                        if(hull<0):
                            hull=0
            elif(enemy_weapon4<=0):
                print('enemy 4 is charging weapons')
                enemy_weapon4=500
    time.sleep(1)
    if(shieldfront==0)and(frontdamage==1):
        rand=random.randint(0,30)
        if(rand==1)and(canon_battery1==True):
            canon_battery1= False
            print('cannon battery 1 offline')
        elif(rand==2)and(canon_battery2==True):
            canon_battery2= False
            print('cannon battery 2 offline')
        elif(rand==3)and(shield_front):
            shield_front= False
            print('shieldgenerator front offline')
    if(shieldmid==0)and(middamage==1):
        rand=random.randint(0,30)
        if(rand==8)and(canon_battery3==True):
            canon_battery3= False
            print('cannon battery 3 offline')
        elif(rand==1)and(canon_battery4==True):
            canon_battery4= False
            print('cannon battery 4 offline')
        elif(rand==2)and(canon_battery5==True):
            canon_battery5= False
            print('cannon battery 5 offline')
        elif(rand==3)and(mainweaponb==True):
            mainweaponb= False
            print('main weapon offline')
        elif(rand==4)and(canon_battery6==True):
            canon_battery6= False
            print('cannon battery 6 offline')
        elif(rand==5)and(shield_mid==True):
            shield_mid= False
            print('shieldgenerator mid offline')
    if(shieldback==0)and(backdamage==1):
        rand=random.randint(0,30)
        if(rand==8)and(canon_battery7==True):
            canon_battery7= False
            print('cannon battery 7 offline')
        elif(rand==1)and(canon_battery8==True):
            canon_battery8= False
            print('cannon battery 8 offline')
        elif(rand==2)and(canon_battery9==True):
            canon_battery9= False
            print('cannon battery 9 offline')
        elif(rand==3)and(shield_back==True):
            shield_back= False
            print('shieldgenerator back offline')
        elif(rand==4)and(engine==True):
            engine= False
            print('engines offline')

input('press enter to exit')
