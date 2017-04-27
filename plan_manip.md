# Plan d'expériences

## Paramètres

$N_obs$ -> nombre d'observations
$N_iter$ -> nombre d'itérations


## Conseils

Ce sont des manips qui sont longues, donc ne pas effacer les données après avoir fini.
A chaque run de l'algorithme, sauvegarder tout (K^(t)), $#c_1^(t), $\alpha^{(t)}$.







## Manip 1

On fixe $\alpha = 1$, on prend Nobs = [100 500 1000 5000 1000].
On l'algo pour chaque valeur de Nobs -> 10000 itérations.
Pour chaque valeur de N, on récupère une chaîne $K^{N, it}$.
On trace les histogrammes associés.








## Manip 2

On ne fixe plus $\alpha$.
On choisit une prior sur $\alpha$.
On choisit une loi Gamma 
$$ p(\alpha; a, b) \propto \alpha^{a-1} exp(-\alpha / b) $$
a -> très petit $10^{-3}$
b -> très grand $10^{3}$.

Pour info $\alpha | y \sim /Gamma(a + K, b + 1 / (\sum_{i=1}^N 1 /i) )$.

On prend N = [100 500 1000 5000 1000].
On l'algo pour chaque valeur de N -> 10000 itérations.
Pour chaque valeur de N, on récupère une chaîne $K^{N, it}$.
On trace les histogrammes associés.

+rajouter les histogrammes sur $\alpha$.







## Manip 3

On reprend la manip 1.
On prend deux valeurs de $\alpha$ -> $\alpha1 > D / 2$ et $\alpha2 < D / 2$.

1. On refait les histogrammes sur K.
2. On estime pour chaque valeur de N la taille des clusters.
On classe les clusters par tailles.
Tu obtient une chaine $#c_1^{n_iter} / Nobs, $#c_2^{n_iter} Nobs$....
Pour chaque valeur de Nobs, tu traces les histogrammes.
