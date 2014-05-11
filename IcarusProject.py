Icarus project

#Icarus project

#beginning conditions
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
question_answer=0
ftl_overload=0
options=['start engines','full power to the shields','jump to ftl']
import time
import random

#mission 1 earth
print('you can use options at all time to display your options')
print('mission 1 earth')
print('you are part of a secret milatary program, project icarus')
print('the project made a spaceship that is capable of ftl')
print('(ftl=faster than light)')
print('you are the captain and the ship wil be launched today, you will control it through this control pannel.')
print('the ship is completely drone opperated')
print('it is controlled through a series of entagled particels')
print('http://en.wikipedia.org/wiki/Quantum_entanglement')
print('all systems online')
while(question_answer<1):
    action=input('what will you do? ')
    if(action=='options'):
        print(options)

    if(action=='start engines'):
        print('engines started, commencing launch in T minus 10 seconds')
        options.pop(0)
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
        print('liftoff')
        print(options)
        question_answer=1

    if(action=='full power to the shields'):
        print('there is no need')

    if action=='jump to ftl':
        print('we will jump to ftl in 60 seconds')
        time.sleep(50)
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
        print('we just jumped to ftl')
        print('error')
        print('system overload')
        print('ship damaged')
        print('weapons 5 to 9 offline')
        ftl_overload=1
        question_answer=1

while(ftl_overload<1):
    action=input('input:')
    if(action=='full power to the shields'):
        print('there is no need')

    if action=='jump to ftl':
        print('we will jump to ftl in 60 seconds')
        time.sleep(50)
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
        print('we just jumped to ftl')
        print('error')
        print('system overload')
        print('ship damaged')
        print('weapons 5 to 9 offline')
        ftl_overload=1

question_answerd=0
options=['scan area','repair damaged parts','full power to the shields','functionality report']
while(question_answer==0):
    action=input('input:')

    if action=='scan area':
        print('area scanned')
        print('computer reports:')
        print('we are in the middle of empty space')
        print('locating near stars and calculating distance to earth')
        time.sleep(5)
        print('estimated distance to earth:')
        time.sleep(2)
        print('unkown')

    if action=='repair damaged parts':
        print('started to repair damaged parts')
        damage_repair= True

    if action=='full power to the shields':
        print('transferring power to the shields')
        energy_transferd=0
        while(shieldfront<600)and(canon_batterys1>0):
            canon_batterys1=canon_batterys1-1
            shieldfront=shieldfront+1
            energy_transferd=energy_transferd+1
        print(energy_transferd,' energy transferred from cannon batteries 1 to the front shield')
        energy_transferd=0
        while(shieldfront<600)and(canon_batterys2>0):
            canon_batterys2=canon_batterys2-1
            shieldfront=shieldfront+1
            energy_transferd=energy_transferd+1
        print(energy_transferd,' energy transferred from cannon batteries 2 to the front shield')
        time.sleep(4)
        print('shields are fully powerd and opperational')
        print('weapons offline')

    if action=='functionality report':
        print('weapons 5 to 9 offline')
        print('hull: damaged')
        power%=70
        print('power is')
                
input('pres enter to exit')
