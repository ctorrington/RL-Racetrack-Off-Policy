# Dependancies.
import numpy as np
import matplotlib.pyplot as plt
# import noise

# Libraries
import random

from constants import Constants

class Racetrack:
    """Racetrack environment."""
    
    def __init__(self):
        """Initialise the environment."""
        
        self.SURFACES = Constants.SURFACES
        self.ACTIONS = Constants.ACTIONS
        
        # Setting the dimensions for the environment.
        self.x_range = range(0, 20)
        self.y_range = range(0, 20)
        self.state_space = {}
        self.maximum_velocity = 5
        self.start_line = [[x, 0] for x in self.x_range]
        self.finish_line = [[x, len(self.y_range)] for x in self.x_range]
        self.environment = {
            self.SURFACES.TRACK: [],
            self.SURFACES.GRAVEL: [],
        }
        
        state_counter = 0
        for x in self.x_range:
            for y in self.y_range:
                if random.randint(0, 1) == 0:
                    self.environment[self.SURFACES.TRACK].append((x, y))
                else:
                    self.environment[self.SURFACES.GRAVEL].append((x, y))
                for v_x in range(self.maximum_velocity):
                    for v_y in range(self.maximum_velocity):
                        state = (x, y, (v_x, v_y))
                        
                        # State values.
                        self.state_space[state] = {
                            "actions": {},
                            "policies": {},
                            "estimated return": 0,
                            "state entries": 0,
                        }
                        
                        # State actions.
                        for action in self.ACTIONS.as_tuple():
                            self.state_space[state]["actions"][action] = {
                                "value": 0,
                                "cumulative weight": 0,
                            }
                            
                        # State policy.
                        self.state_space[state]["policies"] = {
                            "target": 0,
                            "behaviour": random.choice(self.ACTIONS.as_tuple()),
                        }
                            
                        state_counter += 1
                        
        print(f"Generated a field of size {len(self.x_range)} by {len(self.y_range)}.")
        print(f"Created {state_counter} states.")
    
    def generate_race_track(self):
        """Generate the race track."""
        
        scale = 100.0
        octaves = 6
        persistence = 0.5
        lacunarity = 2.0
        
        track = np.zeros((self.x_range, self.y_range))
        
        for x in range(self.x_range):
            for y in range(self.y_range):
                track[x][y] = noise.pnoise2(x / scale,
                                            y / scale,
                                            octaves=octaves,
                                            persistence=persistence,
                                            lacunarity=lacunarity,
                                            repeatx=self.x_range,
                                            repeaty=self.y_range,
                                            base=0)
                
        plt.show(track, cmap="viridis")
        plt.show()
        
    
    def plot_track(self):
        """Plot the track."""
        print(self.environment[self.SURFACES.GRAVEL])
        
        surface = np.zeros((len(self.x_range), len(self.y_range)))
        for state in self.environment[self.SURFACES.TRACK]:
            x, y = state
            surface[x][y] = 1
        
        plt.imshow(surface, cmap="viridis", origin="lower")
        plt.show()
        
    def estimate_value_function(self):
        """Estimate the value function under the policy."""
        
        maximum_number_of_episodes = 1000000
        gamma = 1
        
        print(f"Estimating the value function.")
        print(f"Computing {maximum_number_of_episodes} episodes with gamma {gamma}.")
        
        for episode_counter in range(maximum_number_of_episodes):
            episode = generate_track_lap_episode(self.state_space)
        

if __name__ == "__main__":
    vroom_vroom_beep_beep = Racetrack()
    vroom_vroom_beep_beep.plot_track()
