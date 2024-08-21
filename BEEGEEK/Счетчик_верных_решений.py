from math import ceil

n = int(input())
total_attempt = [input() for e in range(n)]
total_unique_correct_attempt_list = [e for e in total_attempt if e.split(':')[-1] == ' Correct']
total_unique_correct_attempt_set = set(total_unique_correct_attempt_list)

if not total_unique_correct_attempt_list:
    print('Вы можете стать первым, кто решит эту задачу')
else:
    x = (100 * len(total_unique_correct_attempt_list)) / n
    print(f'Верно решили {len(total_unique_correct_attempt_set)} учащихся')
    print(f'Из всех попыток {int(x + 0.5)}% верных')
