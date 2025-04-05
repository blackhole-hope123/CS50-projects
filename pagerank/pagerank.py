import os
import random

import sys
from collections import Counter

DAMPING = 0.85
SAMPLES = 10000

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    res={}
    total=len(corpus)
    for i in corpus:
        res[i]=1/total
    links=corpus[page]
    if len(links)==0:
        return res
    else:
        for i in res:
            res[i]*=(1-damping_factor)
        for i in links:
            res[i]+=damping_factor*1/len(links)
        return res
        


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    
    """
    there is one more mistake: randomness is not introduced!!!
    """
    samples=[]
    pages=list(corpus.items())
    first_sample=pages[random.randint(0,len(pages)-1)][0]
    samples.append(first_sample)
    while len(samples)<n:
        possiblilities_of_the_next=transition_model(corpus,samples[-1],damping_factor)
        items_view=list(possiblilities_of_the_next.items())
        for i in range (0,len(items_view)):
            items_view[i]=list(items_view[i])
            if i>=1:
                items_view[i][1]+=items_view[i-1][1]
        index=random.random()
        for i in range(len(items_view)):
            if items_view[i][1]>index:
                next_sample=items_view[i][0]
                break
        samples.append(next_sample)
    frequency=Counter(samples)
    for i in corpus:
        if i not in frequency:
            frequency[i]=0
    possiblilities={i: frequency[i]/n for i in corpus}
    return possiblilities

def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    links_dict={i:[] for i in corpus}
    for i in corpus:
        for j in corpus:
            if i in corpus[j]:
                links_dict[i].append(j)
    isolated=[]
    for i in corpus:
        if len(corpus[i])==0:
            isolated.append(i)
    N=len(corpus)
    initial={i:(1/N) for i in corpus}
    updated={i:(1/N) for i in corpus}
    updatable=True
    while updatable:
        updatable=False
        for i in updated:
            updates=[]
            for k in links_dict[i]:
                '''if len(corpus[k])==0:
                    print(k)
                    updates.append(initial[k]/len(corpus))
                else:'''
                updates.append(initial[k]/len(corpus[k]))
            updated[i]=(1-damping_factor)/N+damping_factor*sum(updates)+damping_factor*sum([initial[k] for k in isolated])/N
        for i in initial:
            if abs(initial[i]-updated[i])>0.001:
                updatable=True
                initial=updated.copy()
    return updated

if __name__ == "__main__":
    main()
