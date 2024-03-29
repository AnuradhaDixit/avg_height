student_height = input("Input a list of student heights ").split()
height = 0
for n in range(0, len(student_height)):
  student_height[n] = int(student_height[n])
  height += student_height[n]
print(height)
print(len(student_height))
print(n+1)
print(round(height/(n+1)))