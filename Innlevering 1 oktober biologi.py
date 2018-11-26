               #Oppgave 3

T=int(input("Hvor mange tøffeldyr ønsker du å starte med\n"))   #Antall trøffeldyr i starten
T_1=T      
t=int(input("Hvor mange timer ønsker du å se på?\n"))     #Antall timer



for i in range(0,t,2):
    T_1+=T_1

print("Antall tøffeldyr etter", t,"timer er", T_1, "hvis man begynner med",T,"tøffeldyr")

