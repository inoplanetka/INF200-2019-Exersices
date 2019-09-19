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


if __name__ == '__main__':
    text = input('Please enter text to analyse: ')

    frequencies = letter_freq(text)
    for letter, count in sorted(frequencies.items()):
        print('{:3}{:10}'.format(letter, count))
