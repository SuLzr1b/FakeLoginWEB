# FakeLoginWEB

A web-based Python tool using Flask, HTML, CSS, and JavaScript to simulate fake login screens for studying phishing techniques, built for educational purposes.

**WARNING**: This project is for educational purposes only. Do not use to collect real credentials or deceive users. Unauthorized use may violate laws, such as Brazil's General Data Protection Law (LGPD).

## Purpose
This project helps cybersecurity students understand how phishing attacks collect credentials through fake login interfaces. It provides a realistic web-based login screen with username and password fields, logs user inputs, and demonstrates social engineering techniques in a controlled, ethical environment.

## Features
- Simulates a login interface with a styled web page (HTML/CSS) and Flask backend.
- Captures username and password inputs, logging them with timestamps to `login_settings.txt`.
- Displays "invalid credentials" to mimic a phishing attempt, using AJAX for smooth interaction.
- Includes prominent ethical warnings in the code and interface to ensure responsible use.
- Validates empty fields and handles errors gracefully.

## Requirements
- Python 3.x
- Flask (`pip install flask`)
- A modern web browser (e.g., Chrome, Firefox)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/FakeLoginWEB.git
   ```
2. Install Flask:
   ```bash
   pip install flask
   ```
3. Navigate to the project directory:
   ```bash
   cd FakeLoginWEB
   ```

## Usage
1. Run the Flask server:
   ```bash
   python app.py
   ```
2. Open a web browser and go to `http://127.0.0.1:5000`.
3. On the login page:
   - Enter a username and password.
   - Click "Login" to log the attempt and see "invalid credentials" message.
   - Try multiple times to simulate different attempts.
4. Check `login_settings.txt` in the project directory for recorded attempts.

**Note**: Always test in a controlled environment with explicit permission. Do not use to collect real credentials.

## Example Log (`login_settings.txt`)
```
2025-04-29 23:45:15.123456: Usuário: John, Senha: 123
2025-04-29 23:45:16.234567: Usuário: Brow, Senha: 321
```

## Project Structure
```
FakeLoginWEB/
├── app.py                   # Flask server
├── templates/
│   └── index.html           # Login page
├── static/
│   ├── style.css           # Styles for the login page
│   └── script.js           # Client-side logic for form submission
```

## Related Projects
- [FakeLoginTkinter](https://github.com/yourusername/FakeLoginTkinter): A Tkinter-based version of this fake login simulator, using a desktop GUI to demonstrate credential capture.

## Ethical Considerations
This tool is strictly for educational purposes, such as learning about phishing and social engineering in cybersecurity. Do not use it to collect credentials or deceive users, as this may violate privacy laws, including Brazil’s LGPD. Always obtain permission and test in a controlled environment.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
Created by [SuLzr1b] as part of a cybersecurity learning journey.
