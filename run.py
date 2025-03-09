import sys
import os

# Add the src directory to sys.path
src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'src'))
sys.path.append(src_dir)

# Run the main script
from mathsolver.main import main

if __name__ == "__main__":
    main()