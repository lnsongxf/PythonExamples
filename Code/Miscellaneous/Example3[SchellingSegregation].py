#==============================================================================
# purpose: Python implementation of Schelling's segregation model
# https://www.binpress.com/tutorial/introduction-to-agentbased-models-an-implementation-of-schelling-model-in-python/144
# author: tirthankar chakravarty
# created: 23rd march 2015
# revised:
# comments:
# 1. Why is the set of agents empty despite a call to populate()?
#==============================================================================
#! bin/python2.7
import matplotlib.pyplot as plt
import itertools
import random
import copy
import os

plt.ioff()

#====================================================================
# class: Schelling
#====================================================================
class Schelling:
    def __init__(self, width, height, empty_ratio, similarity_threshold, n_iterations, races = 2):
        # Q: do we have to individually unpack all the arguments into the class data members?
        self.width = width
        self.height = height
        self.empty_ratio = empty_ratio
        self.similarity_threshold = similarity_threshold
        self.n_iterations = n_iterations
        self.empty_houses = []
        self.agents = {}
        self.races = races
        self.sim_coeff = []

    def populate(self):
        """This method is used at the start of the simulation. It automatically
         distributed people along a grid.
        """
        # create a grid of houses to populate
        self.all_houses = list(itertools.product(range(self.height), range(self.width)))
        random.shuffle(self.all_houses)  # in-place shuffle

        # set empty & occupied houses
        self.n_empty = int(self.empty_ratio * len(self.all_houses))
        self.empty_houses = self.all_houses[:self.n_empty]
        self.remaining_houses = self.all_houses[self.n_empty:]

        houses_by_race = [self.remaining_houses[i::self.races] for i in range(self.races)]
        for i in range(self.races):
            # the dict produces a dict where the key is house number and value is race
            # Q: why are we adding self.agents.items()
            self.agents = dict(self.agents.items() + dict(zip(houses_by_race[i], [i+1]*len(houses_by_race[i]))).items())

    def is_unsatisfied(self, x, y):
        race = self.agents[(x,y)]
        count_similar = 0
        count_different = 0

        if x > 0 and y > 0 and (x-1, y-1) not in self.empty_houses:
            if self.agents[(x-1, y-1)] == race:
                count_similar += 1
            else:
                count_different += 1

        if y > 0 and (x,y-1) not in self.empty_houses:
            if self.agents[(x,y-1)] == race:
                count_similar += 1
            else:
                count_different += 1

        if x < (self.width-1) and y > 0 and (x+1,y-1) not in self.empty_houses:
            if self.agents[(x+1,y-1)] == race:
                count_similar += 1
            else:
                count_different += 1

        if x > 0 and (x-1,y) not in self.empty_houses:
            if self.agents[(x-1,y)] == race:
                count_similar += 1
            else:
                count_different += 1

        if x < (self.width-1) and (x+1,y) not in self.empty_houses:
            if self.agents[(x+1,y)] == race:
                count_similar += 1
            else:
                count_different += 1

        if x > 0 and y < (self.height-1) and (x-1,y+1) not in self.empty_houses:
            if self.agents[(x-1,y+1)] == race:
                count_similar += 1
            else:
                count_different += 1

        if x > 0 and y < (self.height-1) and (x,y+1) not in self.empty_houses:
            if self.agents[(x,y+1)] == race:
                count_similar += 1
            else:
                count_different += 1

        if x < (self.width-1) and y < (self.height-1) and (x+1,y+1) not in self.empty_houses:
            if self.agents[(x+1,y+1)] == race:
                count_similar += 1
            else:
                count_different += 1

        if (count_similar+count_different) == 0:
            return False
        else:
            return float(count_similar)/(count_similar+count_different) < self.similarity_threshold


    def update(self):
        for i in range(self.n_iterations):
            self.old_agents = copy.deepcopy(self.agents)
            n_changes = 0
            for agent in self.old_agents:
                if self.is_unsatisfied(agent[0], agent[1]):
                    agent_race = self.agents[agent]
                    empty_house = random.choice(self.empty_houses)
                    self.agents[empty_house] = agent_race
                    del self.agents[agent]
                    self.empty_houses.remove(empty_house)
                    self.empty_houses.append(agent)
                    n_changes += 1
            print(n_changes)
            if i % 10 == 0:
                sim_coeff = self.calculate_similarity()
                self.plot('Schelling Model with 2 colors: Iteration '+ str(i) +
                          ' (Similarity coefficient: '+ str(round(sim_coeff, 4)) +  ')',
                          os.path.abspath("Results/schelling_2_80_iteration_" + str(i) + '.png'))
            self.sim_coeff.append(sim_coeff)
            if n_changes == 0:
                break

    def move_to_empty(self, x, y):
        race = self.agents[(x,y)]
        empty_house = random.choice(self.empty_houses)
        self.agents[empty_house] = race
        del self.agents[(x, y)]
        self.empty_houses.remove(empty_house)
        self.empty_houses.append((x, y))

    def plot(self, title, file_name):
        fig, ax = plt.subplots()
        #If you want to run the simulation with more than 7 colors, you should set agent_colors accordingly
        agent_colors = {1:'b', 2:'r', 3:'g', 4:'c', 5:'m', 6:'y', 7:'k'}
        for agent in self.agents:
            ax.scatter(agent[0]+0.5, agent[1]+0.5, color=agent_colors[self.agents[agent]])

        ax.set_title(title, fontsize=10, fontweight='bold')
        ax.set_xlim([0, self.width])
        ax.set_ylim([0, self.height])
        ax.set_xticks([])
        ax.set_yticks([])
        plt.savefig(file_name)
        plt.close()

    def calculate_similarity(self):
        similarity = []
        for agent in self.agents:
            count_similar = 0
            count_different = 0
            x = agent[0]
            y = agent[1]
            race = self.agents[(x,y)]
            if x > 0 and y > 0 and (x-1, y-1) not in self.empty_houses:
                if self.agents[(x-1, y-1)] == race:
                    count_similar += 1
                else:
                    count_different += 1
            if y > 0 and (x,y-1) not in self.empty_houses:
                if self.agents[(x,y-1)] == race:
                    count_similar += 1
                else:
                    count_different += 1
            if x < (self.width-1) and y > 0 and (x+1,y-1) not in self.empty_houses:
                if self.agents[(x+1,y-1)] == race:
                    count_similar += 1
                else:
                    count_different += 1
            if x > 0 and (x-1,y) not in self.empty_houses:
                if self.agents[(x-1,y)] == race:
                    count_similar += 1
                else:
                    count_different += 1
            if x < (self.width-1) and (x+1,y) not in self.empty_houses:
                if self.agents[(x+1,y)] == race:
                    count_similar += 1
                else:
                    count_different += 1
            if x > 0 and y < (self.height-1) and (x-1,y+1) not in self.empty_houses:
                if self.agents[(x-1,y+1)] == race:
                    count_similar += 1
                else:
                    count_different += 1
            if x > 0 and y < (self.height-1) and (x,y+1) not in self.empty_houses:
                if self.agents[(x,y+1)] == race:
                    count_similar += 1
                else:
                    count_different += 1
            if x < (self.width-1) and y < (self.height-1) and (x+1,y+1) not in self.empty_houses:
                if self.agents[(x+1,y+1)] == race:
                    count_similar += 1
                else:
                    count_different += 1
            try:
                similarity.append(float(count_similar)/(count_similar+count_different))
            except:
                similarity.append(1)
        return sum(similarity)/len(similarity)

# ================================================
# initial & final states
# ================================================
schelling_1 = Schelling(50, 50, 0.3, 0.8, 500, 2)
schelling_1.populate()
schelling_1.plot('Schelling Model with 2 colors: Initial State',
                 os.path.abspath("Results/schelling_2_80_initial.png"))
schelling_1.update()
schelling_1.plot('Schelling Model with 2 colors: Final State with Similarity Threshold 20%',
                 os.path.abspath("Results/schelling_2_80_final.png"))
plt.close("all")

# ================================================
# similarity coefficient over time
# ================================================
fig_schelling = plt.figure(facecolor='white')
plt.title('Degree of segregation over time')
plt.ylabel("Similarity coefficient")
plt.xlabel("Iteration")
plt.plot(schelling_1.sim_coeff, 'ro-')
plt.savefig(os.path.abspath("Results/SimCoeffPlot.png"), facecolor=fig_schelling.get_facecolor())
plt.close(fig_schelling)

# END #