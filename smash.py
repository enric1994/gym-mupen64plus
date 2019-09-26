#!/bin/python
import gym, gym_mupen64plus
import subprocess

def startVNC(display):
    subprocess.call("x11vnc -display :{} -localhost -forever -viewonly &".format(str(display)), shell=True)

def main():
    env = gym.make('Smash-mario-v0')
    env.reset()
    startVNC(1)
    # env.render()
    for i in range(10000):
        # Taunt.
        (obs, rew, end, info) = env.step([0, 0, 0, 0, 0, 1, 0, 0])
        (obs, rew, end, info) = env.step([0, 0, 0, 0, 0, 0, 0, 0])
        # env.render()

    raw_input("Press <enter> to exit... ")

    env.close()

if __name__ == "__main__":
    main()