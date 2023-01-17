str1="salut tout le mond"
#recupere la valeur d un idecis
print(str1[3])
#recupere la dernier caratere d un chaine
print(str1[-1])
print(len(str1))
print(str1[len(str1)-1])
#decoupage d une chaine de caractere la borne de 5 il n est pas inclusif
print(str1[0:5])
str2=str1[0:8]
print(str2)
print(str1[6:10])
print(str1[6:15])
str2="sabacada"
print(str2[1::2])#le monre de fois que
print(str1[0:])
print(str1[1::3])
print(str1[:7])
print(str1[-4:])
print(str1[::-1])
str8="krimou"
str9="oussad"
print(str8+" "+str9)
print(str8,str9)
str2=str2+str2
print(str2)
#utilisr les blocs
#afficher la chaines dans la bocles
for i in str2:
    print(i)
for i in enumerate(str2):
    print(i)