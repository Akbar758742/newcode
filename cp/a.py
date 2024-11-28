def max_beauty(test_cases):
    results = []
    for t in range(test_cases):
        n = int(input())
        a = list(map(int, input().split()))
        
        # Compute the global max and min of the array
        global_max = max(a)
        global_min = min(a)
        
        # Initialize the max beauty
        max_beauty = 0
        
        # Check beauty for all adjacent pairs
        for i in range(n - 1):
            max_outside = max(global_max, a[i], a[i + 1])
            min_outside = min(global_min, a[i], a[i + 1])
            max_inside = max(a[i], a[i + 1])
            min_inside = min(a[i], a[i + 1])
            
            # Compute beauty for this pair
            beauty = (max_outside - min_outside) + (max_inside - min_inside)
            max_beauty = max(max_beauty, beauty)
        
        results.append(max_beauty)
    
    # Output results for all test cases
    print("\n".join(map(str, results)))

# Input and Output handling
t = int(input())
max_beauty(t)
