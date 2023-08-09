import unittest
from student_utils import *

import numpy as np
import pandas as pd
from pathlib import Path

# Set path
hw_folder = Path('/Users/zionshane/Develop/ml-course-auto-grader/code/ROC-grader/src/example-question-1/')

# Set constants
POS_INF = float("inf")
NEG_INF = float("-inf")
extra = pd.Series([POS_INF, NEG_INF])

def make_orderer():
    order = {}
    def ordered(f):
        order[f.__name__] = len(order)
        return f
    def compare(a, b):
        return [1, -1][order[a] < order[b]]
    return ordered, compare

ordered, compare = make_orderer()
unittest.defaultTestLoader.sortTestMethodsUsing = compare

class TestROCGenerator(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.data = pd.read_csv(hw_folder / 'data/dataSet4.csv', names=['truth', 'x', 'y'])
        self.data = self.data[['x', 'y', 'truth']]
        self.train_X = self.data[['x', 'y']].values
        self.train_y = self.data['truth']
        self.n_samples = self.train_X.shape[0]
        self.n_features = self.train_X.shape[1]
        self.params = {}
        self.decision_stats = np.array([])
        self.ROC_data = pd.DataFrame([])

    @ordered
    def test_step1(self):
        self.params = train_classifier(self.train_X, self.train_y)
        w = self.params['w']
        b = self.params['b']
        # Check the type of params
        error_msg = 'Incorrect data type of params (should be dict)'
        self.assertIsInstance(self.params, dict, error_msg)
        # Check the length of params
        error_msg = 'Incorrect dictionary length (should only have w and b)'
        self.assertEqual(len(self.params), 2, error_msg)
        # Check the type of w
        error_msg = 'Incorrect data type of w (should be np.array)'
        self.assertIsInstance(w, np.ndarray, error_msg)
        # Check the shape of w
        error_msg = 'Incorrect shape of w (should be (n_features,))'
        self.assertEqual(w.shape, (self.n_features,), error_msg)
        # Check the type of b
        error_msg = 'Incorrect data type of w (should be np.float64)'
        self.assertIsInstance(b, np.float64, error_msg)
        # Check if there is hardcoding
        print('Good job! No error in step 1!')

    @ordered
    def test_step2(self):
        print(self.params)
        self.decision_stats = get_decision_statistics(self.params, self.train_X)
        # Check the type of decision stats
        error_msg = 'Incorrect data type of decision statistics'
        self.assertIsInstance(self.decision_stats, np.ndarray, error_msg)
        # Check the shape of decision stats
        error_msg = 'Incorrect shape of decision statistics'
        self.assertEqual(self.decision_stats.shape, (self.n_samples,), error_msg)
        # Check if there is hardcoding
        print('Good job! No error in step 2!')

    @ordered
    def test_step3(self):
        thresholds = np.concatenate((self.decision_stats, extra))
        ROC_data = get_ROC_data(thresholds, self.train_y, self.decision_stats)
        # Check the type of ROC data
        error_msg = 'Incorrect data type of ROC data table (should be pd.DataFrame)'
        self.assertIsInstance(self.ROC_data, pd.DataFrame, error_msg)
        # Check the shape of ROC data
        error_msg = 'Incorrect shape of ROC data table (should be (len(thresholds),3))'
        self.assertEqual(self.ROC_data.shape, (len(thresholds),3), error_msg)
        # Check the order of P_d and P_fa (both should be either increasing or decreasing)
        P_d = ROC_data['P_d'].tolist()
        P_fa = ROC_data['P_fa'].tolist()
        is_pd_asc   = all(P_d[i] <= P_d[i+1] for i in range(len(P_d) - 1))
        is_pd_desc  = all(P_d[i] >= P_d[i+1] for i in range(len(P_d) - 1))
        is_pfa_asc  = all(P_fa[i] <= P_fa[i+1] for i in range(len(P_fa) - 1))
        is_pfa_desc = all(P_fa[i] >= P_fa[i+1] for i in range(len(P_fa) - 1))
        is_sorted_pd_and_pfa = (is_pd_asc and is_pfa_asc) or (is_pd_desc and is_pfa_desc)
        error_msg = 'P_d and P_fa are not sorted (both should be monotonic)'
        self.assertEqual(is_sorted_pd_and_pfa, True, error_msg)
        # Check if ther is hardcoding
        print('Good job! No error in step 3!')


# run the test
unittest.main()
