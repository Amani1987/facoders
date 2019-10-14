print('Welcome!')
print('Numbers from 1 to 10 GAME')
x=7
y=int(input('Guess the number:'))
while(x!=y):
    if (x!=y):
        y=int(input('Guess the number:'))
        continue
if(x==y):
    print('Great! You did it!')
