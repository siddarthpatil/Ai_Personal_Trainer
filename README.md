# Pose Estimation Web App

This project is a pose estimation application built using OpenCV and MediaPipe, designed to help users check their form while performing common gym exercises such as squats, push-ups, bench press, dips, pull-ups, and crunches. The application has been extended into a web app using Flask, allowing users to select exercises and receive real-time feedback on their form directly in their browser.

## Features

- **Real-time Pose Estimation**: Detects specific exercises using the MediaPipe Pose model.
- **Exercise Selection**: Users can choose from various exercises like squats, push-ups, bench press, dips, pull-ups, and crunches.
- **Visual Feedback**: Displays angles between joints and provides feedback on exercise form.
- **Web Interface**: The application runs as a Flask web app, making it accessible via any web browser.

## Project Structure

```
pose_estimation/
│
├── exercises/               # Package containing different exercise detection modules
│   ├── __init__.py          # Init file to make this directory a package
│   ├── squat.py             # Module for squat detection
│   ├── push_up.py           # Module for push-up detection
│   ├── bench_press.py       # Module for bench press detection
│   ├── dips.py              # Module for dips detection
│   ├── pull_up.py           # Module for pull-up detection
│   └── crunches.py          # Module for crunches detection
│
├── utils/                   # Utility functions
│   ├── __init__.py
│   ├── angle_calculation.py # Module for calculating angles
│   └── visualization.py     # Module for drawing landmarks, angles, and feedback on frames
│
├── templates/               # HTML templates for the Flask web app
│   └── index.html           # Main page with exercise selection
│
├── static/                  # Static files (CSS, images, etc.)
│   └── style.css            # Custom styles for the web app
│
├── main.py                  # Main script to run the Flask web app
├── requirements.txt         # List of dependencies
└── README.md                # Project documentation
```

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)
- OpenCV
- MediaPipe
- Flask

### Setting Up the Project

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/pose-estimation-webapp.git
   cd pose-estimation-webapp
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv pose_estimation_env
   source pose_estimation_env/bin/activate  # On Windows use: pose_estimation_env\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:

   ```bash
   python main.py
   ```

5. **Access the web app**:

   Open your browser and go to `http://127.0.0.1:5000/`.

## Usage

1. Open the web app in your browser.
2. Select the exercise you want to perform.
3. Start performing the exercise in front of your webcam.
4. The app will display real-time feedback on your form, including joint angles and suggestions.

## Customization

### Adding New Exercises

To add a new exercise:

1. Create a new module in the `exercises/` directory, similar to the existing ones (e.g., `new_exercise.py`).
2. Implement the detection logic for the new exercise.
3. Update the `detect_exercise` function in `main.py` to include the new exercise.

### Customizing the Web Interface

You can customize the appearance of the web app by editing the `style.css` file in the `static/` directory and the `index.html` file in the `templates/` directory.

## Contributing

Contributions are welcome! If you have ideas for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.