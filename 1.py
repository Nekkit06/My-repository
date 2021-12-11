N = int(input())
pupils = {}
MARKS_COUNT = 3
marks = [0] * MARKS_COUNT

for _ in range(N):
    pupil = input().split()
    pupils[pupil[0]] = [int(i) for i in pupil[1:]]
    for i in range(MARKS_COUNT):
        marks[i] += pupils[pupil[0]][i]

for i in range(MARKS_COUNT):
    print('%.2f' % (marks[i] / N), end = ' ')
