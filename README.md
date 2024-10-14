
# 1. Cloner le projet

Commencez par cloner le projet depuis le dépôt GitHub :

```bash
git clone https://github.com/hrhouma/RLCode2.git
```

Accédez au dossier du projet :

```bash
cd RLCode2
code .
```

# 2. Création de l'environnement virtuel

Créez un environnement virtuel nommé `mountain_car_env` :

```bash
python3 -m venv mountain_car_env
```

# 3. Activation de l'environnement virtuel

Activez l'environnement :

- Sur macOS et Linux :
  ```bash
  source mountain_car_env/bin/activate
  ```

- Sur Windows :
  ```bash
  mountain_car_env\Scripts\activate
  ```

# 4. Installation des dépendances

Installez les packages nécessaires :

```bash
pip install -r requirements.txt
```

# 5. Structure du projet

Le projet est déjà organisé dans le dépôt que vous avez cloné. Il comprend les fichiers suivants :

- `helpers.py`
- `QLearning.py`
- `main.py`

# 6. Exécution du projet

Avec l'environnement virtuel activé, exécutez le fichier `main.py` pour lancer le projet :

```bash
python main.py
```

# 7. Désactivation de l'environnement virtuel

Une fois que vous avez terminé, vous pouvez désactiver l'environnement avec la commande suivante :

```bash
deactivate
```

---------------------------
# Annexe :
---------------------------



## 1. Création de l'environnement virtuel

Ouvrez un terminal et naviguez vers le dossier de votre projet. Créez un environnement virtuel nommé "mountain_car_env" :

```bash
python3 -m venv mountain_car_env
```

## 2. Activation de l'environnement virtuel

Activez l'environnement :

- Sur macOS et Linux :
```bash
source mountain_car_env/bin/activate
```

- Sur Windows :
```bash
mountain_car_env\Scripts\activate
```

## 3. Installation des dépendances

Installez les packages nécessaires :

```bash
pip install numpy pandas gym
```

## 4. Création du fichier requirements.txt

Créez un fichier `requirements.txt` à la racine de votre projet avec le contenu suivant :

```
numpy==1.23.5
pygame
pandas
gym
matplotlib
```

Alternativement, vous pouvez générer ce fichier automatiquement :

```bash
pip freeze > requirements.txt
pip install -r requirements.txt
```

## 5. Structure du projet

Organisez votre projet avec trois fichiers Python :

- `helpers.py`
- `QLearning.py`
- `main.py`


## 6. Exécution du projet

Dans le terminal, avec l'environnement virtuel activé, exécutez :

```bash
python main.py
```

## 7. Désactivation de l'environnement virtuel

Une fois terminé, désactivez l'environnement :

```bash
deactivate
```

## 8. Partage du projet

Pour partager ou reproduire l'environnement sur un autre système :

1. Incluez le fichier `requirements.txt` dans votre projet.
2. L'autre personne peut créer un nouvel environnement virtuel et installer les dépendances avec :

```bash
python3 -m venv mountain_car_env
source mountain_car_env/bin/activate  # ou mountain_car_env\Scripts\activate sur Windows
pip install -r requirements.txt
```

En suivant ces étapes, vous aurez un projet bien structuré, utilisant un environnement virtuel, avec toutes les corrections nécessaires pour faire fonctionner le code de l'agent Q-Learning pour le problème Mountain Car.


