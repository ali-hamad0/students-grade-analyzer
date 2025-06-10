#1- Prints students names and grades

def display_student_summary(stnames, grades):
    print("here are the students names and their grades : ")
    for x in range(len(stnames)):
        print(stnames[x] + "->" + str(grades[x]))

#2- get the average grade of the class

def get_avg_grade(grades):
    avg = 0
    for grade in grades:
        avg+= grade
    return avg / len(grades)

#3- Prints the highest grade earned (Student name and grade)

def get_highest_grade(stnames,grades):
    h_grade = grades[0]
    h_student = stnames[0]

    for i in range(1, len(grades)):
        if grades[i] > h_grade:
            h_grade = grades[i]
            h_student= stnames[i]
    return h_student , h_grade 

#4- Prints the count of students who passed (grade >= 60)

def count_passed(grades):
    count = 0
    for grade in grades:
        if grade >= 60 :
            count += 1
    return count

#main

num_of_students =  int(input("Enter the number of students"))
    
stnames = [] 
grades = [] 

for i in range(num_of_students):
        name = input("Enter student name : " )
        grade = int(input("Enter " + name + "'s grade : "))
        stnames.append(name)
        grades.append(grade)

display_student_summary(stnames , grades)

avg_grades = get_avg_grade(grades)
print("the average grade of the class is : " + str(avg_grades))

highest_name, highest_grade = get_highest_grade(stnames,grades)
print("the highest grade is :" + str(highest_grade)  + " and it's earned by :" + highest_name )

count_pass = count_passed(grades)
print("the number of students who passed (with grade >=60) is : " + str(count_pass))


        

