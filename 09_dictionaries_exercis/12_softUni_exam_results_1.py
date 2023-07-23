def results_check(submissions_results, username, points):
    if username not in submissions_results:
        submissions_results[username] = points
    if points > submissions_results[username]:
        submissions_results[username] = points
    return submissions_results


def submissions_check(submissions_count, language, points ):
    if language not in submissions_count:
        submissions_count[language] = 0
    submissions_count[language] += 1
    return submissions_count


def ban(submissions_results, username):
    del submissions_results[username]
    return  submissions_results


submissions_results = {}
submissions_count = {}

input_string = input().split('-')

while True:
    if input_string[0] == 'exam finished':
        break
    if len(input_string) == 3:
        username, language, points = input_string[0], input_string[1], int(input_string[2])
        results_check(submissions_results, username, points)
        submissions_check(submissions_count, language, points)

    elif len(input_string) == 2:
        username = input_string[0]
        ban(submissions_results, username)

    input_string = input().split('-')

print('Results:')
for username, points in submissions_results.items():
    print(f'{username} | {points}')
print('Submissions:')
for language, points in submissions_count.items():
    print(f'{language} - {points}')