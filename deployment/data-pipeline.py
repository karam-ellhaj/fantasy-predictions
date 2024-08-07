import numpy as np 
import requests

def input_features()->dict:
    inputed = ['position',
            'assists',
            'bonus',
            'clean_sheets',
            'goals_conceded',
            'goals_scored',
            'minutes',
            'own_goals',
            'penalties_missed',
            'penalties_saved',
            'red_cards',
            'saves',
            'selected',
            'was_home',
            'yellow_cards',
            'GW',
            'total_points_lag']
    to_feed_model = {}
    
    for feature in inputed:
        to_feed_model[feature] = int(input(feature+': '))

    return list(to_feed_model.values())


def catigorical_to_numbers_maps():
    print('position to number map:')
    print('-'*40)
    print('DEF -> 0')
    print('FWD -> 1')
    print('GK -> 2')
    print('MID -> 3')
    print('-'*40)
    print('for is home feature it is 0 for away mathces and 1 for home matches')


catigorical_to_numbers_maps()


# print(input_features())
feats = input_features()
print(feats)

response = requests.post('http://127.0.0.1:5000',json={'X':feats})

print(response.json())