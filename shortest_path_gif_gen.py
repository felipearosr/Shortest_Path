import heapq
import random
import osmnx as ox
import matplotlib.pyplot as plt

place_name = "San Francisco, California, USA"
G = ox.graph_from_place(place_name, network_type='drive')

# Cleaning 'maxspeed' attribute and setting edge weights
for edge in G.edges:
    # Cleaning the "maxspeed" attribute, some values are lists, some are strings, some are None
    maxspeed = 40  # Default speed
    if "maxspeed" in G.edges[edge]:
        maxspeed_value = G.edges[edge]["maxspeed"]
        if isinstance(maxspeed_value, list):
            speeds = [int(speed) for speed in maxspeed_value if speed.isdigit()]
            maxspeed = min(speeds) if speeds else maxspeed  # Use default if no valid speeds found
        elif isinstance(maxspeed_value, str):
            maxspeed = int(maxspeed_value) if maxspeed_value.isdigit() else maxspeed  # Use default if not a digit
    G.edges[edge]["maxspeed"] = maxspeed
    # Adding the "weight" attribute (time = distance / speed)
    G.edges[edge]["weight"] = G.edges[edge]["length"] / maxspeed

def style_unvisited_edge(edge):
    G.edges[edge]["color"] = "#2432B0"
    G.edges[edge]["alpha"] = 0.3
    G.edges[edge]["linewidth"] = 0.5

def style_visited_edge(edge):
    G.edges[edge]["color"] = "#2432B0"
    G.edges[edge]["alpha"] = 1
    G.edges[edge]["linewidth"] = 1

def style_active_edge(edge):
    G.edges[edge]["color"] = '#3F50E7'
    G.edges[edge]["alpha"] = 1
    G.edges[edge]["linewidth"] = 1

def style_path_edge(edge):
    G.edges[edge]["color"] = "white"
    G.edges[edge]["alpha"] = 1
    G.edges[edge]["linewidth"] = 1

def plot_graph(iteration=None):  # Add iteration parameter
    fig, ax = ox.plot_graph(
        G,
        node_size=[G.nodes[node]["size"] for node in G.nodes],
        edge_color=[G.edges[edge]["color"] for edge in G.edges],
        edge_alpha=[G.edges[edge]["alpha"] for edge in G.edges],
        edge_linewidth=[G.edges[edge]["linewidth"] for edge in G.edges],
        node_color="white",
        bgcolor="#0F1126",
        show=False,  # Don't show the plot immediately
        close=False  # Don't close the plot, so we can save it
    )
    if iteration is not None:
        plt.savefig(f'./output/graph_iteration_{6000+iteration}.png', dpi=300)  # Save the figure
    plt.close(fig)  # Close the plot to free up memory

def dijkstra(orig, dest, plot=False):
    for node in G.nodes:
        G.nodes[node]["visited"] = False
        G.nodes[node]["distance"] = float("inf")
        G.nodes[node]["previous"] = None
        G.nodes[node]["size"] = 0
    for edge in G.edges:
        style_unvisited_edge(edge)
    G.nodes[orig]["distance"] = 0
    G.nodes[orig]["size"] = 50
    G.nodes[dest]["size"] = 50
    pq = [(0, orig)]
    step = 0
    while pq:
        _, node = heapq.heappop(pq)
        if node == dest:
            if plot:
                plot_graph(step)  # Save final step before returning
            return
        if G.nodes[node]["visited"]:
            continue
        G.nodes[node]["visited"] = True
        for edge in G.out_edges(node):
            style_visited_edge((edge[0], edge[1], 0))
            neighbor = edge[1]
            weight = G.edges[(edge[0], edge[1], 0)]["weight"]
            if G.nodes[neighbor]["distance"] > G.nodes[node]["distance"] + weight:
                G.nodes[neighbor]["distance"] = G.nodes[node]["distance"] + weight
                G.nodes[neighbor]["previous"] = node
                heapq.heappush(pq, (G.nodes[neighbor]["distance"], neighbor))
                for edge2 in G.out_edges(neighbor):
                    style_active_edge((edge2[0], edge2[1], 0))
        if plot and step % 10 == 0:
            plot_graph(step)
        step += 1

def distance(node1, node2):
    x1, y1 = G.nodes[node1]["x"], G.nodes[node1]["y"]
    x2, y2 = G.nodes[node2]["x"], G.nodes[node2]["y"]
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def a_star(orig, dest, plot=False):
    for node in G.nodes:
        G.nodes[node]["previous"] = None
        G.nodes[node]["size"] = 0
        G.nodes[node]["g_score"] = float("inf")
        G.nodes[node]["f_score"] = float("inf")
    for edge in G.edges:
        style_unvisited_edge(edge)
    G.nodes[orig]["size"] = 50
    G.nodes[dest]["size"] = 50
    G.nodes[orig]["g_score"] = 0
    G.nodes[orig]["f_score"] = distance(orig, dest)
    pq = [(G.nodes[orig]["f_score"], orig)]
    step = 0
    while pq:
        _, node = heapq.heappop(pq)
        if node == dest:
            if plot:
                plot_graph(step)  # Save final step before returning
            return
        for edge in G.out_edges(node):
            style_visited_edge((edge[0], edge[1], 0))
            neighbor = edge[1]
            tentative_g_score = G.nodes[node]["g_score"] + distance(node, neighbor)
            if tentative_g_score < G.nodes[neighbor]["g_score"]:
                G.nodes[neighbor]["previous"] = node
                G.nodes[neighbor]["g_score"] = tentative_g_score
                G.nodes[neighbor]["f_score"] = tentative_g_score + distance(neighbor, dest)
                heapq.heappush(pq, (G.nodes[neighbor]["f_score"], neighbor))
                for edge2 in G.out_edges(neighbor):
                    style_active_edge((edge2[0], edge2[1], 0))
        if plot and step % 10 == 0:
            plot_graph(step)
        step += 1

def bfs(orig, dest, plot=False):
    for node in G.nodes:
        G.nodes[node]["visited"] = False
        G.nodes[node]["previous"] = None
        G.nodes[node]["size"] = 0
    for edge in G.edges:
        style_unvisited_edge(edge)
    G.nodes[orig]["size"] = 50
    G.nodes[dest]["size"] = 50
    queue = [orig]
    step = 0
    while queue:
        node = queue.pop(0)
        if node == dest:
            if plot:
                print("Iterations:", step)
                plot_graph()
            return
        if not G.nodes[node]["visited"]:
            G.nodes[node]["visited"] = True
            for edge in G.out_edges(node):
                style_visited_edge((edge[0], edge[1], 0))
                neighbor = edge[1]
                if not G.nodes[neighbor]["visited"]:
                    G.nodes[neighbor]["previous"] = node
                    queue.append(neighbor)
                    for edge2 in G.out_edges(neighbor):
                        style_active_edge((edge2[0], edge2[1], 0))
            if plot and step % 10 == 0:
                plot_graph(step)
            step += 1

def reconstruct_path(orig, dest, plot=False, algorithm=None):
    for edge in G.edges:
        style_unvisited_edge(edge)
    dist = 0
    speeds = []
    curr = dest
    step_count = 0  # Initialize a counter for the steps
    while curr != orig:
        prev = G.nodes[curr]["previous"]
        if prev is None:  # Add a check for when there is no previous node (e.g., start node)
            break
        dist += G.edges[(prev, curr, 0)]["length"]
        speeds.append(G.edges[(prev, curr, 0)]["maxspeed"])
        style_path_edge((prev, curr, 0))
        if algorithm:
            G.edges[(prev, curr, 0)][f"{algorithm}_uses"] = G.edges[(prev, curr, 0)].get(f"{algorithm}_uses", 0) + 1
        curr = prev

        step_count += 1  # Increment the step counter
        if plot and step_count % 2 == 0:  # Check if the step count is a multiple of 10
            plot_graph(step_count)  # Call your plotting function here

    # Make sure to plot the final path if we haven't done so in the last few steps
    if plot and step_count % 2 != 0:
        plot_graph(step_count)

    # Add 5 extra frames to the end of the GIF
    for i in range(60):
        plot_graph(step_count + i + 1)

    # Print the path metrics
    if speeds:  # Ensure speeds list is not empty to avoid division by zero
        dist /= 1000  # Convert distance to kilometers
        print(f"Distance: {dist} km")
        print(f"Avg. speed: {sum(speeds) / len(speeds)} km/h")
        print(f"Total time: {dist / (sum(speeds) / len(speeds)) * 60} minutes")

start = random.choice(list(G.nodes))
end = random.choice(list(G.nodes))

print(f"Start: {start}")
print(f"End: {end}")

# Used to generate the GIF
# Start: 65336339
# End: 258757444

start = 65336339
end = 258757444

"""
dijkstra(start, end, plot=False)
reconstruct_path(start, end, plot=True)
"""

"""
a_star(start, end, plot=False)
reconstruct_path(start, end, plot=True)
"""

bfs(start, end, plot=False)
reconstruct_path(start, end, plot=True)
"""
"""
