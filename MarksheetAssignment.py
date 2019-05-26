#Marksheet assignment for PIAIC AI class.

subject = ['Mathematics','English','Physics','Chemistry','Computer']
marks = []
grade = []
total_marks = 0
final_grade = ""

for i in range(5):
    print("Enter marks for",subject[i],"\t:\t",end="")
    a = int(input())
    marks.append(a)
    total_marks = total_marks + a

percentage = total_marks/len(subject)
if percentage>=90:
    final_grade = "A*"
elif percentage>=80:
    final_grade = "A"
elif percentage>=70:
    final_grade = "B"
elif percentage>=60:
    final_grade = "C"
elif percentage>=50:
    final_grade = "D"
else:
    final_grade = "UNGRADED"

for j in range(5):
    if marks[j]>=90:
        grade.append("A*")
    elif marks[j]>=80:
        grade.append("A")
    elif marks[j]>=70:
        grade.append("B")
    elif marks[j]>=60:
        grade.append("C")
    elif marks[j]>=50:
        grade.append("D")
    else:
        grade.append("UNGRADED")
for l in range(53):
    print("_",end="")
print("\n\nSUBJECT\t\t\tOBTAINED\tTOTAL\tGRADE")
for l in range(53):
    print("_",end="")
print("\n")
for k in range(5):
    print(subject[k],"\t\t",marks[k],"\t\t","100","\t",grade[k])
for l in range(53):
    print("_",end="")

print("\n\nOVERALL PERCENTAGE :",percentage,"%","\t|\tGRADE :",final_grade,"\n\n")