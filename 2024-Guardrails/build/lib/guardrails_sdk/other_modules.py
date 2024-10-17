# other_modules.py
import openai
import re
import requests

# Predefined default regex patterns
default_patterns = {
    "personal_information": r"(\b\d{3}-\d{2}-\d{4}\b|\b\d{3}\s\d{2}\s\d{4}\b|\b\d{9}\b|"
                            r"\+?\d{1,2}[\s-]?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{4}\b|\b\d{3}[\s-]\d{3}[\s-]\d{4}\b|"
                            r"\b(?:\d[ -]*?){13,16}\b|"
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
    Use OpenAI API to filter content based on dynamic descriptions, such as 'hate speech', 'misinformation', etc.
    Replaces the removed content with a [Filtered: description] tag.
    """
    api_url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    prompt = (f"Analyze the following text and remove any content that matches the description '{description}'. "
              f"For each removed section, replace it with [Filtered: {description}]. Text:\n{input_text}")

    data = {
        "model": "gpt-4",
        "messages": [
            {"role": "system", "content": "You are a content filter."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 500,
        "temperature": 0
    }

    try:
        response = requests.post(api_url, headers=headers, json=data)
        response.raise_for_status()  # Raise an exception for non-200 responses

        response_json = response.json()
        return response_json['choices'][0]['message']['content'].strip()

    except requests.exceptions.RequestException as e:
        print(f"Error calling OpenAI API: {e}")
        return input_text  # Return unmodified text on failure

    except Exception as e:
        print(f"Unexpected error: {e}")
        return input_text  # Return unmodified text in case of general error


def apply_filters(input_text, patterns_to_filter, descriptions_to_filter, api_key):
    """
    Apply both regex-based and OpenAI-based filters sequentially.
    :param input_text: The text to filter.
    :param patterns_to_filter: Dict of regex patterns to apply.
    :param descriptions_to_filter: List of descriptions for OpenAI filtering.
    :param api_key: OpenAI API key.
    :return: Dict containing original, regex-filtered, and OpenAI-filtered text.
    """
    # Step 1: Apply regex-based filters
    filtered_data = filter_content(input_text, patterns_to_filter)
    regex_filtered_text = filtered_data['filtered_output']

    # Step 2: Apply OpenAI-based filters on the regex-filtered text
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
    :param input_text: The text to filter.
    :param patterns_to_filter: Dict of regex patterns to apply.
    :return: Dict containing the original and filtered text, and reasons for filtering.
    """
    filtered_text = input_text
    reasons_dict = {label: [] for label in patterns_to_filter}

    for reason, pattern in patterns_to_filter.items():
        matches = re.findall(pattern, input_text, flags=re.IGNORECASE)
        for match in matches:
            filtered_text = re.sub(re.escape(match), f"[Filtered: {reason}]", filtered_text, flags=re.IGNORECASE)
            reasons_dict[reason].append(match)

    return {
        "original_input": input_text,
        "filtered_output": filtered_text,
        "reasons_dict": reasons_dict
    }


def filter_text_from_string(input_text, filters_config, custom_filters=None, api_key=None):
    """
    Filter text from a string input using both regex and OpenAI filters.
    :param input_text: The input text to filter.
    :param filters_config: Dict of filter categories (e.g., {"credit_card": 1, "offensive_content": 1}).
    :param custom_filters: List of custom filter descriptions (e.g., ["hate speech"]).
    :param api_key: OpenAI API key.
    :return: Dict with original input, regex-filtered output, and OpenAI-filtered output.
    """
    filters_config = {category: bool(value) for category, value in filters_config.items()}

    # Prepare the regex filters based on the config
    patterns_to_filter = {category: default_patterns[category] for category, apply_filter in filters_config.items() if apply_filter}

    # Step 1: Apply regex-based filtering
    filtered_data = filter_content(input_text, patterns_to_filter)
    regex_filtered_output = filtered_data['filtered_output']

    # Step 2: Apply OpenAI-based filtering on the regex-filtered text
    openai_filtered_text = regex_filtered_output
    for description in custom_filters or []:
        openai_filtered_text = call_openai_for_filtering(openai_filtered_text, description, api_key)

    return {
        "original_input": input_text,
        "regex_filtered_output": regex_filtered_output,
        "openai_filtered_output": openai_filtered_text,
        "reasons": filtered_data['reasons_dict']  # Include reasons for regex-based filtering
    }
