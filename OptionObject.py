import math

def std_normal_dist_CDF(z_score) -> float:
    '''
    The CDF of the standard normal distribution. Already accounts for negative values
    @param: a `z-score` can be negative
    :return: a float representation of the probability
    '''
    if z_score>0:
        prob = (1/2)*(1 + math.erf(z_score/math.sqrt(2)))
    else:
        prob = 1 - std_normal_dist_CDF(abs(z_score))
    return prob

def std_normal_dist_PDF(z_score) -> float:
    '''
    The PDF of the standard normal distribution
    @param: a `z-score` can be negative
    :return: a float representation of the probability
    '''
    if z_score>0:
        prob = (1/math.sqrt(2*math.pi))*math.exp(-(z_score**2)/2)
    else:
        prob = 1- std_normal_dist_PDF(abs(z_score))
    return prob

def theo_price(d1,d2,C_P,So,k) -> float:
    ''' 
    This uses the Black-Scholes formula to calculate the theoretical
    price of an European option
    @param: `d1` and `d2` floats
    @param: a boolean `C_P` true if Call
    @param: `So` spot price of stock
    @param: `k` strike price of option
    :return: a float representaion of the price
    ''' 
    price = 0.0
    if C_P == True: #if call
        price = So*std_normal_dist_CDF(d1) - (k*std_normal_dist_CDF(d2))
    else: #if put
        price = k*std_normal_dist_CDF(-d2) - So*std_normal_dist_CDF(-d1)
    return round(price,4)

class Option:
    '''
    An object to represent an option
    '''
    def __init__(self,price = 0, c_p = True, position = True, So = 90, T = 0.25, sigma = 0.3,
                k = 90,delta = 0, r=0) -> None:
        self.C_P : bool = c_p #true if call
        self.Position : bool = position #true if long
        self.So : float = So #initial stock price
        self.T : float = T #time to expiration(years)
        self.sigma : float = sigma #volatility
        self.delta : float = delta #dividend payout at cont rate
        self.r : float = r #risk-free rate
        self.k : float = k #strike price
        self.d1 : float = (math.log(self.So / self.k) + #black-scholes formula
                        ((self.r - self.delta + self.sigma**2)/2)*self.T) / (self.sigma*math.sqrt(self.T))
        self.d2 : float = self.d1 - (self.sigma*math.sqrt(self.T)) #black-scholes
        if price == 0:
            self.price = theo_price(self.d1,self.d2,c_p,So,k) #if price is not predetermined
        else:
            self.price = price #if price is predetermined
        return None
    
    def get_volatility(self):
        '''
        returns a float of the volatility of the underlying asset
        '''
        return self.sigma

    def get_expiration_date(self):
        '''
        returns a float the expiration date
        '''
        return self.T

    def get_C_P(self):
        '''
        returns a boolean if call or put
        '''
        return self.C_P

    def get_strike_price(self):
        '''
        returns a float of the strike price of an option
        '''
        return self.k

    def get_position(self):
        '''
        returns a boolean if the position of the option is long or short
        '''
        return self.Position

    def get_stock_price(self):
        '''
        returns a float of the current stock price So
        '''
        return self.So

    def get_delta(self):
        '''
        returns a float of the annual cont dividend rate
        '''
        return self.delta

    def get_r(self):
        '''
        returns a float of the risk free rate
        '''
        return self.r

    def get_price(self):
        '''
        return a float of the price of the option
        '''
        return self.price

    def get_d1(self):
        '''
        returns the d1 of an option
        '''
        return self.d1

    def get_d2(self):
        '''
        returns the d2 of an option
        '''
        return self.d2

    def __lt__ (self,other) -> bool:
        '''
        determines which option strike-price is smaller
        '''
        return self.get_strike_price() < other.get_strike_price()
    def __gt__ (self,other) -> bool:
        '''
        determines which option strike-price is larger
        '''
        return self.get_strike_price() < other.get_strike_price()
      
    def __repr__(self) -> str:
        '''
        how to print
        '''
        price = str(self.get_price())
        stk_price = str(self.get_strike_price())
        ret_str = "Option Price: " + price + " Strike Price: " + stk_price
        return ret_str






