
def main():
    with open('input.txt') as f:
        lines = f.readlines()

    sum = 0
    d = {}
    for card in lines:
        card = card.strip().split('|')
        winningNumbers = card[0].split(':')[1].strip().split(' ')
        cardNumber = int(card[0].split(':')[0].split(' ')[-1])
        if cardNumber not in d:
            d[cardNumber] = 0
        d[cardNumber] = d[cardNumber] + 1
        myNumbers = card[1].strip().split(' ')
        numWins=0
        for number in myNumbers:
            if len(number)>0 and number in winningNumbers:
                numWins+=1
        for i in range(1,numWins+1):
            copiedCard = cardNumber + i
            if copiedCard not in d:
                d[copiedCard] = 0
            d[copiedCard] = d[copiedCard] + 1 * d[cardNumber]
                
    for c in d:
        sum += d[c]
    print(sum)

if __name__ == '__main__':
    main()
