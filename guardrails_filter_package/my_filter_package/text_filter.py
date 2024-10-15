# text_filter.py
import openai
import re
import requests

# Predefined default regex patterns
default_patterns = {
    "personal_information": r"(\b\d{3}-\d{2}-\d{4}\b|\b\d{3}\s\d{2}\s\d{4}\b|\b\d{9}\b|"
                            r"\+?\d{1,2}[\s-]?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{4}\b|\b\d{3}[\s-]\d{3}[\s-]\d{4}\b|"
                            r"\

                            3






                                b(?:\d[ -]*?){13,16}\b|"
                            r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+|"
                            r"\b\d{2,4}-\d{2,4}-\d{2,4}-\d{1,4}\b)",  # Credit card, email, phone numbers
    "social_security_number": r"\b\d{3}-\d{2}-\d{4}\b",
    "credit_card": r"\b(?:\d[ -]*?){13,16}\b",
    "phone_number": r"\+?\d{1,2}[\s-]?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{4}\b",
    "email": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
    "offensive_content": r"\b(?:terrorists?|hate|discriminat(?:e|ion)|offensive|racist|slur)\b",
    "misinformation": r"\b(?:fake news|false information|misleading)\b",
    "irrelevance": r"\b(?:irrelevant content|off-topic)\b",
    "cybersecurity_risk": r"\b(?:http|www)\S+\b",  # URLs
    "cultural_sensitivity": r"\b(?:racial slur|cultural insensitivity)\b",
    "potential_harm": r"\b(?:suicide|self-harm|depression|anxiety|violence)\b"
}

def call_openai_for_filtering(input_text, description, api_key):
    """
    Use raw HTTP requests to call OpenAI API for filtering content with GPT-4 based on dynamic descriptions,
    and include the reason for filtering.
    """
    # OpenAI API URL for chat-based models (like GPT-4)
    api_url = "https://api.openai.com/v1/chat/completions"

    # Prepare the headers with your API key
    headers = {
        "Authorization": f"Bearer {api_key}",  # Use the passed API key directly
        "Content-Type": "application/json"
    }

    # Prepare the prompt dynamically
    prompt = (f"Analyze the following text and remove any content that matches the description '{description}'. "
              f"For each removed section, replace it with [Filtered: {description}]. "
              f"Text:\n{input_text}\nReturn the filtered text.")

    # Prepare the request payload
    data = {
        "model": "gpt-4",  # Use GPT-4
        "messages": [
            {"role": "system", "content": "You are a content filter."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 500,
        "temperature": 0
    }

    try:
        # Make the POST request to OpenAI's API
        response = requests.post(api_url, headers=headers, json=data)

        # Check for errors
        if response.status_code != 200:
            print(f"Error calling OpenAI API: {response.status_code} - {response.json()}")
            return input_text  # In case of error, return the unmodified input

        # Parse the response and return the filtered content
        response_json = response.json()
        return response_json['choices'][0]['message']['content'].strip()

    except Exception as e:
        print(f"Exception occurred: {e}")
        return input_text  # Return the unmodified input if an exception occurs


def apply_filters(input_text, patterns_to_filter, descriptions_to_filter, api_key):
    """
    Apply both regex-based and OpenAI-based filters to the input text sequentially.
    """
    # Step 1: Apply regex-based filters
    filtered_data = filter_content(input_text, patterns_to_filter)
    regex_filtered_text = filtered_data['filtered_output']

    # Step 2: Apply OpenAI-based filters on the regex-filtered text for each custom filter description
    openai_filtered_text = regex_filtered_text
    for description in descriptions_to_filter:
        openai_filtered_text = call_openai_for_filtering(openai_filtered_text, description, api_key)

    return {
        "original_input": input_text,
        "regex_filtered_output": regex_filtered_text,
        "openai_filtered_output": openai_filtered_text
    }


def filter_content(input_text, patterns_to_filter):
    """
    Apply regex-based filtering based on selected patterns.
    """
    filtered_text = input_text
    reasons_dict = {label: [] for label in patterns_to_filter}

    # Apply regex-based filtering
    for reason, pattern in patterns_to_filter.items():
        matches = re.findall(pattern, input_text, flags=re.IGNORECASE)
        if matches:
            for match in matches:
                # Replace the detected matches with placeholders
                filtered_text = re.sub(re.escape(match),
                                       f"[Filtered: {reason}]",
                                       filtered_text, flags=re.IGNORECASE)
                reasons_dict[reason].append(match)

    return {
        "original_input": input_text,
        "filtered_output": filtered_text,
        "reasons_dict": reasons_dict
    }


def filter_text_from_string(input_text, filters_config, custom_filters=None, api_key=None):
    """
    Filter text from a string input.
    :param input_text: The input text string to be filtered.
    :param filters_config: Dictionary of filter categories (e.g., {"credit_card": 1, "offensive_content": 1})
    :param custom_filters: List of custom filter descriptions (e.g., ["hate speech"])
    :param api_key: OpenAI API key as a string.
    :return: Dictionary with original input, regex-filtered output, and OpenAI-filtered output.
    """
    # Convert binary input (0/1) to boolean values
    filters_config = {category: bool(value) for category, value in filters_config.items()}

    # Prepare the regex filters based on the config passed
    patterns_to_filter = {category: default_patterns[category] for category, apply_filter in filters_config.items() if apply_filter}

    # Apply regex-based filtering
    filtered_data = filter_content(input_text, patterns_to_filter)
    regex_filtered_output = filtered_data['filtered_output']
    regex_reasons = filtered_data['reasons_dict']

    # Apply OpenAI-based filtering on the regex-filtered text
    openai_filtered_text = regex_filtered_output
    for description in custom_filters or []:
        openai_filtered_text = call_openai_for_filtering(openai_filtered_text, description, api_key)

    return {
        "original_input": input_text,
        "regex_filtered_output": regex_filtered_output,
        "openai_filtered_output": openai_filtered_text,
        "reasons": regex_reasons  # Include reasons for regex-based filtering
    }
