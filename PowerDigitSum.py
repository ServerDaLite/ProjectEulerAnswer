result = pow(2, 1000)
result = list(str(result))

summed = 0
for char in result:
    summed += int(char)
    
print(summed)
