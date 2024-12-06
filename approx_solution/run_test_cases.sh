#!/bin/bash

# Color definitions for prettier output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color
DIVIDER="=================================================================="

# Function to run a test case and check its execution
run_test_case() {
    local test_file="$1"
    local description="$2"

    echo -e "\n${BLUE}Testing: ${description}${NC}"
    echo -e "${BLUE}Input file: ${test_file}${NC}"
    echo $DIVIDER

    if [ -f "$test_file" ]; then
        python cs412_mingraphcoloring_approx.py "$test_file"
        if [ $? -eq 0 ]; then
            echo -e "${GREEN}✓ Test completed successfully${NC}"
        else
            echo -e "${RED}✗ Test failed with error code $?${NC}"
        fi
    else
        echo -e "${RED}✗ Error: Test file '${test_file}' not found${NC}"
    fi

    echo $DIVIDER
}

# Main execution
echo -e "${BLUE}Starting Min Graph Coloring Approximation Test Suite${NC}"
echo $DIVIDER

# Run all test cases with descriptions
test_cases=(
    "test_cases/large_nonoptimal.txt:Large Non-Optimal Graph Test"
    "test_cases/large_optimal.txt:Large Optimal Graph Test"
    "test_cases/medium_nonoptimal.txt:Medium Non-Optimal Graph Test"
    "test_cases/medium_optimal.txt:Medium Optimal Graph Test"
    "test_cases/small_nonoptimal.txt:Small Non-Optimal Graph Test"
    "test_cases/small_optimal.txt:Small Optimal Graph Test"
)

# Check if the solution file exists
if [ ! -f "cs412_mingraphcoloring_approx.py" ]; then
    echo -e "${RED}Error: Solution file 'cs412_mingraphcoloring_approx.py' not found!${NC}"
    exit 1
fi

# Execute each test case
for test_case in "${test_cases[@]}"; do
    IFS=':' read -r file description <<< "$test_case"
    run_test_case "$file" "$description"
done

echo -e "\n${GREEN}All test cases have been executed.${NC}"
echo -e "${BLUE}Note: Check above for any individual test failures.${NC}"