from gymnasium.envs.registration import register
import os

resource_dir = os.path.dirname(os.path.realpath(__file__)) + '/'

register(
     id="asteroidsenv/Asteroids-features-v0",
     entry_point="asteroidsenv.env:AsteroidsEnv",
     kwargs={
          "obs_type": "features"
     }
)

register(
     id="asteroidsenv/Asteroids-pixels-v0",
     entry_point="asteroidsenv.env:AsteroidsEnv",
     kwargs={
          "obs_type": "pixels"
     }
)
