print('**** Welcome to the LAB grade calculator! ****\n')
name = input('Who are we calculating the grades for? ==> ')  #asks for the user's name
print()
lab = int(input('Enter the Labs grade? ==> '))  #asks for the lab grade
if lab > 100:  #if the grade is too high, it is changed to 100
    print('The lab value should have been 100 or less. It has been changed to 100.')
    lab = 100
elif lab < 0:  #if the grade is below zero, it is changed to 0
    print('The lab value should have been zero or greater. It has been changed to zero.')
    lab = 0
print()
exam = int(input('Enter the EXAMS grade? ==> '))  #asks for the exam grade
if exam > 100:  #if the grade is too high, it is changed to 100
    print('The exam value should have been 100 or less. It has been changed to 100.')
    exam = 100
elif exam < 0:  #if the grade is below zero, it is changed to 0
    print('The exam value should have been zero or greater. It has been changed to zero.')
    exam = 0
print()
attend = int(input('Enter the Attendance grade? ==> '))  #asks for the attendance grade
if attend > 100:  #if the grade is too high, it is changed to 100
    print('The attendance value should have been 100 or less. It has been changed to 100.')
    attend = 100
elif attend < 0:  #if the grade is below zero, it is changed to 0
    print('The attendance value should have been zero or greater. It has been changed to zero.')
    attend = 0
print()
numGrade = float((lab * 0.7) + (exam * 0.2) + (attend * 0.1))  #calculates weighted grade
if numGrade >= 90:       #these if, elif, and else statements use the weighted grade to find the letter grade
    letterGrade = 'A'
elif numGrade >= 80:
    letterGrade = 'B'
elif numGrade >= 70:
    letterGrade = 'C'
elif numGrade >= 60:
    letterGrade = 'D'
else:
    letterGrade = 'F'
print(f'The weighted grade for {name} is {numGrade}.')  #outputs the weighted grade
print(f'{name} has a letter grade of {letterGrade}')   #outputs the letter grade
print()
print('**** Thanks for using the Lab grade calculator ****')
