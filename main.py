def calculDateDuJour():
    dateInput = input('Saisir une date au format jj/mm/aaaa')
    date = dateInput.split('/')
    if len(date) != 3 or len(date[0]) > 3 or len(date[1]) > 3 or len(date[2]) > 5 or int(date[2]) < 1583 or int(date[2]) > 9999:
        return calculDateDuJour()
    else:
        c = (14 - int(date[1])) // 12
        a = int(date[2]) - c
        m = int(date[1]) + 12 * c - 2
        j = (int(date[0]) + a + a // 4 - a // 100 + a // 400 + (31 * m) // 12) %7
        return jourDeLaSemaine(j)
def jourDeLaSemaine(index):
    jours = {1 : "lundi", 2 : "mardi", 3 : "mercredi", 4 : "jeudi", 5 : "vendredi", 6 : "samedi", 0 : "dimanche"}
    return jours[index]
print(calculDateDuJour())
