#!/bin/bash
# Script to run all test cases for the approximation solution

echo "Running test cases for Min Graph Coloring Approximation..."
python cs412_mingraphcoloring_augment.py test_cases/small_nonoptimal.txt
python cs412_mingraphcoloring_augment.py test_cases/medium_nonoptimal.txt
python cs412_mingraphcoloring_augment.py test_cases/large_nonoptimal.txt
echo "All test cases executed."