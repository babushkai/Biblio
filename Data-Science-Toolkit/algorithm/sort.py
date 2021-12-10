array = [1,2,0,0,0,0,4420,4,0,2,0,55,0,12,0,5,0,7,0,9,3,2,0,0,32,1,3,4,4]

for i in range(len(array)-1):
  for i in range(len(array)-1):
    if array[i]<array[i+1]:
      array[i], array[i+1] = array[i+1], array[i]
    else:
        continue
        
print(array)