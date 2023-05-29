#min of 3 numbers 

a =(input('Enter a 1st number:'))
b =(input('Enter a 2nd number:'))
c =(input('Enter a 3rd number:'))

if a<b and a<c:
    print('a is min')
elif b<a and b<c:
    print('b is min')
else:
    print('c is min')
    