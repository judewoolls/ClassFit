# <ins>*ClassFit*</ins> - booking system

## <ins>About ClassFit</ins>
ClassFit is an online booking system for a local gym that allows the coaches to create classes/events and allows the users to book onto these and log their results/scores.

This project will be used as my capstone project for the Code Institute skills bootcamp. It will be a full stack Python Django application.

The target user for this project will be a gym owner who runs a gym like the CrossFit gym I attend. This is where they have regular classes and times, and these can be managed by the owner and their clients can reserve spaces and log progress.

<ins>Deployed site link: </ins>[ClassFit](https://classfit-9bcca60104a7.herokuapp.com/)

## <ins>Contents</ins>

- [Features](#features)
- [Project planning](#project-planning)
- [Technologies used](#technologies-used)
- [Testing](#testing)
- [Impact of AI Analysis](#impact-of-ai-analysis)
- [Credits](#credits)
- [Evaluation](#evaluation)

## Features

### Main functionality
For the ClassFit app, the key features are the coach being able to set up the classes and for the user to book onto the class. These classes are displayed and styled using Bootstrap for quicker development speed. The classes are displayed in the booking app, and the events for each day are displayed under the corresponding date and are ordered chronologically.

For the user, the booking button is displayed, and they can click on the button to book onto the event or click on the event title to view the event details. For the coach, the cancel button is displayed to delete the event from the database.

The coach also has an additional button which is the create event button that can be used to access the form to add a class. The coach also has access to an edit event button when viewing the event details. This takes them to a similar form that can be used to adjust the details of that event.

### The logbook

The app also provides access to the logbook. The log displays a form to submit scores for exercises. These scores consist of exercise name, number of reps, and the weight in kilograms. The score can then be added to the database. The three most recent scores are presented next to the form, and below is a list of all the user's scores. Each score can also be edited or deleted.

### Homepage

The homepage is used to display the user's three soonest upcoming bookings and most recent scores. Below this is the leaderboard. The leaderboard accesses all the scores from all users and can be filtered through for each exercise, the minimum weight, and reps.

### Nav bar

The nav bar has fully functioning links to different pages.

### Login functionality

The app has full user authentication.

### Footer

The footer has links that currently redirect to the top of the page. This can be replaced with the gym's real social media links and address.

## Project Planning

### User Stories

This project was developed using an agile methodology. To include this in the project, I created a project board with relevant user stories.

These user stories were created to demonstrate who the main user of each feature is, what the feature will do, and why this is beneficial and is followed by an acceptance criteria.

### Classes displayed chronologically

As a gym member, I want to see the classes displayed in chronological order by date and time so that I can easily find and plan for upcoming sessions.

Acceptance criteria

- Classes are sorted by date in ascending order, with the earliest date appearing first.
- Classes on the same date are further sorted by their start time.
- Past classes are not displayed in the list of upcoming classes.
- The class list updates dynamically as new classes are added or past classes expire.

### Create a log in page

As a gym member, I want to log in securely so that I can access personalised features like booking and managing my classes.

Acceptance criteria

- The application has a dedicated login page accessible from the navigation bar or homepage.
- Users log in using their email/username and password.
- Login credentials are validated securely, and incorrect credentials display an appropriate error message.
- Upon successful login, users are redirected to the main dashboard or class listing page.
- Logged-in users can access personalised features, such as viewing their bookings and managing reservations.
- Logged-in users remain authenticated until they log out or their session expires.
- A "Remember Me" option is available for convenience (optional).

### Use the book button to create a booking

As a gym member, I want to use a "Book" button to reserve a spot in a class so that I can easily secure my place.

Acceptance criteria

- Each class displays a "Book" button if there are remaining spots available.
- Clicking the "Book" button creates a booking for the logged-in user.
- After booking, the system updates the remaining capacity for the class.
- If a class is fully booked, the "Book" button is disabled or replaced with a "Fully Booked" label.
- A confirmation message is displayed to the user after a successful booking.

### User Authentication

As a gym member or admin, I want to securely log in and out of the platform, so that I can access my personal bookings, scores, and other features relevant to my role.

Acceptance criteria

- Role-Based Access: Upon login, users are directed to their dashboard, and features are customised based on their role (e.g., member or admin).
- Authentication Feedback: Users see feedback such as “Logged in successfully” or “Incorrect password.”

### Display the class capacity

As a gym member, I want to see the total capacity of a class and the number of remaining spots so that I can know if I can book a place.

Acceptance Criteria:

- Each class displays the total capacity (e.g., "Capacity: 20").
- The number of remaining spots is displayed dynamically (e.g., "Spots Available: 5").
- If the class is fully booked, it clearly shows "Fully Booked" instead of available spots.
- The displayed capacity and remaining spots update automatically as users book or cancel classes.

### Coaches can manage classes

As a Coach, I can add classes so that my clients can book onto events.

Acceptance criteria

- A visible add classes button (only visible to coaches)
- This takes to form and can add event
- Events can be edited/updated
- Events can be deleted

### Display cancel button if already booked

As a gym member, I want to see a "Cancel" button for classes I’ve already booked so that I can easily manage my reservations.

Acceptance criteria

- If the user has already booked a class, the "Cancel" button is displayed instead of the "Book" button.
- Clicking the "Cancel" button removes the user's booking for that class.
- After cancellation, the system updates the remaining capacity for the class.
- A confirmation message is displayed after a successful cancellation.
- The "Cancel" button is replaced with the "Book" button once the user cancels their booking.

### Add a logbook form to submit scores

As a gym member, I want a logbook to record the weights and reps I complete during workouts so that I can track my progress over time.

Acceptance criteria

- A "Logbook" page is accessible from the navigation bar.
- Users can log the following details for each entry:
  - Date
  - Exercise name
  - Weight (kg or lbs)
  - Number of reps
  - Notes (optional)
- Logs are saved to the database and displayed in a list ordered by date (most recent first).
- Users can edit or delete previous entries.
- If no entries exist, a message like "No logs yet. Start tracking your workouts!" is displayed.

### Add an edit feature to change logbook scores

As a gym member, I want to edit my logbook entries so that I can correct mistakes or update my progress as needed.

Acceptance criteria

- Each log entry has an "Edit" button next to it.
- Clicking the "Edit" button takes the user to a form pre-filled with the log entry details.
- The user can change the exercise name, weight, reps, and notes.
- Changes are saved to the database and reflected immediately in the logbook.
- A confirmation message is displayed after successful edits.

### Display recent scores in logbook

As a gym member, I want to see my most recent scores at the top of the logbook so that I can quickly view my latest progress.

Acceptance criteria

- The most recent log entries appear at the top of the logbook page.
- Recent scores are displayed with their exercise name, weight, reps, and date.
- If no entries exist, a message like "No recent scores available" is shown.

### Homepage

As a gym member, I want the homepage to display my upcoming bookings and recent scores so that I can stay updated on my schedule and track my progress.

Acceptance criteria

- The homepage is the first page users see after logging in.
- The "Upcoming Bookings" section lists all the classes the user has booked, ordered by date and time (soonest first).
- Each booking includes the class name, date, time, and location (if applicable).
- If there are no upcoming bookings, the section displays a message like "No upcoming bookings."
- The "Recent Scores" section displays the user's latest performance scores (e.g., workout results, personal bests).
- Each score includes the event name, date, and score achieved.
- If there are no scores, the section displays a message like "No recent scores."
- Both sections are styled for clarity and responsive design.

### Compare scores to other users

As a gym member, I want to compare my performance scores with other gym members, so that I can gauge how my progress measures up against others and stay motivated.

Acceptance criteria

- There should be a leaderboard showing the top-performing gym members based on certain scores (e.g., highest weight lifted, fastest time, most reps, etc.).
- The leaderboard should be sortable by different categories (e.g., by exercise, by date range, by total score).

### URL planning

For this project, the URL and navigation planning was essential as this could cause many issues during development if it was not thought out and followed a logical flow. So for each app, they would have their own URLs file.

'' - used to display the log in/ sign up page or the homepage

<ins>**Booking app**</ins>

- 'booking/*datestring*' - used to display the available classes on a given date
- 'booking/*datestring*/*eventid*' - used to display the event details of the selected event
- <ins>*additional*</ins> 'booking/*datestring*/add' - used by only selected users to add classes on a specific date

<ins>**Log Book app:**</ins>

- 'logbook/' - used to go to the main logbook page that displays scores and new score form
- 'logbook/id/' - used to display form to enter an edited score

<ins>**Home app:**</ins>

'home/' - used to display the home page after log in then using the nav bar and buttons on the home page view the other apps

## Technologies Used

The site was deployed using **Heroku web services** and used **GitHub** for version control.

ClassFit was developed using the Python framework **Django** on the backend working with a **Postgres database**. For the frontend, I made use of **HTML**, **CSS**, **JavaScript**, and I also used the **Bootstrap framework** to improve development speed and allow the project to be responsive. Another key factor in speeding up the development was the use of AI. The main AI tools used were ChatGPT and GitHub Copilot. I will go into further detail about the impact of these tools [here.](#impact-of-ai-analysis)

## Testing

### HTML Validation
All the pages passed with the following message:
![image](readMe-images/HTML-validation.png)

### CSS Validation 

![image](readMe-images/CSS-validation.png)

### Python Standards

Main Python:
- Each Python file has been validated to PEP8 standards 

Testing Python:
- Each Python file has been validated to PEP8 standards

### Automated unit tests

The project has a total of 26 unit tests to test the functionality of the application. As of the most recent deployment all of the tests pass. The tests uses mock data on a separate database used exclusively for testing to avoid the test affecting the database for the deployed site.

> Here is the result of running the tests:
>
> ![image](readMe-images/unit-test.png)

## Impact of AI Analysis

> The main tools used:
>
> - ChatGPT
> - GitHub Copilot

### What these tools added to the project

ChatGPT was great for me to brainstorm ideas. It could feedback to me the positives and negatives of an idea such as the structure of a model for the database. In this example, it might say that using an integer for the ID was a good idea but gave me the correct naming convention to use Django's auto-incrementing ID feature. This cut development time for me because I didn't have to code this myself but also it was able to tell me features I had forgotten or didn't even know existed.

Furthermore, Copilot was able to help me debug code. Where I haven't got the syntax memorised or I'm missing a small detail, Copilot was great for jumping in and correcting these mistakes.

### What were the downsides

The greatest risk when using Copilot was from my own use of the tool. It was important to make sure you can understand the changes Copilot has made. With this in mind, I found that I didn't run into many issues as I refused to add any code in that I wasn't sure of but with that said I made a mistake with ChatGPT that did use up some development time.

When using ChatGPT, it gave me some code snippets for an idea that I had been talking through for the events/classes booking system. For my project, I used different variable names and this caused confusion and I had to go through and change them.

Another frustrating part was when passing the date from Django to JavaScript it initially struggled to change the date format to the required format.

## Credits

>Thanks to [Code Institute](https://github.com/Code-Institute-Solutions/blog/tree/main/11_authorisation/03_custom_template/templates) for the log in and sign up page templates

>The browser icon: [Gymnastic icons created by Hexagon075 - Flaticon](https://www.flaticon.com/free-icons/gymnastic)

## Evaluation

The ClassFit project successfully meets all the acceptance criteria outlined in the user stories and passes all validation and feature tests. The project was significantly enhanced with the use of AI, specifically GitHub Copilot, which streamlined the development process and improved code quality.

### Key Achievements

1. **User and Coach Features**: The project effectively differentiates between users and coaches, providing tailored features for each role. Users can book classes, track their progress, and view their scores, while coaches can create and manage events.

2. **User Experience**: The user interface is intuitive and user-friendly, ensuring that both users and coaches can easily navigate and utilise the platform. The design is responsive, providing a seamless experience across different devices.

3. **Functionality**: All core functionalities, such as booking classes, logging scores, and viewing leaderboards, are implemented and working as intended. The project also includes additional features like filtering leaderboards and managing bookings, which enhance the overall user experience.

4. **Validation and Testing**: The project includes comprehensive validation and testing to ensure data integrity and functionality. All forms have appropriate validation to prevent incorrect data entry, and automated tests cover key features to ensure they work as expected.

5. **AI Integration**: The use of AI, particularly GitHub Copilot, played a crucial role in the development process. It helped in generating code snippets, suggesting improvements, and ensuring best practices were followed, which accelerated the development timeline and improved code quality.

### Areas for Improvement

1. **Scalability**: While the current implementation meets the project requirements, future enhancements could focus on scalability to handle a larger user base and more complex features.

2. **Performance Optimisation**: As the user base grows, optimising the performance of database queries and page load times will be essential to maintain a smooth user experience.

3. **Additional Features**: Future iterations of the project could include more advanced features such as personalised workout plans, integration with fitness tracking devices, and enhanced analytics for users and coaches.

### Conclusion

Overall, the ClassFit project is a robust and well-implemented platform that meets the needs of both users and coaches. The use of AI tools like GitHub Copilot has significantly contributed to the project's success, ensuring high-quality code and efficient development. The project is well-positioned for future enhancements and scalability, making it a valuable tool for fitness enthusiasts and coaches alike.