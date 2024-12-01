
def main():
    with open('input.txt') as f:
        lines = f.readlines()

    sum = 0
    for card in lines:
        card = card.strip().split('|')
        winningNumbers = card[0].split(':')[1].strip().split(' ')
        myNumbers = card[1].strip().split(' ')
        numWins=0
        for number in myNumbers:
            if len(number)>0 and number in winningNumbers:
                numWins+=1
        if numWins > 0:
            sum += 2**(numWins-1)
    print(sum)


if __name__ == '__main__':
    main()
