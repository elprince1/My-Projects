
#####################  imports  ########################33
import random
import gym
import numpy as np
from collections import deque
from tensorflow.keras.models import Sequential,load_model
from tensorflow.keras.layers import Dense, Activation, Flatten, Conv2D
from tensorflow.keras.optimizers import Adam


# os.environ['CUDA_VISIBLE_DEVICES'] = '-1'


env = gym.make("MsPacman-v0")
a=env.reset()                  # shape (210,160,3)  ## this line not used



state_size = (88, 80, 1)

action_size = env.action_space.n       # 9 actions


color = np.array([210, 164, 74]).mean()   #149.3333334

def preprocess_state(state):
    image = state[1:176:2, ::2]     # cropping image in height only (88,80,3)
    
    
    
    image = image.mean(axis=2)  # (88,80)
        
    
    image[image==color] = 0     # improve contrast
    
    
    image = (image - 128) / 128 - 1     # (88,80)
        
    
    #print(image.shape)
    image = np.expand_dims(image.reshape(88, 80, 1), axis=0)    # (1,88,80,1)
    
    #print(image.shape)
    
    return image




class DQN:
    
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.replay_buffer = deque(maxlen=5000)
        self.gamma = 0.9
        self.epsilon = 0.8
        self.update_rate = 1000
        self.main_network = self.build_network()
        self.target_network = self.build_network()
        self.target_network.set_weights(self.main_network.get_weights())
        
        #self.reget()
    def reget(self):
        self.main_network = load_model('Atari_3.keras')
        self.target_network = self.build_network()
        self.target_network.set_weights(self.main_network.get_weights())
    
    def build_network(self):
        model = Sequential()
        model.add(Conv2D(32, (8, 8), strides=4, padding='same', input_shape=self.state_size))
        model.add(Activation('relu'))
        
        model.add(Conv2D(64, (4, 4), strides=2, padding='same'))
        model.add(Activation('relu'))
        
        model.add(Conv2D(64, (3, 3), strides=1, padding='same'))
        model.add(Activation('relu'))
    
        model.add(Flatten())
    
        model.add(Dense(512, activation='relu'))
        model.add(Dense(self.action_size, activation='linear'))
    
        model.compile(loss='mse', optimizer=Adam())

        return model
    
    def store_transistion(self, state, action,reward, next_state, done):
        self.replay_buffer.append((state, action,reward, next_state, done))
    
    def epsilon_greedy(self, state):
          if random.uniform(0,1) < self.epsilon:
              return np.random.randint(self.action_size)
          Q_values = self.main_network.predict(state)
        
          return np.argmax(Q_values[0]) # [[]]  list inside list
     
    def train(self, batch_size):
        
          minibatch = random.sample(self.replay_buffer, batch_size)  # take number of elements from the replay buffer, this number is batch size
         
          for state, action, reward, next_state, done in minibatch:
             
            if not done:
                target_Q = (reward + self.gamma * np.amax(
                    self.target_network.predict(next_state)))
            else:
                target_Q = reward
                
            Q_values = self.main_network.predict(state)
            
            Q_values[0][action] = target_Q
            
            self.main_network.fit(state, Q_values, epochs=1,verbose=0)

    def update_target_network(self):
        self.target_network.set_weights(self.main_network.get_weights())
        
    def save_network(self,i):
        self.main_network.save(f"Atari_{i}.keras")
    def play_Game(self):
        
        model = load_model('Atari_6.keras')
        
        done = False
        
        state = env.reset()
        env.render()
        
        
        while not done:
            
            action = np.argmax(model.predict(preprocess_state(state))[0])
            
            
            next_state, reward, done, _ = env.step(action)
            
            env.render()
            
            state = next_state
            
        env.close()
            
            
    
    

if __name__=="__main__":
    
    
    
        
    num_episodes = 12
    num_timesteps = 20000
    batch_size = 8
    dqn = DQN(state_size, action_size)
    
    #dqn.play_Game()
    
    done = False
    time_step = 0
    for i in range(num_episodes):
        Return = 0
        
        state = preprocess_state(env.reset())
        
        for t in range(num_timesteps):
            
            print(t,'/',i)
            
            env.render()
            time_step += 1
            
            if time_step % dqn.update_rate == 0:
                dqn.update_target_network()
                
            #print(state.shape)
            action = dqn.epsilon_greedy(state)
            
            #print(env.step(action))
            
            next_state, reward, done, _ = env.step(action)
            
            next_state = preprocess_state(next_state)
            
            
            
            dqn.store_transistion(state, action, reward, next_state, done)
            
            state = next_state
            
            Return += reward
            
            if done:
                print('Episode: ',i, ',' 'Return', Return)
                break
            
            if len(dqn.replay_buffer) > batch_size:
                dqn.train(batch_size)
        dqn.save_network(i+4)
            
            
            
            
            
        
        
        
        
        
        
        
        
        
        