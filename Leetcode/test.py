


s = "ab##"
t = "c#d#"

def remover(word):
    word = list(word)
    n= len(word)

    for i in range(n):
        try:
            if word[i] == '#':

                word.remove(word[i-1])
        except:
            continue


    ans = ''

    for i in word:
        if i != '#':
            ans += i

    return ans


print(remover(s))



