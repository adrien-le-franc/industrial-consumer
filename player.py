import numpy as np
import os
from numpy.random import randint

class Player:
    def __init__(self):
        self.dt = 0.5
        self.efficiency=0.95
        self.demand=[]
        self.bill = np.zeros(48) # prix de vente de l'électricité
        self.load= np.zeros(48) # chargement de la batterie (li)
        self.battery_stock = np.zeros(49) #a(t)
        self.capacity = 100
        self.pmax = 100
        self.prices = {"purchase" : [],"sale" : []}
        self.imbalance={"purchase_cover":[], "sale_cover": []}

    def take_decision(self,time):
        
        # TO DO:
        # implement your policy here to return the load charged / discharged in the battery between -pmax and pmax
        # below is a simple example  
            
        if time>24 and time<32:
            if self.prices["purchase"][time-1] < 0.078:
                return +23
            else :
                return +3 
        elif time>12 and time<44:
            if self.prices["purchase"][time-1] < 0.06:
                return +10
            else :
                return -25                    
        else :
            return +20

    def update_battery_stock(self,time,load):
        
        #If the battery isn't enough powerful, the battery load is set to the battery maximum power.

            if abs(load) > self.pmax:
                load = self.pmax*np.sign(load) 
            new_stock = self.battery_stock[time] + (self.efficiency*max(0,load) - 1/self.efficiency * max(0,-load))*self.dt
            
        #If the battery isn't full enough to provide such amount of electricity, 
        #the latter is set to the maximum amount the battery can provide, the load is adjusted.
            
            if new_stock < 0: 
                load = - self.battery_stock[time] / (self.efficiency*self.dt)
                new_stock = 0
    
        #If the amount of electricity purchased outgrows the maximum battery capacity, 
        #enough electricity to fill up the battery is purchased, the load is adjusted.   
    
            elif new_stock > self.capacity:
                load = (self.capacity - self.battery_stock[time]) / (self.efficiency*self.dt)
                new_stock = self.capacity
    
            self.battery_stock[time+1] = new_stock
            
            return load
        
    def compute_load(self,time,demand):
        load_player = self.take_decision(time)
        load_battery=self.update_battery_stock(time,load_player)        
        self.load[time]=load_battery + demand
        
        return self.load[time]
    
    def observe(self, t, demand, price, imbalance):
        self.demand.append(demand)
        
        self.prices["purchase"].append(price["purchase"])
        self.prices["sale"].append(price["sale"])

        self.imbalance["purchase_cover"].append(imbalance["purchase_cover"])
        self.imbalance["sale_cover"].append(imbalance["sale_cover"])
        
    
    def reset(self):
        self.load= np.zeros(48)
        self.bill = np.zeros(48)
        
        last_bat = self.battery_stock[-1]
        self.battery_stock = np.zeros(49)
        self.battery_stock[0] = last_bat
        
        self.demand=[]
        self.prices = {"purchase" : [],"sale" : []}
        self.imbalance={"purchase_cover":[], "sale_cover": []}

