# Installation Guide for MathSolver

This guide provides step-by-step instructions for installing and running the MathSolver application, both in development mode and as a packaged executable.

---

## Prerequisites

Before proceeding, ensure you have the following installed:

- **Python 3.8 or higher**
- **pip** (Python package manager)

---

## Installation Steps

### 1. Clone the Repository

Clone the MathSolver repository to your local machine:

```bash
git clone https://github.com/yourusername/MathSolver.git
cd MathSolver
```

---

### 2. Set Up a Virtual Environment (Optional but Recommended)

Create and activate a virtual environment to isolate dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

---

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

---

### 4. Run the Application in Development Mode

To run the application in development mode, use the following command:

```bash
python run.py
```

---

### 5. Package the Application (Optional)

If you want to package the application into an executable, follow these steps:

1. **Install PyInstaller**:
   ```bash
   pip install pyinstaller
   ```

2. **Build the Executable**:
   - Use the provided `.spec` file to build the executable:
     ```bash
     pyinstaller run.spec
     ```
   - The executable will be located in the `dist/` folder.

3. **Run the Executable**:
   - Navigate to the `dist/` folder and run the executable:
     ```bash
     cd dist
     ./run
     ```

---

### 6. Include Resource Files

If you modify the project structure or add new resource files (e.g., `.ui`, `.qss`, `.json`), ensure they are included in the `.spec` file under the `datas` section. For example:

```python
datas=[
    ('src/mathsolver/data/about.json', 'data'),
    ('src/mathsolver/ui/main_window.ui', 'ui'),
    ('src/mathsolver/ui/style/main_window.qss', 'ui/style'),
],
```

---

## Troubleshooting

### 1. `ModuleNotFoundError`

If you encounter a `ModuleNotFoundError`, ensure all dependencies are installed:

```bash
pip install -r requirements.txt
```

### 2. `FileNotFoundError`

If the application cannot find a resource file (e.g., `about.json`), ensure the file is included in the `.spec` file and the path is correctly specified in the code.

### 3. PyInstaller Issues

If PyInstaller fails to include files or produces errors, double-check the `.spec` file and ensure all paths are correct.

---

## Uninstallation

To uninstall the application, simply delete the project folder:

```bash
rm -rf MathSolver  # On Windows, use `rmdir /s /q MathSolver`
```

If you used a virtual environment, you can deactivate and delete it:

```bash
deactivate
rm -rf venv  # On Windows, use `rmdir /s /q venv`
```

---

## Support

For additional help, please open an issue on the [GitHub repository](https://github.com/codewithbotina/MathSolver/issues) or contact the developer directly.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
