#!/bin/bash
# Script to run a single non-optimal large graph test case

# Define the solution file and test case
SOLUTION_FILE="./cs412_mingraphcoloring_approx.py"
TEST_CASE="test_cases/superlarge_nonoptimal.txt"

# Check if solution file exists
if [ ! -f "$SOLUTION_FILE" ]; then
    echo "Error: Solution file '$SOLUTION_FILE' not found!"
    exit 1
fi

# Check if test file exists
if [ ! -f "$TEST_CASE" ]; then
    echo "Error: Test file '$TEST_CASE' not found!"
    exit 1
fi

# Run the test
echo "Running Non-Optimal Large Graph Test Case..."
echo "This test case demonstrates where the approximation solution does not achieve the optimal answer."
python "$SOLUTION_FILE" "$TEST_CASE"

if [ $? -eq 0 ]; then
    echo "✓ Test completed successfully"
else
    echo "✗ Test failed with error code $?"
fi
