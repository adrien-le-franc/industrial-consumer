# python 3

from player import Player
import random as rd
rd.seed()


industrial_consumer = Player()

for t in range(48):
    demand = rd.random()*100
    load = industrial_consumer.compute_load(t, demand)
    assert industrial_consumer.battery_stock[t] >= 0
    assert industrial_consumer.battery_stock[t] <= industrial_consumer.capacity
    data = {"purchase" : 0.06 ,"sale" : 0.03}
    imbalance = {"purchase_cover" : 0.5 , "sale_cover" : 1}
    relative_grid_load=100
    industrial_consumer.observe(t,demand,data,imbalance,relative_grid_load)

print('test passed')