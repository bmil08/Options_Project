# This tool uses the Black-Scholes option pricing model

import math
from OptionObject import Option, std_normal_dist_CDF, std_normal_dist_PDF, theo_price

def calc_delta(option : Option) ->float:
    '''
    returns the delta of an option
    '''
    if option.C_P == True: #if call
        return round(std_normal_dist_CDF(option.get_d1()),4)
    else: #if put
        return -round(std_normal_dist_CDF(option.get_d1()),4)

def calc_gamma(option : Option) ->float:
    '''
    returns the gamma of an option
    '''
    my_gamma = std_normal_dist_PDF(option.d1)/(option.get_stock_price() * option.get_volatility() * math.sqrt(option.get_expiration_date()))
    return round(my_gamma,4)

def main():
    test1 = Option(c_p=True,So=223.44,k=222.5,T=1/365,sigma=0.3631, price=2.32)
    print(test1)
    return None
main()
    



