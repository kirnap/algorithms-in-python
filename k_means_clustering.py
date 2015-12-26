# This is made for fully educational purposes
# For more information please visit:
# https://www.coursera.org/learn/machine-learning/lecture/czmip/unsupervised-learning-introduction
import random

import numpy as np


def create_data_point(number_of_futures):
    """
    Number of features defines the dimension od a single datapoint
    """
    help_list = []
    for i in range(0, number_of_futures):
        help_list.append(random.uniform(0, 100))
    # Returns A vector of simple data point
    return help_list


def create_dataset(number_of_data_points, number_of_features):
    """
    Returns a matrix of data points in given numbers

    """
    data_matrix = []
    for i in range(0, number_of_data_points):
        data_matrix.append(create_data_point(number_of_features))
    return np.array(data_matrix)


def choose_random_centroid_list_from_given_dataset(number_of_centroid, data_matrix):
    """
    Returns a set of points for initial centroids

    """
    number_of_data_point = data_matrix.shape[0]
    random_number_list = []

    while len(random_number_list) != number_of_centroid:
        random_number = random.randint(0, number_of_data_point - 1)
        if random_number in random_number_list:
            pass
        else:
            random_number_list.append(random_number)

    return data_matrix[random_number_list]


def find_minimum_distanced_centroid(data_point, centroid_list):
    """

    """
    distance_list = []

    for centroid in centroid_list:
            distance_list.append(float(np.linalg.norm(data_point - centroid)))

    centroid_index = distance_list.index(min(distance_list))
    return tuple(centroid_list[centroid_index])


def assign_point_to_centroid(dataset, centroid_list):
    """
    Returns a dictionary in which every key represents a centroid and each key has a point list containing closest
    distances

    """
    result_dict = {}
    for centroid in centroid_list:
        result_dict[tuple(centroid)] = []

    for point in dataset:
        min_centroid = find_minimum_distanced_centroid(point, centroid_list)
        result_dict[min_centroid].append(point)
    return result_dict


def find_average_point_from_point_list(point_list):
    """


    """
    result_point = []
    dimension = len(point_list[0])
    for i in range(0, dimension):
        sum_of_coordinate = 0
        for point in point_list:
            sum_of_coordinate += point[i]
        result_point.append(sum_of_coordinate / len(point_list))

    return result_point


def find_new_centroid_from_centroid_point_dictionary(centroid_point_dictionary):
    """
    Returns a new centroid_list
    """
    new_centroid_list =[]

    for key in centroid_point_dictionary.keys():
        new_centroid_list.append(find_average_point_from_point_list(centroid_point_dictionary[key]))

    return np.array(new_centroid_list)


if __name__  == '__main__':

    # feature_numbers = raw_input('Please enter number of features: ')
    # number_of_data_points = raw_input('Please enter number of data points: ')
    number_of_clusters = 4
    number_of_data_points = 1000
    feature_numbers = 2

    # dataset = create_dataset(number_of_data_points, feature_numbers)

    dataset = np.genfromtxt('datafile.txt', delimiter=' ')
    random_centroid_list = choose_random_centroid_list_from_given_dataset(number_of_clusters, dataset)
    result_dict = assign_point_to_centroid(dataset, random_centroid_list)
    new_centroid_list = find_new_centroid_from_centroid_point_dictionary(result_dict)
    for i in range(0,100):
        result_dict = assign_point_to_centroid(dataset, new_centroid_list)
        new_centroid_list = find_new_centroid_from_centroid_point_dictionary(result_dict)
    print(new_centroid_list)


# TODO implement it in more efficient way
# TODO Implement object oriented version of it

