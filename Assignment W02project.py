import numpy as np
import math
import pandas as pd

import nsepy

from datetime	import date
from nsepy import get_history
sbin = get_history(symbol='SBIN',
                   start=date(2015,1,1),
                   end=date(2015,1,10))

print (sbin)



vix = get_history(symbol="INDIAVIX",
            start=date(2015,1,1),
            end=date(2021,1,10),
            index=True)
print (vix)


import matplotlib.pyplot as plt

data = get_history(symbol='SBIN',
                   start=date(2020,1,1),
                   end=date(2020,1,28))


data['Close'].plot()

plt.show()




















