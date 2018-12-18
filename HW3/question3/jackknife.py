import numpy as np
import dev
import matplotlib.pyplot as plt

'''
JackKnife Method
Input:
1. to_be_cut: 2D numpy array to be cut
2. flag: choose solution for (3b) or (3d).
Output:
1. m_eff: average by jackknife method
2. m_err: deviation by jackkinfe method
'''
def JackKnife(to_be_cut,flag):
    M = to_be_cut.shape[0]
    m_eff_each = [] #对每次切片
    for i in range(0,M):
        cut = np.concatenate( [to_be_cut[:i], to_be_cut[i+1:]], axis=0)

        #mean_1 , mean_2 = np.mean(cut,axis=0)

        if flag == 1:
            col_1 = cut[:,0]
            col_2 = cut[:,1]
            m_eff_list = np.log(col_1/col_2)
        else:
            col_1 = cut[:,0]
            col_2 = cut[:,1]
            col_3 = cut[:,2]
            m_eff_list = np.arccosh((col_1+col_3)*0.5 / col_2)

        #m_eff_mean = np.log(mean_1/mean_2)

        m_eff_mean = np.mean(m_eff_list)
        m_eff_each.append(m_eff_mean)
    
    m_eff_each = np.array(m_eff_each)
    
    m_eff = np.mean(m_eff_each)
    m_err = np.sqrt((M-1)*np.sum((m_eff_each - m_eff)**2) / M)

    return m_eff, m_err

'''
Get the result List for each time piece by Jackknife method
'''
def get_list(filename,question_number):
    C = dev.loadData(filename)

    m_eff_time = []
    m_err_time = []

    if question_number == 1:
        for t in range(0,32):
            to_be_cut = C[:,t:t+2]
            m_eff,m_err = JackKnife(to_be_cut,question_number)

            m_eff_time.append(m_eff)
            m_err_time.append(m_err)
    elif question_number == 2:
        for t in range(0,31):
            to_be_cut = C[:,t:t+3]
            m_eff,m_err = JackKnife(to_be_cut,question_number)

            m_eff_time.append(m_eff)
            m_err_time.append(m_err)           
    else:
        print("error in question_number")
        exit(1)   
    
    return np.array(m_eff_time), np.array(m_err_time)

# if __name__ == '__main__':
#     m_eff_time1, m_err_time1 = dev.get_list('data.dat',1)
#     m_eff_time2, m_err_time2 = dev.get_list('data.dat',2)

#     m_err_time1 = m_err_time1 / m_eff_time1
#     m_err_time2 = m_err_time2 / m_eff_time2
    
#     #plt.plot(np.arange(0,32), m_err_time1,'x')
#     Ys = m_eff_time1
#     errs = 10*m_err_time1
#     plt.errorbar(x=np.arange(0,len(Ys)), y=Ys, yerr=errs)

#     plt.ylabel("$m_{eff}$",fontsize='x-large')
#     plt.xlabel('$t$',fontsize='x-large')
#     #plt.plot(np.arange(0,32), m_err_time1,'x')

#     plt.show()