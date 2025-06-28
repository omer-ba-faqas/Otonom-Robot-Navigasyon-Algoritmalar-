# Autonomous Robot Path Planning with A\*, RRT\*, Genetic Algorithm, and Ant Colony

This project presents a comparative study of four widely-used path planning algorithms — **A\***, **RRT\***, **Genetic Algorithm**, and **Ant Colony Optimization** — tested on different grid environments with varying obstacle densities. The goal is to analyze their performance in terms of path length, computation time, success rate, and path quality for autonomous robot navigation.

## 🧭 Algorithms Implemented

* **A\*** (Search-based deterministic path planner)
* **RRT\*** (Sampling-based planner)
* **Genetic Algorithm** (Evolutionary intelligence-based planner)
* **Ant Colony Optimization** (Swarm intelligence-based planner)

## 🗺️ Grid Environments

The algorithms are tested on 5 different 25x50 grids:

1. **Grid 1**: Medium obstacle density
2. **Grid 2**: Sparse obstacles
3. **Grid 3**: Dense/maze-like obstacles
4. **Grid 4**: Minimal obstacles
5. **Grid 5**: Narrow vertical barriers

## ⚙️ System Requirements

* Python 3.8+
* NumPy
* Matplotlib

Tested on:

```
CPU: Intel 12th Gen Intel(R) Core(TM) i5-12500H 3.10 GHz  
RAM: 8 GB DDR4  
GPU: NVIDIA GeForce RTX 3050 Ti  
OS: Windows / Linux compatible  
```

## 🚀 How to Run

1️⃣ Clone the repository:

```bash
git clone https://github.com/yourusername/robot-path-planning.git
cd robot-path-planning
```

2️⃣ Install dependencies (if not already installed):

```bash
pip install numpy matplotlib
```

3️⃣ Run the algorithm of your choice:

```bash
python astar.py        # A* path planning
python rrt_star.py     # RRT* path planning
python genetic.py      # Genetic Algorithm path planning
python ant_colony.py   # Ant Colony path planning
```

Each script generates:

* A visualization of the explored path
* Performance metrics printed in the console (e.g., path length, execution time, success rate)

## 📊 Results

Each algorithm was run multiple times per grid, and performance metrics were logged, including:

* **Path length**
* **Computation time (ms)**
* **Success rate**
* **Path smoothness / quality**

## 📂 Project Structure

```
robot-path-planning/
├── astar.py            # A* algorithm implementation
├── rrt_star.py         # RRT* algorithm implementation
├── genetic.py          # Genetic Algorithm implementation
├── ant_colony.py       # Ant Colony Optimization implementation
├── grids.py            # Grid definitions (obstacles, start, goal)
└── README.md           # Project documentation
```

## 📌 Notes

* All algorithms are designed for grid-based 2D path planning.
* The project is educational and can be extended for real-time robotics applications.
* Parameters for each algorithm can be adjusted at the top of each script to experiment with performance.

## 📄 License

This project is released under the MIT License.
