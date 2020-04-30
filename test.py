# python 3

from player import Player
import random as rd
rd.seed()


industrial_consumer = Player()

for t in range(48):
    load = industrial_consumer.compute_load(t, rd.random()*100)
    assert industrial_consumer.battery_stock[t] >= 0
    assert industrial_consumer.battery_stock[t] <= industrial_consumer.capacity
    data = {"internal" : 0.06 ,"external_purchase" : 0.1,"external_sale" : 0.03}
    imbalance = {"demand" : 0.5 , "supply" : 1}
    industrial_consumer.observe(t,50,data,imbalance)

print('test passed')
