
def main():
    with open('input.txt') as f:
        lines = f.readlines()

    productSum = 0
    for line in lines:
        data = line.split(':')
        games = data[1].split(';')
        minColors = dict({
            'blue': 0,
            'red': 0,
            'green': 0
        })
        for game in games:
            rolls = game.split(',')
            for roll in rolls:
                info = roll.strip().split(' ')
                diceRolled = int(info[0])
                color = info[1]
                minColors[color] = max(minColors[color], diceRolled)
        productSum += minColors['blue']*minColors['red']*minColors['green']

    print(productSum)
    
if __name__ == '__main__':
    main()
