#Résolution d'equation quadratique en python
a =int(input("Veuillez saisir le nombre representant a dans l'equation: "))
b= int(input("Veuillez saisir le nombre representant b dans l'equation: "))
c=int(input("Veuillez saisir le nombre representant c dans l'equation: "))
if a != 0:
    discriminant = b**2-4*a*c
    if discriminant<0:
        print ("L'equation",a,"* x^2 +",b,"*x +",c,"n’admet pas de solutions réelles.")
    elif discriminant == 0:
        X= (-1*b)/2*a
        print ("L'equation",a,"* x^2 +",b,"*x +",c, "admet une unique solution qui est: ",X)
    elif discriminant > 0:
        X_one= (-1*b-discriminant**0.5)/2*a
        X_two= (-1*b+discriminant**0.5)/2*a
        print ("L equation",a,"* x^2 +",b,"*x +",c,"admet deux solutions qui sont: ",X_one,"Et",X_two)
else: print("a doit etre different de 0 revoyez votre valeur de a")
