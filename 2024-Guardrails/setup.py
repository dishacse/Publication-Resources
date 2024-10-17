from setuptools import setup, find_packages

# Load the README file as long description for the project
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="guardrails_sdk",  # Replace with your project name
    version="1.0",  # Update version as needed
    author="Md Shamsujjoha",
    author_email="md.shamsujjoha@data61.csiro.au",
    description="A SDK for Guardrails functionality including text filtering.",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Make sure your README.md is in Markdown
    url="https://github.com/your-repo-url",  # Replace with your repository URL
    packages=find_packages(),  # Automatically find all packages
    install_requires=[
        "openai",
        "requests",
        "regex",
        "pytest"  # Dependencies from your requirements.txt
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Use your LICENSE type
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Specify the minimum Python version
    entry_points={
        'console_scripts': [
            'filter-text=guardrails_sdk.filter:main',  # Call 'main' to launch CLI
        ],
    },
)
