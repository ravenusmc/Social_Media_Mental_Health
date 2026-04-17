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
    sleep_vs_stress_data = []
    sleep_vs_stress_data = self.data[['Sleep_Quality(1-10)', 'Stress_Level(1-10)']].values.tolist()
    return sleep_vs_stress_data

  def detox_days_vs_stress(self):
    detox_days_vs_stress = []
    detox_days_vs_stress  = self.data[['Days_Without_Social_Media', 'Stress_Level(1-10)']].values.tolist()
    return detox_days_vs_stress 
  
  def exercise_vs_happiness(self):
    exercise_vs_happiness = [] 
    exercise_vs_happiness = self.data[['Exercise_Frequency(week)', 'Happiness_Index(1-10)']].values.tolist()
    return exercise_vs_happiness
  
  def social_media_graph(self):
    social_media_data = []


#🏃 4. Exercise Frequency vs. Happiness (Scatter / Line)

# **Type:** Scatter Plot (or Line if sorted)
# **X-axis:** Exercise_Frequency (week)
# **Y-axis:** Happiness_Index

# **Purpose:**
# Shows whether physical activity relates to happiness.

# **Expected Pattern:**
# More exercise → higher happiness



# Graph flow: 

# 1️⃣ Start: Age vs Screen Time - DONE 
# 2️⃣ Then: Screen Time vs Happiness - DONE 
# 3️⃣ Then: Sleep vs Stress  - Done 
# 4️⃣ Then: Detox Days vs Stress - Working 
# 5️⃣ Then: Exercise vs Happiness
# 6️⃣ End: Platform Comparison

obj = ExamineData()
obj.exercise_vs_happiness()