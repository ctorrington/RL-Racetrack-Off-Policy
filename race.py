"""Race to a finish line."""

from constants import Constants

ACTIONS = Constants.ACTIONS

def simulate_step(state_space):
    """Simulate the cars velocity on its position"""
    
    x, y, (v_x, v_y), surface = state_space
    
    # Add the current velocity to the current position.
    x += v_x
    y += v_y
    # Update the surface depending on where the agent is.
    surface = state_space

def generate_track_lap_episode(state_space):
    
    simulate_step(state_space)