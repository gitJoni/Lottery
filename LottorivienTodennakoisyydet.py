try:
    with open('Eurojackpotnumerot.txt', 'r') as tiedosto:
        rivit = tiedosto.readlines()
except:
    print("Jokin meni vikaan tiedostoa luetteassa.")

paanumerot = []
tahtinumerot = []

for rivi in rivit[:51]:
    mones = 0
    numerot = rivi.split(' ')
    for numero in numerot:
        numero = numero.strip()
        if numero.isdigit():
            if mones < 5:
                paanumerot.append(int(numero))
            else:
                tahtinumerot.append(int(numero))
            mones += 1

suosituin_rivi = []
suosituimmat_tahtinumerot = []
vahiten_suosituin = []
vahiten_suosituimmat_tahtinumerot = []

for i in range(7):
    if i < 5:
        maksimi = max(paanumerot, key=paanumerot.count)
        minimi = min(paanumerot, key=paanumerot.count)
        suosituin_rivi.append(maksimi)
        vahiten_suosituin.append(minimi)
        paanumerot = [i for i in paanumerot if i != maksimi]
        paanumerot = [i for i in paanumerot if i != minimi]
    else:
        maksimi = max(tahtinumerot, key=tahtinumerot.count)
        minimi = min(tahtinumerot, key=tahtinumerot.count)
        suosituimmat_tahtinumerot.append(maksimi)
        vahiten_suosituimmat_tahtinumerot.append(minimi)
        tahtinumerot = [i for i in tahtinumerot if i != maksimi]
        tahtinumerot = [i for i in tahtinumerot if i != minimi]
        
print(sorted(suosituin_rivi), suosituimmat_tahtinumerot)
print(sorted(vahiten_suosituin), vahiten_suosituimmat_tahtinumerot)
