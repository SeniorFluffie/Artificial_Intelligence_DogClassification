import math

class NaiveBayesClassifier(object):
    # dictionary containing the probabilities of each class as well as the mean and deviation of their defining characteristics
    __class_characteristics = {
        '"beagle"': { 'probability': 0.30, 'girth': (41, 6),  'height': (37, 4), 'weight': (10, 2) },
        '"corgi"':  { 'probability': 0.21, 'girth': (53, 9),  'height': (27, 3), 'weight': (12, 2) },
        '"husky"':  { 'probability': 0.14, 'girth': (66, 10), 'height': (55, 6), 'weight': (22, 6) },
        '"poodle"': { 'probability': 0.35, 'girth': (61, 9),  'height': (52, 7), 'weight': (26, 8) },
    }

    def __init__(self, input):
        # input is a three element list with [girth, height, weight]
        girth, height, weight = input

        # execute naive bayes
        self.__most_likely_class, self.__class_probabilities = self.naive_bayes(girth, height, weight)

    # naive bayes classification
    def naive_bayes(self, girth, height, weight):
        # return variables
        most_likely_class = None
        class_probabilities = []

        # dictionary representing each breed's characteristics
        # note: probability value does not matter (as long as it is not a tuple)
        characteristics = { 
            'probability': None,
            'girth': girth,
            'height': height,
            'weight': weight,
        }

        # denominator (sum of class probabilities given evidence)
        denominator = 0.0

        # go through each of the classes
        for breed, densities in self.__class_characteristics.items():
            # track probability between characteristics
            probability = 1.0
            # go through each characteristic (e.g. girth, height, etc.)
            for characteristic, value in characteristics.items():
                # get the corresponding density
                density = densities[characteristic]
                # calculate probability
                probability *= (self.__calculate_characteristic_probability(density, value) 
                    if (type(density) == type(()))
                    else density)
            # add to probability list (alongside the breed)
            class_probabilities.append((breed, probability))
            denominator += probability
        # update class probabilities (dividing by total calculated probability of all classes)
        class_probabilities = [(breed, probability / denominator) for breed, probability in class_probabilities]
        # get most likely class
        most_likely_class = max(class_probabilities, key=lambda x:x[1])[0]
        # return best class and all probabilities
        return most_likely_class, class_probabilities

    # calculate probability of characteristic (based on specified distribution)
    def __calculate_characteristic_probability(self, density, x):
        # separate distrbution data
        mean, deviation = density
        # calculate probability
        numerator = (1 / math.sqrt(2 * math.pi * math.pow(deviation, 2)))
        exponent = -0.5 * math.pow((x - mean) / deviation, 2)
        return numerator * math.pow(math.e, exponent)

    # return most likely class (name of breed)
    def get_most_likely_class(self):
        return self.__most_likely_class

    # return probability values for all classes
    def get_class_probabilities(self):
        return [probability[1] for probability in self.__class_probabilities]