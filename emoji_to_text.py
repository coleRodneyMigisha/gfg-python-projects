emojis = {
    '🥤' : 'cup with straw',
    '🥤,' : 'cup with straw,',
    '🥤.' : 'cup with straw.',
    '🍟' : 'french fries',
    '🍟,' : 'french fries,',
    '🍟.' : 'french fries.',
    '🍔' : 'hamburger',
    '🍔,' : 'hamburger,',
    '🍔.' : 'hamburger.',
    '😁' : 'beaming face with smiling eyes',
    '😁,' : 'beaming face with smiling eyes,',
    '😁.' : 'beaming face with smiling eyes.',
    '😑' : 'expressionless face',
    '😑,' : 'expressionless face,',
    '😑.' : 'expressionless face.',
    '😏' : 'smirking face',
    '😏,' : 'smirking face,',
    '😏.' : 'smirking face.'
}


def rmv_emojis(text):
    text_array = text.split(" ")
    new = []
    for word in text_array:
        if word not in emojis:
            new.append(word)
    return " ".join(new)

def desc_emojis(text):
    text_array = text.split(" ")
    new = []
    for word in text_array:
        if word in emojis:
            new.append(f":{emojis[word]}:")
        else:
            new.append(word)
    return " ".join(new)

def dtct_emojis(text):
    text_array = text.split(" ")
    new = []
    for word in text_array:
        if word in emojis:
            new.append(f"{word}:{emojis[word]}")
    return f"""
{text}
    {new}
"""
    
text = "Nyabamba was feeling 😑, til Atwooki suggested getting 🍔 🍟 🥤, looking at her like 😏. When they were done, she looked like 😁"

print(rmv_emojis(text))
print("")
print(desc_emojis(text))
print("")
print(dtct_emojis(text))