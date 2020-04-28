# python 3

from player import Player
import random as rd 
rd.seed()


industrial_consumer = Player()

for t in range(48):
    load = industrial_consumer.compute_load(t, rd.random()*100)
    assert industrial_consumer.battery_stock[t] >= 0
    assert industrial_consumer.battery_stock[t] <= industrial_consumer.capacity

print('test passed')
