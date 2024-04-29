team_1 = "Мастера кода"
team_2 = "Волшебники данных"
team_1_num = int(input('введите количество игроков в 1й команде ')) #5
team_2_num = int(input('введите количество игроков во 2й команде ')) #6
score_1 = int(input('введите количество решенных задач 1й командой ')) #40
score_2 = int(input('введите количество решенных задач 2й командой ')) #42
team_1_time = float(input('введите время 1й команды ')) #18015.2
team_2_time = float(input('введите время 2й команды ')) #18015.2
# challenge_result = оператор if
tasks_total = score_1 + score_2
time_avg = round((team_1_time/score_1 + team_2_time/score_2)/2, 1)

if score_1 > score_2 and team_1_time == team_2_time or team_1_time > team_2_time:
    challenge_result = f'победа команды {team_1}'
elif score_1 < score_2 and team_1_time == team_2_time or team_1_time < team_2_time:
    challenge_result = f'победа команды {team_2}'
else: challenge_result = f'Ничья'


# Использование метода %:
print("В команде %s участников: %d ! " % (team_1, team_1_num))
print("Итого сегодня в командах участников: %d и %d !" % (team_1_num, team_2_num))


# Использование метода format():
print("Команда {0} решила задач: {1:d} !".format(team_2, score_2))
print("{0} решили задачи за {1:.1f} с !".format(team_2, team_2_time))


# Использование f-строк:
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}!')
print(f'Сегодня было решенно {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')