import sys
import os

# Add the root directory to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "src"))
sys.path.append(project_root)

from mathsolver.main import main

if __name__ == "__main__":
    main()