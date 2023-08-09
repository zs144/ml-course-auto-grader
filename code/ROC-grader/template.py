import numpy as np
import pandas as pd

def train_classifier(train_X, train_y):
    """ Train the classifier and return the estimated parameters.

    Parameters:
        - train_X (array-like of shape (n_samples, n_features)): features of each
        obs in training data.
        - train_y (array-like of shape (n_samples,)): true class of each obs in
        training data.

    Returns:
        params (dictionary with two elements): estimated parameters of the model.
        The classifier has the form of: $f(X) = w^T * X + b$. `params` stores two
        elements - w and b.
        	- `w` (array-like of shape (n_features,)): parameter for each feature.
        	- `b` (np.float64): intercept term.
    """
    # TODO: implement this function
    params = {}
    params['w'] = ...
    params['b'] = ...

    return params


def get_decision_statistics(params, input_X):
    """ Generate decision statistics for each obs in the input.

    Parameters:
    	- params (dictionary with two elements): estimated parameters of the model.
        The classifier has the form of: $f(X) = w^T * X + b$. `params` stores two
        elements - w and b.
        	- `w` (list of length (n_features)): parameter for each feature.
        	- `b` (float): intercept term.
        - input_X (array-like of shape (n_samples, n_features)): features of each obs
        in input data.

    Returns:
    	decision_statistics (array-like of shape (n_samples,)): decision statistics for
    	each obs. This is calculated by $w^T * X + b$, where `w` and `b` are provided
    	in `params`. They should be placed in the same order as they are in `input_X`,
    	ie, the decision statistics of the first obs in `input_X` is the first element
    	in `decision_statistics`, and so on.
    """
    # TODO: implement this function
    decision_statistics = ...
    return decision_statistics


def get_ROC_data(thresholds, truth, decision_stats):
    """Generate a Pandas dataframe with the columns of thresholds, P_d and P_fa.

    Parameters:
        - thresholds (array-like of shape (n_thresholds,)): a list of thresholds.
        - truth (array-like of shape (n_samples,)): true class for each obs.
        - decision_stats (array-like of shape (n_samples,)): decision
        statistics of each observation.

    Returns:
        ROC_data (pd.DataFrame of shape (n_thresholds, 3)):
        The first column is the list of thresholds; The second column is the
        percentage of detection (P_d) under the given threshold, and the third
        column is the percentage of false alarm (P_fa) under the given threshold.
    """
    # TODO: implement this function
    ROC_data = pd.DataFrame(thresholds, columns=["thresholds"])
    ROC_data["P_d"] = ...
    ROC_data["P_fa"] = ...

    ROC_data.to_csv('student_ROC_data.csv')
    return ROC_data


def draw_one_ROC(ROC_data):
    """Draw one ROC curve.

    Parameters:
    - ROC_data (pd.DataFrame of shape (n_thresholds, 3)): a Pandas dataframe with three
    colomns.
    	- The first column is the `thresholds`;
    	- The second colummn is `P_d`;
    	- The third column is `P_fa`.
    """
    # TODO: implement this function
