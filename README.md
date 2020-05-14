# Welcome to **"World of Shape"**

![alt text](https://github.com/MrBrunotte/worldofshape/blob/master/static/images/landingpage.png "World of Shape")

**World of Shape - Your journey starts now!**

[![Build Status](https://travis-ci.org/MrBrunotte/worldofshape.svg?branch=master)](https://travis-ci.org/MrBrunotte/worldofshape)


## **Table of Contents:**

  - [**World of Shape**](#world-of-shape)
    - [**Purpose of Project**](#purpose-of-project)
    - [**Functionality of Project**](#functionality-of-project)
  - [**UX - User Experience**](#ux---user-experience)
  - [**User Experience**](#user-experience)
    - [**User Stories:**](#user-stories)
    - [**Mockup**](#mockup)
  - [**Features**](#features)
    - [**Existing features**](#existing-features)
    - [**Features left to implement**](#features-left-to-implement)
  - [**Testing**](#testing)
    - [**Travis CI - platform**](#travis-ci---platform)
    - [**What is CI - Continuous Integration?**](#what-is-ci---continuous-integration)
    - [**CI Builds and Automation: Building, Testing, Deploying**](#ci-builds-and-automation-building-testing-deploying)
    - [**Bugs**](#bugs)
  - [**Automated Testing**](#automated-testing)
    - [**Coverage**](#coverage)
  - [Setting up URLs](#setting-up-urls)
  - [**Technologies Used**](#technologies-used)
    - [**Languages, Frameworks, Editor and Version Control**](#languages-frameworks-editor-and-version-control)
    - [**Tools used:**](#tools-used)
  - [**Deployment**](#deployment)
    - [**Deploy code locally**](#deploy-code-locally)
    - [**Deploy to Heroku**](#deploy-to-heroku)
  - [**Credits**](#credits)
    - [**Content**](#content)
    - [**Acknowledgments**](#acknowledgments)
    - [**Contact**](#contact)
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

### **Mockup**

[AdobexD](https://www.adobe.com/se/products/xd.html) was used for the mockup.

#### **Desktop & Mobile **

See the WorldofShape Mockups [here](https://xd.adobe.com/view/4e26e532-1880-4f4f-665d-769778239027-3817/) Click on "World of shape" in the top left corner to see all 10 mockups. 

[Back to: _"Table of Contents"_](#table-of-contents)


## **Features**

### **Existing features**

_**Navigation and buttons**:_ 

The navigation consist of a "logged in" navigation and a "guest" navigation. The difference between the two is that when the user is logged in they will be able to reach the "profile" section and the user is also able to add programs and meals to the shopping cart.

There is a navigation row for larger screens and a "hamburger" menu for smaller screens. there is also a navigation bar in the footer.

The idea behind the navigation both from the navigation bar and the different buttons is to direct the user to the correct location so that it is easy for the user to buy the training programs or meals or get the correct information so that they will feel confident and start one of the programs.

The site is constructed so that the user have to do as few clicks as possible to make a purchase, this makes it more likely that the user purchases a product.

On all pages exept "contact" and "Profile" there are buttons for the user to click on to join the program and get directed to a purchase opportunity. 

_**Home** page:_ 

* The **Join Now** button directs the user to the products page where all the training programs are listed. The user can read more or add a program to the shopping cart.
* The **Read More** button in the "training programs" box directs the user to the products page.
* The **Read More** button in the "Weight Loss Analysis" box directs the user to the weight loss page where the user can find out what program suits them best.
* The **Read More** button in the "Healthy Diet Plan" box directs the user to meal page where the meals and dietplans can be purchased. 
* The **Read More** button below About world of Shape directs the user to the About Us page.
* The names of each testimonial is linked to the the testimonials page.
* The **Join Now** button at the bottom of the page directs the user to the products page.

_**About Us** page:_ 

* The **Read More** button directs the user to the text below.
* The **Find Out How It Works Video** link shows the user a pop-up video explaining the World of Shape concept.
* The **Join Now** button directs the user to the products page.
* The **Get Discount** button at the bottom of the page is not linked yet and is left for future implementation.

_**Our Training** and **Our Meals** page:_

This page displays all training program/Meals available for purchase.

* The **Read More** button directs the user to the text below.
* The **Find My Program**Find button directs the user to the "weight loss" page where the user finds the correct program for them. (There is no **Find My Meals** button!)
* The **Read More** button below each program/meal directs the user to the program/meal page where the user can read more about the specific program/meal.
* The **Add To Cart** button puts the chosen program/meal in the shopping cart and the cart navigation in the top navigation bar displays the number of programs/meals in the cart.
* * The **Get Discount** button at the bottom of the page is not linked yet and is left for future implementation.

_**Program** and **Meals** page:_

This page displays an indivicual program/meal available for purchase.

* The **Add To Cart** button at the top and bottom puts the program/meal in the shopping cart and the cart navigation in the top navigation bar displays the number of products/meals in the cart. It redirects the user to the shopping cart so they can checkout and pay for the program/meal.

The user is intentially redirected to the shopping cart because it is most likely that they will only buy one program/meal at a time, so it is better to redirect the user to the checkout rather than back to the homepage or anywhere else.

_**Testimonials** page:_ 

* The **Read More** button directs the user to the text below.
* The names of each testimonial is linked to the the programs page where the user can get started and purchase a program.
* The **Join Now** button at the bottom directs the user to the products page where the user can get started and purchase a program.

_**Contact form**:_ 

From the contact page the user can send an email to World of Shape. After the message is sent the user is informed the the message has been delivered and World of Shape will be in touch soon.

<p align="center">
    <img src="https://github.com/MrBrunotte/worldofshape/blob/master/static/images/contact_form_message.PNG" alt="Message to sender">
</p>

_**Login** page:_ 

* The user logs in with username and password and get directed to the homepage.
* If user have forgotten the password they can request a new password by clicking on the "Forgot Password?" link.
* If the user haven't registered there is a link to "sign up now" that directs the user to the register page.

**Register** page:_ 

* The user register a username, emal, password and confirms the password. There is help-text below each input field that informs the user what format is needed, the help-text is highlited when hovered over.
* When the user clicks register, the user is redirected to hte login page and a message is displayed "_Your Account Has Been Created! You Can Now Log In._"
* If user already is registered there is a link to the login page.

_**Reset Password** page:_ 

* If the user forgot their password they can click on the link to create a new password. They will then be directed to the reset password page

<p align="center">
    <img src="https://github.com/MrBrunotte/worldofshape/blob/master/static/images/reset_password_page.PNG" alt="Reset Password">
</p>

* When the user have requested a reset of their password they are redirected to a message page where they can log in again after they have followed the instructions in their mail inbox or they can go back to the homepage.

<p align="center">
    <img src="https://github.com/MrBrunotte/worldofshape/blob/master/static/images/reset_password_page_message.PNG" alt="Reset Password Message">
</p>

_**Cart** page:_ 

When a product or meal is added they are displayed in the cart page.

* The **Checkout** button redirects the user to the payment page.
* Each program/meal in the cart can be deleted by clicking on the **Delete Item** button.
* If there are more than one item in the cart the total ammount is displayed below the checkout button.

_**Checkout** page:_ 

The checkout page summarizes the items and lets the user scroll down to make sure that the correct items are in the cart.
* The **Change Order** button redirects the user back to the cart to delete an item.
* The user inserts the "Payment Details" and "Card Details" before submitting payment. 
  * If something with the payment is wrong the message "We Were Unable To Take Payment With That Card!" will be displayed and the user is redirected to the checkout page. 
  * If the payment is ok

### **Features left to implement**

* Add a blog function (_already axists as an app in the project_).
* The form help text form Django forms could be displayed more aligned to the input field box.
* The **Get Discount** button in the 15% discount section needs a discount message displayed in form of a popup with the discount code or message.

[Back to: _"Table of Contents"_](#table-of-contents)

## **Testing**

### **Travis CI - platform**

### **What is CI - Continuous Integration?**

I have used the practice of CI (Continuous Integration), which is the the practice of merging in small code changes frequently - rather than merging in a large change at the end of a development cycle. The goal is to build healthier software by developing and testing in smaller increments. 
As a continuous integration platform, Travis CI supports your development process by automatically building and testing code changes, providing immediate **feedback** on the success of the change. Travis CI can also automate other parts of your development process by managing deployments and notifications.

### **CI Builds and Automation: Building, Testing, Deploying**

When you run a build, Travis CI clones your GitHub repository into a brand-new virtual environment, and carries out a series of tasks to build and test your code. If one or more of those tasks fail, the build is considered **broken**. If none of the tasks fail, the build is considered **passed** and Travis CI can deploy your code to a web server or application host.

### **Bugs**

#### **Chrome webbrowser**
When the site was manually tested there was a bug when I tried to play the video on the home- and aboutpage. The bug was due to settings in default settings in Chrome.

To fix this problem do this:

1. Go to [chrome://flags/](chrome://flags/) in your chrome browser.
2. Search for: **#same-site-by-default-cookies** and change it from "default" to "Enable".
3. Search for: **#cookies-without-same-site-must-be-secure** and change it from "default" to "Enable".

## **Automated Testing** 

### **Coverage**

I have used the package 'coverage' to see how effective my testing is. 
I installed the covarage package with 'pip install coverage' and then I ran 'Coverage' and created a covhtml file.

run with:   coverage run --source='users' manage.py test && coverage report && coverage html
            Go to the htmlcov file and run the index file to get the report.
and:        python manage.py test users
    
**"coverage run --source='users' manage.py test && coverage report && coverage html"**


[Automated testing results](static/img/automated_testing_results.PNG)

## Setting up URLs

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

## **Technologies Used**

### **Languages, Frameworks, Editor and Version Control**

* [VSCode](https://code.visualstudio.com/)
* [HTML](https://en.wikipedia.org/wiki/HTML)
* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
* [Django 3.0.4](https://www.djangoproject.com/)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Bootstrap 4](https://getbootstrap.com/)
* [jQuery](https://jquery.com/)
  * [Colorbox (jQuery plugin)](http://www.jacklmoore.com/colorbox/) ~ Plugin for the World of Shape video
  * [Parallax (jQuery plugin)](https://pixelcog.github.io/parallax.js/) ~ A simple parallax scrolling effect.
* [Git](https://git-scm.com/)
* [GitHub](https://github.com/)
* [Heroku](https://www.heroku.com/home)

### **Tools used:**
* [Pep 8 Online Validotr](http://pep8online.com/) ~ Check python code for PEP8 requirements
* [Fontawsome](https://fontawesome.com/)
* [Firefox Dev Tools](https://developer.mozilla.org/en-US/docs/Tools)
* [Adobe Xd](https://www.adobe.com/se/products/xd.html)
****

## **DEPLOYMENT**

If you want to clone this website you need to create the necessary key!

1. Login or create an account at [Stripe](https://stripe.com/en-se) to get your Stripe keys. 
   1. Follow the instructions and if you create a new account verify your email and activate your Stripe account.
   2. Click on _Get your test API keys_ to see your **Publishable key** and your **Secret key**.
2. Create your [SECRET_KEY](https://miniwebtool.com/password-generator/) and set as environment variable (in .env file). 
    * MacOS and Linux ````export SECRET_KEY=<secret key>````
    * Windows ````set SECRET_KEY=<secret key>````
3. When you have your three keys store them in your .env file in the directiory app _**worldofshape**_ (not in the root folder!).

### **Deploy code locally**

If you wish to run this code locally then please follow the instructions below.

1. Download the code from the Github repository from [here](https://github.com/MrBrunotte/worldofshape).
2. Click on _"Clone"_ or _"download then Download ZIP"_. This will download the code into a ZIP folder locally on your computer.
3. Uncompress the ZIP folder.
4. Create a virtual environment.
   1. Create .env file in the **worldofshape** app (not the root folder!)
   2. Make sure you have theses settings in the settings.py file, so that the environment variables can be read:
      1. Import: ````import environ````
      2. Set: ````env = environ.Env(DEBUG=(bool, False))````
      3. Set: ````environ.Env.read_env()````
      4. Set: ````SECRET_KEY = env('SECRET_KEY')````
      5. Set: ````STRIPE_PUBLISHABLE = env('STRIPE_PUBLISHABLE')````
      6. Set: ````STRIPE_SECRET = env('STRIPE_SECRET')````
5. Activate the virtual environment.
6. Install the necessary Python packages in the requirements.txt file.
    * ````pip freeze --local > requirements.txt````
7.  Open up a terminal and run ````python manage.py runserver````.
8.  Follow the link by (Ctrl + click) on **http://127.0.0.1:8000** to view _**World of Shape**_ in your browser.


### **Deploy to Heroku**

This project was deployed to Heroku and uses Heroku for its production environment. Below you have instructions on how to deploy this web application to a production environment in Heroku.

*Git must be installed onto your computer. Instructions for installing Git can be found here.

**Heroku CLI must be installed in order to deploy to Heroku using these instructions. Please follow the instructions here to download and install Heroku CLI.

1.  Login to [Heroku](https://id.heroku.com/login)
2.  Select _New > Create New App_ and fill out the details required then hit _Create App_.
3.  Select _Settings > Reveal Config Vars_. Enter the following environment variables:
    1. DATABASE_URL: the url is automaically set when you add the _add on_ from the _Overview_ tab in the Heroku dashboard.
    2. PORT: 5000
    3. SECRET_KEY: The generated key
    4. STRIPE_PUBLISHABLE: From your env. file
    5. STRIPE_SECRET: From your env. file
 1. Download the code from the Github repository [here](https://github.com/MrBrunotte/foodictionary).
4. Click on _Clone_ or _download then Download ZIP_. This will download the code into a ZIP folder locally on your computer.
5. Uncompress the ZIP folder.
6. Open up a terminal or cmd prompt and login into Heroku CLI.
    * ````heroku login````
7. Check the app is present.
    * ````heroku apps````
8. A Procfile have already been created for this project but make sure that it is present. If for some 
reason it is not then follow the steps below to create it.
    
    * Procfile
        * In a terminal make sure you are in the root directory of the project then run ````web: gunicorn worldofshape.wsgi > Procfile````.
        * Add the following text to the Procfile **web: python manage.py runserver 0.0.0.0:8000**.
1.  Add a new git remote for Heroku.
    * ````git remote add heroku git@heroku.comYOUR_APP_NAME.git````
2.  Push to Heroku.
    * ````git push heroku master````
3.  Give Heroku a few minutes to get it all set up and then check the activity logs under Activity tab in your Heroku 
dashboard. 
13. Once the build is complete click on **open app** top right to see _**World of Shape**_ in action. 

[Back to: _"Table of Contents"_](#table-of-contents)

## **Credits**

### **Content**

Free template, including images downloaded from [**SportFit**](https://themewagon.com/themes/free-bootstrap-4-html5-fitness-website-template-sportfit/)

All images used with permission from [**WorldofShape**](https://worldofshape.com/) 

### **Acknowledgments**

I would like to thank my good friend [**Niklas Lind**](https://github.com/niklaslind) for his support and guidance during the development of this project. 

I would also like to thank my mentor [**Maranatha Ilesanmi**](https://github.com/mbilesanmi) and the tutors at Code Institute for their help.

### **Contact**

Created by [Stefan Brunotte](mrbrunotte@gmail.com)
