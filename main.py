
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
        #print('position_of_equal_open_close:{}'.format(pos))
        text = copy_of_text[0:pos]
        arr.append(text)
        copy_of_text = copy_of_text[pos:]
        #print('text:{}'.format(text))
        #print('json:{}'.format(json.loads(text)))
        #print('remaining text:{}'.format(copy_of_text))

    return arr
