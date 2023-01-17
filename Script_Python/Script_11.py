#utilisation des fonction
str1="  salut tout le monde  "
print(len(str1))#le nombre de caracter
print(str1.strip())#enleve les espace au debut a la fif de la chaine
print(len(str1))
str3=str1.strip()#enleve les espace au debut a la fif de la chaine
print(len(str3))
str4=str1.lstrip()#enleve les espace aa gouche de la chaine
print(len(str4))
str4=str1.rsplit()#enleve les espace a droite  gouche de la chaine
print(len(str4))
#enleve les les caracter au debut et a la fin
str5="***salut***tout***le***monde***"
print(str5)
str6=str5.strip("*")#enleve les etoit au debut et fin
print(str6)
print(str5.replace("*",""))#remplace les etoile par espace de la chaine
str15=str5.replace("*"," ")
print(str5.replace("   "," "))#remplace les espace par un espace de la chaine
str10="SALUT TOUT le monde"
#convertir tout minuscule ou majidscule
print(str10.lower())
print(str10.upper())
str11="salut tout le monde le monde le monde"
#nombre de fois quele mot repete
print(str11.count("le monde"))
print(str11.startswith("salut"))
print(str11.endswith("monde"))
#delimeter les chaine de caracter
str12="un-deux-trois-quatre-cinq-six-sept-huit-neuf-dix"
print(str12.split("-"))
print(str15.replace("   "," "))
