#Практическая работа номер 2 все задания сверху вниз как  в методичке
#Работа со строками
"""
string1="This is a string   ";
string2=" This is another string";
print(string1+string2);
print(len(string1));
string3 = string1.title();
print(string3)
print(string2.lower())
print(string1.upper())
print(string1.rstrip())
print(string1.lstrip())
print(string1.strip('T'))
"""
#----------------------------------------------------------

d="qwerty"
ch=d[2]
#print(ch)
cmh=d[1:3]
#print(cmh)
cmh=d[1:]
cmh=d[:3]
cmh=d[1:5:2]
 
#print(ch)
#-------------------------------------------------
#Работа с числами
"""
int_i=2
int_a=5
print(int_i**2)
print(5%3)
print(7/21)
param="string" + str(15)
print(param)
"""




#--------------------------------------------------------
#Преобразование данных
#param = "string" + str(15)
#n1 = input("Enter the first number: ")
#n2 = input("Enter the second number: ")
#n3 = float(n1) + float(n2)
#print(n1 +" plus " + n2 + " = " , n3)

#Форматирование строк
"""
a=1/3
print("{:7.3f}".format(a))
a=2/3
b=2/9
print("{:7.3f} {:7.3f}".format(a,b))
print("{:10.3e} {:10.3e}".format(a,b))

n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
n3 = float(n1) + float(n2)
_string=n1 +" plus " + n2 + " = " , n3
print(_string,"{:3.12f}".format(n3))
"""
#--------------------------------------------------------------
#Списки
list1 = [82,8,23,97,92,44,17,39,11,12]
#print(dir(list))
#help(list1.insert)
#help(list.append)
#help(list.sort)
#help(list.remove)
#help(list1)
a1=list1[0]
list1[0]=list1[1]
list1[1]=a1
 
list1.append(555)
list1.insert(1,10)
list1.pop(0)
list1.pop()
_list2 = sorted(list1,reverse=True)
list1.sort(reverse=True);
#print(list2)
list2 = [3,5,6,2,33,6,11]
lis=sorted(list2) 
#print(list2,"\n",lis)

#-----------------------------------------
#Кортежи
#print(dir(tuple))
#help(tuple.index)
#help(tuple.count)
seq=(2,8,23,97,92,44,17,39,11,12,8)
#print(seq.count(8))
#print(seq.index(44))
listseq=list(seq)
#print(type(listseq))
listseq.append(777)
#print(listseq)
 
#----------------------------------------------------
#Словари
D={"food":"Apple","quantity":4,"color":"red"}
#print(D["color"])
D["quantity"]+=10
#print(D["quantity"])
#dp={}
#_age=input("Введите ваш возраст")
#_name=input("Введите ваше имя")
#dp["age"]=_age
#dp["name"]=_name
#print(dp)
#----------
#Вложенность хранения данных
"""
rec={"name":{"firstname":"Bob","lastname":"Smith"},
"job":["dev","mgr"],
"age":25}
print(rec["name"])
print("firstname: ",rec["name"]["lastname"])
print("jobs: ",rec["job"])
newJob=input("Enter new job ")
rec["job"].append(newJob)
print(rec)
"""