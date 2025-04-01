# Django AJAX Usernames Management

This project demonstrates how to use Django and AJAX to manage usernames in a web application without refreshing the page. It allows users to add, delete, and edit their usernames through AJAX requests. The main purpose of this project is to show how to integrate front-end interactivity with Django views and models, using JSON responses for dynamic content updates.

## Features

- **Add Usernames**: Users can add new usernames.
- **Delete Usernames**: Users can delete usernames dynamically.
- **Edit Usernames**: Users can update their usernames without refreshing the page.
- **AJAX Integration**: All interactions (add, delete, edit) happen without a page reload.
- **CSRF Protection**: Ensures the AJAX requests are secure using CSRF tokens.
- **Dynamic Updates**: The page updates the username list immediately after any change (add, delete, edit).

## Setup Instructions

### Prerequisites

Make sure you have the following installed:

- Python (preferably version 3.8 or higher)
- Django (installed via `pip install django`)

### Installation Steps

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/django-ajax-usernames.git
