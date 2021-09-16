from definitions import predict_value
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np
from numpy import loadtxt
import time
from functools import reduce
import _pickle

#def convert_date(date_bytes):
#    return mdates.strpdate2num('%Y%m%d%H%M%S')(date_bytes.decode('ascii'))
    
date,bid,ask = np.loadtxt('C:\\python files\\Pattern Recognition\\pattern_final\\thread_count.csv', unpack=True,
                                  delimiter=',')
#,
#                                  converters={0:convert_date}
dataLength = int(bid.shape[0])
print('data length is', dataLength)
    
allData = ((bid+ask)/2)
    
toWhat = 2700


predict_value(toWhat,dataLength,bid,ask)


