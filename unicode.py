def print_all_isupper_false():
    import unicodedata
    import re

    re_digit = re.compile(r'\d')

    #print the unicode codepoint
    for char in range(0x1ffff):
        char = chr(char)
        cased_char = str(char).upper()
        if not char.upper().isupper() and char.isalpha():
            print('U+%04x' % ord(char),
                char.center(6),
                #Show re_dig if character matches the r'\d' regex.
                're_dig' if re_digit.match(char) else '-',
                #Show isdig if char.isdigit() is True.
                'isdig' if char.isdigit() else '-',
                #Show isnum if char.isnumeric() is True.
                'isnum' if char.isnumeric() else '-', 
                'isaplah' if char.isalpha() else '-', 
                unicodedata.category(char),
                unicodedata.name(char),
                sep='\t')

def print_all_lt():
    import unicodedata
    import re

    re_digit = re.compile(r'\d')

    #print the unicode codepoint
    for char in range(0x1ffff):
        char = chr(char)
        cased_char = str(char).upper()
        if unicodedata.category(cased_char) in ['Lt']:
            print('U+%04x' % ord(char),
                char.center(6),
                #Show re_dig if character matches the r'\d' regex.
                're_dig' if re_digit.match(char) else '-',
                #Show isdig if char.isdigit() is True.
                'isdig' if char.isdigit() else '-',
                #Show isnum if char.isnumeric() is True.
                'isnum' if char.isnumeric() else '-', 
                unicodedata.category(char),
                unicodedata.name(char),
                sep='\t')

def print_all_letter_filter_by_categories(categories):
    import unicodedata
    import re

    re_digit = re.compile(r'\d')

    #print the unicode codepoint
    for char in range(0x1ffff):
        char = chr(char)
        if unicodedata.category(char) in categories:
            print('U+%04x' % ord(char),
                char.center(6),
                #Show re_dig if character matches the r'\d' regex.
                're_dig' if re_digit.match(char) else '-',
                #Show isdig if char.isdigit() is True.
                'isdig' if char.isdigit() else '-',
                #Show isnum if char.isnumeric() is True.
                'isnum' if char.isnumeric() else '-', 
                unicodedata.category(char),
                unicodedata.name(char),
                sep='\t')

def print_all_letters():
    import unicodedata
    import re

    re_digit = re.compile(r'\d')
    sample = '1\xbc\xb2\u0969\u136b\u216b\u2466\u2480\u3285\u01CB\u02BD\u02B0'

    #print the unicode codepoint
    for char in range(0x1ffff):
        char = chr(char)
        if unicodedata.category(char) in ['Lm', 'Lt', 'Lu', 'Ll', 'Lo']:
            print('U+%04x' % ord(char),
                char.center(6),
                #Show re_dig if character matches the r'\d' regex.
                're_dig' if re_digit.match(char) else '-',
                #Show isdig if char.isdigit() is True.
                'isdig' if char.isdigit() else '-',
                #Show isnum if char.isnumeric() is True.
                'isnum' if char.isnumeric() else '-', 
                unicodedata.category(char),
                unicodedata.name(char),
                sep='\t')

def print_all_decimal():
    import unicodedata
    import re

    re_digit = re.compile(r'\d')
    sample = '1\xbc\xb2\u0969\u136b\u216b\u2466\u2480\u3285\u01CB\u02BD\u02B0'

    #print the unicode codepoint
    for char in range(0x1ffff):
        char = chr(char)
        if unicodedata.category(char) in ['Nd']:
            print('U+%04x' % ord(char),
                char.center(6),
                #Show re_dig if character matches the r'\d' regex.
                're_dig' if re_digit.match(char) else '-',
                #Show isdig if char.isdigit() is True.
                'isdig' if char.isdigit() else '-',
                #Show isnum if char.isnumeric() is True.
                'isnum' if char.isnumeric() else '-', 
                unicodedata.category(char),
                unicodedata.name(char),
                sep='\t')

def print_all_digits():
    import unicodedata
    import re
    re_digit = re.compile(r'\d')

    #print the unicode codepoint
    for char in range(0x1ffff):
        char = chr(char)
        if char.isdigit() and 'KHAROSHTHI' in unicodedata.name(char):
            #unicodedata.category(char) in ['Nd', 'No']:
            print('U+%04x' % ord(char),
                char.center(6),
                #Show re_dig if character matches the r'\d' regex.
                're_dig' if re_digit.match(char) else '-',
                #Show isdig if char.isdigit() is True.
                'isdig' if char.isdigit() else '-',
                #Show isnum if char.isnumeric() is True.
                'isnum' if char.isnumeric() else '-', 
                unicodedata.category(char),
                unicodedata.name(char),
                sep='\t')

def print_all_notprintable():
    import unicodedata
    import re
    re_digit = re.compile(r'\d')

    #print the unicode codepoint
    for char in range(0x1ffff):
        char = chr(char)
        if unicodedata.category(char) in ['Cc', 'Cf', 'Cs', 'Co', 'Cn',
                                           'Zl', 'Zp']:
            print('U+%04x' % ord(char),
                char.center(6),
                #Show re_dig if character matches the r'\d' regex.
                're_dig' if re_digit.match(char) else '-',
                #Show isdig if char.isdigit() is True.
                'isdig' if char.isdigit() else '-',
                #Show isnum if char.isnumeric() is True.
                'isnum' if char.isnumeric() else '-', 
                unicodedata.category(char),
                unicodedata.name(char),
                sep='\t')

def format_to_print(char):
    import unicodedata
    import re
    re_digit = re.compile(r'\d')
    
    output ='U+%04x' % ord(char) + '\t' + char.center(6)
    reg_dig = 're_dig' if re_digit.match(char) else '-'
    is_dig = 'isdig' if char.isdigit() else '-'
    isnum = 'isnum' if char.isnumeric() else '-'
    
    output = output + '\t' + reg_dig + '\t' + is_dig + '\t' +  isnum
    output = output + '\t' + unicodedata.category(char) + '\t' + unicodedata.bidirectional(char)
    output = output + '\t' +  unicodedata.name(char, 'UNAMED')

    return output

def print_all_space():
    import unicodedata
    import re
    re_digit = re.compile(r'\d')
    

    #print the unicode codepoint
    for char in range(0x1ffff):
        char = chr(char)
        if unicodedata.category(char) in ['Zs'] or\
           unicodedata.bidirectional(char) in ['WS', 'B', 'S']:
            print(format_to_print(char))

print_all_space()

"""
import unicodedata
sample = '1\xbc\xb2\u0969\u136b\u216b\u2466\u2480\u3285\u01CB\u02BD\u02B0'
for char in sample:
   print('U+%04x' % ord(char),
        char.center(6),
        unicodedata.category(char),
        unicodedata.name(char),
        char.isalpha(),
        sep='\t')
        
"""

"""
import unicodedata

u = chr(233) + chr(0x0bf2) + chr(3972) + chr(6000) + chr(13231)

for i, c in enumerate(u):
    print(i, c.center(3),'%04x' % ord(c), unicodedata.category(c), sep='\t', end=" ")
    print(unicodedata.name(c))
"""

def print_all_ascii():
    import unicodedata
    import re
    re_digit = re.compile(r'\d')

    for char in range(0x10000, 0x1007F):
        char = chr(char)
        print('U+%04x' % ord(char),
            char.center(6),
            #Show re_dig if character matches the r'\d' regex.
            're_dig' if re_digit.match(char) else '-',
            #Show isdig if char.isdigit() is True.
            'isdig' if char.isdigit() else '-',
            #Show isnum if char.isnumeric() is True.
            'isnum' if char.isnumeric() else '-', 
            unicodedata.category(char),
            unicodedata.name(char),
            sep='\t')

#print_all_letters()
#print_all_ascii()
#print_all_decimal()
#print_all_digits()
#print_all_notprintable()
