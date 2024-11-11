import random
cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_ade_ghicit = random.choice(cuvinte)
progres = ["for _ in cuvant_de_ghicit"]
incercari_ramase = 6
litere_incercate = []
e = 0
print(f'cuvantul:{" ".join(progres)}')
while incercari_ramase > 0:
    litera =input('Introduceti o litera: ')
    if len(litera) != 1 or not litera.isalpha():
        print('Introduceti o litera valida!')
        continue
    if litera in litere_incercate:
        print('Ati incercat deja aceasta litera!')
        continue
    litere_incercate.append(litera)
    for e in range(len(cuvant_de_ghicit)):
        if cuvant_de_ghicit[e] == litera:
            progres[e] = cuvant_de_ghicit[e]
        e += 1
    print(" ".join(progres))
    if litera not in cuvant_de_ghicit:
        incercari_ramase -= 1
    print(f'incercari ramase:{incercari_ramase}')
    print(f'litere incercate:{litere_incercate}')
    if " ".join(progres) == " ".join(cuvant_de_ghicit):
            break
if incercari_ramase > 0:
    print('Felicitări! Ai ghicit cuvântul!')
else:
    print(f'Ai pierdut! Cuvântul era: {cuvant_de_ghicit}')