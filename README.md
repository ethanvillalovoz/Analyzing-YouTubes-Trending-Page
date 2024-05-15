# CPTS-315-CougCoders

Introduction to Data Mining

Project Name: Analyzing YouTube’s Trending Page

Instructor: Dr. Honghao Wei

Contributors: Ethan Villalovoz, Logan Sutton, Berkeley Conkling, Roy Zabetski, Kyle Hawkins, Chance Bradford, Matthew Bruggeman, Wenjie Wang, Silvestre Pamatz-Rangel

# Summary

YouTube is one of the largest online entertainment industries. Anyone with a Google account can upload short and long-form videos to the platform. People who have found success on the platform, often called content creators, post videos and hope to make it on YouTube’s trending page. What do all of these trending videos have in common? What statistics make the YouTube algorithm classify a video as trending? We want to allow content creators to understand what makes a video get on the YouTube trending page.

Our research will use:

    Association Rule Mining (Apriori)

    Linear Regression

    Logistic Regression


# Repository and Installation setup

- All software used to run our Jupyter Notebooks is in Google Colab.
    - You could also open the Jupyter Notebooks within Visual Studio Code with Jupyter Notebook installed on your device; however, we will not cover how to install/set up that method.
- To access Google Colab, you only need a Gmail account, which you can use for your current or personal email.
    - Here is the website for Google Colab: https://colab.google/
- Download the Jupyter Notebooks along with the clean .csv files (data) from the 'cleaned_data' folder to your local machine.
- Once you have opened Google Colab, on the main website click 'open colab'. This will take you to a new page and prompt you with a box having multiple section tabs.
- Click the 'Upload' tab and select the Jupyter Notebooks on your local machine.
    - Within the Jupyter Notebooks, there will be a cell that you can run that will allow you to choose the .csv files (data files) which you will select and be uploaded within the respective Jupyter Notebook project.

# Original Data Set

For this project, we used the Kaggle Data Set 'Trending YouTube Video Statistics and Comments.' Within this folder, it contains all of the raw data. For further information, you can view the website: https://www.kaggle.com/datasets/datasnaek/youtube

# Cleaned Data (Pre-Processing Data)

This folder contains all the cleaned data we used from the Kaggle Data Set 'Trending YouTube Video Statistics and Comments.' For this project, we only used the 'UScomments.csv' and 'USvideos.csv' because we believed that these were the most relevant to our audience.

Issues that were in these .csv files were:

- Rows were missing newline separators
- Rows were missing columns
- Rows contained extraneous columns
- Rows were missing closing quotes

We resolved these issues by:

- When it is clear that a single newline and nothing else has been lost, it is reinserted in the correct position.
- When a row is missing columns, the entire row is removed.
- When a single item (video or comment) spans multiple rows, all relevant rows are removed because the item is usually abruptly cut off.
- Any row that contains a CSV header in it is removed because some columns are always cut off.
- Columns in rows that are missing a closing quote are removed because we have to assume that the rest of the text is missing.
- Any extraneous columns in rows will be removed if and only if the column can be extracted cleanly.

# Notebooks

- [apriori.ipynb](notebook/apriori.ipynb)
    Uncovers frequent item sets or patterns among categorical variables like video tags or categories. This helps identify associations between different attributes and understand viewer preferences.
- [regression.ipynb](notebook/regression.ipynb)
    Models the relationship between numerical variables such as views, likes, and comments. It helps understand how changes in one variable affect another, thus providing insights into factors influencing video popularity.
- [relationship_analysis.ipynb](notebook/relationship_analysis.ipynb)
    Finds relationships between numerical data categories in terms of strength and direction of the linear relationship between two variables and generates accompanying graphs.

# Documents

For more information on our project, you can view the following documents for an in-depth analysis of our findings:

- Presentation
- Final Report Abstract
- Final Report

