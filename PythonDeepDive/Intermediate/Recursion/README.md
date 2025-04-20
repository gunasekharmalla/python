
                              Recursion
                     ===============================
Recursion is a technique where a function calls itself until it reaches a base condition.
Basic Structure:
    def recursive_function(parameters):
    if base_condition:
        return result  # Base case (stopping condition)
    else:
        return recursive_function(modified_parameters)  # Recursive call

        Types of Recursion:
    ============================
    
Direct Recursion – A function calls itself directly.
Indirect Recursion – A function calls another function, which in turn calls the original function.
Tail Recursion – The recursive call is the last operation in the function.
Head Recursion – The recursive call happens before processing.

                    Recursion vs Iteration
Recursion	                                        Iteration
Uses function calls	                            Uses loops (for, while)
Can lead to stack overflow (too deep calls)	    More memory efficient
Sometimes cleaner and easier to understand	    Usually faster and uses less memory                                          Good for problems            
                                                requiring repetitive 
Good for problems like DFS, backtracking,       calculations
divide & conquer	

                    Recursion Optimization
                  ===========================

Memoization (Top-Down DP) – Store already computed values.
Tail Recursion – Convert recursion into iteration to save stack space.
Bottom-Up DP (Tabulation) – Convert recursion to iteration with an array.
