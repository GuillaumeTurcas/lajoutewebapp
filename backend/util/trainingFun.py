import random

def trainingFun(sujets, equipe, equ):
    nb_sujets = len(sujets)
    ch_rand = random.randint(0, nb_sujets - 1)

    sujet = str(sujets[ch_rand][1])

    simul = ""

    if equipe :
        equip1 = equ["equipe1"]
        equip2 = equ["equipe2"]

        equipe = [equip1, equip2]
        repart = random.randint(0, 1)
        simul = f"Positive : {equipe[repart]} | Négative : {equipe[(repart+1)%2]}"

    return sujet, simul
