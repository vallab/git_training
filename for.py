
def funny_phrases(words):
    # your code here
    ra=([])
    for i in words:
        if len(i)>5 and i[len(i)-1]=='y':
            ra.append (i)

    return ra


    

def print_string_array(strings):
    print repr(strings).replace("'", '"')

print_string_array(funny_phrases(
    ["absolutely", "fly", "sorry", "taxonomy", "eighty", "excellent"]))
print_string_array(funny_phrases(
    ["terrible", "normally", "naughty", "party"]))
print_string_array(funny_phrases(
    ["tour", "guy", "pizza"]))
