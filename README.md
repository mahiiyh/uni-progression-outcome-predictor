# uni-progression-outcome-predictor

# University Progression Outcome Predictor

This Python program predicts progression outcomes for students at the end of each academic year based on the University's regulations. It allows students and academics to input their credits at pass, defer, and fail, and it displays the appropriate progression outcome (progress, progress with module trailer, module retriever, or exclude).

## Features

- **Student Version:** Allows students to input their credits and get their progression outcome.
- **Academics Version:** Allows academics to input credits for multiple students, displays a histogram of the progression outcomes, and saves the data to a list and a text file.
- **Input Validation:** Checks for invalid inputs such as non-integers, out-of-range credits, and incorrect total credits.
- **Histogram Visualization:** Uses the `graphics.py` module (included in the Python standard library) to create a histogram representing the number of students in each progression category.
- **Data Storage:** Stores the progression data in a list (Part 2) and a text file (Part 3) for the Academics Version.

## Requirements

- Python 3.x
- `graphics.py` module (included in the Python standard library)

## Usage

1. Clone or download the repository.
2. Open a terminal or command prompt and navigate to the project directory.
3. Run the program with `python main.py`.
4. Follow the on-screen instructions to choose the desired version (Student or Academics) and input the credits.
    - For the Academics Version, enter 'q' to quit and view the histogram and stored data.

## Code Strcture
### `main.py`
Contains the main program logic and function calls.
- `main()`: Function to run the program and handle user input.

### `functions.py`
Contains the general functions to get inputs, decide outcomes, and handle the program.
- `in_data()`: Function to get valid inputs from the user.
- `get_progression_outcome()`: Function to determine the progression outcome based on the credits.
- `multiple_outcomes_question()`: Function to ask the user if they want to enter another set of data.

### `histogram.py`
Contains the logic and function to draw the Histogram.
- `draw_bar()`: Function to draw a single bar in the histogram.
- `draw_histogram()`: Function to create and display the histogram.

### `student.py`
Contains the logic and function to run the Student Version.
- `student_version()`: Function to run the Student Version.

### `academics.py`
Contains the logic and function to run the Academics Version.
- `academics_version()`: Function to run the Academics Version.

## Coursework Specification

The program is based on the provided Coursework Specification document, which outlines the requirements and marking scheme for the assignment.

## License

This project is licensed under the MIT License.

## Acknowledgements

The coursework specification and requirements were provided by the University of Westminster.

## Additional Notes

- Colors used in the histogram can be found in reference to Wikipedia X11 color names: `https://en.wikipedia.org/wiki/X11_color_names`