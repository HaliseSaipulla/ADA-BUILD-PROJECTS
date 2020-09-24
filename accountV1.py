import random
#2
students = ["Halise Saipulla","Adila Abduwali","Dinnare Muhid","Dilmire Dilmurat","Gulgine Erkin"]

#3
ids = []
for i in range(5):
    ids.append(random.randint(1111,9999))

#4
emails = []
for student in students:
   [first,last] = student.split(" ")
   emails.append(first[0]+last+str(ids[i])[0:3]+"@adadev.or")


#5
for i in range(5):
    print(f"student: (names[i])")
    print(f"id:{ids[i]}")
    print(f"email:{emails[i]}\n")
    #jfgkj