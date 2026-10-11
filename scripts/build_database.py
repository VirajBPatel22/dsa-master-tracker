#!/usr/bin/env python3
"""
Full Striver A2Z 75-Day Pro DSA Master Curriculum Builder
Compiles all ~321 high-yield, interview-defining problems across 75 days (~4 questions/day).
Covers 100% of non-trivial Striver problems while omitting basic syntax/star patterns.
"""

import json
import csv

def build_75day_dataset():
    # Load base dataset
    with open("dsa_planner_database.json", "r", encoding="utf-8") as f:
        existing = json.load(f)

    # Dictionary mapping name -> item
    by_name = {item["name"]: item for item in existing}

    # The ~60 conceptual additions to reach complete coverage
    extra_conceptual = [
        # Sorting fundamentals
        {
            "name": "Merge Sort Algorithm from Scratch",
            "topic": "Arrays & Sorting", "pattern": "Divide and Conquer", "difficulty": "Medium",
            "practice_url": "https://www.geeksforgeeks.org/problems/merge-sort/1",
            "article_url": "https://takeuforward.org/data-structure/merge-sort-algorithm/",
            "video_url": "https://www.youtube.com/watch?v=ogjf7ORKfd8",
            "notes": "Divide at mid, recursively sort left and right, merge with two pointers. Time: O(N log N), Space: O(N)."
        },
        {
            "name": "Quick Sort Algorithm (Hoare & Lomuto Partition)",
            "topic": "Arrays & Sorting", "pattern": "Partitioning", "difficulty": "Medium",
            "practice_url": "https://www.geeksforgeeks.org/problems/quick-sort/1",
            "article_url": "https://takeuforward.org/data-structure/quick-sort-algorithm/",
            "video_url": "https://www.youtube.com/watch?v=WIrA4YexLRQ",
            "notes": "Pick pivot, partition such that elements <= pivot are left, elements > pivot are right. In-place, O(N log N) avg."
        },

        # Doubly Linked List Suite
        {
            "name": "Reverse a Doubly Linked List",
            "topic": "Linked List", "pattern": "DLL Pointer Swap", "difficulty": "Easy",
            "practice_url": "https://www.geeksforgeeks.org/problems/reverse-a-doubly-linked-list/1",
            "article_url": "https://takeuforward.org/data-structure/reverse-a-doubly-linked-list/",
            "video_url": "https://www.youtube.com/watch?v=u3WUW2qe6ww",
            "notes": "For every node, swap node.next and node.prev. Move curr = curr.prev (since pointers are swapped)."
        },
        {
            "name": "Delete All Occurrences of a Given Key in DLL",
            "topic": "Linked List", "pattern": "DLL Deletion", "difficulty": "Medium",
            "practice_url": "https://www.geeksforgeeks.org/problems/delete-all-occurrences-of-a-given-key-in-a-doubly-linked-list/1",
            "article_url": "https://takeuforward.org/data-structure/delete-all-occurrences-of-a-key-in-dll/",
            "video_url": "https://www.youtube.com/watch?v=Mh0NH_PKA8k",
            "notes": "Handle head node deletion carefully (update head = next_node, next_node.prev = None). In-place O(N)."
        },
        {
            "name": "Find Pairs with Given Sum in Sorted DLL",
            "topic": "Linked List", "pattern": "Two Pointers DLL", "difficulty": "Easy",
            "practice_url": "https://www.geeksforgeeks.org/problems/find-pairs-with-given-sum-in-doubly-linked-list/1",
            "article_url": "https://takeuforward.org/data-structure/find-pairs-with-given-sum-in-dll/",
            "video_url": "https://www.youtube.com/watch?v=YitR4dQuddE",
            "notes": "Left pointer at head, right pointer at tail. If sum < target left = left.next; else right = right.prev. O(N)."
        },
        {
            "name": "Remove Duplicates from Sorted DLL",
            "topic": "Linked List", "pattern": "DLL Deduplication", "difficulty": "Easy",
            "practice_url": "https://www.geeksforgeeks.org/problems/remove-duplicates-from-sorted-doubly-linked-list/1",
            "article_url": "https://takeuforward.org/data-structure/remove-duplicates-from-sorted-dll/",
            "video_url": "https://www.youtube.com/watch?v=YJKVTnOJXSY",
            "notes": "Track next_unique node. Adjust curr.next = next_unique and next_unique.prev = curr. Free skipped nodes."
        },

        # Stack Expression Conversions
        {
            "name": "Prefix to Infix Conversion",
            "topic": "Stack & Queue", "pattern": "Expression Parsing", "difficulty": "Medium",
            "practice_url": "https://www.geeksforgeeks.org/problems/prefix-to-infix-conversion/1",
            "article_url": "https://takeuforward.org/data-structure/prefix-to-infix/",
            "video_url": "https://www.youtube.com/watch?v=4pIc9UBHJtk",
            "notes": "Read prefix from right to left. On operand: push to stack. On operator: pop op1, op2, push '(' + op1 + op + op2 + ')'."
        },
        {
            "name": "Prefix to Postfix Conversion",
            "topic": "Stack & Queue", "pattern": "Expression Parsing", "difficulty": "Medium",
            "practice_url": "https://www.geeksforgeeks.org/problems/prefix-to-postfix-conversion/1",
            "article_url": "https://takeuforward.org/data-structure/prefix-to-postfix/",
            "video_url": "https://www.youtube.com/watch?v=4pIc9UBHJtk",
            "notes": "Read from right to left. On operator: pop op1, op2, push op1 + op2 + op."
        },
        {
            "name": "Postfix to Infix Conversion",
            "topic": "Stack & Queue", "pattern": "Expression Parsing", "difficulty": "Medium",
            "practice_url": "https://www.geeksforgeeks.org/problems/postfix-to-infix-conversion/1",
            "article_url": "https://takeuforward.org/data-structure/postfix-to-infix/",
            "video_url": "https://www.youtube.com/watch?v=4pIc9UBHJtk",
            "notes": "Read from left to right. On operator: pop op2, op1, push '(' + op1 + op + op2 + ')'."
        },
        {
            "name": "Postfix to Prefix Conversion",
            "topic": "Stack & Queue", "pattern": "Expression Parsing", "difficulty": "Medium",
            "practice_url": "https://www.geeksforgeeks.org/problems/postfix-to-prefix-conversion/1",
            "article_url": "https://takeuforward.org/data-structure/postfix-to-prefix/",
            "video_url": "https://www.youtube.com/watch?v=4pIc9UBHJtk",
            "notes": "Read from left to right. On operator: pop op2, op1, push op + op1 + op2."
        },
        {
            "name": "Sum of Subarray Ranges",
            "topic": "Stack & Queue", "pattern": "Monotonic Stack Two-Pass", "difficulty": "Medium",
            "practice_url": "https://leetcode.com/problems/sum-of-subarray-ranges/",
            "article_url": "https://takeuforward.org/data-structure/sum-of-subarray-ranges/",
            "video_url": "https://www.youtube.com/watch?v=gduSsAG4gKg",
            "notes": "Range sum = Sum of Subarray Maxima - Sum of Subarray Minima. Solve in two O(N) monotonic stack passes."
        },
        {
            "name": "Number of NGEs to the Right",
            "topic": "Stack & Queue", "pattern": "Queries Stack", "difficulty": "Medium",
            "practice_url": "https://www.geeksforgeeks.org/problems/number-of-nges-to-the-right/1",
            "article_url": "https://takeuforward.org/data-structure/number-of-nges-to-the-right/",
            "video_url": "https://www.youtube.com/watch?v=Du881K7Jtk8",
            "notes": "Count elements greater than query index to its right. Process offline or via monotonic stack."
        },

        # Backtracking Additions
        {
            "name": "Word Break I",
            "topic": "Recursion & Backtracking", "pattern": "Branch Pruning with Memo", "difficulty": "Medium",
            "practice_url": "https://leetcode.com/problems/word-break/",
            "article_url": "https://takeuforward.org/data-structure/word-break-problem/",
            "video_url": "https://www.youtube.com/watch?v=2NaaM_z_Pyo",
            "notes": "dp[i] is True if s[:i] can be segmented. For j in [0, i]: if dp[j] and s[j:i] in wordSet -> dp[i] = True."
        },
        {
            "name": "Expression Add Operators",
            "topic": "Recursion & Backtracking", "pattern": "Operator Rollback Backtracking", "difficulty": "Hard",
            "practice_url": "https://leetcode.com/problems/expression-add-operators/",
            "article_url": "https://takeuforward.org/data-structure/expression-add-operators/",
            "video_url": "https://www.youtube.com/watch?v=v05R1WIIg08",
            "notes": "Manage multiplication precedence: for '*', value = prev_val - prev_mult + prev_mult * curr_num."
        },
        {
            "name": "Combination Sum III (K numbers sum to N)",
            "topic": "Recursion & Backtracking", "pattern": "Bounded Backtracking", "difficulty": "Medium",
            "practice_url": "https://leetcode.com/problems/combination-sum-iii/",
            "article_url": "https://takeuforward.org/data-structure/combination-sum-iii/",
            "video_url": "https://www.youtube.com/watch?v=OyZNWAMyt9w",
            "notes": "Digits 1-9 used at most once. Pick k numbers that sum to n. Standard loop recursion."
        },

        # Heaps Additions
        {
            "name": "Design Twitter",
            "topic": "Heaps", "pattern": "K-Way Merge Max-Heap", "difficulty": "Medium",
            "practice_url": "https://leetcode.com/problems/design-twitter/",
            "article_url": "https://takeuforward.org/data-structure/design-twitter/",
            "video_url": "https://www.youtube.com/watch?v=pNichitDD2E",
            "notes": "Map user -> followed users. Max-heap stores latest tweet per followed user with timestamp counter. Pop 10."
        },
        {
            "name": "Minimum Cost to Connect Sticks / Ropes",
            "topic": "Heaps", "pattern": "Greedy Min-Heap", "difficulty": "Medium",
            "practice_url": "https://www.geeksforgeeks.org/problems/minimum-cost-of-ropes-1587115620/1",
            "article_url": "https://takeuforward.org/data-structure/minimum-cost-to-connect-ropes/",
            "video_url": "https://www.youtube.com/watch?v=2tXqauW8l4A",
            "notes": "Min-heap. Pop two smallest ropes, sum them, add to total cost, push sum back into heap. Repeat until 1 rope."
        },
        {
            "name": "Kth Largest Element in a Stream",
            "topic": "Heaps", "pattern": "Fixed Min-Heap", "difficulty": "Easy",
            "practice_url": "https://leetcode.com/problems/kth-largest-element-in-a-stream/",
            "article_url": "https://takeuforward.org/data-structure/kth-largest-element-in-a-stream/",
            "video_url": "https://www.youtube.com/watch?v=0tUhdA_a87k",
            "notes": "Maintain min-heap of size k. If new element > heap[0], pop and push. Top is always the kth largest."
        },
        {
            "name": "Maximum Sum Combination",
            "topic": "Heaps", "pattern": "2D Coordinate Heap", "difficulty": "Medium",
            "practice_url": "https://www.interviewbit.com/problems/maximum-sum-combinations/",
            "article_url": "https://takeuforward.org/data-structure/maximum-sum-combination/",
            "video_url": "https://www.youtube.com/watch?v=yAs3tTNzH2M",
            "notes": "Sort both arrays desc. Max-heap of (A[i] + B[j], i, j). Pop max, push (i+1, j) and (i, j+1) with visited set."
        },

        # Trees & BST Additions
        {
            "name": "Construct Binary Tree from Postorder & Inorder",
            "topic": "Binary Trees", "pattern": "Tree Reconstruction", "difficulty": "Medium",
            "practice_url": "https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/",
            "article_url": "https://takeuforward.org/data-structure/construct-binary-tree-from-inorder-and-postorder-traversal/",
            "video_url": "https://www.youtube.com/watch?v=LgLRTaEMRVc",
            "notes": "Postorder last element is root. Inorder hashmap partitions left and right subtrees. Recursively build right then left."
        },
        {
            "name": "Inorder Successor & Predecessor in BST",
            "topic": "Binary Search Trees", "pattern": "BST Pointer Search", "difficulty": "Medium",
            "practice_url": "https://www.geeksforgeeks.org/problems/predecessor-and-successor/1",
            "article_url": "https://takeuforward.org/data-structure/inorder-successor-predecessor-in-bst/",
            "video_url": "https://www.youtube.com/watch?v=SXKAD2svfmI",
            "notes": "Successor: if curr.val > key: succ = curr, go left. Else: go right. O(H) time, O(1) auxiliary space!"
        },
        {
            "name": "Merge Two BSTs into Balanced BST / Sorted List",
            "topic": "Binary Search Trees", "pattern": "BST to DLL to Balanced BST", "difficulty": "Hard",
            "practice_url": "https://www.geeksforgeeks.org/problems/merge-two-bst-s/1",
            "article_url": "https://takeuforward.org/data-structure/merge-two-bsts/",
            "video_url": "https://www.youtube.com/watch?v=ssL3sHwPeb4",
            "notes": "Convert both BSTs to sorted lists (or DLLs) in O(M+N). Merge sorted lists. Build balanced BST from sorted array."
        },
        {
            "name": "Root to Node Path in Binary Tree",
            "topic": "Binary Trees", "pattern": "DFS Path Recording", "difficulty": "Medium",
            "practice_url": "https://www.interviewbit.com/problems/path-to-given-node/",
            "article_url": "https://takeuforward.org/data-structure/print-root-to-node-path-in-a-binary-tree/",
            "video_url": "https://www.youtube.com/watch?v=fmflMqVOC7k",
            "notes": "DFS: append node.val to path. If node.val == target return True. If left or right finds target, return True. Else pop and return False."
        },

        # Graph Additions
        {
            "name": "Shortest Path in Directed Acyclic Graph (DAG)",
            "topic": "Graphs", "pattern": "Topological Relaxation", "difficulty": "Medium",
            "practice_url": "https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/1",
            "article_url": "https://takeuforward.org/data-structure/shortest-path-in-directed-acyclic-graph-topological-sort-g-27/",
            "video_url": "https://www.youtube.com/watch?v=ZUFQfFaU-8U",
            "notes": "Compute Topological Sort. Pop nodes from topo order and relax outgoing edges. O(V + E) linear time!"
        },
        {
            "name": "Shortest Path in Undirected Graph with Unit Weights",
            "topic": "Graphs", "pattern": "BFS Shortest Path", "difficulty": "Medium",
            "practice_url": "https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph-having-unit-distance/1",
            "article_url": "https://takeuforward.org/data-structure/shortest-path-in-undirected-graph-with-unit-distance-g-28/",
            "video_url": "https://www.youtube.com/watch?v=C4gxoTaI71U",
            "notes": "Standard BFS starting from src with dist[src] = 0. Queue guarantees shortest path for unit weights. O(V + 2E)."
        },
        {
            "name": "Minimum Spanning Tree - Prim's Algorithm",
            "topic": "Graphs", "pattern": "Prim's Greedy MST", "difficulty": "Medium",
            "practice_url": "https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1",
            "article_url": "https://takeuforward.org/data-structure/prims-algorithm-minimum-spanning-tree-c-and-java-g-45/",
            "video_url": "https://www.youtube.com/watch?v=mJcZjjKzeqk",
            "notes": "Min-heap storing (weight, node, parent). Pop smallest edge connecting to unvisited node. Add to MST. Mark visited."
        },
        {
            "name": "Network Delay Time",
            "topic": "Graphs", "pattern": "Dijkstra Bottleneck", "difficulty": "Medium",
            "practice_url": "https://leetcode.com/problems/network-delay-time/",
            "article_url": "https://takeuforward.org/data-structure/dijkstras-algorithm-using-priority-queue-g-32/",
            "video_url": "https://www.youtube.com/watch?v=V6H1qAeB-l4",
            "notes": "Dijkstra from source node k. Answer is max(dist) among all nodes. If any node unreachable, return -1."
        },
        {
            "name": "Number of Enclaves",
            "topic": "Graphs", "pattern": "Boundary Flood Fill", "difficulty": "Medium",
            "practice_url": "https://leetcode.com/problems/number-of-enclaves/",
            "article_url": "https://takeuforward.org/data-structure/number-of-enclaves/",
            "video_url": "https://www.youtube.com/watch?v=rxKcepXQgU4",
            "notes": "Start BFS/DFS from boundary land cells (1s) and mark them as connected to outside. Count remaining 1s."
        },
        {
            "name": "Number of Distinct Islands",
            "topic": "Graphs", "pattern": "Coordinate Hash Signature", "difficulty": "Medium",
            "practice_url": "https://www.geeksforgeeks.org/problems/number-of-distinct-islands/1",
            "article_url": "https://takeuforward.org/data-structure/number-of-distinct-islands/",
            "video_url": "https://www.youtube.com/watch?v=7zmgQSJghpo",
            "notes": "Store island coordinates relative to base cell (r - base_r, c - base_c) in HashSet. Set size is distinct islands!"
        },

        # Dynamic Programming Additions
        {
            "name": "Print Longest Common Subsequence",
            "topic": "Dynamic Programming", "pattern": "DP Table Backtracking", "difficulty": "Medium",
            "practice_url": "https://www.geeksforgeeks.org/problems/print-all-lcs-sequences3413/1",
            "article_url": "https://takeuforward.org/data-structure/print-longest-common-subsequence-dp-26/",
            "video_url": "https://www.youtube.com/watch?v=-zI4mrF2Pb4",
            "notes": "Build LCS table. Backtrack from (m, n): if s1[i-1] == s2[j-1]: append char, i--, j--. Else move toward max cell."
        },
        {
            "name": "Print Longest Increasing Subsequence",
            "topic": "Dynamic Programming", "pattern": "Parent Pointer Backtracking", "difficulty": "Medium",
            "practice_url": "https://www.geeksforgeeks.org/problems/printing-longest-increasing-subsequence/1",
            "article_url": "https://takeuforward.org/data-structure/printing-longest-increasing-subsequence-dp-42/",
            "video_url": "https://www.youtube.com/watch?v=IFfYfonAFGc",
            "notes": "dp[i] stores LIS ending at i, hash[i] stores predecessor index. Find max dp[i] and trace back through hash array."
        },
        {
            "name": "Number of Longest Increasing Subsequences",
            "topic": "Dynamic Programming", "pattern": "Dual State LIS", "difficulty": "Medium",
            "practice_url": "https://leetcode.com/problems/number-of-longest-increasing-subsequences/",
            "article_url": "https://takeuforward.org/data-structure/number-of-longest-increasing-subsequences-dp-47/",
            "video_url": "https://www.youtube.com/watch?v=cKVl1v9SiHA",
            "notes": "Maintain len[i] and count[i]. If len[j] + 1 > len[i]: len[i] = len[j] + 1, count[i] = count[j]. If equal: count[i] += count[j]."
        },
        {
            "name": "Evaluate Boolean Expression to True",
            "topic": "Dynamic Programming", "pattern": "3D Partition DP", "difficulty": "Hard",
            "practice_url": "https://www.interviewbit.com/problems/evaluate-expression-to-true/",
            "article_url": "https://takeuforward.org/data-structure/boolean-evaluation-to-true-dp-52/",
            "video_url": "https://www.youtube.com/watch?v=MM7fXopgyjw",
            "notes": "f(i, j, isTrue): split at operator k in [i+1, j-1] step 2. Combine left True/False with right True/False based on &, |, ^."
        },
        {
            "name": "Frog Jump with K Distance",
            "topic": "Dynamic Programming", "pattern": "Generalized 1D Transition", "difficulty": "Medium",
            "practice_url": "https://www.geeksforgeeks.org/problems/minimal-cost/1",
            "article_url": "https://takeuforward.org/data-structure/dynamic-programming-frog-jump-with-k-distances-dp-4/",
            "video_url": "https://www.youtube.com/watch?v=Kmh364YlZcY",
            "notes": "dp[i] = min over j in [1, k] (dp[i-j] + abs(height[i] - height[i-j])). O(N*K) time, O(K) space."
        },

        # Greedy Additions
        {
            "name": "Gas Station / Circular Tour",
            "topic": "Greedy", "pattern": "Deficit Tracking Greedy", "difficulty": "Medium",
            "practice_url": "https://leetcode.com/problems/gas-station/",
            "article_url": "https://takeuforward.org/data-structure/gas-station/",
            "video_url": "https://www.youtube.com/watch?v=34j9eF43f0Q",
            "notes": "If total_gas < total_cost, return -1. Track current_tank. If current_tank < 0: start = i + 1, current_tank = 0."
        },
        {
            "name": "Shortest Job First (SJF) Waiting Time",
            "topic": "Greedy", "pattern": "Sorting Greedy", "difficulty": "Easy",
            "practice_url": "https://www.geeksforgeeks.org/problems/shortest-job-first/1",
            "article_url": "https://takeuforward.org/greedy-algorithm/shortest-job-first-or-sjf-cpu-scheduling/",
            "video_url": "https://www.youtube.com/watch?v=3-bZ7gL9Uu8",
            "notes": "Sort burst times ascending. Total wait time = sum over i (wait_time so far). Average = total // n."
        },
        {
            "name": "Page Faults in LRU",
            "topic": "Greedy & Simulation", "pattern": "Cache Simulation", "difficulty": "Medium",
            "practice_url": "https://www.geeksforgeeks.org/problems/page-faults-in-lru5603/1",
            "article_url": "https://takeuforward.org/data-structure/page-faults-in-lru/",
            "video_url": "https://www.youtube.com/watch?v=z9bJUPxzFOw",
            "notes": "Maintain capacity C set/deque. If page in set: update recent. If not: page_fault++, evict oldest if full."
        },

        # Advanced Strings / Binary Search
        {
            "name": "Matrix Median in Row-Wise Sorted Matrix",
            "topic": "Binary Search", "pattern": "BS on Answer in Matrix", "difficulty": "Hard",
            "practice_url": "https://www.geeksforgeeks.org/problems/median-in-a-row-wise-sorted-matrix1527/1",
            "article_url": "https://takeuforward.org/data-structure/median-of-row-wise-sorted-matrix/",
            "video_url": "https://www.youtube.com/watch?v=63fPPOdIr2c",
            "notes": "BS range [min_elem, max_elem]. For mid, count elements <= mid across all rows using upper_bound. Find median count (R*C+1)//2."
        },
        {
            "name": "Count Number of Substrings with Exactly K Distinct Characters",
            "topic": "Sliding Window", "pattern": "AtMost(K) - AtMost(K-1)", "difficulty": "Medium",
            "practice_url": "https://www.geeksforgeeks.org/problems/subarrays-with-k-different-integers/1",
            "article_url": "https://takeuforward.org/sliding-window/subarrays-with-k-different-integers/",
            "video_url": "https://www.youtube.com/watch?v=7wYGbV_LsX4",
            "notes": "Count exactly K distinct = atMost(K) - atMost(K-1). Each atMost is standard sliding window."
        },

        # High-Yield Trees & BST Focus (Bridging Weak Areas)
        {
            "name": "Burning Tree / Minimum Time to Burn Binary Tree",
            "topic": "Binary Trees", "pattern": "Graph BFS / Parent Mapping", "difficulty": "Hard",
            "practice_url": "https://www.geeksforgeeks.org/problems/burning-tree/1",
            "article_url": "https://takeuforward.org/data-structure/minimum-time-taken-to-burn-the-binary-tree-from-a-node/",
            "video_url": "https://www.youtube.com/watch?v=2r5wLmQfD6g",
            "notes": "Map child -> parent using BFS. Start radial BFS from target node. Track burn time using visited set. O(N) time."
        },
        {
            "name": "Children Sum Property in Binary Tree",
            "topic": "Binary Trees", "pattern": "Node Value Transformation", "difficulty": "Medium",
            "practice_url": "https://www.geeksforgeeks.org/problems/children-sum-parent/1",
            "article_url": "https://takeuforward.org/data-structure/check-for-children-sum-property-in-a-binary-tree/",
            "video_url": "https://www.youtube.com/watch?v=fnmisRIL4VU",
            "notes": "If sum(children) < node.val: set children values to node.val. Recurse down. Backtrack: set node.val = sum(children). O(N)."
        },
        {
            "name": "Construct BST from Preorder Traversal",
            "topic": "Binary Search Trees", "pattern": "Upper Bound DFS", "difficulty": "Medium",
            "practice_url": "https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/",
            "article_url": "https://takeuforward.org/data-structure/construct-a-bst-from-a-preorder-traversal/",
            "video_url": "https://www.youtube.com/watch?v=UmJT3j26t1I",
            "notes": "Pass upper_bound. If curr val > bound or index == len: return None. root = Node(val), build left (bound=val), build right (bound=bound). O(N)."
        },
        {
            "name": "Path Sum II (Root-to-Leaf Paths with Given Sum)",
            "topic": "Binary Trees", "pattern": "DFS Path Backtracking", "difficulty": "Medium",
            "practice_url": "https://leetcode.com/problems/path-sum-ii/",
            "article_url": "https://takeuforward.org/data-structure/print-root-to-node-path-in-a-binary-tree/",
            "video_url": "https://www.youtube.com/watch?v=fmflMqVOC7k",
            "notes": "DFS: add node.val to current path. If leaf and target == node.val: record path copy. Backtrack: pop node.val."
        },
        {
            "name": "Same Tree / Check if Two Trees are Identical",
            "topic": "Binary Trees", "pattern": "Structural DFS", "difficulty": "Easy",
            "practice_url": "https://leetcode.com/problems/same-tree/",
            "article_url": "https://takeuforward.org/data-structure/check-if-two-trees-are-identical/",
            "video_url": "https://www.youtube.com/watch?v=BhuvF_-PWS0",
            "notes": "If both None: True. If one None or values differ: False. Return isSame(p.left, q.left) and isSame(p.right, q.right)."
        },
        {
            "name": "Maximum Sum BST in Binary Tree",
            "topic": "Binary Search Trees", "pattern": "Postorder BST State Tracking", "difficulty": "Hard",
            "practice_url": "https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/",
            "article_url": "https://takeuforward.org/data-structure/maximum-sum-bst-in-binary-tree/",
            "video_url": "https://www.youtube.com/watch?v=X0oXMdtUDwo",
            "notes": "Postorder returns (is_bst, sum_val, min_val, max_val). If left and right are valid BSTs and left.max < root.val < right.min: update global max sum."
        },

        # High-Yield Graph Focus (Bridging Weak Areas)
        {
            "name": "Number of Islands",
            "topic": "Graphs", "pattern": "Grid BFS / DFS Traversal", "difficulty": "Medium",
            "practice_url": "https://leetcode.com/problems/number-of-islands/",
            "article_url": "https://takeuforward.org/data-structure/number-of-islands/",
            "video_url": "https://www.youtube.com/watch?v=muncqlKJrH0",
            "notes": "Iterate all cells. When unvisited '1' found: islands++, run BFS/DFS in 4 directions marking all connected land visited."
        },
        {
            "name": "Path With Minimum Effort (Dijkstra on Grid)",
            "topic": "Graphs", "pattern": "Min-Heap 2D Dijkstra", "difficulty": "Medium",
            "practice_url": "https://leetcode.com/problems/path-with-minimum-effort/",
            "article_url": "https://takeuforward.org/data-structure/g-37-path-with-minimum-effort/",
            "video_url": "https://www.youtube.com/watch?v=0ytpZdxHYhA",
            "notes": "Min-heap storing (effort, r, c). Effort to neighbor is max(effort, abs(h[nr][nc] - h[r][c])). Stop when destination reached."
        },
        {
            "name": "Floyd Warshall Algorithm (All-Pairs Shortest Path)",
            "topic": "Graphs", "pattern": "Dynamic Programming Matrix Relaxation", "difficulty": "Medium",
            "practice_url": "https://www.geeksforgeeks.org/problems/implementing-floyd-warshall2042/1",
            "article_url": "https://takeuforward.org/data-structure/floyd-warshall-algorithm-g-42/",
            "video_url": "https://www.youtube.com/watch?v=YbY8cVwWAvw",
            "notes": "matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j]) for each via node k. Detect negative cycles if matrix[i][i] < 0."
        },
        {
            "name": "Word Ladder II (Find All Shortest Transformation Sequences)",
            "topic": "Graphs", "pattern": "BFS Level Mapping + DFS Backtracking", "difficulty": "Hard",
            "practice_url": "https://leetcode.com/problems/word-ladder-ii/",
            "article_url": "https://takeuforward.org/data-structure/word-ladder-ii-shortest-transformation-sequence-g-31/",
            "video_url": "https://www.youtube.com/watch?v=DREutrv2gz0",
            "notes": "Step 1: BFS from startWord to record shortest distance/step of each word. Step 2: Backtrack using DFS from endWord to startWord."
        },
        {
            "name": "Tarjan's Algorithm for Bridges in Graph",
            "topic": "Graphs", "pattern": "DFS Discovery Time & Low Link", "difficulty": "Hard",
            "practice_url": "https://leetcode.com/problems/critical-connections-in-a-network/",
            "article_url": "https://takeuforward.org/data-structure/bridges-in-graph-using-tarjans-algorithm-g-55/",
            "video_url": "https://www.youtube.com/watch?v=qrAub5z8FeA",
            "notes": "Maintain tin[] and low[]. If low[adj] > tin[node]: edge (node, adj) is a bridge (critical connection)!"
        },

        # High-Yield DP Focus (Bridging Weak Areas)
        {
            "name": "Maximal Rectangle with 1s",
            "topic": "Dynamic Programming", "pattern": "2D Matrix to Largest Histogram", "difficulty": "Hard",
            "practice_url": "https://leetcode.com/problems/maximal-rectangle/",
            "article_url": "https://takeuforward.org/data-structure/maximal-rectangle-area-in-binary-sub-matrix-dp-55/",
            "video_url": "https://www.youtube.com/watch?v=tOylVCugy9k",
            "notes": "Maintain heights array of size m. For each row: update height (if '1': height++, else: 0). Run Largest Rectangle in Histogram on heights."
        },
        {
            "name": "Unbounded Knapsack Problem",
            "topic": "Dynamic Programming", "pattern": "Infinite Supply Knapsack", "difficulty": "Medium",
            "practice_url": "https://www.geeksforgeeks.org/problems/knapsack-with-duplicate-items4201/1",
            "article_url": "https://takeuforward.org/data-structure/unbounded-knapsack-dp-23/",
            "video_url": "https://www.youtube.com/watch?v=OgvOZ6OrWgY",
            "notes": "Pick stays on same index: take = val[i] + f(i, W - wt[i]). 1D space optimization: traverse capacity left to right."
        },
        {
            "name": "Minimum Path Sum in Triangular Grid",
            "topic": "Dynamic Programming", "pattern": "Triangular Bottom-Up DP", "difficulty": "Medium",
            "practice_url": "https://leetcode.com/problems/triangle/",
            "article_url": "https://takeuforward.org/data-structure/minimum-path-sum-in-triangular-grid-dp-11/",
            "video_url": "https://www.youtube.com/watch?v=SrP-PiLSYC0",
            "notes": "dp[i][j] = triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1]). Base case: bottom row. Optimize to 1D array of size N."
        },
        {
            "name": "Longest String Chain",
            "topic": "Dynamic Programming", "pattern": "LIS on Word Predecessors", "difficulty": "Medium",
            "practice_url": "https://leetcode.com/problems/longest-string-chain/",
            "article_url": "https://takeuforward.org/data-structure/longest-string-chain-dp-45/",
            "video_url": "https://www.youtube.com/watch?v=YY8iBaYcc4g",
            "notes": "Sort strings by length. For each word, generate predecessors by deleting 1 char. dp[word] = max(dp.get(pred, 0) + 1)."
        },
        {
            "name": "Best Time to Buy and Sell Stock IV (At Most K Transactions)",
            "topic": "Dynamic Programming", "pattern": "3D State DP (Transactions Cap)", "difficulty": "Hard",
            "practice_url": "https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/",
            "article_url": "https://takeuforward.org/data-structure/buy-and-sell-stock-iv-dp-38/",
            "video_url": "https://www.youtube.com/watch?v=IV13PRPUMQU",
            "notes": "State dp[ind][buy][cap]. If buy: max(-prices[i] + f(i+1, 0, cap), f(i+1, 1, cap)). If sell: max(prices[i] + f(i+1, 1, cap-1), f(i+1, 0, cap))."
        }
    ]

    # Combine all unique items
    for item in extra_conceptual:
        if item["name"] not in by_name:
            by_name[item["name"]] = item

    all_items = list(by_name.values())

    # Map the ~310-320 items across 75 days logically by topic order
    # Topic priority:
    # 1. Sorting & Arrays (Days 1-9)
    # 2. Binary Search (Days 10-16)
    # 3. Sliding Window (Days 17-20)
    # 4. Linked List & Strings (Days 21-28)
    # 5. Stacks & Queues & Bit Manipulation (Days 29-35)
    # 6. Recursion & Backtracking (Days 36-41)
    # 7. Binary Trees & BST (Days 42-50)
    # 8. Graphs (Days 51-59)
    # 9. Dynamic Programming (Days 60-68)
    # 10. Heaps, Greedy, Tries & Capstone (Days 69-75)

    def topic_order_key(item):
        t = item.get("topic", "")
        p = item.get("pattern", "")
        
        # 1. Arrays & Sorting & Two Pointers
        if "Sorting" in t or ("Array" in t and "BST" not in t and "Tree" not in t):
            return 1
        # 2. Binary Search (1D, 2D, Answer) - but NOT BST!
        elif "Binary Search" in t and "Tree" not in t and "BST" not in t:
            return 2
        # 3. Sliding Window
        elif "Sliding Window" in t:
            return 3
        # 4. Linked List & Strings
        elif "Linked List" in t or "String" in t:
            return 4
        # 5. Stack & Queue & Bit Manipulation & Math
        elif "Stack" in t or "Bit" in t or "Math" in t:
            return 5
        # 6. Recursion & Backtracking
        elif "Recursion" in t or "Backtrack" in t:
            return 6
        # 7. Binary Trees & Binary Search Trees (Suite)
        elif "Tree" in t or "BST" in t:
            return 7
        # 8. Graphs & Disjoint Set
        elif "Graph" in t or "Disjoint" in t:
            return 8
        # 9. Dynamic Programming
        elif "Dynamic Programming" in t or "DP" in t:
            return 9
        # 10. Heaps, Greedy, Trie & Capstone
        else:
            return 10

    diff_order = {"Easy": 1, "Medium": 2, "Hard": 3}
    groups = {i: [] for i in range(1, 11)}
    for item in all_items:
        groups[topic_order_key(item)].append(item)

    for i in range(1, 11):
        groups[i].sort(key=lambda x: diff_order.get(x.get("difficulty", "Medium"), 2))

    group_config = {
        1: (1, 9, "Phase 1: Arrays & Sorting & Two Pointers"),
        2: (10, 14, "Phase 2: Binary Search (1D, 2D & Answers)"),
        3: (15, 17, "Phase 3: Sliding Window & Two Pointers"),
        4: (18, 25, "Phase 4: Linked Lists & String Algorithms"),
        5: (26, 34, "Phase 5: Stacks, Monotonic Queues & Bit Manipulation"),
        6: (35, 38, "Phase 6: Recursion, Backtracking & Combinatorics"),
        7: (39, 48, "Phase 7: Binary Trees & BST (Complete Suite)"),
        8: (49, 58, "Phase 8: Graph Theory & Shortest Path Algorithms"),
        9: (59, 69, "Phase 9: Dynamic Programming Masterclass (All 7 Archetypes)"),
        10: (70, 75, "Phase 10: Heaps, Greedy, Tries & Pro Capstone")
    }

    final_dataset = []
    for g_id, (s_day, e_day, p_name) in group_config.items():
        items = groups[g_id]
        n_days = e_day - s_day + 1
        for idx, item in enumerate(items):
            day_num = s_day + min(n_days - 1, int(idx / (len(items) / n_days)))
            week_num = min(11, (day_num - 1) // 7 + 1)
            
            clean_item = dict(item)
            clean_item["day"] = day_num
            clean_item["week"] = week_num
            clean_item["phase"] = p_name.replace(",", " &").strip()
            clean_item["topic"] = clean_item.get("topic", "DSA").replace(",", " &").strip()
            clean_item["pattern"] = clean_item.get("pattern", "Core").replace(",", " &").strip()
            clean_item["difficulty"] = clean_item.get("difficulty", "Medium")
            clean_item["notes"] = clean_item.get("notes", "Review key edge cases, constraints, and time/space complexity.")
            final_dataset.append(clean_item)

    # Sort by day ascending
    final_dataset.sort(key=lambda x: (x["day"], diff_order.get(x["difficulty"], 2)))

    # Save to JSON
    with open("dsa_75day_database.json", "w", encoding="utf-8") as f:
        json.dump(final_dataset, f, indent=2)

    # Save to CSV (with Question Name as column 1!)
    fieldnames = [
        "Question Name", "Day", "Week", "Phase", "Topic", "Pattern",
        "Difficulty", "Status", "Confidence", "Practice Link",
        "Striver Article Link", "Striver YouTube Link",
        "Notes & Edge Cases", "Review Date"
    ]
    with open("notion_dsa_75day_planner.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for item in final_dataset:
            writer.writerow({
                "Question Name": item["name"],
                "Day": f"Day {item['day']:02d}",
                "Week": f"Week {item['week']:02d}",
                "Phase": item["phase"],
                "Topic": item["topic"],
                "Pattern": item["pattern"],
                "Difficulty": item["difficulty"],
                "Status": "Not Started",
                "Confidence": "⭐⭐ Confident",
                "Practice Link": item.get("practice_url", ""),
                "Striver Article Link": item.get("article_url", ""),
                "Striver YouTube Link": item.get("video_url", ""),
                "Notes & Edge Cases": item["notes"],
                "Review Date": ""
            })

    print(f"🎉 75-Day Master Curriculum compiled successfully!")
    print(f"Total curated problems: {len(final_dataset)} across 75 days.")
    print(f"Generated: dsa_75day_database.json and notion_dsa_75day_planner.csv")

if __name__ == "__main__":
    build_75day_dataset()
