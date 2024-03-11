import sys
sys.stdin = open('바이러스.txt')


from collections import deque

def bfs(e):
    q = deque()
    v = [0] * (N+1)

    # q에 초기데이터 삽입, 방문표시
    q.append(1)
    v[1] = 1

    while q:
        c = q.popleft()

        for n in adj[c]:  # 연결된 노드
            if v[n] == 0:  # 미방문 노드
                q.append(n)
                v[n] = 1

    return sum(v) - 1  # 정답처리


N = int(input())  # 컴퓨터의 수
E = int(input())  # 노드의 수
adj = [[] for _ in range(N+1)]

for _ in range(E):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)
# print(adj)


ans = bfs(e)
print(ans)