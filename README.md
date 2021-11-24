# CyberAcademy

CyberAcademy is an on online learning platform developed using Python/Django.

And for front-end designing HTML/CSS/JavaScript is used. 


## Live Demo

https://cyberacademy.pythonanywhere.com/


## Features

#### Site access features:
- User must be logged in to Enroll or start a course
- For signup user is required username, fullname, E-mail and password
- For login user is required E-mail and password
- User can access dashboard after logging in
- User can search for a course using search box at the navbar
- User needs to provide person details and ATM details to enroll in the course and make payment
- User must complete the payment to start learning a course
- On the dashboard, the user can find the ongoing or enrolled courses. User can also start learning courses from dashboard or enrolled tab

#### Administrative features:
- Only admin can add or delete courses
- Admin can see enroll details and payment status of a user

## Getting started with development

#### 1. Clone this repository
```bash
  git clone https://github.com/mukesh0x0/CyberAcademy.git
  cd CyberAcademy
```
#### 2. activate the virtualenv
```bash
  source academy_env/bin/activate
```
#### 3. Install dependencies
```bash
  pip install -r reqirements.txt
```

#### 4. Run database migrations
```bash
  python manage.py makemigrations
  python manage.py migrate
```

#### 5. Create superuser
```bash
  python manage.py createsuperuser
```
#### 6. Run development server
```bash
  python manage.py runserver
```
## Tech Stack

**Front-end:** HTML, CSS, JavaScript

**Server-side:** Python/Django


## Screenshots

![App Screenshot](https://raw.githubusercontent.com/mukesh0x0/CyberAcademy/main/screenshots/cyber-academy-homepage.png)


## Feedback

If you have any feedback, please reach out to me at cliuser099@gmail.com


## License

MIT License
