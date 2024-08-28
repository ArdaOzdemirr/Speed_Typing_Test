
Speed Typing Test
Overview
The Speed Typing Test is a simple yet effective typing speed and accuracy test application developed using Python and Pygame. The application presents a random sentence to the user, and measures their typing speed and accuracy as they type the sentence. Results are displayed upon completion, including time taken, accuracy percentage, and words per minute (WPM).

Features
Random Sentences: The application pulls random sentences from a file or uses default sentences if the file is missing.
Typing Speed Calculation: Measures the user's typing speed in words per minute.
Accuracy Calculation: Calculates the accuracy of the typed text compared to the original sentence.
Interactive Interface: Provides a user-friendly interface with an input box and result display.
Requirements
Python 3.x
Pygame library
Installation
Clone the Repository:


git clone https://github.com/ArdaOzdemirr/Speed_Typing_Test.git
Navigate to the Project Directory:


Install Dependencies: Ensure you have Pygame installed. You can install it using pip:


Prepare the Sentences File: Create a file named sentences.txt in the project directory and add sentences, one per line. If the file is missing, default sentences will be used.

Usage
Run the application using Python:

How to Play
The application will display a random sentence.
Type the sentence as quickly and accurately as possible.
Press Enter when finished typing.
The application will display the time taken, typing accuracy, and words per minute (WPM).
Click on the "Reset" button to start a new typing test.
Troubleshooting
Font Not Initialized Error: Make sure to initialize Pygame using pygame.init() at the beginning of the script.
FileNotFoundError: Ensure that sentences.txt is present in the project directory.
Contributing
Feel free to contribute to the project by submitting issues or pull requests. Your feedback and contributions are welcome!

License
This project is licensed under the MIT License. See the LICENSE file for details.
