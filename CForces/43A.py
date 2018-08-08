n = int(input())
score = {}
for i in range(n):
    scorer = input()
    if scorer in score:
        score[scorer] += 1
    else:
        score[scorer] = 1

print(max(score, key=score.get))
