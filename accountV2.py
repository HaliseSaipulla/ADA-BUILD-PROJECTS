import random 
#2 
names = ["Halise Saipulla","Adila Abduwali","Dinnare Muhid","Dilmire Dilmurat","Gulgine Erkin"]
#creat empty lists
students =[]
students_dictio ={}

for i in range(len(names)):
    #generate id
    id = (random.randint(1111,9999))
    #generate email
    [first,last] = names[i].split(" ")
    email = first[0] + last + "@adadev.org"

    # create dictionary
    students_dictio[i] = {"name":names[i], "id":id, "email":email}

    # add each student from dictionary to the sudent list
    students.append(students_dictio[i])
    #print(students_dictio)

    print(f"Printing students[{i}]:{students[i]}")
    #ityuiuy