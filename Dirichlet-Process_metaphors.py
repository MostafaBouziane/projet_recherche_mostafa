from random import * 
from scipy.stats import beta


def chinese_restaurant_process(nbClient, alpha):
    numero_table = [1]
    prochaine_table_vide = 2
    if nbClient <= 0 :
        return [] 
    for i in range (nbClient-1):
        if random()< alpha/(alpha + i+1):
            numero_table.append(prochaine_table_vide)
            prochaine_table_vide = prochaine_table_vide + 1
            print(numero_table)
        else:
            choisir_table = choice(numero_table)
            numero_table.append(choisir_table)  
            print(numero_table)
    return numero_table
    
    
def Black_MacQueen_urn_Scheme(nbrBalls,alpha):
    if nbrBalls<=0:
        return []
    balls_dans_urne=[0.5]
    for i in range (nbrBalls-1):
        if random()<alpha/(alpha+i):
            balls_dans_urne.append(scipy.stats.norm.pdf(i,0,1))
            print(balls_dans_urne)
        else:
            choisir_ball=choice(balls_dans_urne)
            balls_dans_urne.append(choisir_ball)
            print(balls_dans_urne)
    return balls_dans_urne
    

def Stick_breaking(nbrsSticks,alpha):
    a=1
    weights=[a]
    betas = beta.rvs(1, alpha,size=nbrsSticks)
    for i in range(nbrsSticks-1):
        for j in range(i+1):
            a=a*(1-betas[j+1])
        a=a*betas[i]
        weights.append(a)
    return weights
