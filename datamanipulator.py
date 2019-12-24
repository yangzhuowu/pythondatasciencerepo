# -*- coding: utf-8 -*-
"""
@Subject:Create train dataset and test dataset
"""
import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np
HOUSING_PATH  = os.path.join("datasets", "housing")

def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    print(csv_path)
    return pd.read_csv(csv_path)

def split_train_test(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]

if __name__ == "__main__":
    # test load_housing_data function
    housingdata = load_housing_data()
    print(housingdata.head(5))
    print(housingdata['ocean_proximity'].value_counts())
    housingdata.hist(bins=50, figsize=(20, 15))
    plt.show()
    
    # test split_train_test function
    train_set, test_set = split_train_test(housingdata, 0.2)
    print(len(housingdata))
    print(len(train_set))
    print(len(test_set))
