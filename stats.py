def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def convert_sort(num_chars):
    final = []
    for x,y in num_chars.items():
        charnum = {}
        if x.isalpha():
            charnum["char"] = x
            charnum["num"] = y
            final.append(charnum)
    final.sort(reverse=True, key=sort_on)
    return final  

def sort_on(items):
    return items["num"]