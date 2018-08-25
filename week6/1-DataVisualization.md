# Data Visualization

> Data Visualization is the rending of data in a graphical or pictoral format
> It involves using visual elements like charts, maps, graphs etc..
> Data Visualization is the easiest and most popular way of identifying and understanding trend, patterns, outlier etc.. in the data
> Finding information ( like trends) in a massive spreadsheet might be a very difficult task, but if the data from the spreadsheet can be visualized trends can be spotted without much effort
> In the increasingly data driven world, data visualization is a very important skill to have


**Data Visualization in Python**

> There multiple libraries available for Data Visualization
> Some popular ones are : matplotlib, plotly, seaborn, bokeh


**Matplotlib**

> matplotlib is one of the oldest and most popular library
> Pandas is natively integrated with matplotlib
> Pandas data structures like Series and Dataframes can be visualized using matplotlib

**Installation**
```
pip install matplotlib
```

**Basic Usage**

```python
#Assume df is a pandas dataframe

#Plot the DF
df.plot()

```

> In Pycharm or other IDE's, the following method is used to render the graphic

```python

import matplotlib.pyplot as plt

#Assume df is a pandas dataframe

#Plot the DF
df.plot()

#render the graphics
plt.show()

```


**Example**

```python

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({"Population": [160000, 165000, 178000, 190000, 192000,210000, 212000, 225000],
"Year": [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]})

df.plot(x='Year', y='Population')

plt.show()

```


**Types of Charts**

> There are multiple different types of charts
> Some popular ones that can be plotted using matplotlib are :
> line
> bar
> area
> histogram
> pie

**Bar chart Example**

```python

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({"Population": [160000, 165000, 178000, 190000, 192000,210000, 212000, 225000],
"Year": [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]})

df.plot(x='Year', y='Population', kind='bar')

plt.show()

```
