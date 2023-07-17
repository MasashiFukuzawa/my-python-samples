import strcounter

if __name__ == "__main__":
    text = "Hello, World!"
    alphabet_count, digit_count, other_count = strcounter.count_chars(text)
    print(f"{alphabet_count=}")
    print(f"{digit_count=}")
    print(f"{other_count=}")
