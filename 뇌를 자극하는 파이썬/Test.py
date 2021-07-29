import random
person_a = {}
person_b ={}
person_a['Hit_point']=random.randrange(350,500)
person_a['Punch_power']=random.randrange(7,10)
person_a['Effective_blow_rate']=random.randrange(3,7)
person_b['Hit_point'] = random.randrange(350, 500)
person_b['Punch_power'] = random.randrange(7, 10)
person_b['Effective_blow_rate'] = random.randrange(3, 7)
print("A선수에 관한 정보")
print("Hit_point: ",person_a['Hit_point'],"Punch_power:",person_a['Punch_power'],"Effective_blow_rate",person_a["Effective_blow_rate"])
print("B선수에 관한 정보")
print("Hit_point: ", person_b['Hit_point'], "Punch_power:", person_b['Punch_power'], "Effective_blow_rate", person_b["Effective_blow_rate"])
Round_num = 1
while(True):
    print("Round%d" % Round_num)
    person_a['Hit_point']=person_a['Hit_point']-(person_b['Punch_power']*person_b['Effective_blow_rate'])
    person_b['Hit_point'] = person_b['Hit_point'] - (person_a['Punch_power'] * person_a['Effective_blow_rate'])
    print("A선수에 관한 정보")
    print("Hit_point: ",person_a['Hit_point'],"Punch_power: ",person_a['Punch_power'],"Effective_blow_rate:",person_a["Effective_blow_rate"])
    print("B선수에 관한 정보")
    print("Hit_point: ", person_b['Hit_point'],"Punch_power:",person_b['Punch_power'],"Effective_blow_rate:",person_b["Effective_blow_rate"])
    if(person_a['Hit_point']<=0 or person_b['Hit_point']<=0):
        break
    Round_num +=1
    if(Round_num>9):
        break