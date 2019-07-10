def minScore(students):
    minScore = 100
    for x in students:
        minScore = x[1] if x[1] < minScore else minScore
    return minScore

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    scoreMin = minScore(students)

    students = [x for x in students if x[1] != scoreMin]

    scoreMin = minScore(students)

    students = [x[0] for x in students if x[1] == scoreMin]

    students.sort()

    for x in students:
        print(x)
