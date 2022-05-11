from sys import stdin

N = int(stdin.readline())

queue = []
cnt = 0

for _ in range(N):
    command = stdin.readline().split()

    if command[0] == 'push':
        val = int(command[1])
        queue.append(val)
    elif command[0] == 'pop':
        if len(queue)-cnt != 0:
            print(queue[cnt])
            cnt += 1
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(queue)-cnt)
    elif command[0] == 'empty':
        if len(queue)-cnt != 0:
            print(0)
        else: 
            print(1)
    elif command[0] == 'front':
        print(queue[cnt] if len(queue)-cnt != 0 else -1)
    elif command[0] == 'back':
        print(queue[-1] if len(queue)-cnt != 0 else -1)

