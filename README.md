# Pathfinding Algorithms comparasion

This repository contains a Jupyter Notebook demonstrating the use of various pathfinding algorithms on a road network graph generated from OpenStreetMap data. The notebook explores the differences between Dijkstra's Algorithm, A* Algorithm, and Breadth-First Search (BFS) in terms of efficiency and path optimality.

## Notebook Summary

- **Setup and Graph Preparation**: Import necessary libraries, load graph data from OSMnx, and prepare the graph by setting default speeds and cleaning up attributes.
- **Edge and Node Styling Functions**: Define functions for styling the nodes and edges based on their state during the pathfinding process.
- **Graph Plotting Function**: Implement a function to visualize the graph with the applied styles.
- **Pathfinding Algorithms**: Explore the implementation and execution of Dijkstra's Algorithm, A* Algorithm, and Breadth-First Search.
- **Path Reconstruction**: After finding paths using the algorithms, reconstruct and visualize the paths from the start node to the destination.

## Results Summary

The following results were obtained from executing the pathfinding algorithms:

### Dijkstra's Algorithm
- **Iterations**: 5417
- **Distance**: 6.956 km
- **Average Speed**: 40 km/h
- **Total Time**: 10.43 minutes

### A* Algorithm
- **Iterations**: 1536
- **Distance**: 6.975 km
- **Average Speed**: 40 km/h
- **Total Time**: 10.46 minutes

### Breadth-First Search (BFS)
- **Iterations**: 6780
- **Distance**: 8.376 km
- **Average Speed**: 40 km/h
- **Total Time**: 12.56 minutes

## Discussion

The notebook provides insights into how different algorithms perform in terms of iterations (computational effort) and the optimality of the path found (in terms of distance and total travel time). While Dijkstra's and A* algorithms provide similar results and are more efficient for weighted graphs, BFS, although not optimal for weighted paths, gives a unique perspective on unweighted shortest paths.

## How to Use

1. Clone this repository to your local machine.
2. Ensure you have Jupyter Notebook and the required libraries installed.
3. Open the notebook in Jupyter and run the cells to see each algorithm in action.

## Requirements

- Python 3.x
- Jupyter Notebook
- OSMnx
- NetworkX
- Matplotlib
- heapq, random (standard library modules)