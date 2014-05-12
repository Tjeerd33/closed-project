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
print('you are part of a secret military program, project Icarus')
print('the project made a spaceship that is capable of ftl')
print('(ftl=faster than light)')
print('you are the captain and the ship will be launched today, you will control it through this control panel.')
print('the ship is completely drone operated')
print('it is controlled through a series of entangled particles')
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
        time.sleep(5)
        print('error')
        print('system overload')
        print('ship damaged')
        print('weapons 5 to 9 offline')
        ftl_overload=1
        question_answer=1

while(ftl_overload<1):
    action=input('input:')
    
    if(action=='options'):
        print(options)
        
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
        time.sleep(5)
        print('error')
        print('system overload')
        print('ship damaged')
        print('weapons 5 to 9 offline')
        ftl_overload=1

question_answerd=0
options=['scan area','repair damaged parts','full power to the shields','functionality report']
while(question_answerd==0):
    action=input('input:')

    if action=='options':
        print(options)
        
    if action=='scan area':
        print('area scanned')
        print('computer reports:')
        print('we are in the middle of empty space')
        print('locating near stars and calculating distance to earth')
        time.sleep(5)
        print('estimated distance to earth:')
        time.sleep(2)
        print('unknown')
        question_answerd=1

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
        time.sleep(2)
        print('    ',energy_transferd,' energy transferred from cannon batteries 1 to the front shield')
        energy_transferd=0
        while(shieldfront<600)and(canon_batterys2>0):
            canon_batterys2=canon_batterys2-1
            shieldfront=shieldfront+1
            energy_transferd=energy_transferd+1
        time.sleep(2)
        print('    ',energy_transferd,' energy transferred from cannon batteries 2 to the front shield')
        energy_transferd=0
        while(shieldmid<600)and(canon_batterys2>0):
            canon_batterys2=canon_batterys2-1
            shieldmid=shieldmid+1
            energy_transferd=energy_transferd+1
        print('    ',energy_transferd,' energy transferred from cannon batteries 2 to the mid shield')
        energy_transferd=0
        while(shieldmid<600)and(canon_batterys3>0):
            canon_batterys3=canon_batterys3-1
            shieldmid=shieldmid+1
            energy_transferd=energy_transferd+1
        print('    ',energy_transferd,' energy transferred from cannon batteries 3 to the mid shield')
        time.sleep(4)
        print('shields are fully powered and operational')
        print('weapons offline')

    if action=='functionality report':
        print('weapons 5 to 9 offline')
        print('hull: damaged')
        powera=(power/1000)*100
        print('power is',powera,'%')
                
print('starting to sweep area')
print('distance to nearest star:')
time.sleep(2)
print('1,323 lightyears')
cargo_bay={}

question_answerd=0
options=['diagnose ftl drive','repair ftl drive','run repair program']
while(ftl_overload==1):
    action=input('input:')

    if action=='options':
        print(options)

    if action=='smash random things till it works':
        print('it magically repaired itself, good job :D')
        ftl_overload=0

#Mission 2
#Introducing storyline
import time
print('You have arrived at Gamma-492b')
print('scanners show nothing more than dust')
print('We need water to cool down the engines!')
#Interactive question_1
scan=0
while(scan==0):
    answer_1 = input('scan for nearby star systems?')

    #Morphing and comparing answer_1
    answer_1 = answer_1.lower()
    if answer_1 == "yes":
        print('Booting scanner...')
        time.sleep(1)
        print('Scanner booted!')
        time.sleep(3)
        print('Three nearby places have been found!')
        print('Fruhka-2, Zdelta-5 and Phiksi-1')
        scan=1

ftl_active=0
while(ftl_active==0):#will repeat the question untill the ftl drive is active (will be active once ftl_active=1)
    options=['plot course to','repair damaged areas']
    answer_2= input('input:')

    if answer_2=='options':
        print(options)

    if answer_2=='plot course to':
        answer_3=input('    ')
        if answer_3 == "Fruhka-2":
            print("plotting course to Fruhka-2")
            time.sleep(3)
            print('course plotted')
            print('we will jump to ftl in 20 seconds')
            time.sleep(10)
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
            print('jump succesfull')
            time.sleep(1)
            print('all systems fuctioning')
            print('dropp out in T minus 3 seconds')
            time.sleep(1)
            print('3')
            time.sleep(1)
            print('2')
            time.sleep(1)
            print('1')
            ftl_active=1
        elif answer_3 == "Zdelta-5":
            print("plotting course to Zdelta-5")
            time.sleep(3)
            print('course plotted')
            prtin('we will jump to ftl in 20 seconds')
            time.sleep(10)
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
            print('jump succesfull')
            time.sleep(1)
            print('all systems fuctioning')
            print('dropp out in T minus 3 seconds')
            time.sleep(1)
            print('3')
            time.sleep(1)
            print('2')
            time.sleep(1)
            print('1')
            ftl_active=1
        elif answer_3 == "Phiksi-1":
            print("plotting course to Phiksi-1")
            time.sleep(3)
            print('course plotted')
            prtin('we will jump to ftl in 20 seconds')
            time.sleep(10)
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
            print('jump succesfull')
            time.sleep(1)
            print('all systems fuctioning')
            print('dropp out in T minus 3 seconds')
            time.sleep(1)
            print('3')
            time.sleep(1)
            print('2')
            time.sleep(1)
            print('1')
            ftl_active=1




input('pres enter to exit')
