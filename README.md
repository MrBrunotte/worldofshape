# Welcome to the **"World of Shape"**

![alt text](https://github.com/MrBrunotte/worldofshape/blob/master/static/images/landingpage.png "World of Shape")

**World of Shape - Your journey starts now!**

[![Build Status](https://travis-ci.org/MrBrunotte/worldofshape.svg?branch=master)](https://travis-ci.org/MrBrunotte/worldofshape)


## Table of Contents:
- [Welcome to the **"World of Shape"**](#welcome-to-the-%22world-of-shape%22)
  - [Table of Contents:](#table-of-contents)
  - [**World of Shape**](#world-of-shape)
    - [**Purpose of Project**](#purpose-of-project)
    - [**Functionality of Project**](#functionality-of-project)
  - [**UX - User Experience**](#ux---user-experience)
  - [**User Experience**](#user-experience)
    - [**User Stories:**](#user-stories)
  - [**Features**](#features)
    - [Existing features](#existing-features)
    - [Features left to implement](#features-left-to-implement)
  - [**Testing**](#testing)
    - [Travis CI - platform](#travis-ci---platform)
    - [What is CI - Continuous Integration?](#what-is-ci---continuous-integration)
    - [CI Builds and Automation: Building, Testing, Deploying](#ci-builds-and-automation-building-testing-deploying)
  - [AUTOMATED TESTING](#automated-testing)
    - [Coverage](#coverage)
  - [SETTING UP URLs](#setting-up-urls)

## **World of Shape**

World of Shape is a website that aims to get the user in shape and lose weight in 30 days! 


This is attained when the user purchase and attends a 30-day excercise program where the user will have access to World of Shapes personal trainers, the training program and mealplans the user chose to purchase. The user is encuraged to take a "before" and "after" picture of themself in order to monitor thier progress. The World of Shape concept has a proven system that can be validated in the testimonial section of the website.

### **Purpose of Project**

World of Shape is build of an existing website that sells weightloss-training programs and mealplans. The aim of my "World of Shape" website is to improve the existing website and ultimately the profitabillity of the business. This is attained by building a more professinal looking website that is a lot more user friendly and more visually appealing.

The purpose of the project was to create a Full Stack Framework Django site and improve:
* the actual website, 
* the user experiance.
* the profitabillity of the business.

### **Functionality of Project**

The appliction uses Django 3 to encourage rapid development, by following a MTV (model-template-view) architecture pattern. I have used the [**separation of concerns**](https://livebook.manning.com/book/code-like-a-pro/chapter-2/) in the application to utilize the Django Framework effectively.

Alongside the Django framework, I have used sqlite in the project's development phase for local testing. Sqlite is a selfcontained highly reliable SQL database engine that features all the normal relational database management. When the project was ready for deployment I switched to Postgres (PostGreSQL) to ensure that any data entered was visible in my deployed Heroku application. Postgres is open source and boosts a fully technical and easy to use Object relational database management system.

The admin user of World of Shape has full access to the Admin dashboard where the admin can **create, read, update and delete** the training programs or mealplans. 
The Admin dashboard is custom made for the World of Shape website. From the Django dashboard the admin can do the CRUD operations in all 6 applocations. 

The 6 applications are:
* Authentication & authorization
* Blog _(not implemented yet, but is fully functional)_
* Checkout
* Meal
* Products
* Users

The project uses Git and GitHub for version controll and is deployed via Heroku. 

All secret variables are stored in an *env.py* filte that is then ignored by the version control with the gitignore file. This is done to ensure that the project integrity is held at a high security standard.

The application uses Stripe as payment method and when testing the payment functionality please make sure to use the [**Stripe test card numbers**](https://stripe.com/docs/testing#cards). Throughout the development phase of this project I have used:
* Card number: **4242 4242 4242 4242**
* CVV: **Any 3 digit number**
* Card Date: **Any future date**

Please feel free to register a user to fully test the [World of Shape website](ADD HEROKU ADRESS HERE)

[Back to: _"Table of Contents"_](#table-of-contents)

## **UX - User Experience**



## **User Experience**

The typical user is a man or a woman of all ages that want to get in shape but have struggled in the past. World of Shape helps these users to attain this goal by giving them the tools to effectivly reach the goal set by the user. World of Shape helps the user by supplying the necessary tools to best loose weight and get in shape. These tools consists of training programs, mealplans and access to World of Shapes personal trainer on the web.

### **User Stories:**

_**Generic** (Guest/Public) User:_

* As a **Generic** User I can browse the site and access all necessary information I need before making a purchase.
* As a **Generic** User I can search the site by typing keywords that describe my search qriteria.
* As a **Generic** User I can register a profile and add a profile picture.
* As a **Generic** User I can contact World of Shape by sending them a message from the website contact form.
* As a **Generic** User I can view the site on any device I may have, (mobile/tablet/desktop).

_**Registered** (Logged in) User:_

* As a **Registered** User I can login to my site.
* As a **Registered** User I can update my profile picture, username and email settings.
* As a **Registered** User I add products to my shopping cart.
* As a **Registered** User I change the number of items or delete my cart items.
* As a **Registered** User I checkout and pay for my shopping cart items.

_**Application** Admin User:_

* As a site **Admin** User I can log in to the Django Admin Dashboard. In the dashboard I can:
    * Update, add, change or delete **Users**,
    * Update, add, change or delete **Meals**,
    * Update, add, change or delete **Programs**,
    * Update, add, change or delete **Profiles**,
    * Update, add, change or delete **Orders**.

_**Application** Owner:_

* As the **Owner** User I can receive emails from the sites contact from.

_**Developer**:_

* As a **Developer** I wanted to demonstrate my skills as a junior Full Stack Software developer.
* As a **Developer** I wanted to build a project that I could showcase alongside my other projects to potential future employers or customers on GitHub and on my personal portfolio.
* As a **Developer** I wanted to improve the existing website [World of Shape](https://worldofshape.com/) and make it a more inviting and user friendly website.

[Back to: _"Table of Contents"_](#table-of-contents)


## **Features**

### Existing features

_**Contact form**:_ 

When the user uses the contact form to contact World of Shape an email is send to World of Shape and the user is informed that the email is send and that World of Shape will be in touch soon.

<p align="center">
    <img src="" alt="Message to sender">
</p>

### Features left to implement

* Add a blog function (_already axists as an app in the project_).
* The form help text form Django forms could be displayed more aligned to the input field box.

[Back to: _"Table of Contents"_](#table-of-contents)

## **Testing**

### Travis CI - platform

### What is CI - Continuous Integration?

I have used the practice of CI (Continuous Integration), which is the the practice of merging in small code changes frequently - rather than merging in a large change at the end of a development cycle. The goal is to build healthier software by developing and testing in smaller increments. 
As a continuous integration platform, Travis CI supports your development process by automatically building and testing code changes, providing immediate **feedback** on the success of the change. Travis CI can also automate other parts of your development process by managing deployments and notifications.

### CI Builds and Automation: Building, Testing, Deploying

When you run a build, Travis CI clones your GitHub repository into a brand-new virtual environment, and carries out a series of tasks to build and test your code. If one or more of those tasks fail, the build is considered **broken**. If none of the tasks fail, the build is considered **passed** and Travis CI can deploy your code to a web server or application host.

## AUTOMATED TESTING 

### Coverage

I have used the package 'coverage' to see how effective my testing is. 
I installed the covarage package with 'pip install coverage' and then I ran 'Coverage' and created a covhtml file.

run with:   coverage run --source='users' manage.py test && coverage report && coverage html
            Go to the htmlcov file and run the index file to get the report.
and:        python manage.py test users
    
**"coverage run --source='users' manage.py test && coverage report && coverage html"**


[Automated testing results](static/img/automated_testing_results.PNG)

## SETTING UP URLs

Steps to set up url patterns and getting it to work!

**Testimonials example**
1)  Create html page - set Codeblock and DOCTYPE
2) Go to Project urls (WorldofShape) and set urlpattern: path('testimonials/', home_views.contact, name='testimonials'),
3) Go to Home/Views: def testimonials(request):
    """ Contact view takes us to our contactpage """
    return render(request, 'home/testimonials.html')
4) Set urlpattern in Home: path('testimonials/', views.testimonials,
         name='testimonials'),  # from contact view

[Back to: _"Table of Contents"_](#table-of-contents)
