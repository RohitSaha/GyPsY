from api import *
import math
log2 = lambda x: math.log(x, 2)
INF = float('inf')


def id_tree_classify_point(point, id_tree):
    if id_tree.is_leaf():
        return id_tree.get_node_classification()
    else:
        new_tree = id_tree.apply_classifier(point)
        get_point = id_tree_classify_point(point, new_tree)
    return get_point

def split_on_classifier(data, classifier):
    """Given a set of data (as a list of points) and a Classifier object, uses
    the classifier to partition the data.  Returns a dict mapping each feature
    values to a list of points that have that value."""
    #Dictionary which will contain the data after classification.
    class_dict = {}
    #Iterating through all the points in data
    for i in range(len(data)):
        get_value = classifier.classify(data[i])
        if get_value not in class_dict:
            class_dict[get_value] = [data[i]]
        else:
            class_dict[get_value].append(data[i])
    return class_dict


def branch_disorder(data, target_classifier):
    """Given a list of points representing a single branch and a Classifier
    for determining the true classification of each point, computes and returns
    the disorder of the branch."""
    #Getting data after classification based on the target_classifier
    class_dict = split_on_classifier(data, target_classifier)
    if (len(class_dict) == 1):
        #Homogenous condition
        return 0
    else:
        disorder = 0
        for i in class_dict:
            get_len = len(class_dict[i])
            p_term = get_len/ float(len(data))
            disorder += (-1) * p_term * log2(p_term)
        return disorder

def average_test_disorder(data, test_classifier, target_classifier):
    """Given a list of points, a feature-test Classifier, and a Classifier
    for determining the true classification of each point, computes and returns
    the disorder of the feature-test stump."""
    average_disorder = 0.0
    #Getting all the branches after applying test_classifer
    get_branches = split_on_classifier(data, test_classifier)
    #Iterating through the branches
    for i in get_branches:
        disorder = branch_disorder(get_branches[i], target_classifier)
        average_disorder += disorder * (len(get_branches[i])/ float(len(data)))
    return average_disorder

#### CONSTRUCTING AN ID TREE

def find_best_classifier(data, possible_classifiers, target_classifier):
    """Given a list of points, a list of possible Classifiers to use as tests,
    and a Classifier for determining the true classification of each point,
    finds and returns the classifier with the lowest disorder.  Breaks ties by
    preferring classifiers that appear earlier in the list.  If the best
    classifier has only one branch, raises NoGoodClassifiersError."""

    #Base values to start with
    best_classifier = average_test_disorder(data, possible_classifiers[0], target_classifier)
    store_classifier = possible_classifiers[0]

    #Iterating over the list of possible classifiers
    for i in range(len(possible_classifiers)):
        avg_disorder = average_test_disorder(data, possible_classifiers[i], target_classifier)
        if avg_disorder < best_classifier:
            best_classifier = avg_disorder
            store_classifier = possible_classifiers[i]

    get_branches = split_on_classifier(data, store_classifier)
    if len(get_branches)==1:
        #Only 1 branch present
        raise NoGoodClassifiersError
    else:
        return store_classifier



def construct_greedy_id_tree(data, possible_classifiers, target_classifier, id_tree_node=None):
    """Given a list of points, a list of possible Classifiers to use as tests,
    a Classifier for determining the true classification of each point, and
    optionally a partially completed ID tree, returns a completed ID tree by
    adding classifiers and classifications until either perfect classification
    has been achieved, or there are no good classifiers left."""
    #print data
    #print "possible", possible_classifiers
    #print "target", target_classifier
    if id_tree_node == None:
        #Creating a new tree
        id_tree_node = IdentificationTreeNode(target_classifier)
    if branch_disorder(data, target_classifier) == 0:
        id_tree_node.set_node_classification(target_classifier.classify(data[0]))
    else:
        try:
            #Getting the best classifier from the options available
            best_classifier = find_best_classifier(data, possible_classifiers, target_classifier)
            get_branches = split_on_classifier(data, best_classifier)
            id_tree_node = id_tree_node.set_classifier_and_expand(best_classifier, get_branches)
            #possible_classifiers.remove(best_classifier)

            branches = id_tree_node.get_branches()
            for i in branches:
                construct_greedy_id_tree(get_branches[i], possible_classifiers, target_classifier, branches[i])
        except NoGoodClassifiersError:
            pass
    return id_tree_node

possible_classifiers = [\
    feature_test('AGE '),
    feature_test('GENDER'),
    feature_test('MOODS'),
    feature_test('SOLO/GROUP'),
    feature_test('TIMESTAMP'),
    feature_test('WEATHER')
]




tar = feature_test('THEMES')
print construct_greedy_id_tree(data, possible_classifiers, tar)
