
def get_last_key_in_dict(dic):
    l = len(dic)
    count = 1

    for key, value in dic.items():

        if count == l:
            return key

        count = count+1

def split_text_to_scope():
    pass
