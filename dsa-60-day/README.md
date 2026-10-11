# 🚀 60-Day Pro DSA Master Roadmap (Striver A2Z Curriculum)

> **Objective:** A fast-paced, high-yield **60-Day curriculum** designed to build interview-ready mastery across all core Data Structures & Algorithms (Trees, Graphs, DP, Tries, Heaps, Monotonic Stacks).

---

## 🧠 Part 1: Core Principles for Consistent DSA Mastery

### 1. Avoid the "Reset Trap"
A common pitfall in DSA preparation is restarting from Array basics whenever returning from a break. 
- **The Rule:** If a busy week or academic break interrupts your routine, **never restart from Day 01**. 
- Open your planner, spend 1 day reviewing your past notes/spaced repetition cards, and pick up right where you left off. Cumulative progress is key.

### 2. Consistency Over Intensity (The Maintenance Protocol)
- During busy schedules or project deadlines, avoid dropping problem solving to zero.
- Maintain a **Maintenance Routine**: Solve just **1 revision problem daily** (15–20 minutes) or review high-yield flashcard notes. This keeps pattern recognition sharp without taking time away from other priorities.

### 3. The 25-Minute Rule
- Avoid staring at a problem indefinitely without direction.
- **0 to 20 minutes:** Brainstorm, diagram on paper, test boundary cases, and write a brute-force approach.
- **If stuck after 25 minutes:** Consult the Striver editorial / video walkthrough. Understand the underlying pattern (e.g. *"This requires a monotonic stack because we need nearest greater element on the right"*).
- **Close the solution** and implement the code cleanly from scratch. Record key insights in the **Notes & Edge Cases** column.

### 4. Spaced Repetition (The 1-3-7-21 Principle)
- Challenging problems (e.g., Trapping Rain Water, Median of Two Sorted Arrays, Edit Distance) should be flagged as **"Needs Revision"** and revisited after 3 days and 7 days to solidify retention.

---

## 🛠️ Part 2: How to Set Up Your Notion Planner

You have two simple ways to get your full 60-day interactive planner inside Notion:

### Option A: 1-Click CSV Import (Instant, 30 Seconds, No Code Required)
1. Locate the file: `notion_dsa_60day_planner.csv` inside this folder.
2. Open **Notion** on your browser or desktop app.
3. In the sidebar, click **+ Add a page** (or open an existing page).
4. Click the `...` menu (top-right) ➔ **Import**.
5. Select **CSV** and upload `notion_dsa_60day_planner.csv`.
6. Notion will automatically convert the CSV into a database with all 260 questions and columns:
   - `Day`, `Topic`, `Pattern`, `Question Name`, `Difficulty`, `Status`, `Practice Link`, `Striver Article Link`, `Striver YouTube Link`, `Notes & Edge Cases`.
7. **Recommended Views:**
   - **Kanban Board:** Group by `Status` (Not Started / In Progress / Done / Needs Revision).
   - **Daily Timeline:** Group by `Day` or `Week`.
   - **Topic Filter:** Filter or group by `Topic`.

---

### Option B: Direct Notion API Sync (Automated Script)
If you prefer building the database programmatically via the Notion API:
1. Follow the setup instructions in the root [README.md](../README.md).
2. Run the sync command:
   ```bash
   python3 ../scripts/sync_to_notion.py --plan 60
   ```
3. The script creates the database and populates all 260 questions with direct clickable links, difficulty tags, and notes!

---

## 📅 Part 3: The 60-Day Curriculum Breakdown

```
Phase 1: Days 01–07 | Arrays & Two Pointers (High-Yield Core)
Phase 2: Days 08–14 | Binary Search (1D, 2D & On Answers) & Sliding Window
Phase 3: Days 15–21 | Linked Lists (Tortoise-Hare, LRU Cache) & String Patterns
Phase 4: Days 22–28 | Stacks, Monotonic Queues & Bit Manipulation
Phase 5: Days 29–35 | Recursion, Backtracking & Binary Trees (Traversals & Views)
Phase 6: Days 36–42 | BST, Graph Traversals, TopoSort & Shortest Paths (Dijkstra)
Phase 7: Days 43–49 | Disjoint Set Union (DSU), MST & Dynamic Programming Foundations
Phase 8: Days 50–56 | Advanced DP (Strings, Stocks, LIS, MCM & Partition DP)
Phase 9: Days 57–60 | Heaps, Greedy Algorithms, Tries & FAANG Mock Capstones
```

---

### Weekly Roadmap Summary:

#### Week 1 (Days 1–7): Array Mastery & In-Place Algorithms
- **Day 1:** Array Fundamentals, Rotations, In-place De-duplication, Move Zeroes, Union of Sorted Arrays.
- **Day 2:** Single Number, Missing Number, Longest Subarray with Sum K (Prefix Sum Map), Two Sum, Dutch National Flag (Sort Colors).
- **Day 3:** Moore's Voting Algorithm (Majority Element), Kadane's Algorithm (Max Subarray), Best Time to Buy and Sell Stock I, Rearrange by Sign, Next Permutation.
- **Day 4:** Leaders in Array, Longest Consecutive Sequence (HashSet O(N)), Set Matrix Zeroes, Rotate Image 90°, Spiral Matrix, Subarray Sum Equals K.
- **Day 5:** Pascal's Triangle, Majority Element II (> n/3), 3-Sum, 4-Sum, Subarrays with Given XOR K.
- **Day 6:** Merge Overlapping Intervals, Merge Sorted Arrays Without Extra Space (Gap method), Missing and Repeating Number, Count Inversions (Merge Sort), Reverse Pairs, Max Product Subarray.
- **Day 7:** Week 1 Integration: Subarray Sums Divisible by K, Spiral Matrix II, Container With Most Water, Active Recall check.

#### Week 2 (Days 8–14): Binary Search & Sliding Window
- **Day 8:** Binary Search 1D, Lower Bound, Upper Bound, Search Insert Position, First & Last Position, Count Occurrences.
- **Day 9:** Search in Rotated Sorted Array I & II, Find Minimum in Rotated Array, Single Element in Sorted Array, Find Peak Element.
- **Day 10:** BS on Answers: Sqrt(x), Nth Root, Koko Eating Bananas, Min Days for M Bouquets, Capacity to Ship Packages.
- **Day 11:** BS on Answers (Hard): Aggressive Cows, Book Allocation, Split Array Largest Sum, Median of Two Sorted Arrays, K-th Element of Two Sorted Arrays.
- **Day 12:** Search in 2D Matrix I & II, Find Peak Element in 2D Matrix, Matrix Median.
- **Day 13:** Sliding Window: Longest Substring Without Repeating Characters, Max Consecutive Ones III, Fruit Into Baskets, Min Size Subarray Sum, Binary Subarrays with Sum.
- **Day 14:** Sliding Window (Hard): Number of Substrings with a,b,c, Max Points from Cards, Subarrays with K Different Integers (AtMost trick), Minimum Window Substring.

#### Week 3 (Days 15–21): Linked Lists & String Patterns
- **Day 15:** Reverse LL (Iterative & Recursive), Middle of LL, Detect Cycle (Floyd's), Find Loop Start Node.
- **Day 16:** Palindrome LL, Remove Nth Node from End, Odd-Even LL, Sort LL (Merge Sort on LL).
- **Day 17:** Add Two Numbers, Intersection of Two LLs, Reverse in K-Group, Copy List with Random Pointer, Flattening LL, Rotate List, Design LRU Cache, Design LFU Cache.
- **Day 18:** Reverse Words in String, Longest Common Prefix, Isomorphic Strings, Valid Anagram.
- **Day 19:** Sort Characters by Frequency, String to Integer (atoi), Longest Palindromic Substring, Sum of Beauty of Substrings.
- **Day 20:** KMP Algorithm (LPS Array), Rabin-Karp Rolling Hash, Repeated String Match, Shortest Palindrome.
- **Day 21:** Week 3 Review: Swap Nodes in Pairs, Reorder List, Active Recall LRU Cache from scratch.

#### Week 4 (Days 22–28): Stacks, Queues & Bit Manipulation
- **Day 22:** Valid Parentheses, Min Stack O(1), Implement Queue using Stacks, Infix to Postfix, Evaluate Postfix.
- **Day 23:** Monotonic Stack: Next Greater Element I & II, Trapping Rain Water, Sum of Subarray Minimums.
- **Day 24:** Largest Rectangle in Histogram, Maximal Rectangle in 2D Matrix, Sliding Window Maximum (Monotonic Deque), Remove K Digits, Online Stock Span, Celebrity Problem.
- **Day 25:** Bit Hacks (Check, Set, Clear, Toggle), Brian Kernighan's (Count Set Bits), Power of 2, Divide Two Integers without `*` or `/`.
- **Day 26:** Single Number II (Thrice), Single Number III (Twice), Power Set via Bitmasking.
- **Day 27:** Euclidean GCD, Sieve of Eratosthenes, Smallest Prime Factor (SPF), Pow(x, n).
- **Day 28:** Phase 1-4 Milestone Benchmark: Rainwater, Histogram, Single Number III, Sliding Window Max.

#### Week 5 (Days 29–35): Recursion, Backtracking & Binary Trees
- **Day 29:** Generate Parentheses, Combination Sum I & II, Subsets II.
- **Day 30:** Palindrome Partitioning, Word Search in 2D Board, N-Queens, Sudoku Solver, Rat in a Maze, M-Coloring, Permutations.
- **Day 31:** Level Order Traversal (BFS), Maximum Depth, Balanced Tree Check, Diameter of Binary Tree.
- **Day 32:** Binary Tree Max Path Sum, Zigzag Traversal, Boundary Traversal, Vertical Order Traversal.
- **Day 33:** Top & Bottom View, Right & Left View, Lowest Common Ancestor (LCA), Symmetric Tree, Max Width of BT.
- **Day 34:** All Nodes Distance K, Construct BT from Preorder & Inorder, Count Complete Tree Nodes, Flatten BT to LL, Serialize & Deserialize BT.
- **Day 35:** Morris Inorder & Preorder Traversal (O(1) space), All 3 traversals in 1 pass.

#### Week 6 (Days 36–42): BST & Graph Fundamentals
- **Day 36:** BST Search & Insert, Delete Node in BST, Floor and Ceil in BST, K-th Smallest in BST.
- **Day 37:** Validate BST, LCA in BST, BST Iterator, Two Sum in BST, Recover BST (Swapped Nodes), Largest BST in Binary Tree.
- **Day 38:** Graph BFS & DFS, Number of Provinces, Rotting Oranges (Multi-source BFS), Flood Fill.
- **Day 39:** Detect Cycle in Undirected Graph (BFS & DFS), 0/1 Matrix, Surrounded Regions, Is Graph Bipartite?
- **Day 40:** Cycle in Directed Graph (DFS), Topological Sort (Kahn's BFS), Course Schedule I & II, Find Eventual Safe States, Alien Dictionary, Word Ladder I.
- **Day 41:** Dijkstra's Algorithm (Min Heap), Path with Minimum Effort, Shortest Path in Binary Matrix, Cheapest Flights within K Stops.
- **Day 42:** Bellman-Ford, Floyd-Warshall, Number of Ways to Arrive at Destination, Min Multiplications to Reach End, City with Smallest Neighbors at Threshold.

#### Week 7 (Days 43–49): DSU, MST & Dynamic Programming Foundations
- **Day 43:** Disjoint Set Union (Rank & Size), Kruskal's MST, Number of Operations to Make Network Connected, Accounts Merge, Most Stones Removed.
- **Day 44:** Bridges in Graph (Tarjan's), Making a Large Island, Swim in Rising Water, Strongly Connected Components (Kosaraju's), Articulation Points.
- **Day 45:** Intro to DP: Memoization vs Tabulation, Climbing Stairs, Frog Jump, House Robber I & II, Ninja's Training.
- **Day 46:** 2D Grid DP: Unique Paths I & II, Minimum Path Sum, Triangle, Cherry Pickup II (3D DP).
- **Day 47:** Subset Sum Equal to Target, Partition Equal Subset Sum, Partition Set with Min Absolute Sum Diff, 0/1 Knapsack.
- **Day 48:** Coin Change I & II, Target Sum, Unbounded Knapsack, Rod Cutting Problem.
- **Day 49:** DP Milestone Benchmark: Minimum Falling Path Sum, Partitions with Given Difference, Count Subsets with Sum K.

#### Week 8 (Days 50–56): Advanced DP Masterclass
- **Day 50:** Longest Common Subsequence (LCS), Longest Palindromic Subsequence, Shortest Common Supersequence, Min Insertions/Deletions, Longest Common Substring.
- **Day 51:** Distinct Subsequences, Edit Distance, Wildcard Matching.
- **Day 52:** Best Time to Buy and Sell Stock II, III, IV (At Most K), With Cooldown, With Transaction Fee.
- **Day 53:** Longest Increasing Subsequence (O(N log N) Binary Search), Largest Divisible Subset, Longest String Chain, Longest Bitonic Subsequence.
- **Day 54:** Matrix Chain Multiplication (MCM), Minimum Cost to Cut a Stick, Burst Balloons, Palindrome Partitioning II.
- **Day 55:** Count Square Submatrices with All Ones, House Robber III (DP on Trees), Partition Array for Maximum Sum.
- **Day 56:** DP Synthesis Benchmark: Burst Balloons, Wildcard Matching, Edit Distance.

#### Week 9 (Days 57–60): Heaps, Greedy, Tries & Pro Capstone
- **Day 57:** Kth Largest Element, Merge K Sorted Lists, Find Median from Data Stream, Task Scheduler, Hand of Straights.
- **Day 58:** N Meetings in One Room, Non-Overlapping Intervals, Insert Interval, Candy Distribution, Minimum Railway Platforms, Job Sequencing, Jump Game I & II.
- **Day 59:** Implement Trie I & II, Complete String with All Prefixes, Maximum XOR of Two Numbers, Maximum XOR Queries.
- **Day 60:** Pro Capstone Assessment: Word Ladder II, Median of Two Sorted Arrays Benchmark, Serialize & Deserialize BT Benchmark.

---

## 🎯 Pro Tips to Keep Your Streak 100% Intact
1. **Never break the chain:** Even on busy days, solve at least **1 Easy/Medium** or read through 2 solutions actively.
2. **Commit your code to GitHub:** Create a repository `60-Days-DSA` and push your daily solutions with clean comments.
3. **Use the Notion Status column diligently:** Mark `In Progress` when starting and `Done` when accepted. If you required editorial help, immediately set Status to `Needs Revision` so you revisit it 3 days later!
