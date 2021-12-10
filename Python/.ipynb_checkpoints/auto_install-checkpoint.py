import subprocess
import sys


"""When it comes to automating the installation of Python packages, you can create a Python script that runs pip as a subprocess with just a few lines of code:"""

try:
    import pandas as pd
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'pandas'])
finally:
    import pandas as pd

try:
    import pyodbc as odbc
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'pyodbc'])
finally:
    import pyodbc as odbc