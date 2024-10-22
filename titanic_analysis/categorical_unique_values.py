def display_unique_values(data, categorical_features):
    unique_features = {}
    for i in categorical_features:
        unique_features[i] = data[i].unique()
    return unique_features