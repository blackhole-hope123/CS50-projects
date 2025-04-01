## Description

This project is the first project in Week 0. The program uses Breadth-First Search (BFS) to determine the smallest degree of separation between two actors in a movie database, as BFS will guarantee us to find the shortest path.

## How It Works

1.	The program loads a dataset of actors and movies.
2.	It constructs a graph where:
  - Nodes represent actors.
  - Edges represent movies connecting actors.
3.	It takes two actor names as input and finds the shortest path (degrees of separation) between them.
4.	The result is displayed as a sequence of actor-movie connections.

## Running the Program

1.	Clone the repository:
```bash
git clone https://github.com/blackhole-hope123/CS50-projects.git
cd path/CS50-projects
```

2.	Run the program:

```
python degrees.py large
```

3.	Enter two actor names when prompted.

Example:

```bash
Name 1: Tom Hanks
Name 2: Natalie Portman
```

Output:

```
1: Tom Hanks and Julia Roberts starred in Charlie Wilson's War
2: Julia Roberts and Natalie Portman starred in Closer
```

## File Structure

-	degrees.py: Main program that finds the shortest path.
-	large/ : Folder containing a large movie database.
-	small/ : Folder containing a small test database.
-	README.md: Project documentation.

## Concepts Used 
-	Breadth-First Search (BFS): The reason to use BFS here is that it will guarantee us to find the shortest path.
-	Data Structures: Sets, dictionaries, and queues.

## Acknowledgement 
This project is part of CS50’s AI Course by Harvard University.

