This Python program implements a simulator for the Banker's Algorithm (deadlock‐avoidance). It:

Reads the number of processes and resource types.

Reads the Available resource vector.

Reads the Allocation and Maximum demand matrices.

Computes the Need matrix.

Checks if the system is in a safe state and prints a safe sequence if one exists.

Offers the user the option to make one resource request.

If granted, commits the change and shows the updated matrices and new safe sequence.

If unsafe, rolls back and reports the denial.

Files

bankers.py: Main script containing all functions and the interactive CLI.

README.md: This documentation file.

Requirements

Python 3.6 or later

How to Run

Open a terminal or command prompt.

Navigate to the directory containing bankers.py.

Run:

python bankers.py

Follow the prompts:

Enter number of processes (e.g. 5).

Enter number of resources (e.g. 4).

Enter Available vector (space‐separated list of length resources).

Enter Allocation matrix: one row per process.

Enter Max matrix: one row per process.

The program displays the Need matrix and initial safety result.

When asked, enter y to test a resource request or n to exit.

If y, provide process index (0–n-1) and the request vector.

The program will grant or deny based on safety, update state if granted, and display the new matrices.

Function Descriptions

readingvector(prompt, count): Reads a vector of count integers; re‑prompts on invalid input.

readingmatrix(name, processes, resources): Reads a processes × resources matrix, row by row.

calculate_need(max_mat, alloc_mat): Returns Need matrix computed as Max - Allocation.

safetycheck(available, alloc_mat, need_mat): Implements the Banker's safety‐state algorithm. Returns (True, sequence) if safe, otherwise (False, []).

request(available, alloc_mat, need_mat): Performs the resource‐request algorithm:

Validates Request ≤ Need and Request ≤ Available.

Tentatively applies the request to the real matrices.

Re‐runs the safety check.

Commits the change if safe; otherwise reverts.

Displays the updated state.

Notes

Only one request per run is supported; rerun the script to test another request.

The matrices are modified in place on a granted request, modeling a real system.
