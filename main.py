def calculDateDuJour(date):
    print(date)
    c = (14 - int(date[1])) // 12
    a = int(date[2]) - c
    m = int(date[1]) + 12 * c - 2
    j = (int(date[0]) + a + a // 4 - a // 100 + a // 400 + (31 * m) // 12) % 7
    return j
def jourDeLaSemaine(index):
    jours = {0 : "lundi", 1 : "mardi", 3 : "mercredi", 4 : "jeudi", 5 : "vendredi", 6 : "samedi", 7 : "dimanche"}
    return jours[index]

def saisieDate():
    dateInput = input('Saisir une date au format jj/mm/aaaa')
    return jourDeLaSemaine(calculDateDuJour(dateInput.split('/')))

print(saisieDate())
