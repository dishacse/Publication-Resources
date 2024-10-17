# Guardrails SDK

The Guardrails SDK is a Python-based tool that provides powerful text filtering functionalities using both regular expressions (regex) and OpenAI's GPT-4 API. The SDK allows users to define filtering rules for various types of sensitive content and further customize the filtering with OpenAI's API for advanced text moderation.

## Features

- **Rule-Based (Regex) Filtering**: Filter text based on patterns for personal information, credit card numbers, emails, phone numbers, offensive content, and more.
- **OpenAI GPT-4 Based Filtering**: Use OpenAI's API for advanced text filtering and customization with user-defined prompts.
- **Command-Line Interface (CLI)**: Provides an easy-to-use CLI for filtering and customizing rules.
- **Programmatic API**: Directly integrate the SDK into your Python projects for programmatic filtering.

## Installation

### Prerequisites

- Python 3.6 or higher
- [OpenAI API Key](https://beta.openai.com/signup/)

### Installing the SDK

To install the Guardrails SDK, clone the repository and run the following command to install it locally:

```bash
git clone https://github.com/yourusername/guardrails_sdk.git
cd guardrails_sdk
pip install .
```

## Usage

### CLI Usage

You can use the `filter-text` command directly from the terminal. This will prompt you for your OpenAI API key, input text, and filtering options:

```bash
filter-text
```

### Example CLI Interaction
```
Enter your OpenAI API key: 
sk-xxxxx... ... ...

Enter the text you want to filter: 
My medicare number is 123321456 and email is xys at yahoo.com.

Filter personal information (0/1): 1
Filter credit card numbers (0/1): 0
Filter emails (0/1): 1
Filter offensive content (0/1): 0

Enter custom OpenAI filters (comma-separated): remove offensive content

Filtered Output:
Original Input:
My medicare number is 123321456 and email is xys at yahoo.com.

Filtered Output (Regex):
My medicare number is [Filtered: personal_information] and email is [Filtered: email].
```

## Programmatic Usage
You can also use the SDK programmatically by importing it into your Python project:

```
import guardrails_sdk.filter as filter

# Your content
my_content = "my text content with personal information like medicare no 123321456 and email xys at yahoo.com"

# Apply the filter
filtered_content = filter.filter_content(
    input_text=my_content, 
    filter_personal_information=True, 
    filter_emails=True
)

# Print the filtered content
print(filtered_content)
```
______________________________________________________________________________

## How It Works

1. **Regex Filtering**: Uses regular expressions to mask or filter out sensitive information like personal details, credit card numbers, emails, and more based on user preferences.
2. **OpenAI GPT-4 Filtering**: Further enhances text filtering using OpenAI's GPT-4, allowing for more complex and customizable filters (e.g., filtering misinformation, offensive content).

### Customization Options

- **Personal Information Filtering**: Mask sensitive personal information like social security numbers, credit card numbers, emails, etc.
- **OpenAI Custom Filters**: Define custom filtering prompts for OpenAI GPT-4 to handle more advanced text moderation (e.g., removing hate speech, misinformation).

---

## Development Setup

If you want to modify or run the SDK locally, follow these steps:

1. Clone the repository: ``` git clone https://github.com/yourusername/guardrails_sdk.git ```
2. Navigate to the project directory: ``` cd guardrails_sdk  ```
3. Install the required dependencies: ``` pip install -r requirements.txt ```
4. Run the program: ``` python -m guardrails_sdk.filter ```

# License
This project is licensed under the CSIRO License - see the LICENSE file for details.

    
   
