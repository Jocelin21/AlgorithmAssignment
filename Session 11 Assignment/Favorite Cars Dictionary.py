"""
Create a dictionary to store people's favourite car models. Use the names of these people as keys and 
their favourite car models as the values. Each person must have at least 3 favourite cars. There should 
be at least 5 people in the dictionary.
Print each person's name out along with their favourite cars.
Sample output:
JJ likes these cars:
- Golf
- Camry
- LFA
Nicklas likes these cars:
- Innova
- Panther
- Fortuner
"""
car_dict = {
    "Aby": ["Mustang", "Civic", "Corvette"],
    "JJ": ["Golf", "Camry", "LFA"],
    "Kevin": ["Accord", "Corolla", "Wrangler"],
    "Nicklas": ["Innova", "Panther", "Fortuner"],
    "Rein": ["Cherokee", "Beetle", "BRV"]
}

name = list(car_dict)
cars = list(car_dict.values())
index = 0
for i in name:
    print (name[index], "likes these cars:")
    for i in cars[index]:
        print("-", i)
    index += 1
