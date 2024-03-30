# Django Twitter Clone

This project is a Twitter clone built using Django, a high-level Python web framework. It replicates some of the core features of Twitter, including sign-up/login, posting tweets with text and images, liking tweets, and following other users.

## Features

### Sign-up / Login
- Users can create an account by signing up with their email address and password.
- Existing users can log in using their credentials.

### Posting Tweets
- Users can compose tweets consisting of text and optionally attach images to their tweets.
- Tweets are displayed on the user's profile and the main feed.

### Liking Tweets
- Users can like tweets posted by other users.
- The total number of likes for each tweet is displayed alongside the tweet.

### Following People
- Users can follow other users to see their tweets in their main feed.
- The user's profile displays the number of followers and following users.

## Installation

1. Clone the repository:

git clone https://github.com/AmmarHazem/NotTwitterr.git

2. Navigate to the project directory:

3. Install dependencies:

pip install -r requirements.txt

4. Run migrations:

python manage.py migrate

5. Create a superuser (admin):

python manage.py createsuperuser

6. Start the development server:

python manage.py createsuperuser

6. Start the development server:

python manage.py runserver

7. Access the application in your web browser at `http://localhost:8000`.

## Usage

1. Create a new account or log in using existing credentials.
2. Once logged in, you can post tweets by navigating to the "Compose" page.
3. You can like tweets by clicking the like button beneath each tweet.
4. Follow other users to see their tweets in your main feed.

## Contributing

Contributions are welcome! Feel free to submit pull requests or open issues for any bugs or feature requests.
