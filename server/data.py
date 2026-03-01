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
  
  def AgeVsScreenTime(self):
    AgeVsScreenData = []
    bins = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    labels = ['10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80-89']
    self.data['Age_Group'] = pd.cut(self.data['Age'], bins=bins, labels=labels, right=False)
    grouped = self.data.groupby('Age_Group', observed=False)['Daily_Screen_Time(hrs)'].mean().fillna(0)
    for age_group, avg_screen_time in grouped.items():
      AgeVsScreenData.append([str(age_group), round(avg_screen_time, 2)])
    print(AgeVsScreenData)
  
  def screen_time_vs_happeniness(self):
    screenvshappiness = []
    screenvshappiness = self.data[['Daily_Screen_Time(hrs)', 'Happiness_Index(1-10)']].values.tolist()
    return screenvshappiness



# **Type:** Scatter Plot
# **X-axis:** Daily_Screen_Time (hrs)
# **Y-axis:** Happiness_Index

# **Purpose:**
# Shows whether more screen time is associated with higher or lower happiness.

# **Insight You Might Find:**

# * Negative trend → more screen time, less happiness
# * Positive trend → screen time may not be harmful
# * No pattern → weak relationship




## 📈 7. Age vs. Screen Time (Scatter Plot)

# **Type:** Scatter Plot
# **X-axis:** Age
# **Y-axis:** Daily_Screen_Time

# **Purpose:**
# Shows generational differences in screen habits.

# **Possible Finding:**
# Younger users → more screen time

obj = ExamineData()
obj.screen_time_vs_happeniness()