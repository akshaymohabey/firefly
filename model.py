import numpy as np
import matplotlib.pyplot as plt
from plotnine import *
import pandas as pd

from mesa import Agent
from mesa import Model
from mesa.time import SimultaneousActivation
from mesa.space import MultiGrid

class Firefly(Agent):
    def __init__(self, unique_ID,pos, model):
        super._init__(unique_ID,model)
        self.pos = pos
        self.clock = self.random.randint(1,10)

        