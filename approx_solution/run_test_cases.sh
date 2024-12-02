#!/bin/bash
# Script to run all test cases for the approximation solution

echo "Running test cases for Min Graph Coloring Approximation..."
python cs412_mingraphcoloring_approx.py test_cases/graph1.txt
python cs412_mingraphcoloring_approx.py test_cases/graph2.txt
python cs412_mingraphcoloring_approx.py test_cases/graph3_nonoptimal.txt
echo "All test cases executed."
