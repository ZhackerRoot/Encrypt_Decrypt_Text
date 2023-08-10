
#def encrypt_this(text):
#    results = []
#    
#    for word in text.split():
#        # turn word into a list
#        word = list(word)
#        
#        #repalce first letter with ascii code
#        word[0] = str(ord(word[0]))
#        
#        # switch 2 and last latters
#        if len(word) > 2:
#            word[1],word[-1] = word[-1], word[1]
#
#        results.append(''.join(word))
#    
#    return ' '.join(results)
#
#print(encrypt_this(input('Send Massage: ')))
#print(encrypt_this(input('Enter a massage: '))) 
#
#def decrypt_this(string):
#    translated = []
#    for word in string.split():
#        digits = ''
#        for c in word:
#            if c.isdigit():
#                digits += c
#        word = word.replace(digits, chr(int(digits)))    
#        if len(word) > 2:
#            translated.append(''.join([word[0], word[-1], word[2:-1], word[1]]))
#        else:
#            translated.append(word)
#    return ' '.join(translated)
#
#print(decrypt_this(input('Enter decrypt massage: ')))
#print(decrypt_this(input('Enter decrypt massage: ')))

print('encrypt massage!')
#Encrypt Massage > 
def encrypt_text(x):
    enc = []
    for w in x.split():
        w = list(w)
        w[0] = str(ord(w[0]))

        if len(w) > 2:
            w[1], w[-1] = w[-1], w[1]
        enc.append(''.join(w))
    return ' '.join(enc)

print(encrypt_text('hello'))
print(encrypt_text('world'))



print('decrypt massage!')
#Decrypt Massage >
def decrypt_text(x):
    dec = []
    for w in x.split():
        digits = ''
        for i in w:
          if i.isdigit():
             digits += i
        w = w.replace(digits, chr(int(digits)))
        if len(w) > 2:
            dec.append(''.join([w[0], w[-1], w[2:-1],w[1]] ))
        else:
            dec.append(w)
    return' '.join(dec)

print(decrypt_text('104olle'))
print(decrypt_text('119drlo'))