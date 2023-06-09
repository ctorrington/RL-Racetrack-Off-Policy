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
        
        state_counter = 0
        for x in self.x_range:
            for y in self.y_range:
                for v_x in range(self.maximum_velocity):
                    for v_y in range(self.maximum_velocity):
                        state = (x, y, (v_x, v_y), random.choice(self.SURFACES.as_tuple()))
                        
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
        
        surfaces = np.zeros((len(self.x_range), len(self.y_range)))
        for state in self.state_space:
            x, y, (vx, vy), surface = state
            if surface == self.SURFACES.TRACK:
                surface = 1
            else:
                surface = 0
                
            surfaces[x, y] = surface
        
        plt.imshow(surfaces, cmap="viridis", origin="lower")
        plt.show()
        

if __name__ == "__main__":
    vroom_vroom_beep_beep = Racetrack()
    vroom_vroom_beep_beep.plot_track()
