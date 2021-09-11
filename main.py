def calculDateDuJour(date):

    if len(date) != 3 or len(date[0]) > 3 or len(date[1]) > 3 or len(date[2]) > 5 or int(date[2]) < 1583 or int(date[2]) > 9999:
        saisieDate()
    else:
        c = (14 - int(date[1])) // 12
        a = int(date[2]) - c
        m = int(date[1]) + 12 * c - 2
        j = (int(date[0]) + a + a / 4 - a / 100 + a / 400 + (31 * m) // 12) % 7
        return round(j)
def jourDeLaSemaine(index):
    jours = {0 : "lundi", 1 : "mardi", 2 : "mercredi", 3 : "jeudi", 4 : "vendredi", 5 : "samedi", 6 : "dimanche"}
    return jours[index -1]

def saisieDate():
    dateInput = input('Saisir une date au format jj/mm/aaaa')
    return jourDeLaSemaine(calculDateDuJour(dateInput.split('/')))

print(saisieDate())
