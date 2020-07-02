# Fly Away

Milestone Project 3 - Data Centric Development

This website is a game review website, where you can sign up, login, write and view a review. You can find a demo to the website [here.](http://game-scan-flask-mongo.herokuapp.com/)


# UX

The aim of this project was to create a game review website that allows users to create a review of a video game that they've played. They're also able to read other users reviews and also edit their own.

## User Stories

1. A user wants to be able to see who created the book review
2. A user would want to be able to delete/edit their review 
3. A user would be able to access pages through the homepage without having to access the navbar
4. A user wants to be able to go back to the homepage by clicking on the logo on the navbar
5. A user wants to be able to see a log out option on the navbar when 'logged in'


### Strategy

My main aim was to make the website very easy to use.By using Bootstrap Cards and by using the grid system i was making it very easy for the user to use the website.

### Scope

The scope of the website was for users to view or write their own game review, by using a structed form for both my add review and review pages. Users are also able to view other users reviews that they have made through the website.

### Structure

The structure of the website is all kept the same. Wiht majority of the headings being centered such as log in and register. When adding a review, the structure is exactly the same even when you edit a review.

### Skeleton

All my wireframes can be viewed in my *Technologies Used* section.

### Surface

I focused on giving my pages a simple look by only providing two colours and one font for the whole website.

# Feature

#### Existing Features

* Homepage - User is can view the heading with 3 cards below to redirect them to diffrent parts of the website
* Read a Review - A user is able to view all the game reviews made on my website
* Register - Users can register to the website
* Login - Users can log in, When loggin in they're able to create a review. They are also able to edit and delete their reviews.
* Add Review - Allows users to create a game review
* Edit/Delete Review - Users are able to edit and delete their review
* Error Page - When theres an unexecpted error, user will be redirected to an 404 error page

While doing a few of these events, a flash messages appears. For example when registering, once registered. A flash message will pop out saying "Registration Complete!"


#### Features left to Implement

* Adding a Search Bar to my reviews page. To filter thorugh the game reviews


# Technologies Used

1. HTML

* Used to create the website

2. CSS

* Used to style the website

3. Python

* Using Python3 i was able to create the app,routes and functions within the routes.

4. Flask

* Used to create and populate the templates

5. MongoDB

* Used as a backend database

6. Bootstrap 4

* Bootstrap Grid that I have deployed throughout the website, for it to be responsive on all platforms.
* Bootstrap Cards that I have also deployed throughout the website, to give it a more aesthetic look.

7. Github

* Used to remotely store the sourece code in a repository.

8. Heroku

* Used to deploy the whole website

9. Wireframes

* Used to create template of my project.

My Wireframe can be seen here

[Desktop](https://wireframe.cc/DigtlU)

[Tablet](https://wireframe.cc/tJ5pKr)

[Mobile](https://wireframe.cc/URziAN)

# Testing

When it came to testing i had used manual user testing, which was the primary testing for the application. I had asked a few people to go on to the website on different devices. The aim was for them to try and use all the functions on the website to see if there are any bugs in my website. With the feedback i was able to fix a lot of bugs that i didnt know existed.


These tests were done throughtout my project which have also been tested on different web browsers which were:

* Internet Explorer
* Safari
* Mozilla Firefox
* Google Chrome

My project was made, using Google Chrome. This helped as i was able to use Chromes Developer tools to help me debug a few issues happening with my webpage. It also helped when viewing my webpage on different screen sizes

I was able to view my page on these devices:

* Moto G4
* Galaxy S5
* Pixel 2
* Pixel 2 XL
* iPhone 5/SE
* iPhone 6/7/8
* iPhone 6/7/8 Plus
* iPhone X
* iPad
* iPad Pro

#### Testing links

When testing links my aim was to make sure that all links are working and will redirect you to the right pages.

To make sure i was on the right page i have added a title to each of my html pages in my `app.py` file. For example the edit review page and the add reviwew page look identical but if you look at the tab you'll see one saying "Edit a review" and one saying "Add a review" to differentiate between the two

#### Debugging

I had ran throught a few issues while working on project. One being that when adding a review i would be getting a value error. This is because i had two different variable names for it. By keeping them consistent i was able to make the add review page work.

# Deployment

I had created a repository using GitHub. By doing this i was able to keep track on all the commits i had done to my code

You can view my GitHub repository [here](https://github.com/amit238/milestone-project-3)

The initial steps to link my webpage to my repository were as followed:

1. Made my environment using Cloud9.
2. Created all my folders and files.
3. Inside the terminal, I typed the following in this order `ls`, `git init`, `git add .` `git commit` this then created my initial commit.
4. By using `git push` i was then able to link my page to a GitHub repository.

To clone my webpage the steps were as followed:

1. You will need to go to my GitHub [Repo](https://github.com/amit238/milestone-project-3)
2. On the right hand side you will be able to see a Clone or download dropdown button. Click that.
3. Before downloading the website insure that Python3 is installed
4. Create a virtual environment
5. Run the requirements.txt and install the required packages in able to run the app.
6. You may need to add on the env.py file the following:

`os.environ["IP"] = "0.0.0.0"`

` os.environ["PORT"] = "8080"`

7. You should now be able to run the code.

# Credits 

* To my mentor for helping me throughout the project.
* Using [Stack Overflow](https://stackoverflow.com/) and [W3Schools](w3schools.com)helping me understand Python a lot better

### Media Used

All images used was from google images

I used [Favicon](https://realfavicongenerator.net/) to add an icon for my navbar and title.

All the descriptions i have on my reviews page are from [IGN](https://www.ign.com/uk)


# Acknowledgements

This project was inspired from the love i have for games. Since i was a child i was been in the gaming from world playing a wide range of different genres.





