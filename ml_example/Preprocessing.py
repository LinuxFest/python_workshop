from math import sqrt, floor
import numpy as np
from sklearn.datasets import load_iris
from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.feature_selection import f_classif
from sklearn.feature_selection import f_regression
from scipy import stats


def remove_low_variance_features(data_set, threshold):
    sel = VarianceThreshold(threshold=threshold)
    return sel.fit_transform(data_set)


def select_k_best_features(data_set, target, k, test_type):
    if test_type == "chi_square":
        return SelectKBest(chi2, k=k).fit_transform(data_set, target)
    elif test_type == "f_classif":
        return SelectKBest(f_classif, k=k).fit_transform(data_set, target)
    else:
        return SelectKBest(f_regression, k=k).fit_transform(data_set, target)


# Normalize data to N(0, 1)
def normalize_vector(data_set, number_of_columns):
    m = len(data_set)
    for i in range(number_of_columns):
        sum_i = sum_square_i = 0

        for data in data_set:
            sum_i += float(data[i])
            sum_square_i += float(data[i] * data[i])

        mean_i = sum_i / m

        variance_i = sum_square_i - (sum_i * sum_i / m)
        std_i = sqrt(variance_i)

        for j in range(m):
            data_set[j][i] = ((float(data_set[j][i]) - mean_i) / std_i)

    return data_set


# Discretizing of a continuous feature
def discretize_data(feature_vector, feature_number, number_of_classes):
    Q1 = np.percentile(feature_vector, 25)
    median = np.percentile(feature_vector, 50)
    Q3 = np.percentile(feature_vector, 75)
    diameter = Q3 - Q1
    lower_bound = median - diameter
    upper_bound = median + diameter

    interval_length = float((upper_bound - lower_bound) / (number_of_classes - 2))
    for item in feature_vector:
        if item[feature_number] < lower_bound:
            item[feature_number] = 0
        elif item[feature_number] > upper_bound:
            item[feature_number] = number_of_classes - 1
        else:
            item[feature_number] = 1 + floor(float(item[feature_number] - lower_bound) / interval_length)

    return feature_vector


def normal_probability(m, sigma, lower_bound, upper_bound):
    return stats.norm.cdf(upper_bound, loc=m, scale=sigma) - stats.norm.cdf(lower_bound, loc=m, scale=sigma)

"""
# example 1: remove uninformative features with variance threshold method:
print("example 1: remove uninformative features with variance threshold method:")
X = [[0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 1, 1]]
print ("data:", X)
threshold = 0.8 * (1 - 0.8)  # Suppose data follows Bernoulli Distribution, thus variance = p(1-p)
new_X = remove_low_variance_features(X, threshold)
print("new data", new_X)
print("----------------------------------------------------------------------------------")

print("example 2: finding K best features based on a statistical test:")
iris = load_iris()
X, y = iris.data, iris.target
print("iris data dimension", X.shape)
new_X = select_k_best_features(X, y, 2, 'f_regression')
print ("new data dimension:", new_X.shape)
print ("-------------------------------------------------------------------------------")

print("example 3: normalizing data:")
print("iris data", X)
new_X = normalize_vector(X, 4)
print ("iris data after normalization:", new_X)
print ("-------------------------------------------------------------------------------")

print("example 4: discretizing data:")
print("iris data(first column):")
for dat in X:
    print(dat[0])
X = discretize_data(X, 0, 20)
print ("first column after discrtization:")
for dat in X:
    print(int(dat[0]))
"""
print(normal_probability(5, 1, 5.5, 6.5))
