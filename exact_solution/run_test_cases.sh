echo "Running graph coloring on all test cases..."

python3 cs412_mingraphcolor_exact.py test_cases/graph_small.txt
python3 cs412_mingraphcolor_exact.py test_cases/graph_medium.txt

python3 cs412_mingraphcolor_exact.py test_cases/graph_large.txt

echo "All test cases executed."