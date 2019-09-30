def char_counts(textfilename):
    freq = [0] * 256
    with open(textfilename) as a_file:
        text = a_file.read()
        for char in text:
            freq[ord(char)] += 1
    return freq


if __name__ == '__main__':

    filename = 'file_stats.py'
    frequencies = char_counts(filename)
    for code in range(256):
        if frequencies[code] > 0:
            character = ''
            if code >= 32:
                character = chr(code)

            print(
                '{:3}{:>4}{:6}'.format(
                    code, character, frequencies[code]
                )
            )
