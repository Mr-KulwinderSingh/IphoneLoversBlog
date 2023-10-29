## iPhone|Lovers 

![iPhoneLovers](static/images/blog-logo.jpg)

**iPhone|Lovers** blog website is developed using Django Framework as part of Portfolio Project 4 for my Diploma in Full Stack Software Development at Code Institute.

It targets the most loving series of the iPhones as worldwide people like iphones as lot, where user can view the blog post of their favourite iPhone model, they can comment about a particular iPhone model even if they are not iPhone lovers but they want to give some sort of feedback about the smartphone what they like, they do a blog post and comments. When the user is logged in, user can like/unlike a post, comment on a post and add a post from the user page.

You can view the live site here:-  https://iphonelovers-1bcbfe91e39d.herokuapp.com

![image](static/images/iphonelovers-blog.jpeg)


## [Content](#content)
- [iPhoneLovers- Introduction](#iphonelovers---introduction)
  - [User Experience - UX](#user-experience---ux)
    - [User & Blog Goals](#User-&-Blog-Goals)
    - [Agile Methodology](#agile-methodology)
      - [Epics and User Stories](#epics-and-user-stories)
      - [Tasks](#tasks)


  - [Design](#design)
    - [Colours](#colours)
    - [Typography](#typography)
    - [Imagery](#imagery)

  - [Database Diagram](#database-diagram)

    - [Features](#features)
    - [Home Page](#home-page)
      - [Navbar](#navbar)
      - [Hero Image](#hero-image)
      - [AlliPhone Section](#iPhone-section)
      - [Footer](#footer)
    - [User Page](#user-page)
    - [About Page](#about-page)
    - [Blog Page](#blog-page)
      - [Blog Details](#blog-details)
      - [Blog Comments](#blog-comments)
    - [Register](#register)
    - [Login](#login)
    - [Logout](#logout)
    - [AlliPhones](#AlliPhones)
    - [Alert Messages](#alert-messages)   



# User Experience - UX

## User & Blog Goals

### Targeted User Goals:
A user interested in visiting iPhones/smartphones.
A user who likes/loves iPhone or similar in smartphone.
A user that wants a platform to share their own feedback.

### Site User Goals:
For users to be able to interact with the site intuitively.
For users to be able to access and view all posts.
For users to be able to read information oabout iPhones and related posts.
For users to be able to create an account to access additional functionality.
For registered users to be able to log in and out of their account.
For registered users to be able to like and comment on all posts.
For registered users to be able add, edit and delete their own comment.

### Blog Goals:
Offers a platform about the community who love smartphone and related technology.
Provide registered users the access to like, comment with full CRUD functionality.


## Agile Methodology

This blog was developed with agile planning. Each individual user feature was split into a user story. Each user story was defined and included an acceptance criteria. The acceptance criteria were tasks to mark as complete to complete the user story.

Related user stories achieving a certain functionality of the blog were grouped together in to Epics.

Each user story was labeled as Must Have, Should Have and Could Have to help prioritise which were most important to implement.

As the blog evolved, tasks were added or updated, based on the changing needs / understanding of the what the blog should provide the user.

This was implemented through Github Issues and the board in the projects view in Github, the project was divided into a few different sections:

* To Do - All user stories were initially entered in the 'To Do' column
* In Progress - During development stories were moved into the 'In Progress' column
* Done - On completion they get moved into the 'Done' column
* Future - Any 'could have' stories with features that I can look to implement at a later date, where due to time restraints I was unable to work on.

Please find my Board(used to called Kanban) with my user stories [here](https://github.com/users/AmarDange/projects/5/views/1).


## Epics and User Stories

Following Epics were created which were further developed into below User Stories.

### Epic 1: Website UI Features

User Story #1

Site pagination (must have) - As a site user I can view a paginated list of posts so that easily select a post to view.

Acceptance Criteria:
* As a site user I can view max 9 posts per page.
* As a site user it is easy to navigate and view posts to pick which one I want to read.

User Story #2

View post (must have) - As a site user I can view a list of posts so that I can select one to read.

Acceptance Criteria:
* As a site user, I can view posts submitted.
* As a site user, I can view the image,  title and short description to help choose what to read.

User Story #3

Open a post (must have) - As a site user I can click on a post so that I can read the full text.

Acceptance Criteria:
* Clicking on post opens a page where user can view the full post.

### Epic 2: Registration & Account Features

User Story #4

Account registration (must have) - As a site user I can register an account so that I can submit my own post, comment and like.

Acceptance Criteria:
* As a site user, I intuitively know where to go to sign up.
* As a site user, I can easily register my account without issue.

User Story #5

Login & logout (must have) - As a registered user, I can login and logout of the site so that I can have access to my account.

Acceptance Criteria:
* As a registered user, I can login and out successfully.

User Story #6

Comment on a post (must have) - As a registered user I can leave comments on a post.

Acceptance Criteria:
* As a logged-in user I can leave comments on a post so that I can be involved in the conversation.

User Story #7

Like/Unlke (must have) - As a site user I can like or unlike a post.

Acceptance Criteria: 
* As a logged-in user I can like or unlike a post so that I can interact with the content.

User Story #8

Add a post (must have) - As a registered site user I can add a post.

Acceptance Criteria: 
* As a logged-in user I can add a post so that I participate in growing the site.
* As a logged-in user I can edit/delete my post so that I can update/delete my submission.

User Story #9

View my comments / likes (could have) - As a registered site user, I can access all my blog posts and likes easily in one place so that I can easily track my activity on the site.

Acceptance Criteria: 
* As a logged-in user I can view a page with a list of all my posts.
* As a logged-in user I can view a page with a list of all my likes.

### Epic 3: Blog Features

User Story #10

Manage (edit/delet) posts (must have) - As a site admin I can create, read, update and delete posts so that I can manage my blog content.

Acceptance Criteria: 
* As a site admin, I can create new posts.
* As a site admin, I can click and read posts.
* As a site admin, I can edit and delete posts.

User Story #11

Create drafts (should have) - As a site admin I can create draft posts so that I can finish writing the content later.

Acceptance Criteria:
* As a site admin I can start a draft post.
* As a site admin I can return back to my account and finish my draft.
* As a site admin I can then successfully post once ready.

User Story #12

View likes (must have) - As a site user, I can view the number of likes on each post so that I can see which is the most popular or viral.

Acceptance Criteria:
* As a site user, I can clearly view a symbol associated with likes on a post.
* As a site user, I can view the number of likes next to the likes symbol.

User Story #13

View comments (must have) - As a site user, I can view comments on an individual post so that I can read the conversation.

Acceptance Criteria:
* As a site user, I can clearly view a symbol associated with comments on a post.
* As a site user, I can view the number of comment next to the comments symbol.
* I can click on the comments symbol to view the conversation.


<!-- User Story # 
(This one i want to do in the future or if i will manage my time i might add here)
Search bar (could have) - As a site user I can use a search bar to search for a specific place so that I have quick and easy access to the information I want.

Acceptance Criteria:
* As a site user, I can easily find and navigate to the search bar.
* As a site user, I can use the search bar to search by place name.
* As a site user, I can view the results yielded by my search that I can click from. -->


## Tasks

The tasks for the website development process was closely followed as mentioned in CI's Django module "I Think Therefore I Blog" walkthrough project. Not only the one walkthrough project, even the database management system module  was also helpful to understand and execute the whole plan of making a blog webite. The task is generally the developers step towards preparing the app.
The tasks that I have followed during the development phase were carried out in this order.

**Before Project Inception**

- Design ERD and Data 
- Create Repository in GitHub
- Create Project, Epics, User Stories and prepare (Kanban) Board

**Creation of Project in GitPod**

- Create the django project. Check details in [deployment-section](#deployment)
- Deploying app to Heroku - Details in [deployment](#deployment) section
- Create Database Models
	- Set up models.py file in "blog" directory
- Build Admin site
- Set up Templates
	- Create base.html - Navbar and Footer content, which gets extended to all the other template files
	- Add responsiveness to navigation and footer
    - Create index.html, view and style
	- Set up template file features with views.py and urls.py
  - about.html (Description about the bloggers and purpose)
  - blog.html (to view all blog posts)
  - user_page.html (for user's personal collections)
  - post_details.html (for detailed post view)
  - smartphones_post.html (to view blog post for a selected iPhones/ mobile phone)
  - add_post.html (to allow user's input for blog posts)
  - delete_post.html (to allow user to delete his post)
  - update_post.html (to allow user to edit his post)
  - user_post_list.html (to allow user to view all post, which he posted so far)
- Install Allauth for sign in, sign up and sign out templates with-  pip3 install django-allauth 
	- Install crispy-forms to add styles to Django account templates with-  pip3 install crispy-bootstrap5
- Intensive Manual Testing and Validation checks of each page and codes written
- Final Deployment steps

-----

[Back to top](#content)

## Design

### Colours

The colour scheme has considered based on easy accessibility for all and have been consistently maintained throughout the website. 

### Typography

Fonts were imported using Google Fonts. Kay Pho Du was used throughout with a backup of sans-serif. The font is very clear and eay to read for users.

### Imagery

All the imagery is related to the iPhone's various models and generations and website design. Some images including carousel are static.

----

## Database Diagram

Smart Draw was used to create a database schema to visualise the types of custom models the project requires. This schema was used as a guide to what needed to be added to each model. Below is the Database structure that this project is based on. The relationship between Entities Post, Author, Destination and Comment are shown in this diagram.

![ER Diagram](assets/erd/)

----
[Back to top ⇧](#content)

# Features

## Home Page

At the very first glimpse, user can see a Navigation menu with a search button and carousel-images on the homepage. Homepage provides the user with some quick information about the site and make use of all its features. User do not need to be registered to view a blog post. The responsive navigation bar is featured on all pages. 

![Homepage](assets/home-page.jpeg)

----

## Navbar

- The navigation bar is present at the top of every page and navigates all links to the respective pages.
- The options to Sign Up or Log in will change to the option to log out once a user has logged in.
- The navbar is fully responsive, collapsing into a hamburger menu when the screen size becomes smaller.

![Navbar](assets/features/navbar1.jpeg)


## Navbar after loged in user

* If the user is logged in (username Mahi is provided as an example here), navbar will be shown with user name and logout options. On a desktop, the navigation menu will appear as shown below:

![logged-in-user-Navbar](assets/features/navbar.jpeg) 
