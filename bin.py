char = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def conv(n):
    a = ""
    while n > 0:
        a = a+str(n%2)
        n = n // 2
    r = 5 - len(a)
    for i in range(r):
        a = a + "0"
    return a[::-1]


def bin(arr, phrase):
    phrase = phrase.lower()
    binary = ""
    for let in phrase:
        for i in arr:
            if let == i:
                x = arr.index(i)
                if binary == "":
                    binary = conv(x)
                else:
                    binary = binary+" "+conv(x)
            else:
                continue
    print(binary)

exem = input("Mettez votre phrase et je la transforme en ecriture binaire: ")
bin(char,exem)
