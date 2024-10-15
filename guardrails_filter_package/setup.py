# setup.py
from setuptools import setup, find_packages

setup(
    name='guardrails_filter_package',
    version='1.0',
    description='A Python package for text filtering using regex and OpenAI.',
    author='Md Shamsujjoha',
    author_email='firstname.lastname@data61.csiro.au',
    packages=find_packages(),
    install_requires=[
        'openai',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'filter-text=my_filter_package.filter:main',
        ],
    },
)
