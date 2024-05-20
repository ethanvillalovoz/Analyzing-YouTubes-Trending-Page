# CPTS-315-CougCoders

## Introduction to Data Mining

### Project Name: Analyzing YouTube’s Trending Page

#### Instructor: Dr. Honghao Wei

#### Contributors: Ethan Villalovoz, Logan Sutton, Berkeley Conkling, Roy Zabetski, Kyle Hawkins, Chance Bradford, Matthew Bruggeman, Wenjie Wang, Silvestre Pamatz-Rangel

## Project Description 

YouTube is one of the largest online entertainment industries. Anyone with a Google account can upload short and long-form videos to the platform. People who have found success on the platform, often called content creators, post videos and hope to make it on YouTube’s trending page. What do all of these trending videos have in common? What statistics make the YouTube algorithm classify a video as trending? We want to allow content creators to understand what makes a video get on the YouTube trending page.

### Repository Contents

This repository contains all the work completed by the CPTS-315 CougCoders team for the final project. It includes notebooks, documentation, and cleaned data used for the analysis.

### Repository & Installation Setup

- All software used for this project is hosted on Google Colab. Simply follow the provided instructions to access and run the Jupyter Notebooks.
- Ensure you have the necessary data files (`UScomments.csv` and `USvideos.csv`) downloaded from the 'cleaned_data' folder to your local machine.

### Data Description

The data used for this project is sourced from the Kaggle dataset 'Trending YouTube Video Statistics and Comments.' It contains information about video statistics and comments. We preprocessed the data to address issues such as missing values and extraneous columns.

### Notebooks

- [apriori.ipynb](notebooks/apriori.ipynb)
    Uncovers frequent item sets or patterns among categorical variables like video tags or categories. This helps identify associations between different attributes and understand viewer preferences.
- [regression.ipynb](notebooks/regression.ipynb)
    Models the relationship between numerical variables such as views, likes, and comments. It helps understand how changes in one variable affect another, thus providing insights into factors influencing video popularity.
- [relationship_analysis.ipynb](notebooks/relationship_analysis.ipynb)
    Finds relationships between numerical data categories in terms of strength and direction of the linear relationship between two variables and generates accompanying graphs.

### Documentation 

For more information on our project, you can view the following documents for an in-depth analysis of our findings:

- [Presentation](documentation/presentation.pdf)
- [Final Report Abstract](documentation/CPT_S-315-Final-Report-Abstract.pdf)
- [Final Report](documentation/CPT_S-315-Final-Report.pdf)
