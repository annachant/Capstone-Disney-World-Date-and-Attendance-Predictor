# Disney World Date and Attendance Predictor

![Disney Parks](https://github.com/annachant/Capstone-Disney-World-Date-and-Attendance-Predictor/blob/main/images/disney%20parks.jpeg)

## Project Overview

There are 58 million people that go to Disney World in Orlando, FL every year. It is no secret that some days are incredibly busier than others and lines can seem like a mile long. Vi sitorsspend tons of money to provide an unforgettable experience for their family and want to have a great time. Depending on the time of year they go, that experience can be absolutely magnificient. I want people to have the same unforgettable experience with their loved ones as I have had in the past, without all the extra worries that can be avoidable, if planned correctly. 

Using the dataset, I will predict when the perfect time is to go to Disney World's 4 parks:

<ul>
  <li>Magic Kingdom</li>
  <li>Epcot</li>
  <li>Hollywood Studios</li>
  <li>Animal Kingdom</li>
  </ul>


### Business Problems

These were my guiding questions in which my project was modeled:

<ul>
  <li>When is the most ideal time to go to Disney World to avoid long lines with kids?</li>
  <li>When is the most ideal time to go to Disney World to avoid long lines without kids?</li>
  <li>When is the most ideal time to go to a specific Disney park: Magic Kingdom, Epcot, Hollywood Studios, Animal Kingdom?</li>
  <li>What is the best time to ride a particular ride?</li>
  <li>On a given day, is it a good day to go to that particular theme park?</li>
  </ul>
  
### Recommendations

I will recommend the following:

# Data
![databanner](https://github.com/annachant/Capstone-Disney-World-Date-and-Attendance-Predictor/blob/main/images/data-science-banner.jpeg)

The dataset was obtained from https://touringplans.com/walt-disney-world/crowd-calendar#DataSets. It contains wait time information that was collected every 5-10 minutes for the top rides in Disney World from January 2015 to Dec 2021. There are wait times for the following 12 rides across all 4 parks:

<ul>
  <li>Magic Kingdom</li>
      - Seven Dwarfs Mine Train 
  <br>
      - Pirates of the Caribbean
  <br>
      - Splash Mountain
   <br>
  <br>
  
  <li>Epcot</li>
      - Soarin
  <br>
      - Spaceship Earth
  <br>
  <br>
  
  <li>Hollywood Studios</li>
      - Rock n Rollercoaster
  <br>
      - Slinky Dog Ride
  <br>
      - Toy Story Mania
  <br>
  <br>
  
  <li>Animal Kingdom</li>
      - Dinosaur
  <br>
      - Expedition Everest
  <br>
      - Kilimajaro Safari
  <br>
      - Navi River
  </ul>



## Exploratory Data Analysis 

The data was cleaned for all 12 csv files and the following was completed in order to get the most accurate and best analysis:
<ul>
<li>The data used used for the analysis was from 1/1/2015 to 12/31/2019 </li>
  <li>Data was resampled from every 5/10 minutes per day to a daily average per day </li>
 <li>Slinky dog ride was excluded from the analysis due to it beung newer and there is not enough data to make asn accurate prediction</li>
  </ul>

# Modeling & Evaluation
![ML](https://github.com/annachant/Capstone-Disney-World-Date-and-Attendance-Predictor/blob/main/images/ML.jpeg)
Many different techniques were used, including Arima, Sarimax, Random Forest, and Facebook Profit. Ultimately, Facebook Profit had the best results.
This was used to build the final models and make predictions. Many models were tested, but a grid search yielded the best results. The results showed even more improvement when the US Holiday Calender was added into the model with the best parameters from the grid search. 

Below are the results comparing the base model(1), the best parameters from the grid search(2), and those same parameters with the US Holiday Calendar added to the parameters(3):
<br>
![mape](https://github.com/annachant/Capstone-Disney-World-Date-and-Attendance-Predictor/blob/main/images/Screen%20Shot%202022-03-08%20at%2012.45.29%20AM.png)

## Best Disney Day by Attraction

Once the optimal parameters were applied and we take a close look at the results, a very noticeable trend is present for all the rides:
![forecast model](https://github.com/annachant/Capstone-Disney-World-Date-and-Attendance-Predictor/blob/main/images/Screen%20Shot%202022-03-08%20at%201.31.26%20AM.png)

When looking at the rides individually, similar to the model above, September is the most optimal best time . This is true in all cases, except for one ride - Splash Mountain. The best time to go ride on Splash Mountain is in January. According to weatherspark.com, the coldest month of the year in Orlando is January, with an average low of 52°F and high of 71°F. It is very understandble why guests may not want to get soaking wet during a cold month! See below for Splash Mountain:

![splashmountain](https://github.com/annachant/Capstone-Disney-World-Date-and-Attendance-Predictor/blob/main/images/Screen%20Shot%202022-03-08%20at%208.23.58%20AM.png)

## Best Disney Day by Park

### Magic Kingdom

### Epcot

### Hollywood Studios

### Animal Kingdom

## Best Disney Day with Kids

Some days are better than others to attend the park if you have children in your family. I took a look at this by making a forecast using kid friendly rides that are geared more towards children. There is also a very obvious trend of the best days being in the 2nd or 3rd week of September. 

### Magic Kingdom

![mkkids](https://github.com/annachant/Capstone-Disney-World-Date-and-Attendance-Predictor/blob/main/images/Screen%20Shot%202022-03-08%20at%209.50.25%20AM.png)

### Epcot

![epcotkids](https://github.com/annachant/Capstone-Disney-World-Date-and-Attendance-Predictor/blob/main/images/Screen%20Shot%202022-03-08%20at%2010.06.07%20AM.png)

### Hollywood Studios

![HSkids](https://github.com/annachant/Capstone-Disney-World-Date-and-Attendance-Predictor/blob/main/images/Screen%20Shot%202022-03-08%20at%2010.07.20%20AM.png)

### Animal Kingdom

![AKkids](https://github.com/annachant/Capstone-Disney-World-Date-and-Attendance-Predictor/blob/main/images/Screen%20Shot%202022-03-08%20at%2010.08.16%20AM.png)

## Best Disney Day without Kids

### Magic Kingdom

### Epcot

### Hollywood Studios

### Animal Kingdom

# Conclusion & Recommendations
![banner](https://github.com/annachant/Capstone-Disney-World-Date-and-Attendance-Predictor/blob/main/images/banner5.jpeg)



# Next Steps
![crowds](https://github.com/annachant/Capstone-Disney-World-Date-and-Attendance-Predictor/blob/main/images/crowds.jpeg)

