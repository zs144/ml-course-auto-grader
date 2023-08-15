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


class TestROCGenerator(unittest.TestCase):
    data = pd.read_csv(hw_folder / 'data/dataSet4.csv', names=['truth', 'x', 'y'])
    data = data[['x', 'y', 'truth']]
    train_X = data[['x', 'y']].values
    train_y = data['truth']
    n_samples = train_X.shape[0]
    n_features = train_X.shape[1]
    params = {}
    decision_stats = np.array([])
    ROC_data = pd.DataFrame([])

    @classmethod
    def setUpClass(self):
        pass

    def test_step1(self): # step 1: training the clf
        self.__class__.params = train_classifier(self.__class__.train_X, self.__class__.train_y)
        w = self.__class__.params['w']
        b = self.__class__.params['b']
        # Check the type of params
        error_msg = 'Incorrect data type of params (should be dict)'
        self.assertIsInstance(self.__class__.params, dict, error_msg)
        # Check the length of params
        error_msg = 'Incorrect dictionary length (should only have w and b)'
        self.assertEqual(len(self.__class__.params), 2, error_msg)
        # Check the type of w
        error_msg = 'Incorrect data type of w (should be np.array)'
        self.assertIsInstance(w, np.ndarray, error_msg)
        # Check the shape of w
        error_msg = 'Incorrect shape of w (should be (n_features,))'
        self.assertEqual(w.shape, (self.__class__.n_features,), error_msg)
        # Check the type of b
        error_msg = 'Incorrect data type of w (should be np.float64)'
        self.assertIsInstance(b, np.float64, error_msg)
        # Check if there is hardcoding
        print('Good job! No error in step 1!')

    def test_step2(self): # step 1: decision statistics
        self.__class__.decision_stats = get_decision_statistics(self.__class__.params, self.__class__.train_X)
        # Check the type of decision stats
        error_msg = 'Incorrect data type of decision statistics'
        self.assertIsInstance(self.__class__.decision_stats, np.ndarray, error_msg)
        # Check the shape of decision stats
        error_msg = 'Incorrect shape of decision statistics'
        self.assertEqual(self.__class__.decision_stats.shape, (self.__class__.n_samples,), error_msg)
        # Check if there is hardcoding
        print('Good job! No error in step 2!')

    def test_step3(self): # step 3:ROC
        thresholds = np.concatenate((self.__class__.decision_stats, extra))
        self.__class__.ROC_data = get_ROC_data(thresholds, self.__class__.train_y, self.__class__.decision_stats)
        # Check the type of ROC data
        error_msg = 'Incorrect data type of ROC data table (should be pd.DataFrame)'
        self.assertIsInstance(self.__class__.ROC_data, pd.DataFrame, error_msg)
        # Check the shape of ROC data
        error_msg = 'Incorrect shape of ROC data table (should be (len(thresholds),3))'
        self.assertEqual(self.__class__.ROC_data.shape, (len(thresholds),3), error_msg)
        # Check the order of P_d and P_fa (both should be either increasing or decreasing)
        P_d = self.__class__.ROC_data['P_d'].tolist()
        P_fa = self.__class__.ROC_data['P_fa'].tolist()
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
unittest.main(verbosity=2)
