# Maps Pathfinding using Various Algorithms

This repository contains a Jupyter Notebook demonstrating the use of various pathfinding algorithms on a road network graph generated from OpenStreetMap data. The notebook explores the implementation and effectiveness of different pathfinding techniques.

## Algorithms Explained

In this notebook, we explore the following pathfinding algorithms:

### Dijkstra's Algorithm
A classic algorithm for finding the shortest paths from a source node to all other nodes in a graph, which may represent, for example, road networks.

![](https://github.com/felipearosr/Shortest_Path/blob/main/assets/path_dij_end.gif)

### A* Algorithm
An extension of Dijkstra's Algorithm, providing faster pathfinding solutions by using heuristics to guide its search.

![](https://github.com/felipearosr/Shortest_Path/blob/main/assets/path_a_end.gif)

### Breadth-First Search (BFS)
A simple algorithm for traversing or searching tree or graph data structures, exploring the neighbor nodes at the current depth prior to moving on to the nodes at the next depth level.

![](https://github.com/felipearosr/Shortest_Path/blob/main/assets/path_bfs_end.gif)

## How to Use

Follow these steps to set up and run the pathfinding notebook:

1. **Clone the Repository**: Clone this repository to your local machine using the following command:
   ```bash
   git clone https://github.com/felipearosr/Shortest_Path.git
   ```

2. **Install Requirements**: Navigate to the cloned repository directory in your terminal or command prompt and install the necessary Python libraries using:
   ```bash
   pip install -r requirements.txt
   ```

## Inspiration

This project was inspired by the work found in [santifiorino/maps-pathfinding](https://github.com/santifiorino/maps-pathfinding/tree/main). We expanded on the original concepts and adapted the techniques for our specific use case and dataset.

## Notebook Summary

- **Setup and Graph Preparation**: Import necessary libraries, load graph data from OSMnx, and prepare the graph by setting default speeds and cleaning up attributes.
- **Edge and Node Styling Functions**: Define functions for styling the nodes and edges based on their state during the pathfinding process.
- **Graph Plotting Function**: Implement a function to visualize the graph with the applied styles.
- **Pathfinding Algorithms**: Detailed exploration of Dijkstra's Algorithm, A* Algorithm, and Breadth-First Search, including their implementation and execution.
- **Path Reconstruction**: Reconstruct and visualize paths from the start node to the destination after finding paths using the algorithms.

## Requirements

- Python 3.x
- Jupyter Notebook
- OSMnx
- NetworkX
- Matplotlib
- heapq, random (standard library modules)