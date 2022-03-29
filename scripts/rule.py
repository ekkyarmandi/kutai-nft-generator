import random
import json
    
def choose(attributes, probabilities, trait_type):
    weights = [probabilities[trait_type][attr] for attr in attributes[trait_type]]
    weights = [p/sum(weights) for p in weights]
    item = random.choices(attributes[trait_type], weights=weights, k=1)
    return item[0]