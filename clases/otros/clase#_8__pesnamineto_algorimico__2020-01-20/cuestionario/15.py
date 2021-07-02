def intercambiar_may_min(texto):
    new_text = ""
    for c in texto:
        if c == c.upper() :
            new_text +=c.lower()
        else:
            new_text += c.upper()
    return new_text
print(intercambiar_may_min("Daniel"))