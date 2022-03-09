import os
from pathlib import Path
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image



image = Image.open('/Users/dc/desktop/flatiron/projects/Capstone-Disney-World-Date-and-Attendance-Predictor/Streamlit_App/disney_parks.jpeg')

# st.image(image, caption='wdw')

pd.set_option("display.max_rows", None, "display.max_columns", None)

parks = {'magic_kingdom': ['seven_dwarfs_train', 'pirates_of_caribbean', 'splash_mountain'], 'animal_kingdom' : ['dinosaur' , 'expedition_everest', 'kilimanjaro_safaris', 'navi_river'], 'epcot' : ['soarin', 'spaceship_earth'], 'hollywood_studios': ['rock_n_rollercoaster', 'toy_story_mania']}

def convert_date(date, day = True):
    date = datetime.strptime(date, "%Y-%m-%d")
    if day == True:
        date = f'{date.strftime("%A")}, {date.strftime("%B")} {date.day}, {date.year}'
    else:
        date = f'{date.strftime("%B")} {date.day}, {date.year}'  
    return date

datapath = Path.cwd() 
print(datapath)

datasets = os.listdir(datapath)
datasets = list(sorted([i for i in datasets if ".csv" in i]))
print(datasets)

for i in datasets:
    try:
        print(i)
        exec(f"{i.split('.csv')[0]} = pd.read_csv(datapath / i)")
    except:
        print(f"{i} cannot be imported automatically")



#Add sidebar to the app
st.sidebar.markdown("### Aloha!")
st.sidebar.markdown("Welcome to the Disney Day app! This app is designed to predict whether the day you would like to go to a particular park in Disney World is a good day to go! This app uses data sourced from touringplans.com. I hope you enjoy!")

#Add title and subtitle to the main interface of the app
st.title("Walt Disney World Predictor")
st.markdown("Did you know that there are 58 million people that go to Disney World in Orlando, FL every year? It is no secret that some days are incredibly busier than others and lines can seem like a mile long. Visitors spend tons of money to provide an unforgettable experience for their family and want to have a great time. Depending on the time of year you go, that experience can be absolutely magnificient, if the timing is great! I want you to have that same unforgettable experience!")
st.markdown("Input the date of your planned visit, along with the park you would like to attend. The algorithm will work its magic and tell you whether it is a great day to go, or not!")

park_names = []
park_names_lower = []
for i in parks.keys():
    name = i.split("_")
    name = [j[0].upper()+ j[1:] for j in name]
    name = " ".join(name)
    # print(name)
    park_names.append(name)
    park_names_lower.append(i)

selected_park = st.selectbox("Select Park", park_names)


park_idx = park_names.index(selected_park)
park_name = park_names_lower[park_idx] 
best_days = eval(f'best_days_for_{park_name}')
park_data = eval(f'{park_name}_data')
dates = list(best_days["ds"])
now = datetime.now()
date = now
dates = []
while date <= now + timedelta(weeks= 52):
    dates.append(f'{date.year}-{date.month}-{date.day}')
    date += timedelta(days = 1)
dates_human = [convert_date(i, day = False) for i in dates]
selected_date = st.selectbox("Select Date", dates_human)
selected_date = dates[dates_human.index(selected_date)]    

best_metrics = best_days.groupby(by = ['month', 'week', 'weekday']).count();
# display(best_metrics.sort_values('y', ascending = False))
# display(best_metrics)


dt = datetime.strptime(selected_date, '%Y-%m-%d')
month = dt.month
week = dt.isocalendar()[1]
day = dt.weekday()
print(month, week, day)


try:
    x = best_metrics.loc[month, week, day];
    print(f'{convert_date(selected_date)} is a good day to go to the park!')
    st.markdown(f'{convert_date(selected_date)} is a good day to go to the park!')
except KeyError:
    print(f'{convert_date(selected_date)} is a bad day to go to the park!')
    st.markdown(f'{convert_date(selected_date)} is a bad day to go to the park!')

park_data['ds'] = pd.to_datetime(park_data['ds'])
park_data['y']/=len(parks[park_name])
park_data_plot = park_data.loc[park_data['ds'] > now]
print(park_data_plot.head())
park_data_plot.columns = ['Date', 'Wait Time (m)']
park_data_plot.set_index('Date', inplace = True)
st.bar_chart(park_data_plot)

