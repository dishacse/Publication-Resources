# filter.py
from guardrails_sdk.other_modules import filter_text_from_string


def main():
    """
    CLI interface for filtering text content using customizable guardrails.
    """
    # Prompt for OpenAI API Key
    api_key = input("Enter your OpenAI API key: ").strip()

    # Prompt for the text to be filtered
    input_text = input("Enter the text you want to filter: ")

    # Prompt for the filters configuration (1 = True, 0 = False)
    filters_config = {
        "personal_information": int(input("Filter personal information (0/1): ")),
        "credit_card": int(input("Filter credit card numbers (0/1): ")),
        "phone_number": int(input("Filter phone numbers (0/1): ")),
        "email": int(input("Filter emails (0/1): ")),
        "offensive_content": int(input("Filter offensive content (0/1): ")),
        "misinformation": int(input("Filter misinformation (0/1): ")),
        "irrelevance": int(input("Filter irrelevant content (0/1): ")),
        "cybersecurity_risk": int(input("Filter cybersecurity risks (0/1): ")),
        "cultural_sensitivity": int(input("Filter cultural sensitivity (0/1): ")),
        "potential_harm": int(input("Filter potential harm (0/1): "))
    }

    # Prompt for custom filters (via OpenAI)
    custom_filters = input("Enter custom OpenAI filters (comma-separated): ").split(',')

    # Call the filtering function to apply both rule-based and OpenAI-based filters
    result = filter_text_from_string(input_text, filters_config, custom_filters, api_key)

    # Display the results
    print("\nOriginal Input:")
    print(result['original_input'])

    print("\nFiltered Output (Regex):")
    print(result['regex_filtered_output'])

    print("\nFiltered Output (OpenAI):")
    print(result['openai_filtered_output'])


def filter_content(input_text: str, **kwargs):
    """
    Function to filter content programmatically based on various rules and configurations.

    Args:
        input_text (str): The text content to be filtered.
        **kwargs: Keyword arguments for customizable filtering options.
            e.g., filter_personal_information=True, filter_emails=True

    Returns:
        str: Filtered content based on the provided guardrails.
    """
    # Example placeholder filtering logic (should be replaced with actual filtering logic)
    filtered_text = input_text

    if kwargs.get("filter_personal_information", False):
        filtered_text = filtered_text.replace("123321456", "[Filtered: personal_information]")

    if kwargs.get("filter_emails", False):
        filtered_text = filtered_text.replace("xys at yahoo.com", "[Filtered: email]")

    # Apply other filters based on kwargs...
    # Extend this section based on what filters you implement in other_modules.py

    return filtered_text

def filter(input_text, **kwargs):
    # Your filtering logic here
    # For example:
    filtered_content = input_text  # Apply filtering here
    return filtered_content

if __name__ == "__main__":
    main()
