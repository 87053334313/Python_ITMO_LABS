from random import randint
import time

#Ввод имен играющих
igrok1 = input("Введите имя 1-го играющего \n")
igrok2 = input("Введите имя второго играющего \n")




sum_1=0
sum_2=0
for i in range(5):

    #Моделироавание бросания кубика первым играющим 
    print('Кубик бросает игрок ', igrok1)
    time.sleep(2)
    n1 = randint(1,6)
    print("Выпало",n1)

    #Моделироание бросание второго кубика
    print("Кубик бросает игрок ", igrok2)
    time.sleep(2)
    n2 = randint(1,6)
    print("Выпало", n2)
    sum_1+=n1;
    sum_2+=n2
if(sum_1>sum_2):
        print("Победил игрок ", igrok1 ,"у него ",sum_1, "баллов")
elif(sum_1<sum_2):
        print("Победил игрок", igrok2,"у него ",sum_2, "баллов")
else:
        print("Ничья")