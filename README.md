# GamesCave

Welcome to the gamesCave, a web application of social portal designed for games and gamers inspired by www.gry-online.pl. This project is built using a powerful stack of technologies, ensuring a robust and efficient solution.

[![AWS RDS](https://img.shields.io/badge/AWS%20RDS-Cloud-orange)](https://aws.amazon.com/rds/) [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-orange)](https://www.postgresql.org/) [![Django](https://img.shields.io/badge/Django-Backend-blue)](https://www.djangoproject.com/) [![Python](https://img.shields.io/badge/Python-Backend-blue)](https://www.python.org/) [![HTML5](https://img.shields.io/badge/HTML5-Frontend-yellow)](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) [![CSS](https://img.shields.io/badge/CSS3-Frontend-yellow)](https://developer.mozilla.org/en-US/docs/Web/CSS) [![JavaScript](https://img.shields.io/badge/JavaScript-Frontend-yellow)](https://developer.mozilla.org/en-US/docs/Web/JavaScript) [![Bootstrap](https://img.shields.io/badge/Bootstrap-Frontend-yellow)](https://getbootstrap.com/) 

![Home page](https://github.com/Mrokus95/gamesCave/assets/59625513/51a2a712-e509-48d5-bacc-d22a7c1e8e4b)

## Table of contents
* [Installation process](#installation-process)
* [Technologies](#technologies)
* [Features](#Features)


## Installation process:

1. Clone the repository to your local computer:

    ```
    $ git clone 'https://github.com/Mrokus95/gamesCave.git'
    ```

2. Navigate to the project directory:

    ```
    $ cd gamesCave
    ```

3. (Optional) It is recommended to create and activate a Python virtual environment:

    ```
    $ python -m venv venv
    $ python venv/bin/activate
    ```

4. Install the required dependencies:

    ```
    $ pip install -r requirements.txt
    ```

5. Set the environment variables:

    **General Django settings:**
    - `SECRET_KEY`: Django secret key (automatically generated when creating a Django project)

    **AWS RDS settings:**
    - `NAME`: The database name.
    - `USER`: The username that you configured for your database.
    - `PASSWORD`: The password that you configured for your database.
    - `HOST`: The hostname of the DB instance.
    - `PORT`: The port where the DB instance accepts connections. The default value varies among DB engines.

    **AWS S3 settings:**
    - `AWS_ACCESS_KEY_ID` = AWS access key ID
    - `AWS_SECRET_ACCESS_KEY` = AWS secret access key
    - `AWS_STORAGE_BUCKET_NAME` = AWS Storage bucket name
    - `AWS_S3_REGION_NAME` = AWS S3 region name
    - `AWS_S3_FILE_OVERWRITE` = File overwrite option (False/True)
    - `AWS_DEFAULT_ACL` = Default file access control (None/private/public-read)
    - `AWS_S3_VERIFY` = SSL verification for S3 (True/False)
    - `AWS_S3_ADDRESSING_STYLE` = S3 addressing style (e.g., "virtual")
    - `AWS_S3_ENDPOINT_URL` = S3 endpoint URL
    - `DEFAULT_FILE_STORAGE` = Default file storage tool ('storages.backends.s3boto3.S3Boto3Storage')
   
    **Gmail account credentials:**
    - `EMAIL_HOST_USER`: The email address
    - `EMAIL_HOST_PASSWORD`: The key or password app

    **Gmail SMTP settings:**
    - `EMAIL_HOST`: 'smtp.gmail.com'
    - `EMAIL_USE_TLS`: True
    - `EMAIL_PORT`: 587

    **Social portals authentication settings:**
    - `SOCIAL_AUTH_FACEBOOK_KEY` = Facebook app key
    - `SOCIAL_AUTH_FACEBOOK_SECRET` = Facebook app secret

    - `SOCIAL_AUTH_GOOGLE_OAUTH2_KEY` = Google OAuth2 client ID
    - `SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET` = Google OAuth2 client secret

    - `SOCIAL_AUTH_TWITTER_KEY` = Twitter app key
    - `SOCIAL_AUTH_TWITTER_SECRET` = Twitter app secret

  You can set the environment variables on your operating system or place them in a .env file in the project's root directory.

  ***Attention!***
  
  Many social services do not allow redirection to the address 127.0.0.1 or localhost after successful authentication. 
  They require providing a domain name. In Linux or OS X systems, a solution is editing the /etc/hosts file by adding a line that maps any chosen domain to the local computer's address. 
  In our case, this will be gamescave.pl, so the command should look like 127.0.0.1 gamescave.pl.
  
  For Windows systems, the mentioned file can be found at C:\Windows\System32\Drivers\etc\hosts.

7. Run the Django development server:

    ```
    $ python manage.py runserver_plus --cert-file cert.crt
    ```

    The application will be available at http://gamescave.pl:8000/.

## Technologies

I have utilized a diverse range of technologies to develop the gamesCave, ensuring its functionality, scalability, and efficiency.

### AWS RDS (Amazon Relational Database Service) <img src="https://github.com/Mrokus95/SchoolManagmentApp/assets/59625513/93a6776b-0dfb-4d21-8cb7-15af08644212" alt="aws rds" width="25px" height="25px">


I integrated AWS RDS and S3 to host our database and media in the Amazon cloud. This allowed me to develop my AWS skills. The use of Amazon services enables efficient and reliable data storage.

### PostgreSQL Database <img src="https://github.com/Mrokus95/SchoolManagmentApp/assets/59625513/017d3d41-b9bd-4c05-b5c7-8cd1e32e5efc" alt="postgreSQL" width="30px" height="30px">

To surpass the limitations of SQLite and enhance my relational database capabilities, I migrated to PostgreSQL.

### HTML5, CSS, JS, and Bootstrap <img src="https://github.com/Mrokus95/SchoolManagmentApp/assets/59625513/78447f01-ef70-44ce-b7d7-e10729e3c4a0" alt="html5-logo png" width="25px" height="25px"><img src="https://github.com/Mrokus95/SchoolManagmentApp/assets/59625513/be020416-3f50-4d2b-a3e0-85847c5e3312" alt="css3" width="25px" height="25px"><img src="https://github.com/Mrokus95/SchoolManagmentApp/assets/59625513/0c875413-b287-4950-8d9f-d4daeb87346f" alt="js" width="25px" height="25px"><img src="https://github.com/Mrokus95/SchoolManagmentApp/assets/59625513/16bd8ee7-c4b9-4125-a6c1-34aeeb83c5d0" alt="bootstrap" width="25px" height="25px">


For the frontend, I leveraged HTML5, CSS3, JavaScript, and Bootstrap5. These technologies collectively allowed me to design and develop a responsive, user-friendly, and visually appealing user interface.

### Python and Django <img src="https://github.com/Mrokus95/SchoolManagmentApp/assets/59625513/b82413c4-2b4c-4c82-a06d-b0ba5cdeebfe" alt="python" width="25px" height="25px"> <img src="https://github.com/Mrokus95/SchoolManagmentApp/assets/59625513/6cb9996c-5ab0-4797-a422-1c8894d2b7de" alt="django" width="30px" height="30px">

The backend of the project was developed using Python 3.12 and Django 4.2. Python's versatility and readability empowered us to create robust backend logic. Django's high-level framework facilitated rapid development, efficient database management, and seamless integration of various components.


## Features

### authSystem and Profile App

The authSystem and Profile applications serve as the backbone of user authentication and profile management within this project. The authSystem handles user registration, login, and the management of account details. During the registration process, a mechanism for sending activation links via email to the provided address has been meticulously implemented. Additionally, users have the convenience of authenticating through social media platforms, facilitated by seamless integration with APIs from Facebook, Gmail, and Twitter.

Key Features:

- User Registration and Login: Seamlessly create accounts and securely log into the system using the authSystem.
- Email Activation Links: A robust registration process ensures the use of email-based activation links for the purpose of verifying user accounts.
- Social Media Integration: Users can opt for hassle-free authentication via their social media accounts by leveraging the APIs of prominent platforms including Facebook, Gmail, and Twitter.

Registration view:
![rejestracja](https://github.com/Mrokus95/gamesCave/assets/59625513/daf0916d-851a-4705-bd35-11ad76892999)

Email template:
![email](https://github.com/Mrokus95/gamesCave/assets/59625513/a29ff542-68a8-41a8-9509-f83eed9a658a)

Edit profile view:
![edit profile](https://github.com/Mrokus95/gamesCave/assets/59625513/5ae49bcf-3bd3-42ff-8f67-4e4743d7f1ee)

### newsRoom App

The newsRoom application revolves around streamlined article management and publication. It encompasses the essential CRUD (Create, Read, Update, Delete) operations for posts. Furthermore, the application introduces a dynamic comment section for each post, empowering readers to actively engage with the content. An intelligent tagging system enhances the user experience by suggesting related posts.

Key Features:

- Post Management: The newsRoom app offers a comprehensive suite of features for effective article management, including the full spectrum of CRUD functionalities.
- Comment Section: Readers can readily contribute their thoughts and insights by participating in the comment section of articles, fostering a sense of community.
- Tagging System: Articles are efficiently organized through a tagging system, which not only assists in categorization but also suggests related content. This tagging system is skillfully integrated using the taggit library.
- Comment Reporting: Users possess the capability to report inappropriate comments, ensuring a respectful and constructive environment.
- Administrator Control: Administrators are empowered with the authority to modify or delete articles and oversee user comments, contributing to a well-maintained platform.

Skill Enhancement and Learning Opportunities

The development of the authSystem and newsRoom applications has provided invaluable learning experiences and skill growth:

- Django Proficiency: Crafting these features necessitated a deep comprehension of Django's framework, resulting in a considerable augmentation of development skills.
- Integration Prowess: The seamless integration with external APIs such as Facebook, Gmail, and Twitter underscores adeptness in connecting applications with third-party services.
- Library Implementation: The skillful integration of the taggit library for the tagging system showcases a seamless assimilation of third-party tools.
- Real-World Problem Solving: Overcoming challenges such as user authentication, permissions, and interaction with articles has enriched problem-solving abilities.

News list view:
![lista news](https://github.com/Mrokus95/gamesCave/assets/59625513/5287c7e9-796c-4ebf-9b22-dad49f6e424f)

News detail view:
![news_detail](https://github.com/Mrokus95/gamesCave/assets/59625513/88e725ea-7404-4962-9b95-dd49469a8524)

Create new news view:
![create news](https://github.com/Mrokus95/gamesCave/assets/59625513/5795d5e7-7f7d-44fe-8913-9e8b60b0b7ca)

Comments section view:

![comments](https://github.com/Mrokus95/gamesCave/assets/59625513/380a92b6-03ad-4194-b2a5-5a3daedc300f)
