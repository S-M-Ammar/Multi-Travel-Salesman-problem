from operator import imod
import numpy as np
a = np.array([1,7,3,6,2])
b = np.array([1,3,7,2,6])

offspring = [1,]
turn = 0
size = 5
index_1 = 1
index_2 = 1
while(len(offspring)!=size):
    if(index_1<size and index_2<size and a[index_1]==b[index_2]):
        offspring.append(a[index_1])
        index_1+=1
        index_2+=1
    else:
        if(turn==0):
            if(index_1<size and not(a[index_1] in offspring)):
                offspring.append(a[index_1])
                turn = 1
                
            index_1+=1
            
        elif(turn==1):
            if(index_2<size and not(b[index_2] in offspring)):
                offspring.append(b[index_2])
                turn = 0

            index_2+=1
            
        
offspring