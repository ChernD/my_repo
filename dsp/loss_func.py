from scipy.signal import remez, freqz
import  numpy as np


def fir_remez_loss(N, bstop, bpass, per_verh, per_niz,  fs):
    # array_sovp - точки совпадения АЧХ
    b1 = remez(N, [bpass, per_verh, per_niz, bstop], [1, 0], Hz=fs)
    H1, m = freqz(b1, 1)
    H0 = np.append(np.ones(bpass), )
    loss = np.sum((H1 - H0)**2)/len(H1)
    return loss
