# O(# of sol. * time of each sol.) time
# Tree traversal: O(n) time
# Permutation: O(n! * n) time
# Combination: O(2^n * n) time
def dfs(list_of_parameters):
    if recursion_stop:
        record_of_ans
        return
    for all_sol_possibility:
        modify_all_parameters

        dfs(list_of_parameters)
        reverse_all_modified_parameters
    return something # Or no return, depends on divide&conquer    
