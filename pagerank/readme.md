## Description

This project is the first project in Week 2. The program uses two ways, the random surfer model and iterated algorithm to calculate page ranks.

## How It Works

1.	The program loads the corpus.
2.	For the random surfer model, it first computes a transition model, a dictionary of possibilities to link to different pages given a certain page.
3.	It then generates enough sample to evaluate the probability to get on each page.
4.	The iterative algorithm relies heavily on the law of total probability. The probabilities are initialized as the reciprocal of the total number of pages, and then updated according to the law of total probability until they all converge.

## Running the Program

1.	Clone the repository:
```bash
git clone https://github.com/blackhole-hope123/CS50-projects.git
cd path/CS50-projects/pagerank
```

2.	Run the program:

```
python pagerank.py corpus0
```
or 
```
python pagerank.py corpus1
```
or
```
python pagerank.py corpus2
```
to load different data.

Output:


## File Structure

-	corpus0: A simple corpus to test the program.
-	corpus1: A complex corpus to test the program.
-	corpus2: A corpus with some page having no outgoing links, as a special case.
-	pagerank.py: Main program that calculates the page rank.
-	README.md: Project documentation.

## Concepts Used 
-	law of total probability, random surfer model
-	Data Structures: Sets, dictionaries, lists.

## Acknowledgement 
This project is part of CS50’s AI Course by Harvard University.
