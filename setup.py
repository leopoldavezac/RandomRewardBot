from setuptools import setup

with open('requirements.txt') as f:
    requirement_strs = f.read().splitlines()

setup(
    name='random_reward_bot',
    version='1.0',
    description = "a bot to administrate random rewards",
    url = "https://github.com/leopoldavezac/RandomRewardBot",
    author = "Leopold Davezac",
    author_email = "leopoldavezac@gmail.com",
    license = "MIT",
    packages=["random_reward_bot"],
    install_requires = requirement_strs,
    python_requires = ">=3"
)
