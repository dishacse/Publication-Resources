# Guardrails SDK

The Guardrails SDK is a Python-based tool that provides powerful text filtering functionalities using both regular expressions (regex) and OpenAI's GPT-4 API. The SDK allows users to define filtering rules for various types of sensitive content and further customize the filtering with OpenAI's API for advanced text moderation.

## Features

- **Rule-Based (Regex) Filtering**: Filter text based on patterns for personal information, credit card numbers, emails, phone numbers, offensive content, and more.
- **OpenAI GPT-4 Based Filtering**: Use OpenAI's API for advanced text filtering and customization with user-defined prompts.
- **Command-Line Interface (CLI)**: Provides an easy-to-use CLI for filtering and customizing rules.
- **Programmatic API**: Directly integrate the SDK into your Python projects for programmatic filtering.

## Installation Prerequisites
- Python 3.6 or higher
- [OpenAI API Key](https://beta.openai.com/signup/)

### Installing the SDK
To install the Guardrails SDK, clone the repository and run the following command to install it locally:
```
git clone https://github.com/yourusername/guardrails_sdk.git
cd guardrails_sdk
pip install .
```

## Development Setup
If you want to modify or run the SDK locally, follow these steps:
1. Clone the repository: ``` git clone https://github.com/yourusername/guardrails_sdk.git ```
2. Navigate to the project directory: ``` cd guardrails_sdk  ```
3. Install the required dependencies: ``` pip install -r requirements.txt ```
4. Run the program: ``` python -m guardrails_sdk.filter ```

## Programmatic Usage
You can also use the SDK programmatically by importing it into your Python project as follows:

``` import guardrails_sdk.filter as filter

### Your content
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

## Usage CLI Usage
You can use the `filter-text` command directly from the terminal once intalled. This will prompt you for your OpenAI API key, input text, and filtering options:

```
filter-text
```

### Example CLI Interaction
```
Enter your OpenAI API key: 
abcxyz ... ... ...

Enter the text you want to filter: 
My medicare number is 123321456 and email is xys at yahoo.com, lets do the fights.

Filter personal information (0/1): 1
Filter credit card numbers (0/1): 0
Filter emails (0/1): 1
Filter offensive content (0/1): 0
... ... ... 

Enter custom OpenAI filters (comma-separated): remove offensive content

Original Input:
My medicare number is 123321456 and email is xys at yahoo.com, lets do the fights.

Filtered Output (Regex):
My medicare number is [Filtered: personal_information] and email is [Filtered: email], lets do the fights.

Filtered Output (OpenAI):
My medicare number is [Filtered: personal_information] and email is [Filtered: email], [Filtered: offensive content].
```

## How It Works
1. **Regex Filtering**: It uses regular expressions to mask or filter out sensitive information like personal details, credit card numbers, emails, and more based on user preferences, 1 to filter, 0 not filtered.
2. **OpenAI GPT-4 Filtering**: It now asked user to further enhances text filtering using customized OpenAI's prompt e.g., if you give filter misinformation, offensive content, this prompts goes asked OpenAI to do that in runtime.

# License
This project is licensed under the CSIRO License - see the LICENSE file for details.

    
   
