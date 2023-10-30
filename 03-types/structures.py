def charFrequency(sen):
    chars = {}
    for ch in sen:
        chars[ch] = chars.get(ch, 0) + 1
    return sorted([(k, v) for k, v in chars.items()], key=lambda i: i[1], reverse=True)
