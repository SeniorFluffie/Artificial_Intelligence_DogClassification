from naivebayesclassifier import NaiveBayesClassifier

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
  # input is a three element list with [girth, height, weight]
  girth, height, weight = input

  # highest_membership_class is a string indicating the highest membership class, either "beagle", "corgi", "husky", or "poodle"
  # class_memberships is a four element list indicating the membership in each class in the order [beagle probability, corgi probability, husky probability, poodle probability]
  return highest_membership_class, class_memberships