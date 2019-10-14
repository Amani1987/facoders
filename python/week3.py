s1=['Ahmad',18,17,19.5,8,25]
s2=['Sami',20,20,19,9,28]
s3=['Faris',14.5,16,13,7,23]
name=input('Enter student\'s name: ')
names=['Ahmad','Sami','Faris']
score=[sum(s1[1:6]),sum(s2[1:6]),sum(s3[1:6])]
if name=='Ahmad':
    print(names[0],score[0])
elif name=='Sami':
    print(names[1],score[1])
elif name=='Faris':
    print(names[2],score[2])
else:
    print('student\'s name is not recorded',0)
