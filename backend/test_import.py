import os
print(f"Current working directory in test_import.py: {os.getcwd()}")
print(f"Contents of current directory in test_import.py: {os.listdir()}")
try:
    from backend.utils import date_utils
    print("Import from backend.utils successful in test_import.py!")
except ImportError as e:
    print(f"Error importing from backend.utils in test_import.py: {e}")