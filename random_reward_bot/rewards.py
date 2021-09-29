from typing import Dict

import random

import yaml

P_REWARD = 0.4

def get_reward(win_type_nm: str) -> str:

    random_nb = random.random()
    no_reward = True if random_nb < (1 - P_REWARD) else False

    if no_reward:
        reward = 'No reward'
    else:
        rewards = load_rewards()[win_type_nm]
        reward = random.choice(rewards)
    
    return reward


def load_rewards() -> Dict:

    with open('./rewards.yaml', 'r') as f:
        rewards = yaml.load(f, Loader=yaml.FullLoader)

    return rewards

