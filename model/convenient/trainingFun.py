import random

def trainingFun(sujets, equipe, equ):
    i = len(sujets)
    c = random.randint(0, i-1)
    sujet = str(sujets[c][1])
    simul = ""

    if equipe :
        equip1 = equ["equipe1"]
        equip2 = equ["equipe2"]

        eq = [equip1, equip2]
        c = random.randint(0, 1)
        simul = f"Positive : {eq[c]} | Négative : {eq[(c+1)%2]}"

    return sujet, simul
