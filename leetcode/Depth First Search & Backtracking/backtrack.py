"""
Backtracking is a general algorithm for finding all (or some) solutions to some computational problems 
which incrementally builds candidates to the solution and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot lead to a valid solution.

It is due to this backtracking behaviour, the backtracking algorithms are often much faster than the brute-force search algorithm, 
since it eliminates many unnecessary exploration.
"""

def backtrack(candidate):
    if find_solution(candidate):
        output(candidate)
        return
    
    # iterate all possible candidates.
    for next_candidate in list_of_candidates:
        if is_valid(next_candidate):
            # try this partial candidate solution
            place(next_candidate)
            # given the candidate, explore further.
            backtrack(next_candidate)
            # backtrack
            remove(next_candidate)


"""
Overall, the enumeration of candidates is done in two levels:
* at the first level, the function is implemented as recursion. At each occurrence of recursion, the function is one step further to the final solution.
* as the second level, within the recursion, we have an iteration that allows us to explore all the candidates that are of the same progress to the final solution.
"""