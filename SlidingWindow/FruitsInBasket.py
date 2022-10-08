
def totalFruit(fruits):
    if len(fruits) == 0: return 0

    start = 0
    end = 0
    maxLen = 0
    basket = dict()

    for end in range(len(fruits)):
        fruit = fruits[end]
        if fruit in basket.keys():
            basket[fruit] += 1
        else:
            basket[fruit] = 1

        while len(basket.keys()) > 2:
            fruit = fruits[start]
            start += 1
            basket[fruit] -= 1

            if basket[fruit] == 0:
                basket.pop(fruit)

        if (end - start + 1) > maxLen:
            maxLen = end - start + 1

    return maxLen
if __name__ == "__main__":
    print(totalFruit(fruits=[1,2,1]))
