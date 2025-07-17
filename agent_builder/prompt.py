import re


class Prompt:
    max_tokens = 8192
    gpt_model = "gpt-4o"

    def __init__(self, system_message: str, user_message_template: str):
        self.system_message = system_message
        self.user_message_template = user_message_template

    def assert_string_injection_mapping(self, template: str, string_injection_mapping: dict):
        required_variables = self._detect_template_variables(template)
        assert all(
            key in string_injection_mapping.keys() for key in required_variables
        ), f"Required variables {required_variables} not found in 'string_injection_mapping'"

    def format_user_prompt(self, string_injection_mapping: dict):
        self.assert_string_injection_mapping(self.user_message_template, string_injection_mapping)
        return self.user_message_template.format(**string_injection_mapping)

    def format_system_prompt(self, string_injection_mapping: dict):
        self.assert_string_injection_mapping(self.system_message, string_injection_mapping)
        return self.system_message.format(**string_injection_mapping)

    def _detect_template_variables(self, template: str) -> list:
        # find all cases where {variable} is in the string. Ignores double braces {{variable}}
        return re.findall(r"(?<!\{)\{(?!\{)(.*?)(?<!\})\}(?!\})", template)
