def loading_bar(num):
    loaded = int(num / 10) * '%'
    left = (10 - int(num / 10 )) * '.'

    if len(loaded) < 10:
        result = f'{num}% [{loaded}{left}]\nStill loading...'
        return result
    else:
        result = f'100% Complete!\n[{loaded}{left}]'
        return result


num = int(input())
print(loading_bar(num))