from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    "Operating System :: OS Independent",
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='treGen',
    version='3.0.0',
    packages=['src'],
    description='A simple Directory Tree Generator',
    long_description=open('README.MD').read(),  # 'README.MD',
    long_description_content_type='text/markdown',
    url='https://github.com/JRS296/Directory-Tree',
      entry_points={
            'console_scripts': [
                'treGen = src.cli:main',
            ]
        },
    author='Jonathan Rufus Samuel',
    author_email='jrsstudios@skiff.com',
    license='MIT',
    classifiers=classifiers,
    keywords='tree-generator',
    install_requires=['']
)