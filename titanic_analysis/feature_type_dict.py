import numpy as np
def create_feature_type_dict(data):
    feature_types = {
        'numerical': {
            'continuous': [], 
            'discrete': []  
        },
        'categorical': {
            'nominal': [],  
            'ordinal': []
        }
    }
    return feature_types