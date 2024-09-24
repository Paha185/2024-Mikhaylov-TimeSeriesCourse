import numpy as np
import pandas as pd


def ED_distance(ts1: np.ndarray, ts2: np.ndarray) -> float:
    """
    Calculate the Euclidean distance

    Parameters
    ----------
    ts1: the first time series
    ts2: the second time series

    Returns
    -------
    ed_dist: euclidean distance between ts1 and ts2
    """
    
    ed_dist = 0
  
    ed_dist = np.sqrt(np.sum((ts1 - ts2)**2))

    return ed_dist


def norm_ED_distance(ts1: np.ndarray, ts2: np.ndarray) -> float:
    """
    Calculate the normalized Euclidean distance

    Parameters
    ----------
    ts1: the first time series
    ts2: the second time series

    Returns
    -------
    norm_ed_dist: normalized Euclidean distance between ts1 and ts2s
    """

    norm_ed_dist = 0

    # INSERT YOUR CODE

    return norm_ed_dist


def DTW_distance(ts1: np.ndarray, ts2: np.ndarray, r: float = 1) -> float:
    """
    Calculate DTW distance

    Parameters
    ----------
    ts1: first time series
    ts2: second time series
    r: warping window size
    
    Returns
    -------
    dtw_dist: DTW distance between ts1 and ts2
    """

    dtw_dist = 0

    empty_array = pd.DataFrame(np.empty((len(ts1) + 1, len(ts2) + 1)))
    empty_array.iloc[0,:] = float('inf')
    empty_array.iloc[:,0] = float('inf')
    empty_array.iloc[0,0] = 0
    
    for i in range(1, len(ts1) + 1):
      for j in range(1, len(ts2) + 1):
        empty_array.iloc[i,j] = (ts1[i-1] - ts2[j-1])**2 + min(empty_array.iloc[i-1,j],
                                                                    empty_array.iloc[i,j-1],
                                                                    empty_array.iloc[i-1,j-1])
    dtw_dist = empty_array.iloc[-1,-1]
    return dtw_dist
