import jackknife as jackk
import dev
import numpy as np
import matplotlib.pyplot as plt

def chi_2(flag):
    m_eff_time, m_err_time = jackk.get_list('data.dat',flag)

    least_chi_2 = 10000

    for begin in range(0,26):
        for end in range(begin+4,30):
            part_m_err = m_err_time[begin:end]
            part_m_eff = m_eff_time[begin:end]
            sum_1 = np.sum(1.0/part_m_err**2)
            sum_2 = np.sum(part_m_eff/part_m_err**2)
            m = sum_2 / sum_1
            chi_2 = np.sum(((part_m_eff-m)/part_m_err)**2)
            chi_2 = chi_2 / (end-begin -1)
            if chi_2 < least_chi_2:
                least_chi_2 = chi_2
                dimension = end - 1 - begin
                temp = [m, chi_2, dimension, begin, end]
    
    return temp


# if __name__ == "__main__":
#     list1 = chi_2(1)
#     list2 = chi_2(2)
#     print(list1)
#     print(list2)