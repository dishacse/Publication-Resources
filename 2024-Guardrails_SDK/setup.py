from setuptools import setup, find_packages

setup(
    name="guardrails_sdk",  # Name of your SDK
    version="0.1.0",  # Initial version
    description="A customizable Guardrails SDK for content filtering using regex and OpenAI",  # Short description
    author="Md Shamsujjoha",  # Your name or organization
    author_email="md.shamsujjoha@data61.csiro.au",  # Your email
    license="MIT",  # License type
    packages=find_packages(),  # Automatically finds all packages within the project
    install_requires=[
        "openai>=0.11",  # OpenAI library
        "requests>=2.26",  # Requests for HTTP calls
        "regex>=2022.9.13"  # Regex module
    ],
    entry_points={
        'console_scripts': [
            'filter-text=guardrails_sdk.filter:main',  # CLI command 'filter-text' mapped to the main function
        ],
    },
    python_requires='>=3.7',  # Minimum Python version requirement
    classifiers=[
        'Development Status :: 4 - Beta',  # Project maturity level
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    include_package_data=True,  # Ensures non-Python files (e.g., README) are included
    zip_safe=False  # Set to False to avoid issues with running zipped eggs
)
