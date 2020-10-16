'''
glas = "aeoui"
countG = 0

sogl = "sdfghjkl"
countS = 0

str_1 = "Privet, mir ya zdes"
'''

print("hgehgrorehre")
print("hgehgrorehre")
print("hgehgrorehre")
print("hgehgrorehre")
print("hgehgrorehre")
print("hgehgrorehre")
print("hgehgrorehre")
print("hgehgrorehre")
print("""hgehgrorehreerpgkr
e
ger
gkpregkpr[egk
ergregkr
ewgprejgporjegorejg
rejogrejg""")




#Polindrom
    #Numeric polindrom
num_1 = 12321
num_2 = 123321
    #String polindrom
str_1 = "polilop"
str_2 = "Иди иди"
str_3 = "MadamAdam"

#Поиск численного полиндрома
'''
num = int(input())

razryad = 1
delitel = 10

temp_num = num #копируем число в буфер

#Подсчет количества разрядов в числе
while temp_num != 0:
    temp_num //= delitel #temp_num =temp_num / delitel
    razryad *= 10

razryad /= 10 #убираем лишний разряд
#print(f"razryad = {razryad}")

#print(f"last number = {num % 10}") #последня цифра числа
#print(f"first number = {num // razryad}") #первая цифра числа

pol = True #переменная логическая которая хранит ответ полиндром или нет
temp_num = num #копируем число в буфер
while temp_num != 0:
    if temp_num // razryad == temp_num % 10:
        #print(f"{temp_num // razryad} ииии {temp_num % 10}")
        #print(f" Да цифры равны")
        pol = True
    else:
        #print(f"{temp_num // razryad} ииии {temp_num % 10}")
        #print("Цифры не равны")
        pol = False
        break
    temp_num -= (temp_num // razryad) * razryad  # Убираем первую цифру числа
    temp_num //= 10  # выкидываем последнюю цифру числа
    razryad //= 100  # уменьшаю разряд

if pol:
    print("Chislo polindrom")
else:
    print("Chislo ne polindrom")
'''

#Поиск символьного полиндрома
#Classic resolve
'''str_1 = input()
pol = True
for i in range(len(str_1) // 2):
    if str_1[i].lower() == str_1[-i - 1].lower():
        pol = True
    else:
        pol = False
        break
if pol:
    print("Chislo polindrom")
else:
    print("Chislo ne polindrom")
'''
#Classic reduce resolve
'''
str_1 = input()
pol = True
for i in range(len(str_1) // 2):
    if str_1[i].lower() != str_1[-i - 1].lower():
        pol = False
        break
if pol:
    print("String polindrom")
else:
    print("String ne polindrom")
'''
#String slicing resolve
'''str_1 = input()
if str_1 == str_1[:: -1]:
    print("String polindrom")
else:
    print("String ne polindrom")
'''

num_1 = input()
str_1 = str(num_1)
if str_1 == str_1[:: -1]:
    print("String polindrom")
else:
    print("String ne polindrom")

num_1 = 357893453

print("#" * 10)
print("#" + " " * 8 + "#")
print("#" + " " * 8 + "#")
print("#" + " " * 8 + "#")
print("#" + " " * 8 + "#")
print("#" + " " * 8 + "#")
print("#" + " " * 8 + "#")
print("#" * 10)