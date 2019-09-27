def letter_freq(txt):
    dict_ = {}
    txt = txt.lower()
    for n in txt:
        keys = dict_.keys()
        if n in keys:
            dict_[n] += 1
        else:
            dict_[n] = 1
    return dict_


def entropy(message):
    import math
    freq = letter_freq(message)
    teller = len(message)
    list_ = []
    for i in freq.keys():
        p_entropy = -(freq[i]/teller*(math.log2(freq[i]/teller)))
        list_.append(p_entropy)
    entropy_value = sum(list_)
    return entropy_value


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))
