#!/usr/bin/env python3

def main():
    names = ['fluffy', 'spot', 'cujo']
    ages = [3, 7, 12]
    animal_type = ['cat', 'dog', 'mean dog']

    pets = {}
    pets2 = {}
    pets3 = {}
    for a in range(3):
        pets.update({names[a]: {'age': ages[a], 'animal_type': animal_type[a]}})
    print(pets)

    for a in range(3):
        pets2[names[a]] = {'age': ages[a], 'animal_type': animal_type[a]}
    print(pets2)

    for a in range(len(names)):
        pets3.update({names[a]: {'age': ages[a], 'animal_type': animal_type[a]}})
    print(pets3)


main()
