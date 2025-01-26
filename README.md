# <ins>*ClassFit*</ins> - booking system

## <ins>About ClassFit</ins>
ClassFit is an online booking system for a local gym that allows the coaches to create classes/event and allows the users to book on to these and log their results/scores.

This project will be used as my capstone project for the Code Institute skills bootcamp. It will be a full stack python django application.

The target user for this project will be a gym owner who runs a gym like the CrossFit gym I attend. This is where they have regular classes and times and these can be managed by the owner and their clients can reserve spaces and log progress.

<ins>Deployed site link: </ins>[ClassFit](https://classfit-9bcca60104a7.herokuapp.com/)

## <ins>Contents</ins>

- [Features](#features)
- [Project planning](#project-planning)
- [Technologies used](#technoglogies-used)
- [Testing](#testing)
- [Impact of AI Analysis](#impact-of-ai-analysis)
- [Credits](#credits)
- [Evaluation](#evaluation)


## Features

### Main functionality
For the ClassFit app the key features are the coach being able to set up the classes and for the user to book onto the class. These classes are displayed and styled using bootstrap for quicker development speed. The classes are displayed in the booking app and the events for each day are displayed under the corresponding date and are ordered chronologically. 

For the user the booking button is displayed and they can click on the button to book onto the event or click on the event title to view the event details. For the coach the cancel button is displayed to delete the event from the database.

The coach also has an additional button which is the create event button that can be used to access the form to add a class. The coach also has access to an edit event button when viewing the event details. This takes them to a similar form that can be used to adjust the details of that event.

### The logbook

The app also provides access to the logbook. The log displays a form to submit scores for exercises. These scores consist of exercise name, number of reps and the weight in kilograms. The score can then be added to the database. The three most recent scores are presented next to the form and below is a list of all the users scores. Each score can also be edited or deleted.

### Homepage

The homepage is used to display the users three soonest upcoming bookings and most recent scores. Below this is the leaderboard. The leaderboard accesses all the scores from all users and can be filtered through for each exercise, the minimium weight and reps.

### Nav bar

The nav bar has fully functioning links to different pages.

### Login functionality

The app has full user authentication.

### Footer

The footer has links that currently redirect to the top of the page. This can be replaced with the gyms real social media links and address.

## Project Planning

### User Stories

This project was developed using an agile methodology. To include this in the project I created a project board with relevant user stories.

These user stories were created to demonstrate who the main user of each feature is, what the feature will do and why this is beneficial and is followed by an acceptance criteria.


### include user stories

### URL planning

For this project the URL and navigation planning was essential as this could cause many issues during development if it was not thought out and followed a logical flow. So for each app they would have their own urls file.

'' - used to display the log in/ sign up page

<ins>**Booking app:**</ins>

- 'booking/*datestring*' - used to display the available classes on a given date
- 'booking/*datestring*/*eventid*' - used to display the event details of the selected event

- <ins>*additional*</ins> 'booking/*datestring*/add' - used by only selected users to add classes on a specific date

<ins>**Log Book app:**</ins>

- 'logbook/' - used to go to the main logbook page that displays scores and new score form
- 'logbook/update/' - used to display form to enter an edited score

<ins>**Home app:**</ins>

'home/' - used to display the home page after log in then using the nav bar and buttons on the home page view the other apps


## Technoglogies Used

The site was deployed using **heroku web servcies** and used **GitHub** for version control.

ClassFit was developed using the python framework **Django** on the backend working with a **Postgres database**. For the frontend I made use of **HTML**, **CSS**, **Javacript** and I also used the **bootstrap framework** to improve development speed and allow the project to be responsive. Another key factor in speeding up the devlopment was the use of AI. The main AI tools used where ChatGPT and Github Copilot. I will go into further detail about the impact of these tools [here.](#impact-of-ai-analysis)



## Testing

### HTML Validation
All the pages passed with the following message:
![image](readMe-images/HTML-validation.png)

### CSS Validation 

![image](readMe-images/CSS-validation.png)

### Python Standards

Main python:
- Each python file has been validated to pep8 standards 

Testing python:
- None












## Impact of AI Analysis

The main tools used:

 - ChatGPT
 - Github Copilot

 ### What these tools added to the project

 ChatGPT was great for me to brainstorm ideas. It could feedback to me the positives and negatives of an idea such as the structure of a model for the database. In this example it might say that using an integer for the Id was a good idea but gave me the correct naming convention to use djangos autoincrementing Id feature. This cut development time for because I didn't have to code this myself but also it was able to tell me features I had forgotten or didn't even know existed.

 Furthermore, Copilot was able to help me debug code. Where I haven't got the syntax memorised or I'm missing a small detail copilot was great for jumping in and correcting these mistakes.

 ### What were the downsides

 The greatest risk when using Copilot was from my own use of the tool. It was important to make sure you can understand the changes copilot has made. With this in mind I found that I didn't run into many issues as I refused to add any code in that I wasn't sure of but with that said I made a mistake with ChatGPT that did use up some development time.

 When using ChatGPT it gave me some code snippets for an idea that I had been talking through for the events/classes booking system. For my project I used different variable names and this caused confusion and I had to go through and change them.

 Another frustrating part was when passing the date from django to javascript it initially struggled to change the date format to the required format.


## Credits

Thanks to [Code Institute](https://github.com/Code-Institute-Solutions/blog/tree/main/11_authorisation/03_custom_template/templates) for the log in and sign up page templates

 ## Evaluation