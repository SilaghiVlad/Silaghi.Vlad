meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]
tavi = ["tava"] * 7
istoric_comenzi = []
papanasi = comenzi.count('papanasi')
ceafa = comenzi.count('ceafa')
guias = comenzi.count('guias')
portie_papanasi = meniu.count('papanasi') - comenzi.count('papanasi')
portie_ceafa = meniu.count('ceafa') - comenzi.count('ceafa')
portie_guias = meniu.count('guias') - comenzi.count('guias')
i = 0
for i in range(len(studenti)):
    print(studenti[0]  + ' a comandat ' + comenzi[0])
    istoric_comenzi.append([studenti[0],comenzi[0]])
    studenti.pop(0)
    comenzi.pop(0)
    tavi.pop()
    i += 1
print('sau comandat',guias,'guias,',ceafa,'ceafa,',papanasi,'papnasi')
print('Mai sunt',len(tavi),'tavi')
print('Mai este ceafa:',portie_ceafa != 0)
print('Mai este papanasi:',portie_papanasi != 0)
print('Mai este guias',portie_guias != 0)
print(papanasi*7+ceafa*10+guias*5)
i = 0
print(f"Produse care costa cel mut 7 lei: {[pret for pret in preturi if pret[1]<=7]}")