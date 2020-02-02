from scipy.signal import remez, freqz
import  numpy as np


def fir_remez_loss(N, array_sovp, fs):
    # array_sovp - точки совпадения АЧХ
    b1 = remez(N, array_sovp, [1, 0], Hz=fs)
    loss =
    return