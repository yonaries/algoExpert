arr = [['html', 'c#'], ['c#', 'python'], ['python', 'html']]
res = [0, 0, 1]


def pick_winner(competitions, results):
    currentBestTeam = ""
    scores = {currentBestTeam: 0}

    for idx, comp in enumerate(competitions):
        homeTeam, awayTeam = comp
        winningTeam = homeTeam if results[idx] == 1 else awayTeam
        updateScores(winningTeam, 3, scores)

        if scores[winningTeam] > scores[currentBestTeam]:
            currentBestTeam = winningTeam

    return currentBestTeam


def updateScores(team, point, scores):
    if team not in scores:
        scores[team] = 0
    scores[team] += point
