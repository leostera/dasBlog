# Import os.path module
import os.path

# Import PROJECT_DIR var from project settings
from blog.settings import PROJECT_DIR

def full_path(relative_path):
	"""
	Calculate the full path from a relative path inside the project dir.

	relative_path	the path inside PROJECT_DIR to be joined

	returns			full path to relative path incluiding project path
	"""
	return os.path.join( PROJECT_DIR, relative_path )