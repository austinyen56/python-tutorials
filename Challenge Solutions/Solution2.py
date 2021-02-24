#Challenge 2
x = int(input('Input an int: '))
i = 1

if x < 0:
    print('Invalid height')
    
while i < x+1:  
  print('*'* i)
  i+=1