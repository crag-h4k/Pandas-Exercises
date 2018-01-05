#basics of python data visualization tutorial on Lynda.com
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

from numpy.random import randn
from pandas import Series, DataFrom
from matplotlib import rcParams

#this is for Jupyter Notebook
%matplotlib inline
rcParams['figure.figsize']= 5, 4
sb.set_style('whitegrid')

x= range(1,10)
y = [1,2,3,4,0,4,3,2,1]
plt.plot(x,y)

address = 'mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
mpg = cars['mpg']

mpg.plot()

df = cars[['cyl', 'wt', 'mgp' ]]
df.plot()

plt.bar(x,y)

mpg.plot(kind='bar')

mpg.plot(kind='barh')

plt.pie(mpg)
plt.show()

plt.savefig(plt.savefig('pie_chart.jpeg')
