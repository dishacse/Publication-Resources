# filter.py
from .text_filter import filter_text_from_string

def main():
    # Prompt for OpenAI API Key
    api_key = input("Enter your OpenAI API key: ").strip()

    # Prompt for the text to be filtered
    input_text = input("Enter the text you want to filter: ")

    # Prompt for the filters configuration
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

    # Prompt for custom filters
    custom_filters = input("Enter custom OpenAI filters (comma-separated): ").split(',')

    # Call the function to filter text from a string input
    result = filter_text_from_string(input_text, filters_config, custom_filters, api_key)

    # Print the results
    print("Original Input:")
    print(result['original_input'])

    print("\nFiltered Output (Regex):")
    print(result['regex_filtered_output'])

    print("\nFiltered Output (OpenAI):")
    print(result['openai_filtered_output'])

if __name__ == "__main__":
    main()
