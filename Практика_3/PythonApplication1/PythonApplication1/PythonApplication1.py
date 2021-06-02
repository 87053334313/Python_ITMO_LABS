import math
 
print(math.e)
print(dir(math))
import statistics
print(dir(statistics))
 


my_list=[1,2,3,4,5,6,7,8,9,10]
print('summa=',math.fsum(my_list))
print("avg = ",statistics.mean(my_list))
print("mediana = ", statistics.median(my_list));
print("standartnoe otlonenie",statistics.stdev(my_list))

from random import randint
print(randint(1,100))
