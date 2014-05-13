power=1000
canon_batterys1=200
canon_battery1= True
canon_batterys2=200
canon_battery2= True
canon_batterys3=200
canon_battery3= True
canon_batterys4=10 #normal is 200
canon_battery4= True
canon_batterys5=0
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
shieldfront=300 #shields max is 600
shieldmid=350
shieldback=200
mainweapona=400 #full power is 800
mainweaponb= True
question_answerd=0
ftl_overload=0
import time
import random
enemy_numbers=3

#battle interface
enemy_numbers=3
positions=['front','mid','back']

#enemy 1
enemy_shields1=40
enemy_hull1=1000
enemy_weapon1=0
enemy_weapons1= True
position1=random.choice(positions)
#enemy 2
enemy_shields2=40
enemy_hull2=1000
enemy_weapon2=0
enemy_weapons2= True
position2=random.choice(positions)
#enemy 3
enemy_shields3=40
enemy_hull3=1000
enemy_weapon3=0
enemy_weapons3= True
position3=random.choice(positions)

ftl_active=0
shield_total=shieldfront+shieldmid+shieldback
options=['jump to ftl','fire weapons','start repairing','transfer power','status report',
'plot course','scan area','quit']
while(enemy_numbers>0)and(hull>0)and(ftl_active==0):
    if(hull<100):
        print('warning! hull is critically low')
    if(shieldfront==0):
        print('warning! front shield is down')
    if(shieldmid==0):
        print('warning! mid shield is down')
    if(shieldback==0):
        print('warning! rear shield is down')
    action=input('input:')#prompt for action

    if action=='options':
        print(options)

    if action=='status report':#prints the status of all systems
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

    if action=='jump to ftl':
        print('calculating path to nearest star')
        time.sleep(2)
        if(enemy_hull1>0):
            if(enemy_weapon1>0)and(enemy_weapons1==True)and(hull>0):
                print('enemy 1 is locking on')
                time.sleep(1)
                print('enemy 1 is discharging weapons')
                damage=random.randint(10,100)
                enemy_weapon1=enemy_weapon1-10
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
                        if(hull<0):
                            hull=0
                            print('signal lost')
                elif(position1=='mid'):
                    if(shieldback>0):
                        shieldmid=shieldmid-damage
                        if(shieldmid<0):
                            print('mid shields depleted')
                            hull=hull+shieldmid
                            shieldmid=0
                            print('hull damaged')
                    elif(shieldmid==0):
                        hull=hull-damage
                        print('mid shields are down, hull damaged')
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
                        if(hull<0):
                            hull=0
            if(enemy_weapon1<=0):
                print('enemy 1 is charging weapons')
                enemy_weapon1=500
        if(enemy_hull2>0):
            if(enemy_weapon2>0)and(enemy_weapons2==True)and(hull>0):
                print('enemy 2 is locking on')
                time.sleep(1)
                print('enemy 2 is discharging weapons')
                damage=random.randint(10,100)
                enemy_weapon1=enemy_weapon2-10
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
                        if(hull<0):
                            hull=0
                            print('signal lost')
                elif(position2=='mid'):
                    if(shieldback>0):
                        shieldmid=shieldmid-damage
                        if(shieldmid<0):
                            print('mid shields depleted')
                            hull=hull+shieldmid
                            shieldmid=0
                            print('hull damaged')
                    elif(shieldmid==0):
                        hull=hull-damage
                        print('mid shields are down, hull damaged')
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
                damage=random.randint(10,100)
                enemy_weapon3=enemy_weapon3-10
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
                        if(hull<0):
                            hull=0
                            print('signal lost')
                elif(position3=='mid'):
                    if(shieldback>0):
                        shieldmid=shieldmid-damage
                        if(shieldmid<0):
                            print('mid shields depleted')
                            hull=hull+shieldmid
                            shieldmid=0
                            print('hull damaged')
                    elif(shieldmid==0):
                        hull=hull-damage
                        print('mid shields are down, hull damaged')
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
                        if(hull<0):
                            hull=0
            if(enemy_weapon3<=0):
                print('enemy 3 is charging weapons')
                enemy_weapon3=500
        if(hull>0)and(shieldback>0)and(shieldmid>0)and(shieldfront>0):
            print('path calculated, prepairing for jump')
            print('jump in 20 seconds')
            time.sleep(7)
            if(enemy_hull1>0):
                if(enemy_weapon1>0)and(enemy_weapons1==True)and(hull>0):
                    print('enemy 1 is locking on')
                    time.sleep(1)
                    print('enemy 1 is discharging weapons')
                    damage=random.randint(10,100)
                    enemy_weapon1=enemy_weapon1-10
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
                            if(hull<0):
                                hull=0
                                print('signal lost')
                    elif(position1=='mid'):
                        if(shieldback>0):
                            shieldmid=shieldmid-damage
                            if(shieldmid<0):
                                print('mid shields depleted')
                                hull=hull+shieldmid
                                shieldmid=0
                                print('hull damaged')
                        elif(shieldmid==0):
                            hull=hull-damage
                            print('mid shields are down, hull damaged')
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
                            if(hull<0):
                                hull=0
                if(enemy_weapon1<=0):
                    print('enemy 1 is charging weapons')
                    enemy_weapon1=500
            if(enemy_hull2>0):
                if(enemy_weapon2>0)and(enemy_weapons2==True)and(hull>0):
                    print('enemy 2 is locking on')
                    time.sleep(1)
                    print('enemy 2 is discharging weapons')
                    damage=random.randint(10,100)
                    enemy_weapon1=enemy_weapon2-10
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
                            if(hull<0):
                                hull=0
                                print('signal lost')
                    elif(position2=='mid'):
                        if(shieldback>0):
                            shieldmid=shieldmid-damage
                            if(shieldmid<0):
                                print('mid shields depleted')
                                hull=hull+shieldmid
                                shieldmid=0
                                print('hull damaged')
                        elif(shieldmid==0):
                            hull=hull-damage
                            print('mid shields are down, hull damaged')
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
                    damage=random.randint(10,100)
                    enemy_weapon3=enemy_weapon3-10
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
                            if(hull<0):
                                hull=0
                                print('signal lost')
                    elif(position3=='mid'):
                        if(shieldback>0):
                            shieldmid=shieldmid-damage
                            if(shieldmid<0):
                                print('mid shields depleted')
                                hull=hull+shieldmid
                                shieldmid=0
                                print('hull damaged')
                        elif(shieldmid==0):
                            hull=hull-damage
                            print('mid shields are down, hull damaged')
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
                            if(hull<0):
                                hull=0
                if(enemy_weapon3<=0):
                    print('enemy 3 is charging weapons')
                    enemy_weapon3=500
        if(hull>0):
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
        if(hull>0)and(shieldfront>0)and(shieldmid>0)and(shieldback>0):
            print('jump succelsful')
            ftl_active=1
        else:
            print('signal lost')

input('pres enter to exit') 
