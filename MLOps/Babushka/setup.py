from pathlib import Path
from setuptools import setup, find_namespace_packages

BASE_DIR = Path(__file__).parent

# Load packages from requirements.txt
with open(Path(BASE_DIR, "requirements.txt")) as file:
    required_packages = [ln.strip() for ln in file.readlines()]
    
test =["pandas" ]

setup(name="dk", 
    license = "MIT", 
    description = "test", 
    author = "Daisuke Kuwabara", 
    install_requires = test,
    entry_points = {
        "console_scripts": [
            "babushuka" = "babushuka.main:app",
        ],
    },
    )
