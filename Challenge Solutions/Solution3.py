#Challenge 3
x = int(input("Please enter an integer: "))
y = int(input("Please enter a larger integer: "))

def sumOddNumbersInRange(x, y):
  """A function to calculate the sum of odd numbers from x 
  (including x) to y (excluding y) return the result
  e.g. if x = 4 and y = 9 then the result is 5 + 7 = 12 
  """
  assert y > x # Check the input arguments to the function is okay 
  z = 0
  for i in range(x, y):
    if i % 2 == 1:
      z+=i
      
  return z
  

print("The sum of odd integers from: ", x, " up to: ", y, " is: ", 
      sumOddNumbersInRange(x, y))