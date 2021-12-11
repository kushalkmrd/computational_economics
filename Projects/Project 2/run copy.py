# Computational Economics, Chapman University Fall 2021
# Instructor: Dr. Ryan French
##Project 2
# Author: Kushal Kumar Reddy
# kreddy@chapman.edu


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

class Agent:
    """An Agent Class representing Each Agent, it has 3 parameters"""
    def __init__(self, model):
        self.model = model
        self.is_alive = 0
        self.x = 0
        self.y = 0

class Model:
    """Model Class representing the Model layout to store the Grid, Agents and Update them each period"""

    # Initialisation Function
    def __init__(self):
        self.agents = {}  # Agents Dictionary
        self.locations = {} # Locations of the grid
        self.is_alive=[]  # Array to note the status of each Agent

    # Function to add agents and setup, with an option for Four Agents in Four Corners
    def add_agents(self, n,p,is_4=0):
        # Idea is to call each agent and loop them to place in grid one by one
        self.agent_count=n
        for i in range(n):
            for j in range(n):
                agent = Agent(self)
                if is_4:
                    if (i==n-1 and j==n-1) or (i==n-1 and j==0) or (i==0 and j==n-1) or (i==0 and j==0)  :
                        agent.is_alive = 1
                elif random.random() < p:
                    agent.is_alive = 1
                (agent.x, agent.y)=(i,j)
                pos = (agent.x, agent.y)
                self.agents[pos] = agent
        self.is_alive = self.alive_agents()

    # Function to obtain the neighbors of a cell, gets the reflected neighbors as well
    def get_neighbors(self,pos):
        #Set up the delta function and loop through it to get the neighbors, using a mod function
        adj = {(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)}
        li = []
        x, y = pos
        n = self.agent_count
        for dy, dx in adj:
                li.append(((x + dx)%n, (y + dy)%n))
        alive=0
        for posn in li:
            if self.agents[posn].is_alive:
                alive+=1
        return alive

    # Function to update agents each timestep
    def update_agents(self):
        #Get the agent status, and then use the rules to update them
        current_agents = {}
        agentscopy=self.agents.items()
        alive_dict={}
        for pos, agent in agentscopy:
            alive_dict[pos]=self.get_neighbors(pos)
        for pos, agent in agentscopy:
            alive=alive_dict[pos]
            if alive==3:
                agent.is_alive=1
            elif alive>3:
                agent.is_alive=0
            elif alive<2:
                agent.is_alive=0
            current_agents[pos]=agent
        self.agents = current_agents
        agents_alive=[]
        for pos, agent in current_agents.items():
            agents_alive.append(agent.is_alive)
        self.is_alive =agents_alive

    def alive_agents(self):
        agents_alive = []
        for pos, agent in self.agents.items():            
            agents_alive.append(agent.is_alive)
        return agents_alive

if __name__ == "__main__":
    # Function to return the array each time step for plotting
    def runmodel_func(model,timesteps):
        n = 50
        model.add_agents(n, 0.1)
        positions=[np.array(model.is_alive).reshape(n, n)]
        for i in range(timesteps):
            model.update_agents()
            positions.append(np.array(model.is_alive).reshape(n, n))
        return positions

    model = Model()
    # To run 100 steps get the FPS and Seconds, for 100 frames
    fps = 5
    Seconds = 25
    fig = plt.figure(figsize=(8, 8))
    plt.title("Conway's Game of Life", fontsize=20)
    snapshots = runmodel_func(model, fps * Seconds)
    a = snapshots[0]
    im = plt.imshow(a, interpolation='none', aspect='auto', vmin=0, vmax=1)
    def animation_func(i):
        im.set_array(snapshots[i])
        return [im]
    anim = animation.FuncAnimation(fig,animation_func,frames = Seconds * fps,blit=True)
    writergif = animation.PillowWriter(fps=fps)
    anim.save('game_of_life_50by50.gif',writer=writergif)
    plt.show()


# Uncomment In case to plot the figures in the Matplotlib without animation
# if __name__ == "__main__":
#     model = Model()
#     n=30
#     model.add_agents(n, 0.55)
#     timesteps = 100
#
#     for i in range(timesteps):
#         #model.add_agents(10,0.5)
#         positions = np.array(model.is_alive).reshape(n,n)
#         fig, ax = plt.subplots()
#         img = ax.imshow(positions, interpolation='nearest')
#         model.update_agents()
#         plt.pause(1e-6)
#     plt.show()
# Get the funciton and run it
