import numpy as np
import load
import matplotlib.pyplot as plt

'''
JackKnife Method
Input:
1. to_be_cut: 2D numpy array to be cut
2. flag: choose solution for (3b) or (3d).
Output:
1. m_eff: average by jackknife method
2. m_err: loadiation by jackkinfe method
'''
def JackKnife(to_be_cut,flag):
    M = to_be_cut.shape[0]
    m_eff_each = [] #对每次切片
    for i in range(0,M):
        cut = np.concatenate( [to_be_cut[:i], to_be_cut[i+1:]], axis=0)

        if flag == 1:
            mean_1, mean_2 = np.mean(cut,axis=0)
            m_eff_mean = np.log(mean_1/mean_2)
        else:
            mean_1, mean_2, mean_3 = np.mean(cut,axis=0)
            m_eff_mean = np.arccosh((mean_1+mean_3)*0.5 / mean_2)

        m_eff_each.append(m_eff_mean)
    
    m_eff_each = np.array(m_eff_each)
    
    m_eff = np.mean(m_eff_each)
    m_err = np.sqrt((M-1)*np.sum((m_eff_each - m_eff)**2) / M)

    return m_eff, m_err

'''
Get the result List ($m_{eff}$,$\Delta m_{eff}$) for each time piece by Jackknife method
'''
def get_list(filename,question_number):
    C = load.loadData(filename)

    m_eff_time = []
    m_err_time = []

    if question_number == 1:
        for t in range(1,31):
            to_be_cut = C[:,t:t+2]
            m_eff,m_err = JackKnife(to_be_cut,question_number)

            m_eff_time.append(m_eff)
            m_err_time.append(m_err)
    elif question_number == 2:
        for t in range(1,30):
            to_be_cut = C[:,t:t+3]
            m_eff,m_err = JackKnife(to_be_cut,question_number)

            m_eff_time.append(m_eff)
            m_err_time.append(m_err)           
    else:
        print("error in question_number")
        exit(1)   
    
    return np.array(m_eff_time), np.array(m_err_time)