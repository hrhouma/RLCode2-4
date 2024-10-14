----------------
# Objectif: 
----------------

- Nous allons mettre l'accent sur la démonstration de l'impact de alpha (taux d'apprentissage) dans l'algorithme Q-Learning pour le problème Mountain Car. 

----------------
# Démonstration de l'impact du taux d'apprentissage (alpha) dans Q-Learning pour Mountain Car
----------------

- Ce projet vise à illustrer l'effet du taux d'apprentissage (alpha) sur les performances d'un agent Q-Learning dans l'environnement Mountain Car de OpenAI Gym.

----------------
# Prérequis
----------------

- Python 3.7+
- pip

----------------
# Installation
----------------

## 1. Clonez ce dépôt :
   ```
   git clone https://github.com/hrhouma/RLCode2.git
   cd RLCode2
   ```

## 2. Créez un environnement virtuel :
   ```
   python3 -m venv venv
   source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\activate`
   ```

## 3. Installez les dépendances :
   ```
   pip install -r requirements.txt
   ```

# Structure du projet

- `qlearning_agent.py`: Implémentation de l'agent Q-Learning
- `helpers.py`: Fonctions utilitaires pour la discrétisation de l'état
- `experiment.py`: Script pour exécuter les expériences avec différentes valeurs d'alpha
- `visualize_results.py`: Script pour visualiser les résultats des expériences

# Exécution des expériences

Pour exécuter les expériences avec différentes valeurs d'alpha :

```
python3 experiment.py
```

Ce script entraînera des agents avec différentes valeurs d'alpha et sauvegardera les résultats.

# Visualisation des résultats

Pour visualiser les résultats des expériences :

```
python3 visualize_results.py
```

Ce script générera des graphiques montrant l'impact des différentes valeurs d'alpha sur les performances de l'agent.

# Interprétation des résultats

- Un alpha faible (ex: 0.1) entraîne un apprentissage lent mais stable.
- Un alpha élevé (ex: 0.9) permet un apprentissage rapide mais peut conduire à une instabilité.
- Un alpha modéré (ex: 0.5) offre généralement un bon équilibre entre vitesse d'apprentissage et stabilité.

Observez comment les différentes valeurs d'alpha affectent la vitesse de convergence et la performance finale de l'agent.


# 2. qlearning_agent.py :

```python
import numpy as np
from helpers import discretize

class QLearningAgent:
    def __init__(self, env, n_states, n_actions, alpha, gamma, epsilon):
        self.env = env
        self.n_states = n_states
        self.n_actions = n_actions
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = np.zeros((n_states, n_actions))

    def choose_action(self, state):
        if np.random.random() < self.epsilon:
            return self.env.action_space.sample()
        else:
            return np.argmax(self.q_table[state])

    def update(self, state, action, reward, next_state):
        best_next_action = np.argmax(self.q_table[next_state])
        td_target = reward + self.gamma * self.q_table[next_state][best_next_action]
        td_error = td_target - self.q_table[state][action]
        self.q_table[state][action] += self.alpha * td_error

    def train(self, n_episodes):
        rewards_per_episode = []
        for episode in range(n_episodes):
            state = discretize(self.env.reset()[0])
            total_reward = 0
            done = False
            while not done:
                action = self.choose_action(state)
                next_state, reward, done, _, _ = self.env.step(action)
                next_state = discretize(next_state)
                self.update(state, action, reward, next_state)
                state = next_state
                total_reward += reward
            rewards_per_episode.append(total_reward)
        return rewards_per_episode
```

# 3. helpers.py :

```python
import numpy as np
import pandas as pd

N_BINS = 20

position_bins = pd.cut([-1.2, 0.6], bins=N_BINS, retbins=True)[1][1:-1]
velocity_bins = pd.cut([-0.07, 0.07], bins=N_BINS, retbins=True)[1][1:-1]

def build_state(features):
    state_no = 0
    for i, feat in enumerate(features):
        state_no += (N_BINS ** i) * (feat - 1)
    return int(state_no)

def to_bin(value, bins):
    return np.digitize(x=[value], bins=bins)[0]

def discretize(state):
    position, velocity = state
    return build_state([to_bin(position, position_bins),
                        to_bin(velocity, velocity_bins)])
```

# 4. experiment.py :

```python
import gym
import numpy as np
from qlearning_agent import QLearningAgent
import pickle

def run_experiment(alpha, n_episodes=1000):
    env = gym.make('MountainCar-v0')
    agent = QLearningAgent(env, n_states=20*20, n_actions=3, alpha=alpha, gamma=0.99, epsilon=0.1)
    rewards = agent.train(n_episodes)
    env.close()
    return rewards

if __name__ == "__main__":
    alphas = [0.1, 0.3, 0.5, 0.7, 0.9]
    results = {}

    for alpha in alphas:
        print(f"Running experiment with alpha = {alpha}")
        rewards = run_experiment(alpha)
        results[alpha] = rewards

    with open('experiment_results.pkl', 'wb') as f:
        pickle.dump(results, f)

    print("Experiments completed. Results saved in 'experiment_results.pkl'")
```

# 5. visualize_results.py :

```python
import pickle
import matplotlib.pyplot as plt
import numpy as np

def moving_average(data, window_size):
    return np.convolve(data, np.ones(window_size), 'valid') / window_size

def visualize_results():
    with open('experiment_results.pkl', 'rb') as f:
        results = pickle.load(f)

    plt.figure(figsize=(12, 8))
    for alpha, rewards in results.items():
        smoothed_rewards = moving_average(rewards, 50)
        plt.plot(smoothed_rewards, label=f'α = {alpha}')

    plt.xlabel('Episodes')
    plt.ylabel('Average Reward (Moving Average)')
    plt.title('Impact of Learning Rate (α) on Q-Learning Performance')
    plt.legend()
    plt.grid(True)
    plt.savefig('learning_rate_impact.png')
    plt.show()

if __name__ == "__main__":
    visualize_results()
```

# 6. requirements.txt :

```
numpy==1.23.5
pygame
pandas
gym
matplotlib
```

Pour exécuter cette démonstration :

1. Assurez-vous d'avoir installé toutes les dépendances listées dans `requirements.txt`.
2. Exécutez `experiment.py` pour lancer les expériences avec différentes valeurs d'alpha.
3. Une fois les expériences terminées, exécutez `visualize_results.py` pour générer un graphique montrant l'impact des différentes valeurs d'alpha.

- Cette structure permet une démonstration claire de l'impact du taux d'apprentissage (alpha) sur les performances de l'agent Q-Learning dans l'environnement Mountain Car. 
- Vous puvez observer comment différentes valeurs d'alpha affectent la vitesse d'apprentissage et la performance finale de l'agent.
