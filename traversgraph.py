from collections import deque


def bfs_traversal(graph, start):
  """Explores the social network level by level (Breadth-First)."""
  queue = deque([start])
  seen = {start}
  order = []

  while queue:
    person = queue.popleft()
    order.append(person)

    for friend in graph.get(person, []):
      if friend not in seen:
        seen.add(friend)
        queue.append(friend)

  return order


def dfs_traversal(graph, start):
  """Explores a single chain of friendships deeply (Depth-First)."""
  stack = [start]
  seen = set()
  order = []

  while stack:
    person = stack.pop()

    if person not in seen:
      seen.add(person)
      order.append(person)

      # Reverse to visit friends in standard order from left to right
      for friend in reversed(graph.get(person, [])):
        if friend not in seen:
          stack.append(friend)

  return order


# --- 1. Dynamic Social Network Input from User ---
network = {}
print("=== Build Your Social Network ===")
print("Enter friendships in the format: Person1, Person2")
print("Type 'done' when you are finished entering connections.\n")

while True:
  user_input = input("Enter friendship (or 'done'): ").strip()
  if user_input.lower() == "done":
    break

  parts = [p.strip() for p in user_input.split(",")]
  if len(parts) == 2:
    p1, p2 = parts
    # Add bidirectional friendship (undirected graph)
    if p2 not in network.setdefault(p1, []):
      network[p1].append(p2)
    if p1 not in network.setdefault(p2, []):
      network[p2].append(p1)
  else:
    print("Invalid format. Please use: Person1, Person2")

# --- 2. Traversal Start Input from User ---
if not network:
  print("\nNo network created. Exiting program.")
else:
  print("\n--- Available People in Network ---")
  for person in sorted(network.keys()):
    print(f" - {person}")

  print("-" * 35)
  start_person = input("Enter the starting person for traversal: ").strip()

  if start_person not in network:
    print(f"\nError: '{start_person}' does not exist in the social network.")
  else:
    print("\n--- Traversal Results ---")
    bfs_result = bfs_traversal(network, start_person)
    dfs_result = dfs_traversal(network, start_person)

    print("BFS (Level-by-Level):", " -> ".join(bfs_result))
    print("DFS (Deep Chain):", " -> ".join(dfs_result))
