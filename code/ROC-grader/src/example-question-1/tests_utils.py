import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def roc_curves_visual_cmp(our_ROC_data, student_ROC_data):
    """ Draws two ROC curves with the area between them.

    Parameters:
    - our_ROC_data (pd.Dataframe of shape (n_samples, 3)): ROC data for the ROC
    curve used as our benchmark.
    - student_ROC_data (pd.Dataframe of shape (n_samples, 3)): ROC data given by
    a student.

    Note:
    The benchmark ROC curve is drawn in blue, whereas the student's ROC curve is
    red. For areas where our ROC curve is higher, we color the area between the
    curves (ABC) blue. Otherwise, the area will be filled in red.
    """
    # NOTE: thresholds must be decreasing for the convenince of interpolation.
    our_ROC_data.sort_values(by='thresholds', ascending=False, inplace=True)
    student_ROC_data.sort_values(by='thresholds', ascending=False, inplace=True)
    _, ax = plt.subplots()
    plt.xlabel("P_fa")
    plt.ylabel("P_d")
    plt.xlim(-0.01, 1.01)
    plt.ylim(-0.01, 1.01)
    plt.plot(our_ROC_data["P_fa"], our_ROC_data["P_d"], c="b", lw=1, label="Benchmark")
    plt.plot(student_ROC_data["P_fa"], student_ROC_data["P_d"], c="r", lw=1, label="Student")
    Pd_2_interp = np.interp(our_ROC_data["P_fa"], student_ROC_data["P_fa"], student_ROC_data["P_d"])
    plt.fill_between(our_ROC_data["P_fa"], our_ROC_data["P_d"], Pd_2_interp,
                     where=our_ROC_data["P_d"] < Pd_2_interp, interpolate=True,
                     color="crimson", alpha=0.3)
    plt.fill_between(our_ROC_data["P_fa"], our_ROC_data["P_d"], Pd_2_interp,
                     where=our_ROC_data["P_d"] > Pd_2_interp, interpolate=True,
                     color="dodgerblue", alpha=0.3)
    plt.plot(ax.get_xlim(), ax.get_ylim(), c="black", alpha=0.6, ls='--') # diagonal
    plt.legend()
    plt.gca().set_box_aspect(1)
    plt.show()


def compute_ABC(our_ROC_data, student_ROC_data):
    """ Compute the area between the two ROC curves.

    Parameters:
    - our_ROC_data (pd.Dataframe of shape (n_samples, 3)): ROC data for the ROC
    curve used as our benchmark.
    - student_ROC_data (pd.Dataframe of shape (n_samples, 3)): ROC data given by
    a student.

    Returns:
    abc (float): the area between the two ROC curves. Note that the parts where
    our ROC curve is higher and the parts where the student's curve is higher are
    all counted as positive area.
    """
    Pd_2_interp = np.interp(student_ROC_data["P_fa"], our_ROC_data["P_fa"], our_ROC_data["P_d"])
    roc_diff = np.abs(student_ROC_data["P_d"] - Pd_2_interp)
    abc = integrate.trapz(roc_diff, student_ROC_data["P_fa"])
    return abc