import heapq


def shortest_path(graph, start, end):
  queue = [(0, start, [start])]
  seen = set()

  while queue:
    cost, node, path = heapq.heappop(queue)

    if node in seen:
      continue
    seen.add(node)

    if node == end:
      return cost, path

    for next_node, weight in graph.get(node, {}).items():
      if next_node not in seen:
        heapq.heappush(queue, (cost + weight, next_node, path + [next_node]))

  return float("inf"), []


network = {}
print("=== Build Your Transport Network ===")
print("Enter connections in the format: City1, City2, Distance")
print("Type 'done' when you are finished entering connections.\n")

while True:
  user_input = input("Enter edge (or 'done'): ").strip()
  if user_input.lower() == "done":
    break

  parts = [p.strip() for p in user_input.split(",")]
  if len(parts) == 3:
    c1, c2, dist_str = parts
    try:
      dist = float(dist_str)
      network.setdefault(c1, {})[c2] = dist
      network.setdefault(c2, {})[c1] = dist
    except ValueError:
      print("Error: Distance must be a number. Try again.")
  else:
    print("Invalid format. Please use: City1, City2, Distance")

if not network:
  print("\nNo network created. Exiting program.")
else:
  print("\n--- Available Cities ---")
  for city in sorted(network.keys()):
    print(f" - {city}")

  print("-" * 30)
  start = input("Enter the starting city: ").strip()
  end = input("Enter the destination city: ").strip()

  if start not in network or end not in network:
    print("\nError: One or both of the entered cities do not exist in the network.")
  else:
    dist, route = shortest_path(network, start, end)

    if dist == float("inf"):
      print(f"\nNo path found between {start} and {end}.")
    else:
      print(f"\nShortest Path: {' -> '.join(route)}")
      print(f"Total Distance: {dist}")
