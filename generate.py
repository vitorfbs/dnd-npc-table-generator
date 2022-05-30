from ctypes import alignment
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

def generate_alignment():
    alignment_axis = ["good", "neutral", "evil"]
    order_axis = ["lawful", "neutral", "chaotic"]
    alignment = alignment_axis[select_random(2)]
    order = order_axis[select_random(2)]
    return [order, alignment]

def generate_physical():
    pass

def generate_trait():
    traits_file = open('./data/traits.json')
    traits = json.load(traits_file)
    
    index = select_random(len(traits) - 1)
    
    return traits[index]["trait"]

def generate_manner():
    manners_file = open('./data/manners.json')
    manners = json.load(manners_file)
    
    index = select_random(len(manners) - 1)
    
    return manners[index]["manner"]

def generate_ideal(order_alignment):
    ideals_file = open('./data/ideals.json')
    ideals = json.load(ideals_file)
    
    order_ideal = ideals[0][order_alignment[0]]
    order_index = select_random(len(order_ideal) - 1)
    
    alignment_ideal = ideals[0][order_alignment[0]]
    alignment_index = select_random(len(alignment_ideal) - 1)

    other_ideal = ideals[0]["other"]
    other_index = select_random(len(other_ideal) - 1)
    
    return f"{order_ideal[order_index]['ideal']}, {alignment_ideal[alignment_index]['ideal']} e {other_ideal[other_index]['ideal']}"

def generate_talent():
    talents_file = open('./data/talents.json')
    talents = json.load(talents_file)
    
    index = select_random(len(talents) - 1)
    
    return talents[index]["talent"]

def generate_bond():
    pass

name = generate_name()
order_alignment = generate_alignment()
ideals = generate_ideal(order_alignment)
trait = generate_trait()
talent = generate_talent()
manner = generate_manner()

print(f"###################")
print(f"Nome: {name}")
print(f"Gênero: {gender}")
print(f"Raça: {race}")
print(f"---------------")
print(f"Alinhamento: {order_alignment}")
print(f"---------------")
print(f"Ideais: {ideals}")
print(f"---------------")
print(f"Traço: {trait}")
print(f"---------------")
print(f"Talento: {talent}")
print(f"---------------")
print(f"Manerismo: {manner}")
print(f"###################")

with open('npcs.txt', 'w') as f:
    f.write(name)
    f.write('\n')
    f.write(f"{race},{gender}")
    f.write('\n')
    f.write(f"{order_alignment[0]} {order_alignment[1]}")
    f.write('\n')
    f.write(ideals)
    f.write('\n')
    f.write(trait)
    f.write('\n')
    f.write(talent)
    f.write('\n')
    f.write(manner)