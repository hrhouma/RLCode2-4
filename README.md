# 🚗🚗🚗 Projet RLCode2-2 : Impact du Paramètre Alpha dans Q-Learning 🚗🚗🚗

--------------------
# 🎮 Première exécution avec rendu visuel 🎮
--------------------

```bash
git clone https://github.com/hrhouma/RLCode2-2.git
cd RLCode2-2
python3 -m venv mountain_car
mountain_car\Scripts\activate  # Sur Windows
source mountain_car/bin/activate  # Sur macOS/Linux
pip install -r requirements.txt
python main1-pygame-alphas.py  # Première exécution avec rendu visuel
deactivate
```

--------------------
# 📊 Deuxième exécution sans rendu visuel 📊
--------------------

```bash
git clone https://github.com/hrhouma/RLCode2-2.git
cd RLCode2-2
python3 -m venv mountain_car
mountain_car\Scripts\activate  # Sur Windows
source mountain_car/bin/activate  # Sur macOS/Linux
pip install -r requirements.txt
python main2-matlplotlib-alphas.py  # Deuxième exécution sans rendu visuel
deactivate
```

--------------------
# 🔍 Différences clés entre les deux fichiers **`main1-pygame-alphas.py`** et **`main2-matplotlib-alphas.py`** :
--------------------

### 1. **Différence principale : Mode d'affichage pendant la simulation**

#### a) **`main1-pygame-alphas.py`** :
- **🎬 Affichage en temps réel** : Ce script **affiche la simulation en temps réel** avec un rendu graphique de la voiture dans l'environnement **MountainCar-v0** pendant que l'agent prend des décisions. Cela permet de voir la voiture se déplacer dans l'environnement pendant les essais.
- **📺 Fenêtre `gym` rendue** : Utilisation du mode de rendu de **gym** pour visualiser le déplacement de la voiture à chaque étape dans une fenêtre séparée.
- **🤖 Simulation interactive** : Chaque essai se déroule dans un environnement visuel où vous pouvez observer le comportement de l'agent pendant la simulation. Ensuite, à la fin de chaque essai, les résultats sont collectés pour produire des graphiques récapitulatifs.

#### b) **`main2-matplotlib-alphas.py`** :
- **⏩ Simulation sans rendu visuel en temps réel** : Dans ce script, les simulations sont effectuées **sans affichage visuel** pendant les essais. L'agent prend des décisions et l'environnement est mis à jour, mais il n'y a pas de rendu graphique montrant la voiture en mouvement.
- **📊 Affichage à la fin** : Les résultats sont uniquement affichés après la fin de tous les essais sous forme de graphiques. Vous ne voyez pas le comportement de la voiture pendant les simulations.

### 2. **Utilisation de `pygame` dans `main1`**

- **`main1-pygame-alphas.py`** utilise **`pygame`** et **`gym`** pour afficher la simulation en temps réel. Cela permet de voir l'agent agir directement dans l'environnement, ce qui est utile pour des démonstrations interactives où vous souhaitez observer le comportement de l'agent pendant l'apprentissage.
  
- En revanche, **`main2-matplotlib-alphas.py`** n'utilise pas **`pygame`** ou le rendu en temps réel de **gym**. L'accent est mis uniquement sur la collecte des résultats des essais et l'affichage des graphiques une fois que toutes les simulations sont terminées.

### 3. **📈 Affichage graphique des résultats**

- **Dans les deux scripts** : À la fin de la simulation (après les essais), les deux scripts génèrent des graphiques avec **matplotlib** pour résumer les résultats des simulations. Chaque script crée des graphiques montrant :
  - ✅ Le succès ou l'échec de chaque essai en fonction de la valeur d'**alpha**.
  - ⏱️ Le nombre de pas de temps nécessaires pour chaque essai.
  
- **Différence d'implémentation** :
  - **Dans `main1-pygame-alphas.py`**, les graphiques sont générés après avoir observé la simulation en temps réel.
  - **Dans `main2-matplotlib-alphas.py`**, les graphiques sont générés immédiatement après l'exécution des essais, sans observer le processus en direct.

### 4. **🎯 Scénarios d'utilisation**

#### a) **`main1-pygame-alphas.py`** :
- **Idéal pour les démonstrations interactives** où vous souhaitez observer le comportement de l'agent en temps réel pendant l'apprentissage. Vous pouvez voir comment l'agent explore l'environnement et s'améliore au fil du temps.

#### b) **`main2-matplotlib-alphas.py`** :
- **Meilleur pour des simulations rapides** où l'affichage en temps réel n'est pas nécessaire. Cela permet d'exécuter les simulations plus rapidement sans ouvrir des fenêtres graphiques. Il est utile lorsque vous souhaitez simplement analyser les résultats après l'exécution des essais.

### 5. **📝 Conclusion pour les lecteurs** :
- **Si vous voulez observer l'apprentissage de l'agent en temps réel**, utilisez **`main1-pygame-alphas.py`**. Cela est particulièrement utile pour montrer visuellement comment différentes valeurs d'**alpha** affectent le comportement de l'agent dans un environnement interactif.
  
- **Si vous préférez effectuer des simulations rapidement sans affichage en temps réel**, alors **`main2-matplotlib-alphas.py`** est plus approprié. Vous aurez directement les résultats sous forme de graphiques après la simulation.

Cela permet aux utilisateurs de choisir le script qui correspond le mieux à leurs besoins, selon qu'ils souhaitent une démonstration visuelle ou une exécution rapide sans visualisation.


------------------
# Annexe et Interprétation
------------------

![Figure_1](https://github.com/user-attachments/assets/5a7fdb88-634c-4a4d-9284-a804a95000d5)


- Le code génère des visualisations de l'impact de différentes valeurs de **alpha (α)** sur la performance d'agents Q-Learning dans l'environnement **MountainCar-v0**. 
- Il compare les résultats en termes de succès ou d'échecs pour chaque essai, ainsi que le nombre de pas nécessaires pour chaque essai.

---

### **Structure du Code :**

#### 1. **Boucle d'entraînement et évaluation :**
   - Le code entraîne des agents avec trois valeurs de **alpha** : **0.1, 0.5, 0.9**.
   - Pour chaque valeur de **alpha**, l'agent est entraîné sur **2000 épisodes** puis évalué sur **10 essais**.
   - **Résultats des essais** :
     - Le **taux de succès** : Le nombre d'essais où l'agent a atteint son objectif (réussir à gravir la colline en moins de 200 pas).
     - Le **nombre de pas** nécessaires pour atteindre l'objectif ou échouer.
  
#### 2. **Visualisation des résultats :**
   - **Graphiques des succès/échecs** : Pour chaque valeur de **alpha**, un graphique indique si l'agent a réussi (1) ou échoué (0) à chaque essai.
   - **Graphiques des pas de temps** : Un autre graphique montre le nombre de pas nécessaires pour chaque essai. Ces données sont représentées sous forme de courbes rouges.

---

### **Interprétation des graphiques :**

#### **Alpha (α) = 0.1 :**
   - **Graphique des succès (en bleu)** :
     - L'agent a un taux de succès de **70%** (7 réussites sur 10).
     - Cependant, il échoue à certains essais (entre les essais 4 et 6), ce qui suggère que la faible valeur d'**alpha** entraîne un apprentissage plus lent.
   - **Graphique des pas de temps (en rouge)** :
     - Le nombre de pas varie beaucoup, ce qui indique une certaine instabilité dans la performance. Par exemple, à l'essai 4, l'agent a besoin de plus de 220 pas, alors qu'à l'essai 10, il réussit avec beaucoup moins de pas (~140).

#### **Alpha (α) = 0.5 :**
   - **Graphique des succès (en bleu)** :
     - Ici, l'agent a un taux de succès de **100%**. Il réussit tous ses essais, montrant que **α = 0.5** est une valeur qui permet un bon compromis entre exploration et exploitation.
   - **Graphique des pas de temps (en rouge)** :
     - Le nombre de pas est plus stable et tend vers une **moyenne de 150 pas** pour chaque essai, avec moins de fluctuations. Cela suggère que l'agent a appris une politique efficace avec cette valeur d'alpha.

#### **Alpha (α) = 0.9 :**
   - **Graphique des succès (en bleu)** :
     - Comme pour **α = 0.5**, l'agent a un taux de succès de **100%**. Cependant, la performance ne semble pas aussi stable que pour **α = 0.5**.
   - **Graphique des pas de temps (en rouge)** :
     - Les résultats sont moins stables avec **α = 0.9**, avec des variations dans le nombre de pas, bien qu'elles soient moins extrêmes que pour **α = 0.1**. À l'essai 3, l'agent prend plus de pas que lors des autres essais (~148 contre ~142 dans les autres).

---

### **Analyse des résultats :**
- **Alpha faible (0.1)** : L'agent prend plus de temps à apprendre, et son taux de succès est inférieur, bien qu'il parvienne à résoudre certains essais. La performance est instable.
- **Alpha modéré (0.5)** : L'agent réussit tous les essais avec un nombre de pas relativement stable. Cette valeur d'**alpha** semble bien équilibrer exploration et exploitation.
- **Alpha élevé (0.9)** : L'agent réussit également tous les essais, mais avec une performance moins stable, ce qui peut indiquer une exploration excessive.

### **Conclusion pédagogique :**
- Les graphiques montrent que **α = 0.5** semble être la valeur optimale dans cet environnement, offrant un bon compromis entre l'apprentissage rapide et une politique stable. Les valeurs d'alpha trop faibles ou trop élevées entraînent des performances moins stables.

Ces graphiques vous permettent de **visualiser l'effet des différentes valeurs de taux d'apprentissage** et de comprendre comment elles influencent l'apprentissage d'un agent **Q-Learning** dans un environnement simulé.
