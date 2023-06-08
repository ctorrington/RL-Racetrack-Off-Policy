# Dependancies.
import numpy as np
import matplotlib.pyplot as plt

# Libraries
import random

from constants import Constants

class Racetrack:
    """Racetrack environment."""
    
    def __init__(self):
        """Initialise the environment."""
        
        self.SURFACES = Constants.SURFACES
        
        # Setting the dimensions for the environment.
        self.x_range = range(0, 10)
        self.y_range = range(0, 10)
        self.state_space = {}
        
        for x in self.x_range:
            for y in self.y_range:
                state = (x, y, random.choice(self.SURFACES.as_tuple()))
                
                # State values.
                self.state_space[state] = {
                    "state actions": {},
                    "policies": {},
                    "estimated return": 0,
                    "state entries": 0,
                }
                
                # State actions.
    
    def plot_track(self):
        """Plot the track."""
        
        surfaces = np.zeros((len(self.x_range), len(self.y_range)))
        for state in self.state_space:
            x, y, surface = state
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