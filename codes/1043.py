N, M = map(int, input().split())
people = list(map(int, input().split()))[1:]

visited = [0 for _ in range(N)]
for k in people:
    visited[k - 1] = 1

parties = []
for _ in range(M):
    guests = list(map(int, input().split()))[1:]
    parties.append(guests)

party_visit = [0 for _ in range(M)]

while people:
    known_guest = people.pop()

    candidate = set()

    for party_idx in range(len(parties)):
        party = set(parties[party_idx])
        if known_guest in party:
            candidate = candidate.union(party)
            party_visit[party_idx] = 1

    for guest in candidate:
        if not visited[guest - 1]:
            people.append(guest)
            visited[guest - 1] = 1

print(party_visit.count(0))