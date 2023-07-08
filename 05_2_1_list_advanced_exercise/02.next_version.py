version = input().split('.')

version = [int(num) for num in version]

for i in range(len(version) -1 , -1, -1):
    if version[i] < 9:
        version[i] += 1
        break
    else:
        version[i] = 0
        if version[i-1] < 9:
            version[i-1] += 1
            break
        else:
            version[i-1] = 0
            version[i-2] += 1
            break
version = f'{version[0]}.{version[1]}.{version[2]}'

print(version)