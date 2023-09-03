# EDUENV - Educational Environment 📚

<p align="center"><img width=2500 height=300 src="https://media.giphy.com/media/7WfJ4qp5hvjwaiPF5O/giphy.gif"></p>

**EDUENV** is a simple educational environment developed for the [Hack the Classroom](https://hack-the-classroom.devpost.com/?ref_feature=challenge&ref_medium=your-open-hackathons&ref_content=Submissions+open) hackathon, designed to provide essential functionality for both students and teachers. This project aims to enhance the learning experience within a short timeframe.

## Features

### For Students 🎓

- **Resource Library:** Access essential educational materials such as textbooks, articles, and videos.
- **🗓️ Time Table:** Keep track of your class timings.
- **⏲️ POMODORO:** Improve your concentration with the Pomodoro technique.
- **Courses:** Explore courses for personal development.

### For Teachers 👩‍🏫

- **Content Creation:** Quickly create and publish educational content, including lectures and assignments.
- **Assignment Management:** Easily distribute assignments to students.
- **Time Table:** Create and manage class schedules effortlessly.

## Setup

Follow these steps to set up and run EDUENV on your local machine:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/vishan01/EDUENV.git
   cd eduenv
   ```

2. **Create a Virtual Environment (Optional but recommended)**

   It's a good practice to work within a virtual environment to isolate project dependencies.

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Database Setup (SQLite is used by default)**

   You can use SQLite for development purposes. If you plan to use a different database, please configure it accordingly.

   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser (Admin Account)**

   This step is essential for managing the application.

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

   The application will be available at `http://localhost:8000/`.

## Support

If you have any questions or encounter issues with the application, please don't hesitate to contact our team at [EMAIL](vishnureddy228@gmail.com).

## License

This project is licensed under the [MIT License](./LICENSE.md). Feel free to use and modify EDUENV to suit your needs.

## Credits

Special thanks to the following resources and projects that contributed to the development of EDUENV:

- [Schedule Builder](https://schedulebuilder.org/)
- [Pomofocus](https://pomofocus.io/)
- [freeCodeCamp](https://freecodecamp.org)

Feel free to contribute and improve this file to make EDUENV even better! 🚀
