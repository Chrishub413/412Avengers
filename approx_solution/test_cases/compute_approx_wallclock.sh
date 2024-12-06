#!/bin/bash

# Directory containing the script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Run the runtime analysis
echo "Running runtime analysis..."
python "${DIR}/../runtime_analysis.py"

echo "Analysis complete!"
echo "Check the analysis_results directory for the runtime comparison plot"