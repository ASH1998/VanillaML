import unittest

from vanilla_ml.classifier.supervised.perceptron import Perceptron
from vanilla_ml.util import data_io
from vanilla_ml.util.metrics.accuracy import accuracy_score


class TestPerceptron(unittest.TestCase):

    def test_two_moons(self):
        train_X, test_X, train_y, test_y = data_io.get_setosa_vericolour_iris_train_test()
        print("train_X's shape = %s, train_y's shape = %s" % (train_X.shape, train_y.shape))
        print("test_X's shape = %s, test_y's shape = %s" % (test_X.shape, test_y.shape))

        clf = Perceptron(max_iterations=50)
        print("clf: %s" % clf)

        print("Fitting ...")
        clf.fit(train_X, train_y)

        print("Predicting ...")
        pred_y = clf.predict(test_X)
        print("y = %s" % test_y)
        print("pred_y = %s" % clf.predict(test_X))

        accuracy = accuracy_score(test_y, pred_y)
        print("Accuracy = %g%%" % (100 * accuracy))

        self.assertGreaterEqual(accuracy, 0.95)

if __name__ == '__main__':
    unittest.main()