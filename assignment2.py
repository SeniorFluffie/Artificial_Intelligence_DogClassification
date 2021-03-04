from naivebayesclassifier import NaiveBayesClassifier
from fuzzyclassifier import FuzzyClassifier

def naive_bayes_classifier(input):
  # empty input
  if (input is None or len(input) < 3):
    raise Exception('input variable empty')

  # calculate most likely class (using naive bayes)
  naive_bayes_classifier = NaiveBayesClassifier(input)
  most_likely_class = naive_bayes_classifier.get_most_likely_class()
  class_probabilities = naive_bayes_classifier.get_class_probabilities()

  # most_likely_class is a string indicating the most likely class, either "beagle", "corgi", "husky", or "poodle"
  # class_probabilities is a four element list indicating the probability of each class in the order [beagle probability, corgi probability, husky probability, poodle probability]
  return most_likely_class, class_probabilities


def fuzzy_classifier(input):
  # empty input
  if (input is None or len(input) < 3):
    raise Exception('input variable empty')

  # calculate most likely class (using naive bayes)
  fuzzy_classifier = FuzzyClassifier(input)
  highest_membership_class = fuzzy_classifier.get_highest_membership_class()
  class_memberships = fuzzy_classifier.get_class_memberships()

  # highest_membership_class is a string indicating the highest membership class, either "beagle", "corgi", "husky", or "poodle"
  # class_memberships is a four element list indicating the membership in each class in the order [beagle probability, corgi probability, husky probability, poodle probability]
  return highest_membership_class, class_memberships

if __name__ == "__main__":
  print('------------------------------------------------------Example 1: Naive------------------------------------------------------')
  most_likely_class, class_probabilities = naive_bayes_classifier([59, 32, 17])
  print('Actual Output:   ', most_likely_class, ',', class_probabilities)
  print('Expected output: ', '"corgi", [0.0017212721198989387, 0.8444998269543612, 0.003430911965564154, 0.15034798896017576]')
  print('------------------------------------------------------Example 2: Naive------------------------------------------------------')
  most_likely_class, class_probabilities = naive_bayes_classifier([65, 55, 30])
  print('Actual Output:   ', most_likely_class, ',', class_probabilities)
  print('Expected output: ', '"poodle",  [2.4342947465727013e-29, 7.511501676401435e-37, 0.2390117475045523, 0.7609882524954477]')
  print('------------------------------------------------------Example 1: Fuzzy------------------------------------------------------')
  highest_membership_class, class_memberships = fuzzy_classifier([59, 32, 17])
  print('Actual Output:   ', highest_membership_class, ',', class_memberships)
  print('Expected output: ', '"corgi", [0.0, 0.5333333333333333, 0, 0.0]')
  print('------------------------------------------------------Example 2: Fuzzy------------------------------------------------------')
  highest_membership_class, class_memberships = fuzzy_classifier([65, 55, 30])
  print('Actual Output:   ', highest_membership_class, ',', class_memberships)
  print('Expected output: ', '"poodle", [0.0, 0.0, 0.125, 0.375]')
  