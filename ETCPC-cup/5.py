n, m = map(int, input().split())
courses = {}
for i in range(m):
    pre, course = map(str, input().split())
    if pre in courses:
        courses[pre].append(course)
    else:
        courses[pre] = [course]

def dfs(node, visited, rec_stack):
    if node in rec_stack:
        return False
    if node in visited:
        return True

    visited.add(node)
    rec_stack.add(node)

    for neighbor in courses.get(node, []):
        if not dfs(neighbor, visited, rec_stack):
            return False

    rec_stack.remove(node)
    stack.append(node)
    return True

visited = set()
stack = []

for course in list(courses.keys()) + [item for sublist in courses.values() for item in sublist]:
    if course not in visited:
        rec_stack = set()
        if not dfs(course, visited, rec_stack):
            print("IMPOSSIBLE")
            break
else:
    print(" ".join(stack[::-1]))

