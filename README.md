<h1 align="center">La Grill - Fine Dinning Restaurant</h1>

[View the live project here.](https://la-grill-pp4-40d10c869885.herokuapp.com/)

Welcome to La Grill, a fine dining restaurant. Here we have specially catered food from the top chefs around the world.

<h2 align="center"><img src="https://github.com/MikesCodingCreations/pp4/blob/main/la-grill-full-site.png"></h2>

## User Experience (UX)

-   ### User stories

    - ### Viewing & Navigation

    - ### Registration & User Accounts
        1. Account registration: 
    - ### Sorting & Searching


    -   #### Customer Goals
        1. As a Customer I can scroll through/review the website so that easily understand the main purpose of the site and learn more about what the restaurant offers.
        2. As a Customer I can navigate the website smoothly so that I can find the menu, how much items cost, and what they look like from photos.
        3. As a Customer I can analyze the staff, so that I can be assured of the quality of food/service I will receive.
        4. As a Customer I can locate the companies' social media links so that I can determine how trusted and known they are.
        5. As a Customer I can receive a notification so that I can confirm my reservation.
        6. As a Customer I can Adjust my table size and time/date of reservation so that I can control when I can secure my visit to the restaurant.

    -   #### Site Owner Goals
        1. As a Site owner I can modify site content so that I can keep users up to date with the company's ongoings.
        2. As a Site owner I can easily modify menu content, so that I can make changes to the menu and therefore offer customers valid information.
        3. As a Site owner I can review/accept/delete reservation requests so that I ensure the restaurant is not overbooked and customers are notified of their reservation.

-   ### Design
    -   #### Colour Scheme
        -   The three main colors used are black, white, and gold.
            - The reasoning behind the color choices is from backed studies from [[AlabamaChain](https://alabamachanin.com/journal/2015/01/inspiration-black-and-gold)], [LoveHappens Magazine] (https://www.lovehappensmag.com/blog/2023/01/10/black-and-gold-an-iconic-color-combo/)] and [[My Smart Blog], (https://mystart.com/blog/shining-in-contrast-unveiling-the-symbolism-behind-black-gold/)] that indicate colors such as black and gold are associated with importance, luxury, or prestige. Something the company strives for. Moreover, the white is then used for text to stand out on the page.
    -   #### Typography
        -   The Rozha One font is the main font used throughout the whole website with  Serif as the fallback font in case for any reason the font isn't being imported into the site correctly. Rozha One is a clean font used frequently in restaurant websites, so it is both attractive and appropriate.
    -   #### Imagery
        -   Imagery is important, and so is the lack of imagery. The large, background hero page which is just black signifies the simplicity and fine dining establishment that it is. You will see from trends that the lower class an organization/restaurant is, the more colors and images they have going on. Therefore keeping the background image a plain black page with strong colors such as white and gold will provide the user with all the information they need.

## Features
-   Responsive on all device sizes.
-   Interactive elements such as the Nav bar and menu page.
-   Ability to POST a reservation request to the backend.
-   Ability to login to view reservations.
-   Able to login to interact with blog posts.

## Technologies Used
-   [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML)
-   [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
-   [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
-   [Python](https://developer.mozilla.org/en-US/docs/Glossary/Python)
-   [Django](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)
-   [AllAuth](https://docs.allauth.org/en/latest/)

### Frameworks, Libraries & Programs Used
1. [Bootstrap 5.3.2:](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
    - Bootstrap was used to assist with the responsiveness and styling of the website.
1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Roza One' font into the style.css file which is used on all pages throughout the project.
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
1. [Unsplash:](https://unsplash.com/)
    - Unplash was used to gather images for the site.
1. [Pexels:](https://www.pexels.com/)
    - Pexels was used to gather images for the site.

## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

-   [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) 
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
-   [JSHint JavaScript Validator](https://jshint.com/)

### Testing User Stories from the User Experience (UX) Section

-   #### First-Time Visitor/User Goals

    1. As a Visitor/User, I want to easily understand the main purpose of the site and learn more about what the restaurant offers.

        1. Upon entering the site, users are automatically greeted with a clean and easily readable navigation bar to go to the page of their choice. Underneath there is a Hero page with Text and a "Reservations" Call to action button which navigates the user to make a reservation via a form.
        2. The main points are made immediately with the hero page which displays the name of the site, the logo, and an option to scroll further down.
        3. The user has multiple options. They may use the navigation bar to navigate to their preferred page, the reservation button to make a reservation, or scroll down to view more information. 

    2. As a Visitor/User, I want to be able to easily navigate through the site to find content such as the menu, how much items cost, and what they look like from photos. 

        1. Upon navigating down to the menu or clicking the menu icon in the navigation bar, users will be able to view the current menu options that La Grill offers.
        2. Users will be able to read about each menu item, view the photo, and find out how much each item costs.
        3. For more information, users can click on an individual menu item to find more details such as how many guests it feeds.

    3. As a Visitor/User, I want to verify who is preparing the food in an 'about the chef's section' so I am aware of the quality i will recieve. 

        1. Upon navigating to the 'About Us' section of the site via the Navbar, users will find the up to date information of the current staff.
        2. Each staff member will be displayed with an image, their title, and a short paragraph about their background and speciality. 

    4. As a Visitor/User, I want to locate their social media links to see verify the followings on social media to determine how trusted and known they are.

        1. As a user, you may navigate to the Contact Us part of the page located in the footer or in the hero page where the social media links are located.
        2. Users will be greeted with a hover effect to display the ability of the clickable links which will direct them to the relevant social pages.

    5. As a Visitor/User, I want to be able to make reservations and receive a confirmation on the screen that my reservation has been confirmed. 

        1. Users have multiple options to make a reservtion. The first is using the navigation bar 'Reservation' link. Here you will be directed to the reservation form page. Upon filling out details, you will be greeting with a 'thank you' page to confirm the reservation.
        2. Users may also get to the same reservation page by clicking on the rather large reservation icon on the hero page.
        3. Certain information is required from the user such as their name, email address, phone number, guest party size, date and finally time of their desired booking.
        4. There are validation inputs that will display if a user does not meet the minimum criteria such as a valid email, phone number or date/time.

-   #### Admin/Owner Goals
    1. As a Owner/Admin, I want to easily modify content on the backend which will display on the live site such as 'about us' or 'contact' information.

        1. Owners will be able to navigate to the backend by entering '/admin' into the URL bar. Here they will be greeted with the simple Django interface.
        2. On the left-hand side, the owner/admin will be able to navigate to pages such as About Us where they can update company policies or history information. 

    2. As a Owner/Admin, I want to have the ability to make changes to the chef's information such as pictures/titles or bios.

        1. Using the same login as above, the owner/admin can make changes to their chef's section such as changing the image of a chef.
        2. There is also the ability to make changes to the menu items via the admin panel login.

    3. As a Owner/Admin, I want to view reservations made and the ability to cancel them.

        1. Navigating to the admin login, the owner/admin can view all reservations made. 
        2. Here they can delete a reservation if they find it is false or they do not wish to take it on.

### Further Testing
-   The Website was tested on Google Chrome, Microsoft Edge and Safari browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop, and iPhone X.
-   A large amount of testing was done to ensure that all pages were connecting correctly.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Known Bugs
-   On some mobile devices the About Us and menu sections are not centrally aligned.

## Deployment

### Heroku
The project was deployed to Heroku using the following steps...

1. Log in to Heroku and locate your [apps](https://dashboard.heroku.com/apps)
2. Click 'new' on the right-hand side of the page and click on 'create new app' in the dropdown
3. Enter a unique app name and choose your region
4. Access the settings of the app and scroll down 'reveal configs'
    1. Here you much connect your security key and database url
    2. These URL's must match the ones in the ENV.PY file
5. Once entered, save them then navigate to 'deploy'
6. Ensure you are connected to github and you select the correct respository.
7. Include the app url in the allowed hosts within your settings file.
8. Hit deploy in Heroku and your app should be live.

### Content

-   All content was written by the developer.

### Media

-   All Images were gathered from Pexels and Upsplash..

<!-- images -->
<!-- 
    Chef 1 - https://unsplash.com/photos/man-in-black-t-shirt-holding-stainless-steel-bowl-eBmyH7oO5wY
    Chef 2 - https://unsplash.com/photos/man-preparing-food-v3OlBE6-fhU
    Chef 3 - https://unsplash.com/photos/a-man-cooking-food-in-a-kitchen-wNQoaYCFcsI
    Chef 4 - https://unsplash.com/photos/man-in-black-nike-jacket-wearing-white-cap-SiQgni-cqFg

    Menu item 1 (pasta) - https://unsplash.com/photos/pasta-in-tomato-sauce-PLyJqEJVre0
    Menu item 2 (osyers) - https://www.pexels.com/photo/delicious-oysters-with-lemon-served-in-fancy-restaurant-4946440/
    Menu item 3 (gnocci) - https://www.pexels.com/photo/plate-of-food-next-to-glass-of-red-wine-2878742/
    Menu item 4 (lobster) - https://www.pexels.com/photo/delicious-boiled-lobster-on-plate-in-restaurant-4553120/
    Menu item 5 (steak) - https://www.pexels.com/photo/appetizing-steak-served-on-table-with-mussel-salad-6542793/
    Menu item 6 (tacos) - https://www.pexels.com/photo/tacos-served-in-a-restaurant-19250424/ 
-->
