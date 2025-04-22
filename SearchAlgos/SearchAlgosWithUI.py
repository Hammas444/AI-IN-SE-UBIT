# import streamlit as st
# import networkx as nx
# import matplotlib.pyplot as plt
# import random
# from collections import deque

# st.title("Graph Search Visualizer")

# # 1. Data Input
# st.header("1. Input Graph")
# nodes = st.text_input("Enter nodes (comma separated)", "A,B,C,D,E")
# edges = st.text_area("Enter edges (format: node1,node2,weight per line)", "A,B,1\nB,C,2\nC,D,3\nD,E,4\nA,E,10")

# # Parse input
# node_list = [n.strip() for n in nodes.split(",") if n.strip()]
# edge_list = [tuple(line.strip().split(",")) for line in edges.strip().split("\n") if line.strip()]
# edge_list = [(a, b, int(w)) for a, b, w in edge_list]

# # 2. Build Graph
# G = nx.Graph()
# G.add_nodes_from(node_list)
# G.add_weighted_edges_from(edge_list)

# # 3. Algorithm Selection
# st.header("2. Choose Search Algorithm")
# algo = st.selectbox(
#     "Choose Search Algorithm",
#     ["Random", "Uniform Cost Search", "Closed List", "Open List", "BFS", "DFS"]
# )
# start = st.selectbox("Start Node", node_list)
# goal = st.selectbox("Goal Node", node_list)

# # 4. Visualize Input Graph
# st.subheader("Graph Visualization")

# def draw_graph(G, path=[]):
#     pos = nx.spring_layout(G)
#     edge_colors = ['red' if (u, v) in path or (v, u) in path else 'black' for u, v in G.edges()]
#     nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color=edge_colors, node_size=500, font_size=14)
#     nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
#     st.pyplot(plt.gcf())
#     plt.clf()

# draw_graph(G)

# # 5. Run Algorithm
# st.header("3. Run Search")
# path_result = []

# def run_random_search(G, start, goal):
#     path = [start]
#     current = start
#     visited = set()
#     while current != goal:
#         neighbors = list(G.neighbors(current))
#         neighbors = [n for n in neighbors if n not in visited]
#         if not neighbors:
#             break
#         current = random.choice(neighbors)
#         path.append(current)
#         visited.add(current)
#     return path

# def run_uniform_cost_search(G, start, goal):
#     import heapq
#     queue = [(0, start, [])]
#     visited = set()
#     while queue:
#         cost, node, path = heapq.heappop(queue)
#         if node in visited:
#             continue
#         path = path + [node]
#         if node == goal:
#             return path
#         visited.add(node)
#         for neighbor in G.neighbors(node):
#             if neighbor not in visited:
#                 total_cost = cost + G[node][neighbor]['weight']
#                 heapq.heappush(queue, (total_cost, neighbor, path))
#     return []





# def run_closed_list_search(G, start, goal):
#     def get_child_nodes(node):
#         return list(G.neighbors(node))
    
#     def closed_list_search(initial_node, target_node, get_child_nodes):
#         queue = deque([(initial_node, [initial_node])])  # (current_node, path)
#         closed_list = set()

#         while queue:
#             x, path = queue.popleft()
#             if x == target_node:
#                 return "Success", path
#             closed_list.add(x)
#             S = get_child_nodes(x)
#             for x_prime in S:
#                 if x_prime not in closed_list:
#                     queue.append((x_prime, path + [x_prime]))
#         return "Failure", []
    
#     status, path = closed_list_search(start, goal, get_child_nodes)
#     return path if status == "Success" else []













# def run_open_list_search(G, start, goal):
#     def get_child_nodes(node):
#         return list(G.neighbors(node))

#     def open_list_search(initial_node, target_node, get_child_nodes):
#         open_list = [(initial_node, [initial_node])]  # (node, path)
#         closed_list = set()

#         while open_list:
#             x, path = open_list.pop(0)
#             if x == target_node:
#                 return "Success", path
#             closed_list.add(x)
#             S = get_child_nodes(x)
#             for x_prime in S:
#                 if x_prime not in closed_list and x_prime not in [n for n, _ in open_list]:
#                     open_list.append((x_prime, path + [x_prime]))
#         return "Failure", []

#     status, path = open_list_search(start, goal, get_child_nodes)
#     return path if status == "Success" else []







# def run_dfs(G, start, goal):
#     visited = set()
#     stack = [(start, [start])]  # (node, path)

#     while stack:
#         node, path = stack.pop()
#         if node == goal:
#             return path
#         if node not in visited:
#             visited.add(node)
#             for neighbor in reversed(list(G.neighbors(node))):  # Reverse for consistent ordering
#                 if neighbor not in visited:
#                     stack.append((neighbor, path + [neighbor]))
#     return []






# def run_bfs(G, start, goal):
#     from collections import deque

#     visited = set()
#     queue = deque([(start, [start])])  # (node, path)

#     while queue:
#         node, path = queue.popleft()
#         if node == goal:
#             return path
#         if node not in visited:
#             visited.add(node)
#             for neighbor in G.neighbors(node):
#                 if neighbor not in visited:
#                     queue.append((neighbor, path + [neighbor]))
#     return []



# if st.button("Run"):
#     if algo == "Random":
#         path_result = run_random_search(G, start, goal)
#     elif algo == "Uniform Cost Search":
#         path_result = run_uniform_cost_search(G, start, goal)
#     # Closed List / Open List can be added similarly
#     elif algo == "Closed List":
#         path_result = run_closed_list_search(G, start, goal)

#     elif algo == "Open List":
#         path_result = run_open_list_search(G, start, goal)

#     elif algo == "BFS":
#         path_result = run_bfs(G, start, goal)
#     elif algo == "DFS":
#         path_result = run_dfs(G, start, goal)


#     if path_result:
#         st.success(f"Path Found: {' → '.join(path_result)}")
#         edge_path = [(path_result[i], path_result[i+1]) for i in range(len(path_result)-1)]
#         draw_graph(G, edge_path)
#     else:
#         st.error("No path found!")

import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import random
from collections import deque
import heapq

st.title("Graph Search Visualizer")

# 1. Data Input
st.header("1. Input Graph")
nodes = st.text_input("Enter nodes (comma separated)", "A,B,C,D,E")
edges = st.text_area("Enter edges (format: node1,node2,weight per line)", "A,B,1\nB,C,2\nC,D,3\nD,E,4\nA,E,10")

# Parse input
node_list = [n.strip() for n in nodes.split(",") if n.strip()]
edge_list = [tuple(line.strip().split(",")) for line in edges.strip().split("\n") if line.strip()]
edge_list = [(a, b, int(w)) for a, b, w in edge_list]

# 2. Build Graph
G = nx.Graph()
G.add_nodes_from(node_list)
G.add_weighted_edges_from(edge_list)

# 3. Algorithm Selection
st.header("2. Choose Search Algorithm")
algo = st.selectbox(
    "Choose Search Algorithm",
    ["Random", "Uniform Cost Search", "Closed List", "Open List", "BFS", "DFS", "A*", "Best-First Search", "Greedy First Search"]
)
start = st.selectbox("Start Node", node_list)
goal = st.selectbox("Goal Node", node_list)

# 4. Heuristic Values
if algo in ["A*", "Best-First Search", "Greedy First Search"]:
    st.subheader("3. Set Heuristic Values")
    heuristic_values = {}
    for node in node_list:
        heuristic_values[node] = st.number_input(f"Enter heuristic value h({node})", min_value=0, value=0, key=node)

# 5. Visualize Input Graph
st.subheader("Graph Visualization")

def draw_graph(G, path=[]):
    pos = nx.spring_layout(G)
    edge_colors = ['red' if (u, v) in path or (v, u) in path else 'black' for u, v in G.edges()]
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color=edge_colors, node_size=500, font_size=14)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
    st.pyplot(plt.gcf())
    plt.clf()

draw_graph(G)

# 6. Run Algorithm
st.header("4. Run Search")
path_result = []

# Define search algorithms
def run_random_search(G, start, goal):
    path = [start]
    current = start
    visited = set()
    while current != goal:
        neighbors = list(G.neighbors(current))
        neighbors = [n for n in neighbors if n not in visited]
        if not neighbors:
            break
        current = random.choice(neighbors)
        path.append(current)
        visited.add(current)
    return path

def run_uniform_cost_search(G, start, goal):
    queue = [(0, start, [])]
    visited = set()
    while queue:
        cost, node, path = heapq.heappop(queue)
        if node in visited:
            continue
        path = path + [node]
        if node == goal:
            return path
        visited.add(node)
        for neighbor in G.neighbors(node):
            if neighbor not in visited:
                total_cost = cost + G[node][neighbor]['weight']
                heapq.heappush(queue, (total_cost, neighbor, path))
    return []

def run_closed_list_search(G, start, goal):
    def get_child_nodes(node):
        return list(G.neighbors(node))
    
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
    
    status, path = closed_list_search(start, goal, get_child_nodes)
    return path if status == "Success" else []

def run_open_list_search(G, start, goal):
    def get_child_nodes(node):
        return list(G.neighbors(node))

    def open_list_search(initial_node, target_node, get_child_nodes):
        open_list = [(initial_node, [initial_node])]  # (node, path)
        closed_list = set()

        while open_list:
            x, path = open_list.pop(0)
            if x == target_node:
                return "Success", path
            closed_list.add(x)
            S = get_child_nodes(x)
            for x_prime in S:
                if x_prime not in closed_list and x_prime not in [n for n, _ in open_list]:
                    open_list.append((x_prime, path + [x_prime]))
        return "Failure", []

    status, path = open_list_search(start, goal, get_child_nodes)
    return path if status == "Success" else []

def run_dfs(G, start, goal):
    visited = set()
    stack = [(start, [start])]  # (node, path)

    while stack:
        node, path = stack.pop()
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in reversed(list(G.neighbors(node))):  # Reverse for consistent ordering
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
    return []

def run_bfs(G, start, goal):
    from collections import deque

    visited = set()
    queue = deque([(start, [start])])  # (node, path)

    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in G.neighbors(node):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return []

# A* Search Algorithm with user-provided heuristic values
def run_astar(G, start, goal, heuristic_values):
    open_list = [(0 + heuristic_values[start], 0, start, [])]
    visited = set()
    while open_list:
        _, cost, node, path = heapq.heappop(open_list)
        if node in visited:
            continue
        path = path + [node]
        if node == goal:
            return path
        visited.add(node)
        for neighbor in G.neighbors(node):
            if neighbor not in visited:
                total_cost = cost + G[node][neighbor]['weight']
                heapq.heappush(open_list, (total_cost + heuristic_values[neighbor], total_cost, neighbor, path))
    return []

# Best-First Search Algorithm with user-provided heuristic values
def run_best_first_search(G, start, goal, heuristic_values):
    open_list = [(heuristic_values[start], start, [])]
    visited = set()
    while open_list:
        _, node, path = heapq.heappop(open_list)
        if node in visited:
            continue
        path = path + [node]
        if node == goal:
            return path
        visited.add(node)
        for neighbor in G.neighbors(node):
            if neighbor not in visited:
                heapq.heappush(open_list, (heuristic_values[neighbor], neighbor, path))
    return []

# Greedy First Search Algorithm with user-provided heuristic values
def run_greedy_first_search(G, start, goal, heuristic_values):
    open_list = [(heuristic_values[start], start, [])]
    visited = set()
    while open_list:
        _, node, path = heapq.heappop(open_list)
        if node in visited:
            continue
        path = path + [node]
        if node == goal:
            return path
        visited.add(node)
        for neighbor in G.neighbors(node):
            if neighbor not in visited:
                heapq.heappush(open_list, (heuristic_values[neighbor], neighbor, path))
    return []

if st.button("Run"):
    if algo == "Random":
        path_result = run_random_search(G, start, goal)
    elif algo == "Uniform Cost Search":
        path_result = run_uniform_cost_search(G, start, goal)
    elif algo == "Closed List":
        path_result = run_closed_list_search(G, start, goal)
    elif algo == "Open List":
        path_result = run_open_list_search(G, start, goal)
    elif algo == "BFS":
        path_result = run_bfs(G, start, goal)
    elif algo == "DFS":
        path_result = run_dfs(G, start, goal)
    elif algo == "A*":
        path_result = run_astar(G, start, goal, heuristic_values)
    elif algo == "Best-First Search":
        path_result = run_best_first_search(G, start, goal, heuristic_values)
    elif algo == "Greedy First Search":
        path_result = run_greedy_first_search(G, start, goal, heuristic_values)

    if path_result:
        st.success(f"Path Found: {' → '.join(path_result)}")
        edge_path = [(path_result[i], path_result[i+1]) for i in range(len(path_result)-1)]
        draw_graph(G, edge_path)
