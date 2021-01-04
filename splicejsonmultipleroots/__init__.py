
def position_of_equal_open_close(txt: str):
    parenthesis = 0
    i = 0
    # Strip is required because the first char needs to be an {
    for entry in txt.strip():
        if i > 0 and parenthesis == 0:
            return i
        if entry == '{':
            parenthesis += 1
        elif entry == '}':
            parenthesis -= 1

        i += 1


def splice_json(input_text: str):
    copy_of_text = input_text.strip()

    arr = []
    pos = 0

    while pos is not None:
        pos = position_of_equal_open_close(copy_of_text)
        text = copy_of_text[0:pos]
        arr.append(text)
        copy_of_text = copy_of_text[pos:]

    return arr
