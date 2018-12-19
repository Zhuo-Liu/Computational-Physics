import jackknife as jackk
import numpy as np
import matplotlib.pyplot as plt

'''
find the min chi_2/d.o.f
return a list [m, chi_2, dimension, begin, end]
1. m: the value of $m_{eff}$
2. chi_2: list $\chi^2$
3. dimension: $t_{max}-t_{min}$
4. begin: $t_{min}$
5. end: $t_{max}+1$
'''
def chi_2(flag):
    m_eff_time, m_err_time = jackk.get_list('data2.dat',flag)

    least_chi_2 = 10000

    for begin in range(0,26):
        for end in range(begin+4,30):
            part_m_err = m_err_time[begin:end]
            part_m_eff = m_eff_time[begin:end]
            sum_1 = np.sum(1.0/part_m_err**2)
            sum_2 = np.sum(part_m_eff/part_m_err**2)
            m = sum_2 / sum_1
            dimension = end - 1 - begin
            chi_2 = np.sum(((part_m_eff-m)/part_m_err)**2)
            chi_2 = chi_2 / dimension
            if chi_2 < least_chi_2:
                least_chi_2 = chi_2
                temp = [m, chi_2, dimension, begin, end]
    
    return temp