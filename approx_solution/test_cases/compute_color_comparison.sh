#!/bin/bash

# Directory containing the script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Run the value analysis
echo "Running color value analysis..."
python "${DIR}/../analyze_values.py"

echo "Analysis complete!"
echo "Check the analysis_results directory for the color comparison plot"