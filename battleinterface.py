
power=10000
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

#star system info
planets=3
planet_class=['gass giant','iron based','gass giant']
starsystems=['Delta-37g2','Gamma-492b2']

#battle interface
enemy_numbers=3
positions=['front','mid','back']
target=0
go=1
classes=['scout','scout','scout','battleship','battleship','transport','commandship']


#enemy 1
position1=random.choice(positions)
class1=random.choice(classes)
if(class1=='scout'):
    enemy_shields1=450
    enemy_hull1=500
    enemy_weapon1=0
    enemy_weapons1= True
    enemy1_damagemin=5
    enemy1_damagemax=50
elif(class1=='battleship'):
    enemy_shields1=900
    enemy_hull1=1000
    enemy_weapon1=0
    enemy_weapons1= True
    enemy1_damagemin=10
    enemy1_damagemax=100
elif(class1=='transport'):
    enemy_shields1=1000
    enemy_hull1=1500
    enemy_weapon1=0
    enemy_weapons1= True
    enemy1_damagemin=5
    enemy1_damagemax=40
elif(class1=='commandship'):
    enemy_shields1=1500
    enemy_hull1=2000
    enemy_weapon1=40
    enemy_weapons1= True
    enemy1_damagemin=20
    enemy1_damagemax=200
#enemy 2
position2=random.choice(positions)
class2=random.choice(classes)
if(class2=='scout'):
    enemy_shields2=450
    enemy_hull2=500
    enemy_weapon2=0
    enemy_weapons2= True
    enemy2_damagemin=5
    enemy2_damagemax=50
elif(class2=='battleship'):
    enemy_shields2=900
    enemy_hull2=1000
    enemy_weapon2=0
    enemy_weapons2= True
    enemy2_damagemin=10
    enemy2_damagemax=100
elif(class2=='transport'):
    enemy_shields2=1000
    enemy_hull2=1500
    enemy_weapon2=0
    enemy_weapons2= True
    enemy2_damagemin=5
    enemy2_damagemax=40
elif(class2=='commandship'):
    enemy_shields2=1500
    enemy_hull2=2000
    enemy_weapon2=40
    enemy_weapons2= True
    enemy2_damagemin=20
    enemy2_damagemax=200
#enemy 3
position3=random.choice(positions)
class3=random.choice(classes)
if(class3=='scout'):
    enemy_shields3=450
    enemy_hull3=500
    enemy_weapon3=0
    enemy_weapons3= True
    enemy3_damagemin=5
    enemy3_damagemax=50
elif(class3=='battleship'):
    enemy_shields3=900
    enemy_hull3=1000
    enemy_weapon3=0
    enemy_weapons3= True
    enemy3_damagemin=10
    enemy3_damagemax=100
elif(class3=='transport'):
    enemy_shields3=1000
    enemy_hull3=1500
    enemy_weapon3=0
    enemy_weapons3= True
    enemy3_damagemin=5
    enemy3_damagemax=40
elif(class3=='commandship'):
    enemy_shields3=1500
    enemy_hull3=2000
    enemy_weapon3=40
    enemy_weapons3= True
    enemy3_damagemin=20
    enemy3_damagemax=200
#enemy 4
position4=random.choice(positions)
class4=random.choice(classes)
enemy_shields4=0
enemy_hull4=0
enemy_weapons4=0
enemy_weapons4= True

ftl_active=0
repair=0
shield_total=shieldfront+shieldmid+shieldback
course_plot=0
rand=0
scan=0
options=['jump to ftl','fire weapons','start repairing','transfer power','status report',
'plot course','scan area','quit']
while(enemy_numbers>0)and(hull>0)and(ftl_active==0):
    repaired= random.randint(0,90)
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
    enemy_numbers=number1+number2+number3
    if(repaired==1)and(repair==1)and(canon_batterys1==False):
        canon_battery1= True
        print('cannon 1 repaired')
    if(repaired==2)and(repair==1)and(canon_batterys2==False):
        canon_battery2= True
        print('cannon 2 repaired')
    if(repaired==3)and(repair==1)and(canon_batterys3==False):
        canon_battery3= True
        print('cannon 3 repaired')
    if(repaired==4)and(repair==1)and(canon_batterys4==False):
        canon_battery4= True
        print('cannon 4 repaired')
    if(repaired==5)and(repair==1)and(canon_batterys5==False):
        canon_battery5= True
        print('cannon 5 repaired')
    if(repaired==6)and(repair==1)and(canon_batterys6==False):
        canon_battery6= True
        print('cannon 6 repaired')
    if(repaired==7)and(repair==1)and(canon_batterys7==False):
        canon_battery7= True
        print('cannon 7 repaired')
    if(repaired==8)and(repair==1)and(canon_batterys8==False):
        canon_battery8= True
        print('cannon 8 repaired')
    if(repaired==9)and(repair==1)and(canon_batterys9==False):
        canon_battery9= True
        print('cannon 9 repaired')
    if(repaired==10)and(repair==1)and(mainweaponb==False):
        mainweaponb= True
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
    time.sleep(1)
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
    action=input('input:')#prompt for action

    if(action=='scan area'):
        print('scanning area')
        time.sleep(2)
        print("enemy's in this area:")
        time.sleep(3)
        print('    ',enemy_numbers)
        print('enemy postions:')
        time.sleep(3)
        print('    ',position1)
        print('    ',position2)
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
        if(enemy_hull1>0):
            print('    ',enemy_hull1)
        if(enemy_hull2>0):
            print('    ',enemy_hull2)
        if(enemy_hull3>0):
            print('    ',enemy_hull3)
        print('density')
        time.sleep(1)
        print('enemy classes are:')
        if(enemyhull1>0):
            print('    ',class1)
        if(enemyhull2>0):
            print('    ',class2)
        if(enemyhull3>0):
            print('    ',class3)
        print('planets in this system:')
        time.sleep(2)
        print(planets)
        time.sleep(1)
        print('class:')
        time.sleep(2)
        print(planet_class)
        time.sleep(1)
        scan=1
        print('systems nearby:')
        time.sleep(2)
        print(starsystems)
        time.sleep(3)
        if(enemy_hull1>0):
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
        if(enemy_hull2>0):
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
        if(enemy_hull3>0):
            if(enemy_weapon3>0)and(enemy_weapons3==True)and(hull>0):
                print('enemy 3 is locking on')
                time.sleep(1)
                print('enemy 3 is discharging weapons')
                damage= random.randint(enemy3_damagemin,enemy3_damagemzx)
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
        if(enemy_hull4>0):
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
        if(enemy_hull1>0):
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
        if(enemy_hull2>0):
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
        if(enemy_hull3>0):
            if(enemy_weapon3>0)and(enemy_weapons3==True)and(hull>0):
                print('enemy 3 is locking on')
                time.sleep(1)
                print('enemy 3 is discharging weapons')
                damage= random.randint(enemy3_damagemin,enemy3_damagemzx)
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
        if(enemy_hull4>0):
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
        alter=input('alter:')
        if(alter=='options'):
            print('weapons or shields')
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
                print('cannot maintain more than 500 power in normal weapons and can not maintain more than 800 power in main weapon')
            elif(newcanon_batterys1<0)or(canon_batterys2<0)or(newcanon_batterys3<0)or(newcanon_batterys4<0)or(newcanon_batterys5<0)or(newcanon_batterys6<0)or(newcanon_batterys7<0)or(newcanon_batterys8<0)or(newcanon_batterys9<0)or(newmainweapona<0):
                print('error, power can not be lower than 0')
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
                print('error shields can not contain more than 900 power')
            elif(newshieldmid<0)or(newshieldfront<0)or(newshieldback<0):
                print('error shields can not contain less than 0 power')
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
        if(enemy_hull1>0):
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
        if(enemy_hull2>0):
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
        if(enemy_hull3>0):
            if(enemy_weapon3>0)and(enemy_weapons3==True)and(hull>0):
                print('enemy 3 is locking on')
                time.sleep(1)
                print('enemy 3 is discharging weapons')
                damage= random.randint(enemy3_damagemin,enemy3_damagemzx)
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
        if(enemy_hull4>0):
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


    elif action=='start repairing':
        time.sleep(1)
        print('started repairs')
        repair=1
        if(enemy_hull1>0):
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
        if(enemy_hull2>0):
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
        if(enemy_hull3>0):
            if(enemy_weapon3>0)and(enemy_weapons3==True)and(hull>0):
                print('enemy 3 is locking on')
                time.sleep(1)
                print('enemy 3 is discharging weapons')
                damage= random.randint(enemy3_damagemin,enemy3_damagemzx)
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
        if(enemy_hull4>0):
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


    elif action=='fire weapons':
        while(target!='1')and(target!='2')and(target!='3'):
            target=input('target:')
            if(target=='1')and(enemy_hull1<=0):
                print('cannot find target')
                target=0
            if(target=='2')and(enemy_hull2<=0):
                print('cannot find target')
                target=0
            if(target=='3')and(enemy_hull3<=0):
                print('cannot find target')
                target=0
        time.sleep(1)
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
        if(target=='1'):
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
        if(target=='2'):
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
        if(target=='3'):
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
        if(enemy_hull1>0):
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
        if(enemy_hull2>0):
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
        if(enemy_hull3>0):
            if(enemy_weapon3>0)and(enemy_weapons3==True)and(hull>0):
                print('enemy 3 is locking on')
                time.sleep(1)
                print('enemy 3 is discharging weapons')
                damage= random.randint(enemy3_damagemin,enemy3_damagemzx)
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
        if(enemy_hull4>0):
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

        
                
    elif action=='options'or action=='?' or action=='help':
        print(options)              

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
        print("enemy's in this area:")
        time.sleep(3)
        print('    ',enemy_numbers)
        print('enemy postions:')
        time.sleep(3)
        if(hull1>0):
            print('    ',position1)
        if(hull2>0):
            print('    ',position2)
        if(hull3>0):
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
        if(enemy_hull1>0):
            print('    ',enemy_hull1)
        if(enemy_hull2>0):
            print('    ',enemy_hull2)
        if(enemy_hull3>0):
            print('    ',enemy_hull3)
        print('density')
        if(scan==1):
            print('enemy classes are:')
            if(enemyhull1>0):
                print('    ',class1)
            if(enemyhull2>0):
                print('    ',class2)
            if(enemyhull3>0):
                print('    ',class3)

    elif action=='jump to ftl':
        if(course_plot<1):
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
            if(enemy_hull1>0):
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
            if(enemy_hull2>0):
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
            if(enemy_hull3>0):
                if(enemy_weapon3>0)and(enemy_weapons3==True)and(hull>0):
                    print('enemy 3 is locking on')
                    time.sleep(1)
                    print('enemy 3 is discharging weapons')
                    damage= random.randint(enemy3_damagemin,enemy3_damagemzx)
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
            if(enemy_hull4>0):
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
            if(hull>0)and(go==1):
                if(course_plot<1):
                    print('path calculated, prepairing for jump')
            print('jump in 20 seconds')
            time.sleep(7)
            if(enemy_hull1>0):
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
            if(enemy_hull2>0):
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
            if(enemy_hull3>0):
                if(enemy_weapon3>0)and(enemy_weapons3==True)and(hull>0):
                    print('enemy 3 is locking on')
                    time.sleep(1)
                    print('enemy 3 is discharging weapons')
                    damage= random.randint(enemy3_damagemin,enemy3_damagemzx)
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
            if(enemy_hull4>0):
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
        if(hull>0)and(go==1):
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
        if(hull>0)and(shieldfront>0)and(shieldmid>0)and(shieldback>0)and(go==1)and(jump==1):
            print('jump succesful')
            ftl_active=1
        elif(go==0):
            print('jump canceld')
        else:
            print('signal lost')
            hull=0

    else:
        print('error: unkown command')
        if(enemy_hull1>0):
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
        if(enemy_hull2>0):
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
        if(enemy_hull3>0):
            if(enemy_weapon3>0)and(enemy_weapons3==True)and(hull>0):
                print('enemy 3 is locking on')
                time.sleep(1)
                print('enemy 3 is discharging weapons')
                damage= random.randint(enemy3_damagemin,enemy3_damagemzx)
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
        if(enemy_hull4>0):
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


input('pres enter to exit')  
