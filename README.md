Gym Equipment Online Store
Overview:
This project is an online store for gym equipment. The homepage, named "HARVARD HTML", features a navigation bar with Bootstrap 5, a container with JavaScript and Bootstrap 5, which displays a message informing customers that orders over $69 receive free shipping. There is also a container that says "Welcome to our site" and introduces the gym company as being founded in 2023, offering a variety of gym equipment. Another Bootstrap navigation bar with the heading "Explore Our Store" allows users to navigate to different sections of the website. A toast appears on the screen with the message "Click here to sign up." If the user signs up, the toast directs them to "SignIn.html", which is a container with a login form. If the user logs in, the data is sent to the database, and Flask Python code is used to handle the POST request and respond with the message "Congratulations! You just logged in." Similar functionality exists in "SignUp.html", which is a sign-up form. The data from both the login form and sign-up form are stored in the same database but in different columns.

The website also features two products, "Bench Press" and "Dumbbells", each with its own product code, image, and price. When the user selects a product, they are taken to a corresponding HTML page, "theo.html" for dumbbells and "2nd page.html" for the bench press. These pages have a "Add to Bag" button, which, when clicked, takes the user to a "bag.html" page where the selected product is displayed in a table along with an "Explore" navigation bar that has a sign-up button and links to other products. If the user hasn't signed up or wants to add another product to the bag, they can do so. If they click "Buy", they are taken to a form where they need to fill in their address, postal code, card number, etc. This page is called "payment.html". Once the form is filled out, a pop-up message appears expressing congratulations on the recent purchase.

The primary functionality of the website is implemented in the Python file "database.py", which contains app routes, database inserts, render templates, request forms, etc. Each page also includes photos.
Technologies Used

    Front-end: HTML, CSS, Bootstrap 5, JavaScript
    Back-end: Flask (Python)
    Database:Sqlite3
    Deployment: Runs Local in Pycharm
    Url for youtube video:https://youtu.be/KDvPt_8D59U

Team Members

    Project Manager: [Theodore Kokkonis]
    Front-end Developer: [Theodore Kokkonis]
    Back-end Developer: [Theodore Kokkonis]
    UI/UX Designer: [Theodore Kokkonis]

Project Timeline

    Project Kickoff: [February 4th 2023]
    Front-end Development: [1 month]
    Back-end Development: [1 month]
    Testing and Debugging: [5 days]
    Deployment and Launch: [5 days]

Conclusion

The Gym Equipment Online Store project is a comprehensive e-commerce website for gym enthusiasts. It offers a user-friendly interface, multiple product options, and integration with a backend database for storing user information and processing orders. With its appealing design and robust features, the website aims to provide a seamless online shopping experience for customers looking to purchase gym equipment.