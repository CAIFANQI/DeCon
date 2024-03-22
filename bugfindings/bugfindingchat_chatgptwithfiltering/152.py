
def compare(game,guess):
    """I think we all remember that feeling when the result of some long-awaited
    event is finally known. The feelings and thoughts you have at that moment are
    definitely worth noting down and comparing.
    Your task is to determine if a person correctly guessed the results of a number of matches.
    You are given two arrays of scores and guesses of equal length, where each index shows a match. 
    Return an array of the same length denoting how far off each guess was. If they have guessed correctly,
    the value is 0, and if not, the value is the absolute difference between the guess and the score.
    
    
    example:

    compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) -> [0,0,0,0,3,3]
    compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) -> [4,4,1,0,0,6]
    """
    return [abs(x-y)+abs(y-x) for x,y in zip(game,guess)]
assert compare([1,2,3],[1,2,3]) == [0,0,0], "Test case 1 failed"
assert compare([1,2,3],[4,5,6]) == [3,3,3], "Test case 2 failed"
assert compare([1,2,3],[0,1,2]) == [1,1,1], "Test case 3 failed"
assert compare([1,2,3],[2,3,4]) == [1,1,1], "Test case 4 failed"
assert compare([1,2,3],[4,5,6]) == [3,3,3]
assert compare([1,2,3],[0,0,0]) == [1,2,3]
assert compare([1,2,3],[1,1,1]) == [0,1,2]
assert compare([1,2,3],[3,2,1]) == [2,0,2]
assert compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]
assert compare([1, 2, 3], [0, 0, 0]) == [1, 2, 3]
assert compare([1,2,3],[0,0,0]) == [1,2,3], "Test case 3 failed"
assert compare([1,2,3],[2,1,0]) == [1,1,3], "Test case 4 failed"
assert compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3], "Test case 2 failed"
assert compare([1, 2, 3], [0, 1, 2]) == [1, 1, 1], "Test case 3 failed"
assert compare([1, 2, 3], [2, 1, 3]) == [1, 1, 0], "Test case 4 failed"
assert compare([1, 2, 3], [3, 2, 1]) == [2, 0, 2], "Test case 5 failed"
assert compare([1,2,3],[2,4,6]) == [1,2,3]
assert compare([1,2,3],[1,3,2]) == [0,1,1]
assert compare([1, 2, 3], [0, 1, 2]) == [1, 1, 1]
assert compare([1, 2, 3], [2, 4, 6]) == [1, 2, 3]
assert compare([1, 2, 3], [1, 1, 1]) == [0, 1, 2]
assert compare([1, 2, 3], [2, 2, 2]) == [1, 0, 1]
assert compare([1, 2, 3], [3, 2, 1]) == [2, 0, 2]
assert compare([1, 2, 3], [2, 3, 4]) == [1, 1, 1]
assert compare([1, 2, 3], [3, 4, 5]) == [2, 2, 2]
assert compare([1,2,3],[1,5,3]) == [0,3,0]
assert compare([1,2,3],[2,1,3]) == [1,1,0]
assert compare([1,2,3],[-1,-2,-3]) == [2,4,6]
assert compare([1,2,3],[0,1,2]) == [1,1,1]
assert compare([1,2,3],[2,3,4]) == [1,1,1]
assert compare([1,2,3],[3,4,5]) == [2,2,2]
assert compare([1,2,3],[2,2,3]) == [1,0,0]
assert compare([1,2,3],[1,3,3]) == [0,1,0]
assert compare([1,2,3,4],[1,2,2,4]) == [0,0,1,0]
assert compare([1,2,3,4],[2,3,4,5]) == [1,1,1,1]
assert compare([1,2,3,4],[5,4,3,2]) == [4,2,0,2]
assert compare([1, 2, 3], [1, 3, 2]) == [0, 1, 1]
assert compare([1,2,3],[2,1,0]) == [1,1,3]
assert compare([1,2,3,4,5], [1,2,2,4,5]) == [0,0,1,0,0]
assert compare([1,2,3,4,5], [2,3,4,5,6]) == [1,1,1,1,1]
assert compare([1,2,3,4,5], [0,0,0,0,0]) == [1,2,3,4,5]
assert compare([1,2,3,4,5], [5,4,3,2,1]) == [4,2,0,2,4]
assert compare([1,2,3],[2,2,2]) == [1,0,1]
assert compare([1, 2, 3], [2, 3, 4]) == [1, 1, 1], "Test case 2 failed"
assert compare([1, 2, 3], [3, 2, 1]) == [2, 0, 2], "Test case 4 failed"
assert compare([1,2,3],[1,2,4]) == [0,0,1]
assert compare([1,2,3],[1,3,4]) == [0,1,1]
assert compare([1, 2, 3], [0, 0, 0]) == [1, 2, 3], "Test case 3 failed"
assert compare([1, 2, 3], [2, 2, 2]) == [1, 0, 1], "Test case 4 failed"
assert compare([1, 2, 3], [0, 2, 3]) == [1, 0, 0]
assert compare([1, 2, 3], [2, 2, 3]) == [1, 0, 0]
assert compare([1, 2, 3], [1, 3, 3]) == [0, 1, 0]
assert compare([1, 2, 3], [1, 2, 4]) == [0, 0, 1]
assert compare([1, 2, 3], [1, 3, 5]) == [0, 1, 2]
assert compare([1,2,3],[5,4,3]) == [4,2,0], "Test case 5 failed"
assert compare([1,2,3],[5,6,7]) == [4,4,4]
assert compare([1,2,3],[1,0,3]) == [0,2,0]
assert compare([1,2,3],[0,3,6]) == [1,1,3]
assert compare([1, 2, 3], [1, 1, 1]) == [0, 1, 2], "Test case 4 failed"
assert compare([1, 2, 3], [2, 3, 4]) == [1, 1, 1], "Test case 5 failed"
assert compare([1, 2, 3], [0, 2, 4]) == [1, 0, 1]
assert compare([1, 2, 3], [2, 2, 4]) == [1, 0, 1]
assert compare([1, 2, 3], [0, 3, 2]) == [1, 1, 1]
assert compare([1,2,3], [4,5,6]) == [3,3,3]
assert compare([1,2,3], [0,0,0]) == [1,2,3]
assert compare([1,2,3], [2,3,4]) == [1,1,1]
assert compare([1,2,3], [3,2,1]) == [2,0,2]
assert compare([1, 2, 3], [4, 3, 2]) == [3, 1, 1]
assert compare([1,2,3,4,5],[2,3,4,5,6]) == [1,1,1,1,1]
assert compare([1,2,3,4,5],[0,0,0,0,0]) == [1,2,3,4,5]
assert compare([1,2,3,4,5],[5,4,3,2,1]) == [4,2,0,2,4]
assert compare([1,2,3,4,5],[6,7,8,9,10]) == [5,5,5,5,5]
assert compare([1,2,3,4,5],[0,1,2,3,4]) == [1,1,1,1,1]
assert compare([1, 2, 3], [5, 6, 7]) == [4, 4, 4]
assert compare([1,2,3], [2,2,3]) == [1,0,0]
assert compare([1,2,3], [1,3,3]) == [0,1,0]
assert compare([1,2,3], [1,2,4]) == [0,0,1]
assert compare([1,2,3], [2,2,2]) == [1,0,1]
assert compare([1, 2, 3], [4, 4, 4]) == [3, 2, 1]
