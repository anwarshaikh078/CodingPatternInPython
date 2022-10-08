def LongestSubStringWithKDistinctCharacters(str, k):

    #base
    str = str1
    if k == 0: return 0
    start=0
    end=0
    maxLen = 0
    table = dict()

    for end in range(len(str)):
        newCharacter = str[end]

        if newCharacter in table.keys():
            table[newCharacter] += 1
        else:
            table[newCharacter] = 1

        while(len(table.keys()) > 2):
            character = str[start]
            start += 1
            table[character] -= 1

            if table[character] == 0:
                table.pop(character)

        if (end - start + 1) > maxLen:
            maxLen = end - start + 1
    return maxLen

if __name__ == "__main__":

    str1 = "eceba"
    k = 2
    ans = LongestSubStringWithKDistinctCharacters(str1,k)
    print("Length of LongestSubStringWithKDistinctCharacters:- "+str(ans))