# Import the package/module directly
from guardrails_sdk.other_modules import filter_text_from_string


# Test function to check personal information filtering
def test_filter_personal_info():
    input_text = "My SSN is 123-45-6789"

    # Config for the personal information filter
    filters_config = {
        "personal_information": 1,
        "credit_card": 0,
        "phone_number": 0,
        "email": 0,
        "offensive_content": 0,
        "misinformation": 0,
        "irrelevance": 0,
        "cybersecurity_risk": 0,
        "cultural_sensitivity": 0,
        "potential_harm": 0
    }

    # Run the filter using filter_text_from_string
    result = filter_text_from_string(input_text, filters_config)

    # Check if the filtered output is correct
    assert "[Filtered: personal_information]" in result["regex_filtered_output"]


# Test function to check email filtering
def test_filter_email():
    input_text = "Contact me at user@example.com"

    # Config for the email filter
    filters_config = {
        "personal_information": 0,
        "credit_card": 0,
        "phone_number": 0,
        "email": 1,
        "offensive_content": 0,
        "misinformation": 0,
        "irrelevance": 0,
        "cybersecurity_risk": 0,
        "cultural_sensitivity": 0,
        "potential_harm": 0
    }

    # Run the filter using filter_text_from_string
    result = filter_text_from_string(input_text, filters_config)

    # Check if the filtered output is correct
    assert "[Filtered: email]" in result["regex_filtered_output"]
