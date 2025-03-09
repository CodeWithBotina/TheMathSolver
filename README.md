# MathSolver

MathSolver is a Python-based application designed to solve mathematical problems in areas such as sets, functions, relations, and induction. It provides an intuitive graphical user interface (GUI) built with PyQt6, allowing users to input formulas and select problem categories easily.

---

## Features

- **Mathematical Problem Solving**: Supports solving problems in sets, functions, relations, and induction.
- **User-Friendly Interface**: Built with PyQt6 for a smooth and professional user experience.
- **Customizable Styles**: Uses `.qss` files for styling the UI.
- **About Section**: Displays project information from an `about.json` file.

---

## Requirements

- Python 3.10 or higher
- PyQt6
- PyInstaller (for packaging the application)

---

## Installation

For detailed installation instructions, see the [INSTALL.md](INSTALL.md) file.

---

## Usage

1. **Run the Application**:
   - In development mode:
     ```bash
     python run.py
     ```
   - Using the packaged executable (after building with PyInstaller):
     ```bash
     ./dist/run
     ```

2. **Select a Problem Category**:
   - Use the dropdown menu to select a problem type (e.g., Sets, Functions, Relations, Induction).

3. **Input a Formula**:
   - Enter your formula in the input field and click "Send" to get a solution.

4. **View the About Section**:
   - Click "About" in the menu to see project information.

---

## **Project Structure**

```
MathSolver/
├── src/
│   └── mathsolver/          # Main application module
│       ├── __init__.py      # Module initialization
│       ├── main.py          # Main application logic
│       ├── ui/              # UI files
│       │   ├── main_window.ui
│       │   └── style/
│       │       └── main_window.qss
│       ├── data/            # Data files
│       │   └── about.json
│       └── logic/           # Application logic
│           ├── ui_loader.py
│           ├── chat_handler.py
│           └── about_handler.py
├── run.py                   # Entry point for the application
├── run.spec                 # PyInstaller configuration file
├── README.md                # Project overview
├── INSTALL.md               # Installation instructions
├── requirements.txt         # Python dependencies
└── .gitignore               # Specifies files to ignore in Git
```

---

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed description of your changes.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Thanks to the PyQt6 team for providing an excellent framework for building GUIs.
- Special thanks to Diego Alejandro Botina for developing this project.

---

## Contact

For questions or feedback, please contact:
- **Diego Alejandro Botina**
- Email: your.email@example.com
- GitHub: [CodeWithBotina](https://github.com/codewithbotina)
