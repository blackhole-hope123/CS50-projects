import csv
import sys
from collections import deque
from util import Node, StackFrontier, QueueFrontier

# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")


endNode = None

# lvlTable to keep track of depth of nodes

lvlTable = {}
lvl = 1


def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """
    if source == target: 
        return []
    global endNode
    global lvl
    global lvlTable
    explored = set([(None, source)])
    currFrontier = deque([(None, source)])
    nextFrontier = deque([])
    
    # the reason to use bfs here is because bfs can guarantee that the shortest path is found
    # keep track of visited nodes to avoid loop in the tree (used implicitly)
    def bfs(visited,curr,nxt):
        global endNode
        global lvl
        global lvlTable
        if len(curr)==0:
            if len(nxt)==0:
                # no children
                return
            else:
                # proceed to the next level of the tree
                lvl+=1
                curr=nxt
                nxt=deque()
                bfs(visited, curr, nxt)
        else:
            #update the lvlTable accordingly
            node=curr.popleft()
            neighbors=neighbors_for_person(node[1])
            if lvl==1:
                if lvl not in lvlTable:
                    lvlTable[lvl]=set()
                    for i in neighbors:
                        if i not in visited and i[1]!=source:
                            lvlTable[lvl].add(i)
                else:
                    for i in neighbors:
                        if i not in visited and i[1]!=source:
                            lvlTable[lvl].add(i)
            else:
                if lvl not in lvlTable:
                    lvlTable[lvl]={}
                    for i in neighbors:
                        if i not in visited:
                            lvlTable[lvl][i]=node
                else:
                    for i in neighbors:
                        if i not in visited:
                            lvlTable[lvl][i]=node
            for i in neighbors:
                if i not in visited:
                    nxt.append(i)
                if i[1]==target:
                    endNode=i
                    return
            for i in neighbors:
                visited.add(i)
            bfs(visited,curr,nxt)
    bfs(explored,currFrontier,nextFrontier)
    if not endNode:
        return None
    else:
        res=deque([endNode])
        while lvl>1:
            curr=res[0]
            nxt=lvlTable[lvl][curr]
            res.appendleft(nxt)
            lvl-=1
        return list(res)


def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors

#to ensure that the main() function runs only when the script is executed directly, not when it's imported as a module in another script, preventing the main() function from running unintentionally when the script is imported elsewhere.
if __name__ == "__main__":
    main()
