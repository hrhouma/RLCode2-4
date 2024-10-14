import matplotlib.pyplot as plt
import numpy as np
from QLearning import QLAgent
from helpers import discretize
import gym

######## CONSTANTS ########
EPISODES = 2000
TRIALS = 10
N_STATES = 20 * 20
N_ACTIONS = 3

# Différentes valeurs de alpha à tester
alphas = [0.1, 0.5, 0.9]

# Tableau pour stocker les résultats
results = []

for alpha in alphas:
    env = gym.make('MountainCar-v0', render_mode=None)
    agent = QLAgent(env=env, n_states=N_STATES, n_actions=N_ACTIONS, lr=alpha, discount=0.95)

    # Entraîner l'agent
    agent.learn(episodes=EPISODES)

    # Évaluer l'agent avec rendu en temps réel
    successes = []
    timesteps_per_trial = []
    for tr in range(TRIALS):
        state, _ = env.reset()
        
        # Créer un environnement avec le rendu visuel activé
        env_render = gym.make('MountainCar-v0', render_mode='human')
        state_render, _ = env_render.reset()

        t = 0
        while True:
            env_render.render()  # Affiche la voiture en temps réel
            action = agent.act(discretize(state_render))
            state_render, reward, done, _, info = env_render.step(action)
            t += 1
            if done:
                timesteps_per_trial.append(t)
                successes.append(1 if t < 200 else 0)
                break

        env_render.close()  # Ferme l'environnement une fois terminé

    # Stocker les résultats pour cette valeur de alpha
    results.append((alpha, successes, timesteps_per_trial))
    env.close()

# Visualisation côte à côte
fig, axes = plt.subplots(len(alphas), 2, figsize=(12, 8))

for i, (alpha, successes, timesteps_per_trial) in enumerate(results):
    # Graphique des succès/échecs
    axes[i, 0].plot(range(1, TRIALS + 1), successes, 'bo-')
    axes[i, 0].set_title(f"Succès pour alpha = {alpha}")
    axes[i, 0].set_xlabel('Numéro d\'essai')
    axes[i, 0].set_ylabel('Succès (1) / Échec (0)')
    axes[i, 0].set_ylim(-0.1, 1.1)
    axes[i, 0].grid(True)

    # Graphique des pas de temps par essai
    axes[i, 1].plot(range(1, TRIALS + 1), timesteps_per_trial, 'ro-')
    axes[i, 1].set_title(f"Pas de temps pour alpha = {alpha}")
    axes[i, 1].set_xlabel('Numéro d\'essai')
    axes[i, 1].set_ylabel('Nombre de pas de temps')
    axes[i, 1].grid(True)

    # Ajouter une légende avec les paramètres utilisés
    textstr = f"Alpha utilisé: {alpha}"
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    axes[i, 1].text(0.05, 0.95, textstr, transform=axes[i, 1].transAxes, fontsize=10,
                    verticalalignment='top', bbox=props)

plt.tight_layout()
plt.show()
