from .project_generator import Project

version_info = (0, 1, 2, '')
__version__ = '.'.join(map(str, version_info[:3])) + ''.join(version_info[3:])