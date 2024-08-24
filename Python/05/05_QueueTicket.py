currentTicket = 0
queue = []
currentQueue = 0
queueTime = []
currentQueueTime = 0
waitTime = []
n = int(input())
for i in range(n):
    ops = input().split()
    match ops[0]:
        case 'reset':
            currentTicket = int(int(ops[1]))
        case 'new':
            queue.append(currentTicket)
            queueTime.append(int(ops[1]))
            print(f'ticket {currentTicket}')
            currentTicket += 1
        case 'next':
            currentQueue = queue[0]
            currentQueueTime = queueTime[0]
            queue.remove(currentQueue)
            queueTime.remove(queueTime[0])
            print(f'call {currentQueue}')
        case 'order':
            dt = int(ops[1]) - currentQueueTime
            waitTime.append(dt)
            print(f'qtime {currentQueue} {dt}')
        case 'avg_qtime':
            avgWaitTime = round(sum(waitTime)/len(waitTime), 4)
            print(f'avg_qtime {avgWaitTime}')