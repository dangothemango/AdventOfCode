

max = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def main():
    with open('input.txt') as f:
        lines = f.readlines()

    validGames = []
    for line in lines:
        data = line.split(':')
        games = data[1].split(';')
        gameNumber = data[0].split(' ')[1]
        brea = False
        for game in games:
            rolls = game.split(',')
            for roll in rolls:
                info = roll.strip().split(' ')
                diceRolled = int(info[0])
                color = info[1]
                print (diceRolled, color)
                if max[color] < diceRolled:
                    brea = True
        if not brea:
            validGames.append(int(gameNumber))
    print(validGames)
    print(sum(validGames))

if __name__ == '__main__':
    main()
