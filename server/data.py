#Main file to examine the CSV data. 

# importing supporting libraries
import numpy as np
import pandas as pd
import calendar
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

class ExamineData():
  
  def __init__(self): 
    self.data = pd.read_csv('./data/Mental_Health_Dataset.csv')

  def test(self):
    print(self.data.head())
  
  def AgeVsScreenTime(self):
    pass




## 📈 7. Age vs. Screen Time (Scatter Plot)

# **Type:** Scatter Plot
# **X-axis:** Age
# **Y-axis:** Daily_Screen_Time

# **Purpose:**
# Shows generational differences in screen habits.

# **Possible Finding:**
# Younger users → more screen time

obj = ExamineData()
obj.test()