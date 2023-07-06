from setuptools import setup, find_packages
from src import tree
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  "Operating System :: OS Independent",
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='treGen',
  version='2.1.1',
  description='A simple Directory Tree Generator',
  long_description='README.MD', #open('README.MD').read(),
  long_description_content_type='text/markdown',
  url='https://github.com/JRS296/Directory-Tree',  
  # entry_points='''
  #       [console_scripts]
  #       treGen = ROOT_TREE_GENERATOR
  #   ''',
  entry_points={
        'console_scripts': [
            'treGen = tree',
        ]
    },
  author='Jonathan Rufus Samuel',
  author_email='jrsstudios@skiff.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='tree-generator', 
  packages=find_packages(),
  install_requires=[''] 
)