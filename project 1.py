print("Name of the clubs:-")
print("Enter the name of a club")
print("sports")
print("song")
print("literature")
print("science")
print("art")

sport = []
song = []
literature = []
science = []
art = []

teacher = input("Enter the name of the club: ")

if teacher == "sports":
    number = int(input("Enter the number of students: "))
    f = open("sports.txt", "w")
    for i in range(1, number+1):
        name = input("Enter the name of {} the student: ".format(i))
        f.write(name + "\n")
        sport.append(name)
    f.close()
elif teacher == "song":
    number1 = int(input("Enter the number of students: "))
    f = open("song.txt", "w")
    for x in range(1, number1 + 1):
        name1 = input("Enter the name of {} the student: ".format(x))
        f.write(name1 + "\n")
        song.append(name1)
    f.close()
elif teacher == "literature":
    number2 = int(input("Enter the number of students: "))
    f = open("literature.txt", "w")
    for y in range(1, number2+1):
        name2 = input("Enter the name of {} the student: ".format(y))
        f.write(name2 + "\n")
        literature.append(name2)
    f.close()
elif teacher == "science":
    number3 = int(input("Enter the number of students: "))
    f = open("science.txt", "w")
    for z in range(1, number3+1):
        name3 = input("Enter the name of {} the student: ".format(z))
        f.write(name3 + "\n")
        science.append(name3)
    f.close()
elif teacher == "art":
    number4 = int(input("Enter the number of students: "))
    f = open("art.txt", "w")
    for a in range(1, number4 + 1):
        name4 = input("Enter the name of {} the student: ".format(a))
        f.write(name4 + "\n")
        art.append(name4)
    f.close()
else:
    print("Error !!!!! | ENTER A VALID CLUB NAME !!!!")