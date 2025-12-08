while True:
    command = input('> ')

    match command.split():
        case ['reverse', s]:
            print(s[-1::-1])
        case ['reverse', *s]:
            print('cannot reverse multiple words')
        case ['echo', *s]:
            print(*s)
        case ['square', s] if s.isdigit():
            print(int(s)**2)
        case ['quit'|'bye']:
            print('bye')
            break
        case _:
            print('try again')

