import numpy as np
import load

def BootStrap(data):
    rst = np.zeros_like(data)
    N, _ = data.shape
    for i in range(N):
        rst[i] = data[np.random.randint(0, N)]
    return rst


def cov_helper(data, i, j):
    N, _ = data.shape
    i_mean = data[:,i].mean()
    j_mean = data[:,j].mean()
    i_t = data[:, i] - i_mean
    j_t = data[:, j] - j_mean
    return (i_t @ j_t)/(N-1)

'''
calculate the $C_{t,t'}$ with BootStrap method
'''
def cov(data, NB=1000):
    _, n_x = data.shape
    covs = np.zeros(shape=(n_x, n_x, NB))
    for cnt in range(NB):
        BS_data = BootStrap(data)
        for x_ in range(n_x):
            for y_ in range(n_x):
                covs[x_, y_, cnt] = cov_helper\
                    (BS_data, x_, y_)
    return covs


def rho_helper(covs, i, j):
    _, _, NB = covs.shape

    cov_ii = covs[i, i, :]
    cov_jj = covs[j, j, :]
    cov_ij = covs[i, j, :]

    den = np.sqrt(cov_ii * cov_jj)
    rhos_ = cov_ij / den
    rho_mean = rhos_.mean()
    delta_rho = np.sqrt(
        ((rhos_ - rho_mean)**2).sum()/(NB-1)
    )
    return rho_mean, delta_rho