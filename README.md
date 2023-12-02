# Color Detection using Webcam and Color Picker

This project allows users to detect and choose different colors using the webcam on their personal system. The application captures video from the webcam, processes each frame to identify prominent colors, and provides the user with the option to select colors from a color picker.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Pramod3245/Color-detection
   ```

2. **Navigate to the Project Directory:**
   ```bash
   cd color-detection-webcam
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Application:**
   ```bash
   python color_detection.py
   ```

2. **Webcam Access:**
   - Grant access to your webcam when prompted.

3. **Color Selection:**
   - Use the color picker to select different colors from the video stream.

4. **Quit:**
   - Press `Q` to exit the application.

## Features

- **Real-time Color Detection:**
  The application captures video from the webcam and provides real-time color detection.

- **Color Picker:**
  Users can choose specific colors from the video stream using a built-in color picker.

- **Webcam Support:**
  The application utilizes the webcam on the user's personal system.If you have any external cameras change the camera code in the main.py to appropriate code.

- **Simple Interface:**
  The user interface is designed to be user-friendly with easy-to-use controls.

## Dependencies

- OpenCV
- NumPy
- Tkinter (for GUI components)

## Contributing

Contributions are welcome! If you would like to contribute to the project, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push to your fork and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Feel free to customize and enhance the project according to your needs! If you encounter any issues or have suggestions, please open an issue on the GitHub repository.
