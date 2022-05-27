import json

male_human_names = ["Alexei", "Adenir", "Arthur", "Apolo", "Ary", "Alfonso", "Alonzo", "Adrian", "Andre", "Angelo", "Bren", "Bael", "Bev", "Bert", "Boren", "Bras", "Bose", "Baldir", "Brandon", "Barge", "Cleto", "Cesar", "Cuno", "Crest", "Camilo", "Ciro", "Carmino", "Chen", "Chao", "Cass", "Dario", "Demetrio", "Daniel", "Desmond", "Diogenes", "Dular", "Dirceu", "Dred", "David", "Daron", "Eduardo", "Emir", "Elton", "Ergo", "Elohim", "Elias", "Evram", "Evans", "Eggsy", "Eller", "Ferdinando", "Farlan", "Frederico", "Fuad", "Ford", "Filipe", "Flange", "Forin", "Fez", "Franz", "Gabriel", "Gale", "Grin", "Gael", "Gop", "Gen", "Gino", "Garbo", "Glenn", "Guliver", "Heitor", "Hector", "Henri", "Haroldo", "Hermes", "Hito", "Hal", "Ham", "Holler", "Henrico", "Iago", "Ian", "Irineu", "Italo", "Iman", "Izzy", "Ifran", "Icaro", "Ipe", "Isla", "Jonas", "James", "Jess", "Jerico", "Juca", "Jeda", "Jet", "Julius", "Jesper", "Joren", "Kelvin", "Kevin", "Karl", "Kretz", "Kit", "Keith", "Kenneth", "Klemens", "Karto", "Korban", "Lionel", "Leander", "Lano", "Lobe", "Lennie", "Leslie", "Liam", "Lester", "Letto", "Luan", "Manoel", "Marfisio", "Maerte", "Marston", "Miguel", "Melon", "Marco", "Mesme", "Morgan", "Milton", "Ned", "Nelson", "Naldo", "Ness", "Neto", "Nemo", "Nero", "Nuno", "Nefer", "Nolan", "Omar", "Otto", "Orion", "Orton", "Ollie", "Ozzy", "Oneary", "Ossia", "Otelo", "Osvaldo", "Pietro", "Pauli", "Punto", "Preston", "Pepe", "Posen", "Parno", "Penor", "Plesio", "Pieran", "Quintanilha", "Quentin", "Quisen", "Quincas", "Querubim", "Quintilo", "Quirino", "Quiliom", "Quemuel", "Quinn", "Regis", "Ricardo", "Richard", "Rasmos", "Romulo", "Rian", "Renne", "Rizzo", "Raul", "Roland", "Saulo", "Severino", "Sebastian", "Solomon", "Senna", "Soren", "Silas", "Samuel", "Sergio", "Serian", "Tadeu", "Timotio", "Teller", "Tomen", "Trento", "Tremere", "Tomas", "Teb", "Tico", "Telar", "Ulisses", "Uren", "Uira", "Ulrico", "Uba", "Venicio", "Vance", "Vern", "Viktor", "Volt", "Vilas", "Vent", "Vulcan", "Vinn", "Vex", "William", "Wilhelm", "Wallace", "Wanton", "Winston", "Waka", "Walsburg", "Webber", "Wellington", "Wesley", "Xavier", "Xin", "Xarp", "Xolmo", "Xeiq", "Yuri", "Ylag", "Yeze", "Yilian", "Yom", "Zeca", "Zacarias", "Zed", "Zora", "Zel"]
female_human_names = ["Aria", "Arabella", "Alana", "Alexia", "Ana", "Beirin", "Brenna", "Bianca", "Bella", "Bessie", "Camilla", "Catalina", "Caterine", "Cassandra", "Cesaria", "Derlina", "Darla", "Danielle", "Donna", "Durma", "Eliana", "Evelin", "Elrona", "Elizabeth", "Esme", "Felina", "Farla", "Fiona", "Fasbeth", "Frida", "Gertrude", "Giulia", "Giorna", "Genie", "Gabrielle", "Hilda", "Hella", "Hina", "Helen", "Helena", "Irina", "Izzy", "Isla", "Ilona", "Irene", "Joana", "Jean", "Joule", "Jessica", "Janete", "Kellen", "Katherina", "Killian", "Kess", "Kadra", "Lena", "Laura", "Luna", "Leslie", "Lenira", "Mirta", "Melina", "Melissa", "Mirtra", "Mirian", "Nadia", "Nilia", "Nena", "Norma", "Nice", "Olga", "Onera", "Olinda", "Ornella", "Opala", "Priscila", "Panello", "Paulina", "Poliana", "Pulia", "Quellen", "Qerina", "Quadra", "Qalla", "Quamalla", "Regina", "Reniere", "Rafaella", "Risa", "Ronda", "Suzana", "Siena", "Serena", "Suelen", "Samara", "Tatiana", "Tamara", "Teresa", "Tina", "Tabata", "Uma", "Ulia", "Ursula", "Una", "Ulyana", "Victoria", "Vanessa", "Vivian", "Venca", "Volna", "Wanda", "Winnie", "Winona", "Willow", "Warner", "Xaria", "Xena", "Xandra", "Xiya", "Ximena", "Yvette", "Yara", "Yona", "Yeva", "Yosselin", "Zara", "Zelda", "Zoe", "Zada", "Zeferina"]

male_elf_names = ["Aegnor", "Aego", "Agis", "Ailmar", "Akkar", "Beleg", "Beluar", "Bialaer", "Blythe", "Braern", "Cameron", "Celeborn", "Cirdan", "Conail", "Curunir", "Dakath", "Dior", "Doreir", "Dalyor", "Daynor", "Edrahil", "Elanjar", "Eldar", "Eldrin", "Evindal", "Faelar", "Fenris", "Filvendor", "Folduin", "Faenor", "Gael", "Gaylia", "Gaemon", "Gil-galad", "Glynkas", "Haemir", "Hagduin", "Haryk", "Horith", "Hubyr", "Iefyr", "Iliven", "Inarie", "Intevar", "Inchel", "Kevan", "Kolvar", "Kuskyn", "Kyrtaar", "Kelkalyn", "Larael", "Liryk", "Loryagis", "Laekkar", "Levindal", "Morgan", "Morthil", "Myril", "Myrin", "Molostroi", "Neldor", "Nieven", "Nym", "Nardual", "Nelaeryn", "Orym", "Orris", "Oribel", "Onas", "Oslarelar", "Pharom", "Pirphal", "Paeris", "Phaendar", "Pyrder", "Raegel", "Rhistel", "Reysalor", "Raunaeril", "Ravaphine", "Saevel", "Seiveril", "Sharian", "Silvyr", "Sudryl"]
female_elf_names = ["Aemma", "Aegnor", "Aelene", "Akashi", "Alais", "Baelen", "Blythe", "Bonna", "Braerindra", "Baela", "Calarel", "Chandrelle", "Cauladra", "Caerthynna", "Celebrian", "Daealla", "Daena", "Doreah", "Daenys", "Daeharice", "Elaria", "Ellania", "Elora", "Elyssa", "Elenwe", "Filaurel", "Fraeya", "Filauria", "Fildaerae", "Finduilas", "Gaelira", "Galadriel", "Gaylia", "Gilgalad", "Gweyr", "Haela", "Halama", "Holone", "Hycis", "Holcene", "Ialantha", "Idril", "Imizael", "Ithirae", "Imdalace", "Jahandra", "Jassinya", "Jhaeriana", "Jhaana", "Jhaartyria", "Kaeda", "Kaylessa", "Keerla", "Keya", "Kythaela", "Laeanna", "Laena", "Lazziar", "Leandra", "Lorelei", "Maegelle", "Meara", "Mereena", "Miriel", "Morwen", "Nuovis", "Nusahala", "Nylaathria", "Nym", "Nieven", "Oluevaera", "Oona", "Orymia", "Orrisya", "Onas", "Phaerle", "Phantyni", "Phyrra", "Pirphala", "Paerisa", "Quaula", "Quamara", "Quaerla", "Quiphala", "Quevena", "Reinys", "Rubrae", "Rathiain", "Renestrae", "Ryllae", "Shalana", "Sheedra", "Saelihn", "Sasha", "Soliania", "Taena", "Taeriel", "Talindra", "Tamara", "Takari", "Urmica", "Uona", "Uendra", "Ureliaena", "Ureven", "Vaella", "Veara", "Vestele", "Viserra", "Valindra", "Ymeha", "Ymiela", "Yaereene", "Yrlissa", "Ynshael", "Zeale", "Zabbas", "Zaltarish", "Zaeliena", "Zelya"]

human_names = {
    "human" : {
        "male": [],
        "female": []
    }
}

elf_names = {
    "elf" : {
        "male": [],
        "female": []
    }
}

name_list = [human_names, elf_names]

for name in male_human_names:
    name_entry = { "name": name}
    name_list[0]["human"]["male"].append(name_entry)

for name in female_human_names:
    name_entry = { "name": name}
    name_list[0]["human"]["female"].append(name_entry)

for name in male_elf_names:
    name_entry = { "name": name}
    name_list[1]["elf"]["male"].append(name_entry)

for name in female_elf_names:
    name_entry = { "name": name}
    name_list[1]["elf"]["female"].append(name_entry)


with open('names.json', 'w') as f:
    json.dump(name_list, f, ensure_ascii=False, indent=4)