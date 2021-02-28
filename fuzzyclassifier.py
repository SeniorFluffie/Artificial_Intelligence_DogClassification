class FuzzyClassifier(object):
    # dictionary containing the probabilities of each class as well as the mean and deviation of their defining characteristics
    __class_characteristics = {
        'girth': [[0, 0, 40, 50], [40, 50, 60, 70], [60, 70, 100, 100]],
        'height': [[0, 0, 25, 40], [25, 40, 50, 60], [50, 60, 100, 100]],
        'weight': [[0, 0, 5, 15], [5, 15, 20, 40], [20, 40, 100, 100]],
    }

    def __init__(self, input):
        # input is a three element list with [girth, height, weight]
        girth, height, weight = input

        # execute naive bayes
        self.__highest_membership_class, self.__class_memberships = self.classify(girth, height, weight)

    # calculate most likely class
    def classify(self, girth, height, width):
        # TODO
        return (None, None)

    # function for calculating fuzzy membership
    def fuzzy_membership(self, x, values):
        # values of the trapezoid shape
        a, b, c, d = values

        # trapedoizal function describing each characteristic
        if (x <= a):
            return 0
        elif (a < x < b):
            return (x - a) / (b - a)
        elif (b <= x <= c):
            return 1
        elif (c < x < d):
            return (d - x) / (d - c)
        elif (d <= x):
            return 0

    # return most likely class
    def get_highest_membership_class(self):
        # TODO
        return self.__highest_membership_class
    
    # return list of all membership probabilities
    def get_class_memberships(self):
        return self.__class_memberships