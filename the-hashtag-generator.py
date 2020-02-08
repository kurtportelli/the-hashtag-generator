def generate_hashtag(s):
    words = s.split()
    
    if len(words) == 0:
        return False
        
    cap_words = []
    for word in words:
        cap_words.append(word[0].upper() + word[1:].lower())
        
    result = '#' + ''.join(cap_words)
    
    if len(result) > 140:
        return False
    else:
        return result
