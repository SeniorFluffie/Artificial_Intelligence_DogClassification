class FuzzyClassifier(object):
    # dictionary containing the probabilities of each class as well as the mean and deviation of their defining characteristics
    __class_characteristics = {
        'girth': {'small': (0, 0, 40, 50), 'medium': (40, 50, 60, 70), 'large': (60, 70, 100, 100)},
        'height': {'short': (0, 0, 25, 40), 'medium': (25, 40, 50, 60), 'tall': (50, 60, 100, 100)},
        'weight': {'light': (0, 0, 5, 15), 'medium': (5, 15, 20, 40), 'heavy': (20, 40, 100, 100)},
    }

    def __init__(self, input):
        # input is a three element list with [girth, height, weight]
        girth, height, weight = input

        # execute naive bayes
        self.__highest_membership_class, self.__class_memberships = self.__classify(girth, height, weight)

    # calculate most likely class
    def __classify(self, girth, height, weight):
        memberships = self.__get_membership((girth, height, weight))
        # get the strengths of all fuzzy rules
        rule_strengths = self.__get_rule_strengths(memberships)
        # retrieve most likely class
        most_likely_class = max(rule_strengths, key=lambda x:x[1])[0]
        # format class memberships (to only show values)
        class_memberships = [value for breed, value in rule_strengths]
        return (most_likely_class, class_memberships)

    def __get_membership(self, inputs):
        # store memberships
        memberships = {}
        # go through each of the characteristics (girth, height, etc.)
        for index, characteristic_name in enumerate(self.__class_characteristics):
            # get the value of the characteristic (and corresponding input value)
            characteristic = self.__class_characteristics[characteristic_name]
            x = inputs[index]
            # calculate membership for each size
            sizes = {size: self.__calculate_membership(x, characteristic[size]) for size in characteristic}
            # set value in membership dict
            memberships[characteristic_name] = sizes
        return memberships
        # go through and calculate value for each characteristic (and size)
        

    def __get_rule_strengths(self, memberships):
        # list of all strengths
        rule_strengths = []
        # get individual elements (for convenience)
        girth, height, weight = memberships['girth'], memberships['height'], memberships['weight']
        # add fuzzy rules
        rule_strengths.append(('"beagle"', self.__fuzzy_and(height['medium'], self.__fuzzy_or(girth['small'], weight['light']))))
        rule_strengths.append(('"corgi"', self.__fuzzy_and(self.__fuzzy_and(girth['medium'], height['short']), weight['medium'])))
        rule_strengths.append(('"husky"', self.__fuzzy_and(self.__fuzzy_and(girth['large'], height['tall']), weight['medium'])))
        rule_strengths.append(('"poodle"', self.__fuzzy_and(self.__fuzzy_or(girth['medium'], height['medium']), weight['heavy'])))
        # return list of fuzzy values
        return rule_strengths

    # function for calculating fuzzy membership
    def __calculate_membership(self, x, values):
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
        
    # goguen t-norm (AND)
    def __fuzzy_and(self, x, y):
        return x * y

    # goguen s-norm (OR)
    def __fuzzy_or(self, x, y):
        return (x + y) - (x * y)

    # return most likely class
    def get_highest_membership_class(self):
        return self.__highest_membership_class
    
    # return list of all membership probabilities
    def get_class_memberships(self):
        return self.__class_memberships