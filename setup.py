import sys
from setuptools import setup, find_packages

setup(
   name = "h2t",
   versionb = "1.0",
   description = "Turn HTML into equivalent Markdown-structured text.",
   author = "Wesagn Dawit",
   # author_email = "",
   classifiers=[
       'Programming Language :: Python',
       'Programming Language :: Python :: 2',
       'Programming Language :: Python :: 2.3',
       'Programming Language :: Python :: 2.4',
       'Programming Language :: Python :: 2.5',
       'Programming Language :: Python :: 2.6',
       'Programming Language :: Python :: 2.7',
       'Programming Language :: Python :: 3',
       'Programming Language :: Python :: 3.0',
       'Programming Language :: Python :: 3.1',
       'Programming Language :: Python :: 3.2'
     ],
    entry_points="""
        [console_scripts]
        h2t=h2t:main
    """,
   license='iCog-Laws',
   packages=find_packages(),
   py_modules=['h2t'],
   include_package_data=True,
   zip_safe=False,
)
