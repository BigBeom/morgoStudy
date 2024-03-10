import sys
sys.stdin = open('절댓값힙.txt')


import heapq

min_heap = []
heap_items = []

N = int(input())
for i in range(N):
    heap_items.append(int(input()))
    # print(heap_items)

for item in heap_items:
    if item == 0:
        if not min_heap:
            # max_heap이 비었으면 0 출력
            print(0)
        else:
            # heappop: 가장 큰 수 출력한 후 pop
            min_item = heapq.heappop(min_heap)[1]
            print(min_item)
    # 0이 아니면 max_heap에 item 추가
    else:
        heapq.heappush(min_heap, (abs(item), item))

