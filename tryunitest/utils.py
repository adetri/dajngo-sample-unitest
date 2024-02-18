def fail_print(text):
    return print(f"\x1b[1;31m{text}\x1b[0m")


def succes_print(text):
    # Green color for success
    return print(f"\x1b[1;32m{text}\x1b[0m")
