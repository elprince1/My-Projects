
import numpy as np

#----------------------------dies models-----------------------
class FairDie():
    def __init__(self):
        self.values = np.array([i for i in range(1,7)])
        self.probs = np.array([1/6]*6)
        
    def sample(self):
        samples = np.random.choice(self.values, size=1, p=self.probs)
        return samples[0]
    
class UnFairDie():
    def __init__(self):
        self.values = np.array([i for i in range(1,7)])
        self.probs = [0.5,0.1,0.1,0.1,0.1,0.1]
        
    def sample(self):
        samples = np.random.choice(self.values, size=1, p=self.probs)
        return samples[0]
#--------------------------------------------------------------
    
#---------------------------fair die---------------------------
## for fair die and P(x) is known
x=np.array([i for i in range(1,7)])
p_x = np.array([1/6]*6)

E_X1 = np.sum(np.multiply(x,p_x))
print(f"For fair die: E(x): {E_X1} with known P_X")

## for an fair die (By sampling)
fairDie = FairDie()
N_samples = 1000
sum_samples = 0
for i in range(N_samples):
    sum_samples+=fairDie.sample()
    
E_X2 = sum_samples/N_samples
print(f"For fair die: E(x): {E_X2} with known P_X")
#--------------------------------------------------------------


#---------------------------unfair die-------------------------
## for an unfair die (By sampling we don't know p(x))
unfairDie = UnFairDie()
N_samples = 1000
sum_samples = 0
for i in range(N_samples):
    sum_samples+=unfairDie.sample()
    
E_X3 = sum_samples/N_samples
print(f"For unfair die: E(x): {E_X3} with known P_X")

## to check
x=np.array([i for i in range(1,7)])
p_x = np.array([0.5,0.1,0.1,0.1,0.1,0.1])

E_X4 = np.sum(np.multiply(x,p_x))
print(f"For unfair die: E(x): {E_X4} with known P_X")
#--------------------------------------------------------------




