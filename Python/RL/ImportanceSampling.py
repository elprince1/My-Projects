
import numpy as np

class GridWorldEnv():
    def __init__(self,policy):
        self.p0_s = {"A":0.5,"D":0.3,"E":0.2}
        self.policy = policy
        self.episodes = {"A":{"Right":{"episode":"AB","return":-1},
                               "Down":{"episode":"ADEFI","return":5},
                               "Up":{},
                               "Left":{}},
                         "D":{"Right":{"episode":"DEFI","return":4},
                               "Down":{},
                               "Up":{},
                               "Left":{}},
                         "E":{"Right":{"episode":"EFI","return":3},
                               "Down":{},
                               "Up":{},
                               "Left":{}}}
        
    def sample(self):
        init_states = list(self.p0_s.keys())
        init_probs = list(self.p0_s.values())
        
        init_state = np.random.choice(init_states, size=1, p=init_probs)[0]
        episodes = self.episodes[init_state]
        
        actions = list(self.policy[init_state].keys())
        actions_prob = list(self.policy[init_state].values())
        action = np.random.choice(actions, size=1, p=actions_prob)[0]
        
        episode = episodes[action]
        episode['action'] = str(action)
        return episode
        
        
#-------------------------- old policy --------------------
old_policy = {"A":{"Left":0,"Right":0.3,"Up":0,"Down":0.7},
              "D":{"Left":0,"Right":1,"Up":0,"Down":0},
              "E":{"Left":0,"Right":1,"Up":0,"Down":0},
              "F":{"Left":0,"Right":0,"Up":0,"Down":1}}

env = GridWorldEnv(old_policy)
N = 1000
sum_samples=0
old_samples = []
for i in range(N):
    episode = env.sample()
    sum_samples+=episode['return']
    old_samples.append(episode)
    
E_X = sum_samples/N
print(f"J of the old policy: {E_X}")
#---------------------------------------------------------- 


#-------------------------- new policy --------------------
new_policy = {"A":{"Left":0,"Right":0.2,"Up":0,"Down":0.8},
              "D":{"Left":0,"Right":1,"Up":0,"Down":0},
              "E":{"Left":0,"Right":1,"Up":0,"Down":0},
              "F":{"Left":0,"Right":0,"Up":0,"Down":1}}

# env = GridWorldEnv(new_policy)
# N = 1000
# sum_samples=0
# for i in range(N):
#     episode = env.sample()
#     sum_samples+=episode['return']
    
# E_X = sum_samples/N
# print(f"J of the new policy: {E_X}")
#---------------------------------------------------------- 


#------------------- using importance sampling ------------
sum_samples=0
N_samples = len(old_samples)
for episode in old_samples:
    init_state = episode['episode'][0]
    action = episode['action']
    sum_samples+=episode['return']*(new_policy[init_state][action]/
                                    old_policy[init_state][action])
    
E_X = sum_samples/N
print(f"J of the new policy: {E_X}")
    






