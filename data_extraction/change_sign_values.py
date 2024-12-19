def change_signs(string_value):
    if string_value.startswith("-"):
        string_value = '+' + string_value[1:]
    elif string_value.startswith("+"):
        string_value = '-' + string_value[1:]

    return string_value