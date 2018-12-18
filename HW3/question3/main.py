# python 3
import numpy as np
import matplotlib.pyplot as plt

import dev
import jackknife as jackk
import bootstrap as boots
import chi_2 as chi

if __name__ == "__main__":
    '''
    solution for (3a)
    '''
    C = dev.loadData('data.dat')
    mean = C.mean(axis=0)

    sum = np.zeros((1,33))
    for line in C:
        sum = sum + (line - mean)**2
    deviation = np.sqrt(sum / (200*199))

    rel_dev = deviation / mean * 100

    plt.plot(np.arange(0,33),np.abs(rel_dev).reshape(33,),'o-')
    plt.ylabel("$\Delta C / C \%$",fontsize='x-large')
    plt.xlabel('$t$',fontsize='x-large')
    #plt.savefig("3a.jpg")
    plt.show()

    '''
    solution for (3b),(3c),(3d). 
    index 1 for (3b) & (3c) ; index 2 for (3d)
    '''
    m_eff_time1, m_err_time1 = jackk.get_list('data.dat',1)
    m_eff_time2, m_err_time2 = jackk.get_list('data.dat',2)

    m_err_time1 = m_err_time1 / m_eff_time1
    m_err_time2 = m_err_time2 / m_eff_time2
    
    #plt.plot(np.arange(0,32), m_err_time1,'x')
    Ys = m_eff_time1
    errs = 10*m_err_time1
    plt.errorbar(x=np.arange(0,len(Ys)), y=Ys, yerr=errs)

    plt.ylabel("$m_{eff}$",fontsize='x-large')
    plt.xlabel('$t$',fontsize='x-large')
    #plt.plot(np.arange(0,32), m_err_time1,'x')
    plt.show()

    list1 = chi.chi_2(1)
    list2 = chi.chi_2(2)
    print(list1)
    print(list2)

    '''
    solution for (3e)
    '''
    data = dev.loadData('data.dat')
    boots.rho(data)