import gymnasium as gym
from gym import Wrapper
from play import play
import json
import numpy as np
import os
from datetime import datetime

# Function to generate timestamped folder name
def get_timestamped_foldername():
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    return f"./logs/videos_{timestamp}/"

# Create environment and set up video recording
env = gym.make("Alien-v4", render_mode="rgb_array")
video_folder = get_timestamped_foldername()
env = gym.wrappers.RecordVideo(env=env, video_folder=video_folder, episode_trigger=lambda e: True)

# Reset environment and start playing
env.reset()
play(env, zoom=4, log_dir=video_folder)

# Close environment after playing
env.close()