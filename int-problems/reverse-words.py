

def rev_words(str):

    if ' ' not in str:
        return str

    # pointer start and end pointing to end to start reading string from end
    start = len(str)-1
    end = start

    # loop while i reaches begining
    curr = len(str)-1
    rev = ''
    while curr >= 0:
        # if curr char is space point end to curr
        if str[curr] == ' ':
            # when start becomes less than end append to rev string
            if(start < end):
                if (len(rev) == 0):
                    rev = str[start: end+1]
                else:
                    rev = rev+' '+str[start: end]
            end = curr
        # if curr char is not space point start to curr
        else:
            start = curr
        curr = curr-1
    rev = rev+' '+str[start: end]
    return rev


str = 'a b c d'
print(rev_words(str))
