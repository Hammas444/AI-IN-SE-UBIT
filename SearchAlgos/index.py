import random
import heapq
from collections import deque


def open_list_search(initial_node, target_node, get_child_nodes):
    open_list = [initial_node]
    closed_list = set()

    while open_list:
        x = open_list.pop(0)
        if x == target_node:
            return "Success"
        closed_list.add(x)
        S = get_child_nodes(x)
        for x_prime in S:
            if x_prime not in closed_list:
                open_list.append(x_prime)
    return "Failure"
    
    
    
    

def uniform_cost_search(initial_node, target_node, get_child_nodes, get_cost):
    open_list = [(0, initial_node, [])]
    closed_list = set()

    while open_list:
        cost, x, path = heapq.heappop(open_list)
        if x == target_node:
            return "Success", path + [x]
        if x not in closed_list:
            closed_list.add(x)
            S = get_child_nodes(x)
            for x_prime in S:
                if x_prime not in closed_list:
                    new_cost = cost + get_cost(x, x_prime)
                    heapq.heappush(open_list, (new_cost, x_prime, path + [x]))
    return "Failure", []
    
    
    
    

def random_search(initial_node, target_node, get_child_nodes, max_attempts=10):
    for _ in range(max_attempts):
        x = initial_node
        visited = set()
        path = [x]  # Track the path

        while x != target_node:
            visited.add(x)
            S = get_child_nodes(x)
            if not S:  
                break  # No more child nodes to explore

            # Randomly choose a node that hasn't been visited
            unvisited_nodes = [node for node in S if node not in visited]
            
            if not unvisited_nodes:
                break  # No unvisited nodes left, restart search
            
            x = random.choice(unvisited_nodes)
            path.append(x)  # Add the new node to the path

        if x == target_node:
            return "Success", path  # If the target is reached, return success

    return "Failure", []  # Return failure after max attempts

    
    
def closed_list_search(initial_node, target_node, get_child_nodes):
    queue = deque([(initial_node, [initial_node])])  # (current_node, path)
    closed_list = set()

    while queue:
        x, path = queue.popleft()
        if x == target_node:
            return "Success", path
        closed_list.add(x)
        S = get_child_nodes(x)
        for x_prime in S:
            if x_prime not in closed_list:
                queue.append((x_prime, path + [x_prime]))
    return "Failure", []
    
    
    
    
    
    
    
    
    
    
def create_graph():
    graph = {}
    while True:
        node = input("Enter a node (or type 'done' to finish): ")
        if node.lower() == 'done':
            break
        connections = input(f"Enter connections for node {node} (comma-separated): ").split(',')
        connections = [c.strip() for c in connections if c.strip()]
        graph[node] = connections
    return graph

def create_costs(graph):
    costs = {}
    for node in graph:
        for neighbor in graph[node]:
            cost = input(f"Enter the cost from {node} to {neighbor}: ")
            costs[(node, neighbor)] = int(cost)
    return costs

# Create the graph and costs
graph = create_graph()
costs = create_costs(graph)

# Define helper functions
def get_child_nodes(node):
    return graph.get(node, [])

def get_cost(node1, node2):
    return costs.get((node1, node2), float('inf'))

# Get initial and target nodes from user
initial_node = input("Enter the initial node: ")
target_node = input("Enter the target node: ")


    
    
    # Menu-driven interface
while True:
    print("\n--- Choose Search Algorithm ---")
    print("1. Closed List Search (BFS)")
    print("2. Open List Search")
    print("3. Uniform Cost Search")
    print("4. Random Search")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        result, path = closed_list_search(initial_node, target_node, get_child_nodes)
        print("Closed List Search Result:", result)
        print("Path:", path)

    elif choice == '2':
        result = open_list_search(initial_node, target_node, get_child_nodes)
        print("Open List Search Result:", result)

    elif choice == '3':
        result, path = uniform_cost_search(initial_node, target_node, get_child_nodes, get_cost)
        print("Uniform Cost Search Result:", result)
        print("Path:", path)

    elif choice == '4':
        result, path = random_search(initial_node, target_node, get_child_nodes)
        print("Random Search Result:", result)
        print("Path:", path)

    elif choice == '5':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice! Please select a valid option (1-5).")
