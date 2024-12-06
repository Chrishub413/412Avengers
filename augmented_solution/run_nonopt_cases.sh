#!/bin/bash

# Color definitions for prettier output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color
DIVIDER="=================================================================="

# Check if solution file exists
if [ ! -f "cs412_mingraphcoloring_augment.py" ]; then
    echo -e "${RED}Error: Solution file 'cs412_mingraphcoloring_augment.py' not found!${NC}"
    exit 1
fi

# Check if test file exists
if [ ! -f "test_cases/superlarge_nonoptimal.txt" ]; then
    echo -e "${RED}Error: Test file 'test_cases/superlarge_nonoptimal.txt' not found!${NC}"
    exit 1
fi

echo -e "${BLUE}Running Non-Optimal Large Graph Test Case${NC}"
echo -e "${BLUE}This test case demonstrates where the approximation solution"
echo -e "does not achieve the optimal answer.${NC}"
echo $DIVIDER

# Run the test
python cs412_mingraphcoloring_augment.py test_cases/superlarge_nonoptimal.txt

if [ $? -eq 0 ]; then
    echo -e "\n${GREEN}✓ Test completed successfully${NC}"
else
    echo -e "\n${RED}✗ Test failed with error code $?${NC}"
fi

echo $DIVIDER
echo -e "${BLUE}Non-optimal test case execution completed.${NC}"