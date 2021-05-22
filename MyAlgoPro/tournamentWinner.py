# O(n) time / O(k) space - where n is the # of competitions, k is the # of teams
def tournamentWinner(competitions, results):
	currentWinningTeam = ""
	scores = {currentWinningTeam: 0}
	
	for idx, competition in enumerate(competitions):
		winningResult = results[idx]
		homeTeam, awayTeam = competition
		
		winningTeam = homeTeam if winningResult == 1 else awayTeam
		
		updateScores(winningTeam, 3, scores)
		
		if scores[winningTeam] > scores[currentWinningTeam]:
			currentWinningTeam = winningTeam
			
	return currentWinningTeam

def updateScores(team, points, scores):
	if team not in scores:
		scores[team] = 0
	
	scores[team] += points

  
######################################################################  
import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
        results = [0, 0, 1]
        expected = "Python"
        actual = program.tournamentWinner(competitions, results)
        self.assertEqual(actual, expected)
