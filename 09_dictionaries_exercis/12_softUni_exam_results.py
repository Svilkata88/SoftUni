submissions = {}
submissions_count = {}

input_string = input().split('-')

while True:
    if input_string[0] == 'exam finished':
        break
    if len(input_string) == 3:
        username, language, points = input_string
        if username not in submissions:
            submissions[username] = {language: points}
            if language not in submissions_count:
                submissions_count[language] = 0
            submissions_count[language] += 1
        elif username in submissions:
            if language not in submissions[username].keys():
                submissions[username][language] = points
                if language not in submissions_count:
                    submissions_count[language] = 0
                submissions_count[language] += 1
            elif language in submissions[username].keys():
                submissions_count[language] += 1
                if points > submissions[username][language]:
                    submissions[username][language] = points

    elif len(input_string) == 2:
        username, command = input_string
        del submissions[username]

    input_string = input().split('-')

print('Results:')
for name, value in submissions.items():
    print(f'{name} | {max(value.values())}')
print('Submissions:')
for language, points in submissions_count.items():
    print(f'{language} - {points}')
