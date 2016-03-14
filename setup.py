import re
from setuptools import setup


version = re.search(
   '^__version__\s*=\s*"(.*)"',

   #folder name/ name_module.py
   open('project/project_module.py').read(),
   re.M
   ).group(1)

#create README in master folder
with open("README.rst", "rb") as f:
   long_descr = f.read().decode("utf-8")


setup(
  #name is the project/module name 
   name = "project",
  #packages = nested folder name
   packages = ["project_module"],
   entry_points = {
  #project_pip(dont know) = nested folder.module py: function called
       "console_scripts": ['project_pip = project.project_module:projects']
       },
   version = version,
   description = "Python command line html creator",
   long_description = long_descr,
   author = "William Morgan",
   author_email = "akulais@gmail.com",
   url = "https://github.com/akulais/project.git"
)
