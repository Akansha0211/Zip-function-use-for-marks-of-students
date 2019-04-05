a=int(input("Number of students"))
marks_in_bme=[]
name=[]
for i in range (a):
    h=input("Enter name of students")
    name.append(h)
    i=int(input("Enter marks"))
    marks_in_bme.append(i)
print(name)
print(marks_in_bme)
result=zip(name,marks_in_bme)
result_set=set(result)
print(result_set)
