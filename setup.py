from setuptools import setup, find_packages

setup(
    name='betternorm',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        'colorama',  # Add colorama to the list of dependencies
    ],
    entry_points={
        'console_scripts': [
            'betternorm=betternorm.cli:main',
        ],
    },
)