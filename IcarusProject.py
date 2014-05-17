
#Icarus project

#beginning conditions
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
cargobay={'nitrogen':400,'drones':40,'metal':50,'hydrogen':500}
shieldoverdrive=0

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
options=['scan area','repair damaged parts','functionality report']
while(question_answerd==0):
    repaired=random.randint(0,100)
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
        repair=1

    if action=='functionality report':
        print('weapons 5 to 9 offline')
        print('hull: damaged')
        powera=(power/10000)*100
        print('power is',powera,'%')
                
print('starting to sweep area')
print('distance to nearest star:')
time.sleep(2)
print('1,323 lightyears')
cargo_bay={}

question_answerd=0
problem_identify=0
repair_program=0
options=['diagnose ftl drive','repair ftl drive','run repair program']
while(ftl_overload==1):
    repaired=random.randint(0,100)
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
    action=input('input:')

    if action=='options':
        print(options)
        
    if action=='diagnose ftl drive':
        print('running diagnosis program')
        time.sleep(8)
        print('loading coordinate calculations')
        time.sleep(2)
        print('calculating power fluctuations')
        time.sleep(3)
        print('loading path calculating program')
        time.sleep(5)
        print('identify problem')
        time.sleep(7)
        problem_identify=1
        print('problem identified')
    
    if(action=='run repair program'):
        if(problem_identify!=1):
            print('unkown problem')
        if(problem_identify==1):
            print('running repair program')
            time.sleep(4)
            print('repair systems found. problem can be fixed')
            repair_program=1
            
    if(action=='repair ftl drive'):
        if(problem_identify!=1)and(repair_program!=1):
            print('unkown problem')
        if(problem_identify==1)and(repair_program!=1):
            print('repair routine unkown')
        if(problem_identify==1)and(repair_program==1):
            print('fixing problem')
            time.sleep(10)
            print('problem fixed')
            ftl_overload=0

    if action=='smash random things till it works':
        print('it magically repaired itself, good job :D')
        ftl_overload=0

ftl_active=0
options=['jump to ftl',"repair damaged areas"]
while(ftl_active==0):
    repaired=random.randint(0,100)
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
    action=input('input:')
    
    if(action=='options'):
        print(options)
    
    if(action=="repair damaged areas"):
        print("starting to repair damaged areas")
        time.sleep(2)
        repair=1
    
    if(action=='jump to ftl'):
        print('plotting course to Gamma-429b')
        time.sleep(3)
        print('course plotted')
        time.sleep(1)
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
        print('we just jumped to ftl')
        time.sleep(5)
        print('systems opperational')
        ftl_active=1

#Mission 2
#Introducing storyline
print('You have arrived at Gamma-492b') #Spectraalklasse B (die andere is G) 
print('scanners show nothing more than dust')
print('We need nitrogen to cool down the engines!')
#Interactive question_1
scan=0
while(scan==0):
    repaired=random.randint(0,100)
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
    repaired=random.randint(0,100)
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
    answer_2= input('input:')

    if answer_2=='options':
        print(options)
        
    if answer_2=='repair damaged areas':
        print('starting to repair damaged areas')
        time.sleep(2)
        repair=1

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
        elif answer_3 == "Phiksi-1":
            print("plotting course to Phiksi-1")
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




input('pres enter to exit')
