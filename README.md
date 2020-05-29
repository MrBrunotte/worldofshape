<h1 align="center">
    Welcome to "World of Shape"
</h1>


![World of shape landingpage](https://github.com/MrBrunotte/worldofshape/blob/master/media/images/landingpage.PNG "World of Shape")

Vist my site [**World of Shape**](https://worldofshape.herokuapp.com/)

You have two options to test **World of Shape**

1. [**Register**](https://worldofshape.herokuapp.com/register/) as a new user
   
   or

2. [**Login**](https://worldofshape.herokuapp.com/login/)  as "testuser" with the following credentials:

   * Username: **testuser**
    * Password: **testworldofshape**


## <h2><strong>World of Shape</strong> table of content</h2>

  - [**Welcome to "World of Shape"**](#world-of-shape)
    - [**Purpose of Project**](#purpose-of-project)
    - [**Functionality of Project**](#functionality-of-project)
  - [**UX - User Experience**](#ux---user-experience)
    - [**User Stories:**](#user-stories)
    - [**Mockup**](#mockup)
  - [**Features**](#features)
    - [**Existing features**](#existing-features)
    - [**Features left to implement**](#features-left-to-implement)
  - [**Testing**](#testing)
    - [**Automated Testing**](#automated-testing)
    - [**Manual Testing**](#manual-testing)
    - [**Responsiveness**](#Responsiveness)
    - [**Code check**](#code-check)
  - [**Technologies Used**](#technologies-used)
    - [**Languages, Frameworks, Editor and Version Control**](#languages-frameworks-editor-and-version-control)
    - [**Databases used**](#databases-used)
    - [**Tools used:**](#tools-used)
  - [**Deployment**](#deployment)
    - [**Deploy code locally**](#deploy-code-locally)
    - [**Deploy to Heroku**](#deploy-to-heroku)
  - [**Credits**](#credits)
    - [**Content**](#content)
    - [**Acknowledgments**](#acknowledgments)
  - [**Contact**](#contact)

## **World of Shape**

World of Shape is a website that aims to get the user in shape and lose weight within 30 days! 


The user purchase and attends a 30-day excercise program where the user will have access to World of Shapes personal trainers, training programs and mealplans the user choose to purchase. The user is encuraged to take a "before" and "after" picture of themself in order to monitor their progress. The World of Shape concept has a proven system that can be validated in the testimonial section of the website.

### **Purpose of Project**

World of Shape is build of an existing website that sells weightloss-training programs and mealplans. The aim of my "World of Shape" website is to improve the existing website and ultimately the profitabillity of the business. This is attained by building a more professinal looking website that is a lot more user friendly and more visually appealing.

The purpose of the project was to create a Full Stack Framework Django site and improve:
* the actual website, 
* the user experiance.
* the profitabillity of the business.

### **Functionality of Project**

The appliction uses Django 3 to encourage rapid development, by following a MTV (model-template-view) architecture pattern. I have used the [**separation of concerns**](https://livebook.manning.com/book/code-like-a-pro/chapter-2/) in the application to utilize the Django Framework effectively.

Alongside the Django framework, I have used SQlite in the project's development phase for local testing. SQlite is a selfcontained highly reliable SQL database engine that features all the normal relational database management. When the project was ready for deployment I switched to Postgres (PostGreSQL) to ensure that any data entered was visible in my deployed Heroku application. PostGreSQL is open source and boosts a fully technical and easy to use Object relational database management system.

The admin user of World of Shape has full access to the Admin dashboard where the admin can **create, read, update and delete** the Training programs, Mealplans, User settings and Checkout orders. 
The Admin dashboard is custom made for the World of Shape website. From the Django dashboard the admin can do the CRUD operations in all 6 applocations. 

The 7 applications are:
* **Worldofshape**
* Cart
* Checkout
* Home
* Meals
* Products
* Users

The project uses Git and GitHub for version controll and is deployed via Heroku. 

All secret variables are stored in an *env.py* file that is then ignored by the version control with the .gitignore file. This is done to ensure that the project integrity is held at a high security standard.

The application uses Stripe as payment method and when testing the payment functionality please make sure to use the [**Stripe test card numbers**](https://stripe.com/docs/testing#cards). Throughout the development phase of this project I have used, and they can be used to test the production version as well:
* Card number: **4242 4242 4242 4242**
* CVV: **Any 3 digit number**
* Card Date: **Any future date**

Please feel free to [register](https://worldofshape.herokuapp.com/register/) a user to fully test the World of Shape website or you can [login](https://worldofshape.herokuapp.com/login/) as the **_testuser_**:

 * Username: testuser
 * Password: testworldofshape

[Back to: _"Table of Contents"_](#table-of-contents)

## **UX - USER EXPERIENCE**

The typical user is a man or a woman of all ages that want to get in shape but have struggled in the past. World of Shape helps these users to attain this goal by giving them the tools to effectivly reach the goal set by the user. World of Shape helps the user by supplying the necessary tools to best loose weight and get in shape. These tools consists of training programs, mealplans and access to World of Shapes personal trainers on the web.

### **User Stories:**

_**Generic** (Guest/Public) User:_

* As a **Generic** User I can browse the site and access all necessary information I need before making a purchase.
* As a **Generic** User I can register a profile and add a profile picture.
* As a **Generic** User I can contact World of Shape by sending them a message from the website contact form.
* As a **Generic** User I can view the site on any device I may have, (mobile/tablet/desktop).

_**Registered** (Logged in) User:_

* As a **Registered** User I can login to my site.
* As a **Registered** User I can update my profile picture, username and email settings.
* As a **Registered** User I can add products to my shopping cart.
* As a **Registered** User I can delete my cart items.
* As a **Registered** User I can checkout and pay for my shopping cart items.

_**Application** Admin User:_

* As a site **Admin** User I can log in to the Django Admin Dashboard. In the dashboard I can:
    * Update, add, change or delete **Users**,
    * Update, add, change or delete **Meals**,
    * Update, add, change or delete **Programs**,
    * Update, add, change or delete **User-profiles**,
    * Update, add, change or delete **Orders**,
    * Change or delete **User-passwords**,

_**Application** Owner:_

* As the **Owner** User I can receive emails from the sites contact from.

_**Developer**:_

* As a **Developer** I wanted to demonstrate my skills as a junior Full Stack Software developer.
* As a **Developer** I wanted to build a project that I could showcase alongside my other projects to potential future employers or customers on GitHub and in my personal portfolio: [Stefan Brunottes Portfolio](www.stefanbrunotte.com) Site is under constructio!.
* As a **Developer** I wanted to improve the existing website [World of Shape](https://worldofshape.com/) and make it a more inviting and user friendly website.

### **Mockup**

[AdobexD](https://www.adobe.com/se/products/xd.html) was used for the mockup.

#### **Desktop & Mobile **

See the WorldofShape Mockups [here](https://xd.adobe.com/view/4e26e532-1880-4f4f-665d-769778239027-3817/) Click on "World of shape" in the top left corner to see all 10 mockups. 

[Back to: _"Table of Contents"_](#table-of-contents)

## **FEATURES**

### **Existing features**

_**Navigation and buttons**:_ 

The navigation consist of a "logged in" navigation and a "guest" navigation. The difference between the two is that when the user is logged in they will be able to reach the "profile" section and the user is also able to add programs and meals to the shopping cart. If a user isnt logged in and adds something to the cart they will be directed to the login page before they are able to checkout and pay for the item.

There is a navigation row for larger screens and a "hamburger" menu for smaller screens. There is also a navigation bar in the footer.

The idea behind the navigation both from the navigation bar, footer and different buttons is to easily direct the user to the correct location so that it is easy for the user to buy the training programs or meals or get the correct information so that they will feel confident and start one of the programs.

The site is constructed so that the user have to do as few clicks as possible to make a purchase, this makes it more likely that the user purchases a product or mealplan.

On all pages except "contact" and "Profile" there are buttons for the user to click on to join the program and get directed to a purchase opportunity. 

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

* The **Add To Cart** button at the top and bottom puts the program/meal in the shopping cart and also displays the amount of items currently in the cart. It redirects the user to the shopping cart so they can checkout and pay for the program/meal.

The user is intentially redirected to the shopping cart because it is most likely that they will only buy one program/meal at a time, so it is better to redirect the user to the checkout rather than back to the homepage or somewhere else.

_**Testimonials** page:_ 

* The **Read More** button directs the user to the text below.
* The names of each testimonial is linked to the the programs page where the user can get started and purchase a program.
* The **Join Now** button at the bottom directs the user to the products page where the user can get started and purchase a program.

_**Contact form**:_ 

From the contact page the user can send an email to World of Shape. After the message is sent the user is informed the the message has been delivered and World of Shape will be in touch soon.

<p align="center">
    <img src="https://github.com/MrBrunotte/worldofshape/blob/master/media/html_images/contact_form_message.PNG" alt="Message to sender that we will contact you shortly">
</p>

_**Login** page:_ 

* The user logs in with username and password and get directed to the homepage.
* If user have forgotten the password they can request a new password by clicking on the "Forgot Password?" link.
* If the user haven't registered there is a link to "sign up now" that directs the user to the register page.

**Register** page:_ 

* The user register a username, email, password, and confirms the password. There is help-text below each input field that informs the user what format is needed, the help-text is highlited when hovered over.
* When the user clicks register, the user is redirected to hte login page and a message is displayed "_Your Account Has Been Created! You Can Now Log In._"
* If user already is registered there is a link to the login page.

_**Reset Password** page:_ 

* If the user forgot their password they can click on the link to create a new password. They will then be directed to the reset password page

<p align="center">
    <img src="https://github.com/MrBrunotte/worldofshape/blob/master/media/html_images/reset_password_page.PNG" alt="Reset Password">
</p>

* When the user have requested a reset of their password they are redirected to a message page where they can log in again after they have followed the instructions in their mail inbox or they can go back to the homepage.

<p align="center">
    <img src="https://github.com/MrBrunotte/worldofshape/blob/master/media/html_images/reset_password_page_message.PNG" alt="Reset Password Message">
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
  * If the payment is ok the user will be redirected to the homepage and a message will be shown that states _**"You have successfully paid"**_
  
_**Error** pages:_

There are three custom error pages, **403-error**, **404-error** and **500-error**. All three error pages have the same format and design.

On the error pages the user is informed what the error is and they are able to click on a link that takes them back to the homepage.

See the 404-error page here: 

<p align="center">
    <img src="https://github.com/MrBrunotte/worldofshape/blob/master/media/html_images/404_error_page.PNG" alt="Image of 404-error page">
</p>

### **Features left to implement**

* Add static, and media files to an S3 bucket.
* Add a blog function for the registered users to communicate with each other.
* The **Get Discount** button in the 15% discount section needs a discount message displayed in form of a popup with the discount code or message.
* Add tests to get 100% coverage in all apps.
* Work on Accessibililty features and make the web page adhere more to the [WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/) (Web Content Accessibility Guidelines)

[Back to: _"Table of Contents"_](#table-of-contents)

## **TESTING**

I have conducted both manual and automated testing on the website.

### **Automated Testing** 

Automated testing was conducted on each app. I used Djangos [**TestCase**](https://docs.djangoproject.com/en/3.0/topics/testing/tools/#testcase) and [**SimpleTestCase**](https://docs.djangoproject.com/en/3.0/topics/testing/tools/#simpletestcase) to test the apps. 

I then used [**Coverage**](https://coverage.readthedocs.io/en/coverage-5.1/) to see the "coverage" of my tests, I was not able to get 100% on all apps but that is mentioned above in the section: _Features left to implement_.

I ran the tests on my SQlite development database.

**[See](https://github.com/MrBrunotte/worldofshape/blob/master/media/html_images/coverage_report.jpg)** the Coverage report.

**[See](https://github.com/MrBrunotte/worldofshape/blob/master/media/html_images/automated_testing_results.PNG)** the Automated tests (_TestCase and SimpleTestCase_).

### **Manual Testing**

Summary of manual testing of user functions [here](https://github.com/MrBrunotte/worldofshape/blob/master/media/images/manual_testing_page_functions.PNG)

I have conducted testing both as a **Guest** user and as a **Logged in** user.

_**Navigation and buttons**:_ 

* Test that all URLs patterns in the navbar point to the correct view.
* Make sure that the there is a profile and logout option in the navbar and that they point to the correct view.
* Test the "hamburger" menu on smaller screens and make sure all navbar options work correctly.
* Test the footer navbar and make sure all navbar options work correctly.

_**Home** page:_ 

* Test that the **Join Now** button directs the user to the products page.
* Test that the **Read More** button in the "training programs" box directs the user to the products page.
* Test that the **Read More** button in the "Weight Loss Analysis" box directs the user to the weight loss page.
* Test that the **Read More** button in the "Healthy Diet Plan" box directs the user to meal page.
* Test that the **Read More** button below About world of Shape directs the user to the About Us page.
* Test that the names of each testimonial is linked to the testimonials page.
* Test that the **Join Now** button at the bottom of the page directs the user to the products page.

_**About Us** page:_ 

* Test that the **Read More** button directs the user to the text below.
* Test that the **Find Out How It Works Video** pops up and the video is played.
* Test that the **Join Now** button directs the user to the products page.
* Test that the **Get Discount** button at the bottom of the page is a dummy link and the user stays on the about page.

_**Our Training** and **Our Meals** page:_

* Test that the **Read More** button directs the user to the text below.
* Test that the **Find My Program** button directs the user to the "weight loss".
* Test that the **Read More** button below each program/meal directs the user to the correct program/meal page.
* Test that the **Add To Cart** button puts the chosen program/meal in the shopping cart and the cart navigation in the top navigation bar displays the number of programs/meals in the cart.
* Test that the **Get Discount** button at the bottom of the page is a dummy link and the user stays on the current page.

_**Program** and **Meals** page:_

* Test that the **Add To Cart** button at the top and bottom puts the program/meal in the shopping cart and also displays the amount of items currently in the cart. And redirects the user to the shopping cart so they can checkout and pay for the program/meal.

_**Testimonials** page:_ 

* Test that the **Read More** button directs the user to the text below.
* Test that the names of each testimonial is linked to the the programs page.
* Test that the **Join Now** button at the bottom directs the user to the products page.

_**Contact form**:_ 

Test that the user the user can send an email to World of Shape, and gets a message telling the user that the email was sent.

_**Login** page:_ 

* Test that the user can log in with username and password and get directed to the homepage.
* Test that the "Forgot Password?" link works correctly.
* Test that the "sign up now" link works and redirects the user to the register page.

**Register** page:_ 

* Test that the user can register as a user and is redirected to the login page and greated with a message saying: "_Your Account Has Been Created! You Can Now Log In._"
* Test that the link to the login page works and redirects the user to the login page.

_**Reset Password** page:_ 

* Test that the link to create a new password works correctly and redirects the user to the reset password page
* Test that the user can log in again after they have followed the instructions in their mail inbox.
* Test that the link back to the homepage works.

_**Cart** page:_ 

* Test that the **Checkout** button redirects the user to the payment page.
* Test that each program/meal in the cart can be deleted by clicking on the **Delete Item** button.
* Teest to make sur that if there are more than one item in the cart the total ammount is displayed below the checkout button.

_**Checkout** page:_ 

* Test that the **Change Order** button redirects the user back to the cart.
* Test that the user is able to inserts "Payment Details" and "Card Details" properly.
* Test that the payment works and that the user is redirected to the homepage and a message is shown saying: _**"You have successfully paid"**_ 
* Test that the if something with the payment is wrong the message _**"We Were Unable To Take Payment With That Card!"**_ will be displayed and the user is redirected to the checkout page. 

### **Responsiveness**

Summary of manual testing of responsivness [see it here](https://github.com/MrBrunotte/worldofshape/blob/master/media/images/manual_testing_responsivness.PNG)

I have used media queries to build a responsive website. I have looked for "natural" breakpoints on my site and these are the best breakpoints for my design:

  * **Hamburger menu break** ~ @media only screen and (max-width: 1190px)
  * **> 1200px** ~ @media only screen and (min-width: 1199px)
  * **992 - 1199px** ~ @media only screen and (min-width: 991px) and (max-width: 1199px)
  * **768 - 991px** ~ @media only screen and (min-width: 767px) and  (max-width: 991px)
  * **575 - 767px** ~ @media only screen and (min-width: 575px) and (max-width: 767px)
  * **< 575px** ~ @media only screen and (max-width: 574px)

I have tested the responsiveness in browsers:

* Firefox and 
* Chrome
  
I have also tested responsivness for portrait and landscape settings.

### **Code Check**

I have ran all my code through differnt validators to make sure that my code is ok and up to date with current code standards.

#### **HTML code**

It is a bit tricky to test the HTML code due to the use of a base.html, templates and jinja. Therefore I created a HTML testing template called **code_testing.html**. I created a base layout and tested it with the Validator and got no errors. I then pasted in the HTML between the "block content" and the "endblock content" from each app template and tested it in the HTML validator.

My [code_testing.html](https://github.com/MrBrunotte/worldofshape/blob/master/media/html_images/code_testing_html.PNG) template

I filtered out **"bad Values"**

[Bad Values](https://github.com/MrBrunotte/worldofshape/blob/master/media/html_images/error_html_filter.PNG)

When the filter was applied all my templates passed the validator.

To validate my HTML code I used: [Validator W3 Org](https://validator.w3.org/#validate_by_input)

#### **CSS code**

My CSS code was checked with [Jigsaw W3 Org](https://jigsaw.w3.org/css-validator/#validate_by_input)

I got 96 warnings and they were all warnings about unknown vendor extension. These came with the css code from the template I downloaded so I have ignored them!

Everything else was labeled **"valid CSS information"** by the validator!

#### **Python code**

My Python code was checked with [PEP8 online](http://pep8online.com/)

When testing I have ignored the code result W291 which is an indication of "trailing whitespace".

[Back to: _"Table of Contents"_](#table-of-contents)

## **TECHNOLOGIES USED**

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

### **Databases used:**
* [SQLite](https://www.sqlite.org/index.html) ~ Database used in **development**
* [Heroku Postgres](https://elements.heroku.com/addons/heroku-postgresql) ~ Database used in **production**
  
### **Tools used:**
* [Pep 8 Online Validator](http://pep8online.com/) ~ Check python code for PEP8 requirements
* [Jigsaw W3 Org](https://jigsaw.w3.org/css-validator/#validate_by_input) ~ Check CSS code
* [Validator W3 Org](https://validator.w3.org/#validate_by_input) ~ Check HTML code
* [Fontawsome](https://fontawesome.com/)
* [Firefox Dev Tools](https://developer.mozilla.org/en-US/docs/Tools)
* [Chrome Dev Tools](https://developers.google.com/web/tools/chrome-devtools)
* [Adobe Xd](https://www.adobe.com/se/products/xd.html)

[Back to: _"Table of Contents"_](#table-of-contents)

## **DEPLOYMENT**

If you want to clone this website you need to create the necessary keys!

1. Login or create an account at [Stripe](https://stripe.com/en-se) to get your Stripe keys. 
   1. Follow the instructions and if you create a new account verify your email and activate your Stripe account.
   2. Click on _Get your test API keys_ to see your **Publishable key** and your **Secret key**.
2. Create a random [SECRET_KEY](https://miniwebtool.com/password-generator/) and set as environment variable (in .env file).
    * MacOS and Linux ````export SECRET_KEY=<secret key>````
    * Windows ````set SECRET_KEY=<secret key>````
3. When you have your three keys store them in your env.py file in the directory app _**worldofshape**_ (not in the root folder!).

In order to make the contact form work you need your gmail username and password.

### **Deploy code locally**

If you wish to run this code locally then please follow the instructions below.

1. Download the code from the GitHub repository from [here](https://github.com/MrBrunotte/worldofshape).
2. Click on _"Clone"_ or _"download then Download ZIP"_. This will download the code into a ZIP folder locally on your computer.
3. Uncompress the ZIP folder.
4. Create a virtual environment.
   1. Create env.py file in the **worldofshape** app (not the root folder!)
   2. Make sure you have theses settings in the env.py file, so that the environment variables can be read:
      1. Import: ````import os````
      3. Set: ````os.environ[’SECRET_KEY] = ‘ …. ‘ ````
      4. Set: ```` os.environ[’EMAIL_USER’] = ‘ …. ‘ ````
      5. Set: ```` os.environ[’EMAIL_PASS’] = ‘ …. ‘ ````
      6. Set: ```` os.environ[’STIRIPE_PUBLISHABLE’] = ‘ …. ‘ ````
      7. Set: ```` os.environ[’STIRIPE_SECRET’] = ‘ …. ‘ ````
      8. Set: ```` os.environ[’DATABASE_URL’] = ‘ …. ‘ ````
5. Activate the virtual environment.
6. Install the necessary Python packages in the requirements.txt file.
    * ````pip freeze --local > requirements.txt````
7.  Open up a terminal (VSCode) and run ````python manage.py runserver````.
8.  Follow the link by (Ctrl + click) on **http://127.0.0.1:8000** to view _**World of Shape**_ in your browser.


### **Deploy to Heroku**

This project was deployed to Heroku and uses Heroku for its production environment. Below you have instructions on how to deploy this web application to a production environment in Heroku.

*Git must be installed onto your computer. Instructions for installing Git can be found here.

**Heroku CLI must be installed to deploy to Heroku using these instructions. Please follow the instructions here to download and install Heroku CLI.

1.  Login to [Heroku](https://id.heroku.com/login)
2.  Select _New > Create New App_ and fill out the details required then hit _Create App_.
3.  Select _Settings > Reveal Config Vars_. Enter the following environment variables:
    1. DATABASE_URL: the URL is automatically set when you add the _add on_ from the _Overview_ tab in the Heroku dashboard.
    2. PORT: 8000
    3. SECRET_KEY: The generated key
    4. STRIPE_PUBLISHABLE: From your env.py file
    5. STRIPE_SECRET: From your env.py file
    6. EMAIL_USER: Your Gmail username
    7. EMAIL_PASS: Your Gmail password
    8. Set: DISABLE_COLLECTSTATIC = 1
    9. Set: HOSTNAME = “name of app”
4. Download the code from the GitHub repository [here](https://github.com/MrBrunotte/foodictionary).
5. Click on _Clone_ or _download then Download ZIP_. This will download the code into a ZIP folder locally on your computer.
6. Uncompress the ZIP folder.
7. Open up a terminal or cmd prompt and login into Heroku CLI.
    * ````heroku login````
8. Check the app is present.
    * ````heroku apps````
9. A Procfile have already been created for this project but make sure that it is present. If for some 
reason it is not then follow the steps below to create it.
    
    * Procfile
        * In a terminal make sure you are in the root directory of the project then run ````web: gunicorn worldofshape.wsgi:application > Procfile````.
        * Check that the following text is in the Procfile **web: gunicorn worldofshape.wsgi:application**.
  
10.   Add a new git remote for Heroku.
    * ````git remote add heroku git@heroku.comYOUR_APP_NAME.git````
11.  Push to Heroku.
    * ````git push heroku master````
12.  Give Heroku a few minutes to get it all set up and then check the activity logs under Activity tab in your Heroku 
dashboard. 
13. Once the build is complete click on **open app** top right to see _**World of Shape**_ in action. 

[Back to: _"Table of Contents"_](#table-of-contents)

## **CREDITS**

### **Content**

Free template, including images downloaded from [**SportFit**](https://themewagon.com/themes/free-bootstrap-4-html5-fitness-website-template-sportfit/)

All images used with permission from [**WorldofShape**](https://worldofshape.com/) 

### **Acknowledgments**

I would like to thank my good friend [**Niklas Lind**](https://github.com/niklaslind) for his support and guidance during the development of this project. 

I would also like to thank my mentor [**Maranatha Ilesanmi**](https://github.com/mbilesanmi).

Finally I would like to thank all the tutors at Code Institute for their fantastic help in guiding me in the correct direction, especially Tim and Stephen for their patience and great tutoring!

## **CONTACT**

Created by [Stefan Brunotte](stefanbrunotte.com) (site under construction)

[Back to: _"Table of Contents"_](#table-of-contents)
