import random
import json
    
def choose(attributes, key):
    probability = json.load(open("source\\probability.json"))
    weights = [probability[key][attr] for attr in attributes[key]]
    weights = [p/sum(weights) for p in weights]
    item = random.choices(attributes[key], weights=weights, k=1)
    return item[0]