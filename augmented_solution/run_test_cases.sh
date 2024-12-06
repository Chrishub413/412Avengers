#!/bin/bash
# Script to run all test cases for the approximation solution

echo "Running test cases for Min Graph Coloring Approximation..."
python cs412_mingraphcoloring_augment.py test_cases/small_optimal.txt
python cs412_mingraphcoloring_augment.py test_cases/medium_optimal.txt
python cs412_mingraphcoloring_augment.py test_cases/large_optimal.txt
echo "All test cases executed."