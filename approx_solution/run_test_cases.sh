#!/bin/bash
# Script to run test cases for the approximation solution

# Define the correct solution file
SOLUTION_FILE="./cs412_mingraphcoloring_approx.py"

# Check if the solution file exists
if [ ! -f "$SOLUTION_FILE" ]; then
    echo "Error: Solution file '$SOLUTION_FILE' not found!"
    exit 1
fi

# Define test cases
TEST_CASES=(
    "test_cases/small_optimal.txt"
    "test_cases/medium_optimal.txt"
    "test_cases/large_optimal.txt"
    "test_cases/superlarge_nonoptimal.txt"
)

# Run the test cases
echo "Running test cases for Min Graph Coloring Approximation..."
for TEST_CASE in "${TEST_CASES[@]}"; do
    if [ -f "$TEST_CASE" ]; then
        echo "Running test case: $TEST_CASE"
        python "$SOLUTION_FILE" "$TEST_CASE"
    else
        echo "Error: Test case '$TEST_CASE' not found!"
    fi
done
echo "All test cases executed."
