import re


def extract_warehouse_number(value: str) -> str:
    """
    Из строки типа '84 3709' возвращает '3709'
    """
    if not value:
        return ""

    value = str(value).strip()

    numbers = re.findall(r"\d+", value)

    if not numbers:
        return ""

    return numbers[-1]