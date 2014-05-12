#this part is only for the interface to work independently
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
enemy_weapons1=0
#enemy 2
enemy_shields2=40
enemy_hull2=1000
enemy_weapons2=0
#enemy 3
enemy_shields3=40
enemy_hull3=1000
enemy_weapons3=0

ftl_active=0
options=['jump to ftl','fire weapons','start repairing','transfer power','status report',
'plot course','scan area']
while(enemy_numbers>0)and(hull>0)and(ftl_active==0):
    action=input('input:')#prompt for action

    if action=='options':
        print(options)

    if action=='status report':#prints the status of all systems
        print('status report:')
        print('shields are at')
        print('    front:',shieldfront,'power')
        print('    mid:  ',shieldmid,'power')
        print('    back: ',shieldback,'power')
        shield_total=shieldfront+shieldmid+shieldback
        print('total shield:',shield_total)
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
        time.sleep(1)
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
        if(enemy_hull1>0):
            print('    ',enemy_hull1)
        if(enemy_hull2>0):
            print('    ',enemy_hull2)
        if(enemy_hull3>0):
            print('    ',enemy_hull3)
        print('density')

    

    
