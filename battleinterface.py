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

#enemy 1
enemy_shields1=40
enemy_hull1=1000
enemy_weapon1=0
enemy_weapons1= True
#enemy 2
enemy_shields2=40
enemy_hull2=1000
enemy_weapon2=0
enemy_weapons2= True
#enemy 3
enemy_shields3=40
enemy_hull3=1000
enemy_weapon3=0
enemy_weapons3= True

ftl_active=0
shield_total=shieldfront+shieldmid+shieldback
options=['jump to ftl','fire weapons','start repairing','transfer power','status report',
'plot course','scan area','quit']
while(enemy_numbers>0)and(hull>0)and(ftl_active==0):
    action=input('input:')#prompt for action

    if action=='options':
        print(options)

    if action=='status report':#prints the status of all systems
        print('status report:')
        print('shields are at')
        time.sleep(1)
        shieldfront=shield_total/3
        shieldmid=shield_total/3
        shieldback=shield_total/3
        print('    front:',shieldfront,'power')
        print('    mid:  ',shieldmid,'power')
        print('    back: ',shieldback,'power')
        shield_total=shieldfront+shieldmid+shieldback
        print('total shield:',shield_total)
        time.sleep(3)
        print('weapons are at')
        print('    1:',canon_batterys1)
        print('    1:',canon_battery1)
        print('    2:',canon_batterys2)
        print('    2:',canon_battery2)
        print('    3:',canon_batterys3)
        print('    3:',canon_battery3)
        print('    4:',canon_batterys4)
        print('    4:',canon_battery4)
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
        print('main weapon:',mainweapona,'status:',mainweaponb)
        print('hull is at',hull,'density')
        print("enemy's in this area:")
        time.sleep(3)
        print('    ',enemy_numbers)
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
            if(enemy_weapon1>0)and(enemy_weapons1==True):
                print('enemy 1 is locking on to us')
                time.sleep(1)
                print('enemy 1 is discharging weapons')
                damage=random.randint(10,100)
                enemy_weapon1=enemy_weapon1-10
                print('enemy 1 did',damage,'damage')
                if(shield_total>0):
                    shield_total=shield_total-damage
                    if(shield_total<0):
                        print('shields depleted')
                        hull=hull+shield_total
                        shield_total=0
                elif(shield_total==0):
                    hull=hull-damage
                    if(hull<0):
                        hull=0
            if(enemy_weapon1<=0):
                print('enemy 1 is charging weapons')
                enemy_weapon1=500
        if(enemy_hull2>0):
            if(enemy_weapon2>0)and(enemy_weapons2==True):
                print('enemy 2 is locking on to us')
                time.sleep(1)
                print('enemy 2 is discharging weapons')
                damage=random.randint(10,100)
                enemy_weapon1=enemy_weapon2-10
                print('enemy 2 did',damage,'damage')
                if(shield_total>0):
                    shield_total=shield_total-damage
                    if(shield_total<0):
                        print('shields depleted')
                        hull=hull+shield_total
                        shield_total=0
                        print('hull damaged')
                elif(shield_total==0):
                    hull=hull-damage
                    print('shields are down, hull damaged')
                    if(hull<0):
                        hull=0                
            elif(enemy_weapon2<=0):
                print('enemy 2 is charging weapons')
                enemy_weapon2=500
        if(enemy_hull3>0):
            if(enemy_weapon3>0)and(enemy_weapons3==True):
                print('enemy 3 is locking on to us')
                time.sleep(1)
                print('enemy 3 is discharging weapons')
                damage=random.randint(10,100)
                enemy_weapon3=enemy_weapon3-10
                print('enemy 3 did',damage,'damage')
                if(shield_total>0):
                    shield_total=shield_total-damage
                    if(shield_total<0):
                        print('shields depleted')
                        hull=hull+shield_total
                        shield_total=0
                elif(shield_total==0):
                    hull=hull-damage
                    print('shields are down, hull damaged')
                    if(hull<0):
                        hull=0
            if(enemy_weapon3<=0):
                print('enemy 3 is charging weapons')
                enemy_weapon3=500

input('pres enter to exit')  

