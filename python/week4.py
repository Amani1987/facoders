
grade_one= {'Sami': [19, 18, 19.5, 30, 10], 'Ahmad': [15, 14, 16, 21, 7], 'Faris': [18, 19, 17, 26, 9], 'Salem': [20, 20, 19, 30, 10], 'Mahmoud': [12, 13, 11, 18, 7]}
grade_two= {'Lana': [17, 19, 20, 28, 9], 'Dina': [18.5, 19.5, 20, 29, 10], 'Maha': [20, 20, 18, 26, 9], 'Abeer': [16, 18, 19.5, 25, 8]}
grade_three= {'Rima': [18, 19, 18, 26, 9], 'Tala': [20, 20, 19, 29, 10], 'Lamar': [19, 20, 18, 26, 9], 'Rola': [15, 14, 16, 19, 7], 'Naya': [9, 6, 11, 14, 7], 'Dalal': [1, 5, 2, 6, 7], 'Ola': [19.5, 20, 20, 29.5, 10]}

x=input("Choose one: students_names, student_score, students_count :")
grade=[grade_one, grade_two, grade_three]

if x=="students_names":
    s=input("Choose one: grade_one, grade_two, grade_three :")
    if s=="grade_one":
        students_names=grade_one.keys()
    elif s=="grade_two":
        students_names=grade_two.keys()
    elif s=="grade_three":
        students_names=grade_three.keys()
    print(students_names)
if x=='student_score':
    s=input("Choose one: grade_one, grade_two, grade_three :")
    if s=="grade_one":
        i=input('Enter student name: ')
        a=grade_one.get(i)
        score=sum(a)
    if s=="grade_two":
        i=input('Enter student name: ')
        a=grade_two.get(i)
        score=sum(a)
    if s=="grade_three":
        i=input('Enter student name: ')
        a=grade_three.get(i)
        score=sum(a)
    print(score)
if x=='students_count':
    s=input("Choose one: grade_one, grade_two, grade_three :")
    students_count=len(s)
    print(students_count)
b=input('done or more? ')
while b=='more':
    grade_one= {'Sami': [19, 18, 19.5, 30, 10], 'Ahmad': [15, 14, 16, 21, 7], 'Faris': [18, 19, 17, 26, 9], 'Salem': [20, 20, 19, 30, 10], 'Mahmoud': [12, 13, 11, 18, 7]}
    grade_two= {'Lana': [17, 19, 20, 28, 9], 'Dina': [18.5, 19.5, 20, 29, 10], 'Maha': [20, 20, 18, 26, 9], 'Abeer': [16, 18, 19.5, 25, 8]}
    grade_three= {'Rima': [18, 19, 18, 26, 9], 'Tala': [20, 20, 19, 29, 10], 'Lamar': [19, 20, 18, 26, 9], 'Rola': [15, 14, 16, 19, 7], 'Naya': [9, 6, 11, 14, 7], 'Dalal': [1, 5, 2, 6, 7], 'Ola': [19.5, 20, 20, 29.5, 10]}

    x=input("Choose one: students_names, student_score, students_count :")
    grade=[grade_one, grade_two, grade_three]

    if x=="students_names":
        s=input("Choose one: grade_one, grade_two, grade_three :")
        if s=="grade_one":
            students_names=grade_one.keys()
        elif s=="grade_two":
            students_names=grade_two.keys()
        elif s=="grade_three":
            students_names=grade_three.keys()
        print(students_names)
    if x=='student_score':
        s=input("Choose one: grade_one, grade_two, grade_three :")
        if s=="grade_one":
            i=input('Enter student name: ')
            a=grade_one.get(i)
            score=sum(a)
        if s=="grade_two":
            i=input('Enter student name: ')
            a=grade_two.get(i)
            score=sum(a)
        if s=="grade_three":
            i=input('Enter student name: ')
            a=grade_three.get(i)
            score=sum(a)
        print(score)
    if x=='students_count':
        s=input("Choose one: grade_one, grade_two, grade_three :")
        students_count=len(s)
        print(students_count)
    b=input('done or more? ')
print('done!')
