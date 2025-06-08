# cloud-todo-app

A simple cloud-based to-do app that allows you to store and manage planned activities. The app syncs tasks across devices using Firebase and is built with a Flask backend.

## Features

- **Task Management**: Add and remove planned tasks.
- **Cloud Sync**: All your tasks are stored in Firebase and synced across devices.
- **User Authentication**: Secure login and registration via Firebase Authentication.
- **Simple Interface**: Focuses solely on planned activities without any unnecessary complexity.

## Technologies Used

- **Frontend**:
  - HTML, CSS, JavaScript
  - [Vanilla JS](https://developer.mozilla.org/en-US/docs/Web/JavaScript) or any other JS framework you may have used (React, Vue, etc.)
  
- **Backend**:
  - **Flask**: Python web framework for handling backend logic.
  
- **Database**:
  - **Firebase Realtime Database** for storing user tasks.

- **Authentication**:
  - **Firebase Authentication** for secure user sign-ups and logins.

## OUTPUT

![Image](https://github.com/user-attachments/assets/f7048768-ad93-4ec7-acfb-751b45ce8bfa)

## Installation

To run the project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/priyabhaargavi/cloud-todo-app.git
    cd cloud-todo-app
    ```

2. Install the frontend dependencies (if any):
    ```bash
    pip install
    ```

3. Install the backend dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up Firebase:
    - Go to [Firebase Console](https://console.firebase.google.com/).
    - Create a new project and add the Firebase credentials to your app (either in a config file or environment variables).
    - Set up Firebase Authentication and Realtime Database.

5. Run the Flask app locally:
    ```bash
    python app.py
    ```

The app should now be running on `http://localhost:5000`.


