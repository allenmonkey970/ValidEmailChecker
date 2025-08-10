# ValidEmailChecker

ValidEmailChecker is a simple desktop application for checking if an email address is valid, disposable, and has valid DNS records. It uses a Python Tkinter GUI for the client and a small Node.js Express server as a backend. The backend queries the [Disify email validation API](https://www.disify.com/).

## Features

- **Easy-to-use GUI**: Just enter an email address and get instant feedback.
- **Disposable email detection**: Know if an email is from a disposable service.
- **DNS check**: See if the domain has valid DNS records.
- **API-based validation**: Uses the Disify API for accuracy.

## How it Works

1. The user enters an email address in the desktop app.
2. The Python client sends a request to the local Node.js server.
3. The server fetches validation info from Disify and returns it to the client.
4. Results are displayed in the GUI in a friendly format.

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/allenmonkey970/ValidEmailChecker.git
cd ValidEmailChecker
```

### 2. Start the Backend Server

The backend is written in Node.js.

```bash
cd ValidEmailChecker
npm install
node server.js
```

The server will start on `http://localhost:5000`.

### 3. Run the Python Client

Make sure you have Python 3 and pip installed.

#### Install dependencies:

```bash
pip install pillow requests
```

#### Run the client:

```bash
python client.py
```

> **Note:** The `logo.png` file is required in the same directory as `client.py` for the GUI icon.

## File Structure

- `client.py` – Python Tkinter GUI client.
- `server.js` – Node.js Express backend server.
- `logo.png` – App icon/logo.

## Screenshots

<img src="https://github.com/allenmonkey970/ValidEmailChecker/blob/main/blank.png" alt="Blank Use of App"/>
<img src="https://github.com/allenmonkey970/ValidEmailChecker/blob/main/email.png" alt="Results of App"/>

## Troubleshooting

- **CORS Errors:** The server uses CORS, but if you run into CORS issues, make sure the server is running before starting the client.
- **Connection Errors:** Ensure the backend server is running on localhost:5000 before launching the client.
- **Logo Issues:** If you get an error related to `logo.png`, make sure the image exists in the same folder as `client.py`.

## License

This project is for learning and demo purposes. Use it as you wish.

## Credits

- [Disify Email Validation API](https://www.disify.com/)
- [Flaticon (Gmail Logo)](https://www.flaticon.com/free-icon/gmail_732200?term=email&page=1&position=10&origin=tag&related_id=732200))

