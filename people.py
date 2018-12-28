import json

people = [
    {'id': 1, 'name': 'BRANDON,PATTERSON'},
    {'id': 2, 'name': 'LAUREN,WHITE'},
    {'id': 3, 'name': 'WESLEY,PATTERSON'}
]

for p in people:
    name = p['name'].split(',')
    full_name = f"{name[0]} {name[1]}".title()

    print(full_name)

json.dump(people, open("people.json", "w"))
