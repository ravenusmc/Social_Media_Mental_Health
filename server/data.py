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
  
  def sleep_vs_stress(self):
    sleep_vs_stress = []
    sleep_vs_stress = self.data[['Sleep_Quality(1-10)', 'Stress_Level(1-10)']].values.tolist()
    return sleep_vs_stress

## 😴 2. Sleep Quality vs. Stress Level (Scatter Plot)

# **Type:** Scatter Plot
# **X-axis:** Sleep_Quality
# **Y-axis:** Stress_Level

# **Purpose:**
# Explores whether better sleep relates to lower stress.

# **Likely Hypothesis:**
# Higher sleep → lower stress



obj = ExamineData()
obj.screen_time_vs_happeniness()