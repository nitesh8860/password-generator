# Password Generator Django App

The **Password Generator** is a simple Django-based web application that allows users to generate strong and random passwords.

## Features

- Generate random and secure passwords.
- Specify the length and complexity of passwords.
- Customize password characters to include numbers, symbols, and more.

## How to Run

Follow these steps to set up and run the Password Generator Django app:

1. Clone the Repository:

   ```shell
   git clone https://github.com/your-username/password-generator.git
   cd password-generator
   ```

2. Create a Virtual Environment:

   ```shell
   python -m venv venv
   source venv/bin/activate
   ```

3. Install Dependencies:

   ```shell
   pip install -r requirements.txt
   ```

4. Apply Database Migrations:

   ```shell
   python manage.py migrate
   ```

5. Create a Superuser (Admin):

   ```shell
   python manage.py createsuperuser
   ```

   Follow the prompts to create an admin account.

6. Run the Development Server:

   ```shell
   python manage.py runserver
   ```

7. Access the App:

   Open your web browser and visit `http://localhost:8000` to access the Password Generator.

8. Admin Access:

   You can access the admin panel at `http://localhost:8000/admin` using the superuser credentials you created earlier.

## Usage

- Use the web interface to generate passwords with different settings.
- Customize the password length, include numbers, symbols, and more.

## Contributing

Contributions are welcome! If you have any improvements or feature suggestions, please create a pull request.

## License

This project is open-source and available under the [MIT License](LICENSE). You are free to use and modify the application as needed.

Enjoy generating strong passwords with the Password Generator Django app!
