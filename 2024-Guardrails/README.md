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
