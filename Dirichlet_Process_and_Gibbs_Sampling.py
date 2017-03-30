import numpy as np
import math
from random import random
from math import exp

#------------------------------- fonctions nécessaires pour l'échantillonage de Gibbs et le calcul du logarithme de vraisemblance---------------#

def tirage_multinomiale(x):
    a=random()
    b=0
    for i in range (len(x)):
        b=b+x[i]
        if a<b :
            break
    return i


def LikeHood_Log(p,data):
    logv=0
    for i in range (len(data)):
        m=p[2*i]
        s=p[2*i+1]
        logv=logv- 0.5 * math.log(s) - (data[i] - m)**2/(2*s)
    return logv


def maj_of_Params(donne):
    """
        Input:
            - donne : N'xD matrix, with D the dataset size, and N' the number
            of observations of the current cluster
        Output:
            - p is a list of D lists, where D is the ambiant dimension, and
            each of the D element is a two components list composed of
            the mean of the dataset and its standard deviation.
            $[[\mu1, \sigma1], [\mu2, \sigma2], \dots]$
    """
    p=[]
    for a in range (donne.shape[1]):
        m = np.mean(donne[:,a])
        v = np.std(donne[:,a])
        if v==0:
            v=1
        p = p + [m, v]
    return p

    
  #------------------------------------L'algorithme Principale: échantillonage de Gibbs et processus de Dirichlet------------------------------#
  
  
def Dirichlet_vs_Gibbs(data,alpha,iterations):
    """
        data should be a NxD matrix, where N is the number of observations and D is the dataset dimension.
    """
    for e in range (iterations):
        clusters=len(data[:,0])*[0]
        nbrp=[]
        to=[]
        eta=[]
        ab=max(clusters)
        if ab==0:
            ab=1
        for b in range (ab+1):
            nbrp.append(clusters.count(b))
        MaxLikeHood=-float("inf")  
        for c in range (ab):
            for d in range (len(clusters)):
                if clusters[d]==c:
                    to.append(data[d])
            to=np.array(to)
            eta.append(maj_of_Params(to))
        for f in range (len(np.array(data)[:,0])):
            ge=[]
            be=[]
            proba=[]
            nbrp=[]
            ab=max(clusters)
            if ab==0:
                nbrp=[150]
            else :
                for b in range (ab+1):
                    nbrp.append(clusters.count(b))
            nbrp[clusters[f]]=nbrp[clusters[f]]-1
            if nbrp[clusters[f]]==0:
                del eta[f]
                del clusters[f]
                for g in range (len(clusters)-f):
                    clusters[g+f]=clusters[g+f]-1
            else:
                for k in range (len(clusters)):
                       if clusters[k]==clusters[f]:
                           be.append(data[clusters[k]])
                be=np.array(be)
                eta[clusters[f]] = maj_of_Params(be)
            for l in range (len(nbrp)) :
                proba.append(math.log10(nbrp[l]))
            proba.append(math.log10(alpha))
            for m in range (len(nbrp)):
                proba[m]=proba[m]+LikeHood_Log(eta[m],data[m])
            for n in range (len(proba)):
                proba[n]=exp(proba[n]-max(proba))
            probas=np.array(proba)
            probas=probas/sum(probas)
            clusters[f]=tirage_multinomiale(probas)
            nbrp[0]=clusters.count(0)
            ab=max(clusters)
            for b in range (ab,ab+1):
                 nbrp.append(clusters.count(b))
            if max(clusters)<clusters[f]:
                nbrp[clusters[f]]=0
            else:
                nbrp[clusters[f]]=nbrp[clusters[f]]+1
                for q in range(len(clusters)):
                    if clusters[q]==clusters[f]:
                        ge.append(data[clusters[q]])
                ge=np.array(ge)
                eta.append(maj_of_Params(ge))
    if iterations>1:
           v=0
           for r in range(len(np.array(data)[:,0])):
               v=v+LikeHood_Log(eta[clusters[r]],data[r])
           if v>MaxLikeHood:
              MaxLikeHood=v
              LikeHoodClusters=clusters
    else:
        LikeHoodClusters =clusters
    return LikeHoodClusters
    
