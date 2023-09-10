from datetime import date
import csv
import random

today = date.today()

def generateKirbyOTD():

    with open('pastkirbyotds.csv', 'r+', newline='') as db:
        fldnames = ['date','copyAbility']
        reader = csv.DictReader(db)
        writer = csv.DictWriter(db, fieldnames=fldnames)
        dbAbilities = []
        dbLength = 0
            
        #count abilities and add to list
        abilityCount = 0
        tempAbilitiesList = []
        with open('kirbycopyabilities.txt', 'r') as abilities:
            for line in abilities:
                abilityCount += 1
                tempAbilitiesList.append(line.strip())

        #check if today already has a kirby
        for row in reader:
            if row['date'] == str(today):
                return row['copyAbility']
            dbLength += 1
            dbAbilities.append(row['copyAbility'])

        #check if the database has more entries than abilities and if yes erases them all
        if dbLength >= abilityCount:
            db.seek(0)
            db.truncate()
            db.write('date,copyAbility\n')
            dbAbilities = []

        abilityOTD = random.choice(tempAbilitiesList)
        while dbAbilities.count(abilityOTD) > 0:
            tempAbilitiesList.remove(abilityOTD)
            abilityOTD = random.choice(tempAbilitiesList)
            
        writer.writerow({'date': today, 'copyAbility': abilityOTD})
        return abilityOTD
           
print(f"Today is: {today}\nToday's Kirby is: {generateKirbyOTD()} Kirby!")


            

