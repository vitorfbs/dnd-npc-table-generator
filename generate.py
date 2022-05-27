import json
import random
import sys

###############
# Genders
# ---------
# male = 0
# female = 1
###############
genders = ["male", "female"]

###############
# Races
# ---------
# human = 0
# elf = 1
# dwarf = 2
# gnome = 3
# halfling = 4
# orc = 5
###############
races = ["human","elf","dwarf","gnome","halfling","orc"]


if(len(sys.argv) >= 2):
    gender_index = int(sys.argv[1])
else:
    gender_index = random.randint(0, 1)
if(len(sys.argv) >= 3):
    race_index = int(sys.argv[2])
else:
    # race_index = random.randint(0, len(races) - 1)
    race_index = random.randint(0, 1)


gender = genders[gender_index]
race = races[race_index]


def select_random(limit):
    return random.randint(0, limit)

def generate_name():
    names_file = open('./data/names.json')
    names = json.load(names_file)
    random_name_index = select_random(len(names[race_index][race][gender]) - 1)
    return names[race_index][race][gender][random_name_index]['name']

def generate_race():
    pass

def generate_physical():
    pass

def generate_trait():
    traits_file = open('./data/traits.json')
    traits = json.load(traits_file)
    index = select_random(len(traits) - 1)
    return traits[index]["trait"]

def generate_manner():
    pass

def generate_ideal():
    pass

def generate_talent():
    pass

def generate_bond():
    pass

name = generate_name()
trait = generate_trait()

print(f"Name: {name}")
print(f"Gender: {gender}")
print(f"Race: {race}")
print(f"---------------")
print(f"Trait: {trait}")

with open('npcs.txt', 'w') as f:
    f.write(name)
    f.write('\n')
    f.write(f"{race},{gender}")
    f.write('\n')
    f.write(trait)