from datetime import date



print("Bitte verwende nur Zahlen als Input!")
print('--------------------------------------------')
join_year = input('Join Jahr: ')
join_monat = input('Join Monat: ')
join_tag = input('Join Tag: ')


date_input = date(int(join_year), int(join_monat), int(join_tag))
date_today = date.today()
delta = date_today - date_input
year = (((int(delta.days) /30) / 6) + 1)

year = str(year).split('.')

print(f'\nDer User bekommt die Rolle Jahr {year[0]}')
input("\n \nDrücke Enter um das Programm zu beenden")
