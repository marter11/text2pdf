
def get_last_key_in_dict(dic):
    l = len(dic)
    count = 1

    for key, value in dic.items():

        if count == l:
            return key

        count += 1

def split_text_to_scope(scope, text, separated_shift_difference=0):
    container = []
    counter = separated_shift_difference
    l = len(scope)
    start = scope[0]-separated_shift_difference
    stop = scope[1]-separated_shift_difference

    if text[:start] != "":
        container.append(text[:start])

    container.append(text[start:stop])
    affected_item_index = len(container)-1
    container.append(text[stop:])

    for i in range(2):
        counter += len(container[i])

    return container, counter, affected_item_index
