import re


def snake_case_keys(data):
    if isinstance(data, dict):
        for key, value in list(data.items()):
            if isinstance(value, dict):
                snake_case_keys(value)
            elif isinstance(value, list):
                for item in value:
                    snake_case_keys(item)
            data.pop(key)
            data[replace_key(key)] = value

    elif isinstance(data, list):
        for item in data:
            snake_case_keys(item)
    return data


def replace_key(text: str) -> str:
    if text == text.upper():
        return snake_case_from_acronym(text)
    else:
        return snake_case_from_kebab(snake_case_from_camel_or_pascal(snake_case_from_word_and_number(text)))


def snake_case_from_camel_or_pascal(text: str) -> str:
    for char in text:
        if char.isupper():
            text = text.replace(char, "_" + char.lower())
    return text.lstrip("_")


def snake_case_from_kebab(text: str) -> str:
    return text.replace("-", "_")


def snake_case_from_acronym(text: str) -> str:
    return "_".join(text.lower())


def snake_case_from_word_and_number(text: str) -> str:
    return re.sub(r"([\D])([\d*])", r"\1_\2", text)
