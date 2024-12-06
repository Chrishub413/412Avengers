import matplotlib.pyplot as plt
import subprocess
import os
import numpy as np

def run_algorithm_for_value(algorithm_path, input_file):
    """Run algorithm and get the chromatic number"""
    try:
        process = subprocess.run(['python', algorithm_path, input_file],
                               capture_output=True, text=True)
        if process.returncode == 0:
            # First line of output contains the chromatic number
            return int(process.stdout.split('\n')[0])
        else:
            print(f"Error running algorithm: {process.stderr}")
            return None
    except Exception as e:
        print(f"Error running {algorithm_path} on {input_file}: {e}")
        return None

def analyze_values():
    # Get the directory paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)
    comparison_dir = os.path.join(script_dir, "test_cases", "comparison")

    # Define paths
    exact_path = os.path.join(project_dir, "exact_solution", "exact.py")
    approx_path = os.path.join(script_dir, "cs412_mingraphcoloring_approx.py")

    # Create analysis_results directory if it doesn't exist
    output_dir = os.path.join(script_dir, "analysis_results")
    os.makedirs(output_dir, exist_ok=True)

    # Test cases from comparison directory
    test_cases = {
        "small": [
            os.path.join(comparison_dir, "small_optimal.txt"),
            os.path.join(comparison_dir, "small_nonoptimal.txt")
        ],
        "medium": [
            os.path.join(comparison_dir, "medium_optimal.txt"),
            os.path.join(comparison_dir, "medium_nonoptimal.txt")
        ]
    }

    results = {
        "exact": {"sizes": [], "colors": [], "details": []},
        "approx": {"sizes": [], "colors": [], "details": []}
    }

    def get_graph_size(file_path):
        try:
            with open(file_path, 'r') as f:
                edges = int(f.readline().strip())
                vertices = set()
                for _ in range(edges):
                    u, v = map(int, f.readline().strip().split())
                    vertices.add(u)
                    vertices.add(v)
            return len(vertices)
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")
            return None

    # Run tests and collect data
    for size, files in test_cases.items():
        for file in files:
            file_name = os.path.basename(file)
            print(f"\nAnalyzing {size} graph: {file_name}")

            graph_size = get_graph_size(file)
            if graph_size is None:
                continue

            print(f"Graph size: {graph_size} vertices")

            # Get approximation solution value
            print("Running approximation algorithm...")
            approx_colors = run_algorithm_for_value(approx_path, file)
            if approx_colors is not None:
                results["approx"]["sizes"].append(graph_size)
                results["approx"]["colors"].append(approx_colors)
                results["approx"]["details"].append(f"{size}_{file_name}")
                print(f"Approximation colors: {approx_colors}")

            # Get exact solution value
            print("Running exact algorithm...")
            exact_colors = run_algorithm_for_value(exact_path, file)
            if exact_colors is not None:
                results["exact"]["sizes"].append(graph_size)
                results["exact"]["colors"].append(exact_colors)
                results["exact"]["details"].append(f"{size}_{file_name}")
                print(f"Exact colors: {exact_colors}")

    # Create value comparison plot
    if results["approx"]["sizes"] and results["exact"]["sizes"]:
        plt.figure(figsize=(12, 8))

        # Calculate approximation ratios
        ratios = []
        for i in range(len(results["approx"]["sizes"])):
            if i < len(results["exact"]["colors"]):
                ratio = results["approx"]["colors"][i] / results["exact"]["colors"][i]
                ratios.append(ratio)
                print(f"\nGraph: {results['approx']['details'][i]}")
                print(f"Approximation ratio: {ratio:.2f}")
                print(f"Exact colors: {results['exact']['colors'][i]}")
                print(f"Approx colors: {results['approx']['colors'][i]}")

        # Create bar plot
        x = range(len(results["exact"]["sizes"]))
        width = 0.35

        plt.bar([i - width/2 for i in x], results["exact"]["colors"], width,
                label='Exact Solution', color='red', alpha=0.7)
        plt.bar([i + width/2 for i in x], results["approx"]["colors"][:len(results["exact"]["sizes"])],
                width, label='Approximation', color='blue', alpha=0.7)

        # Add value labels on bars
        for i in x:
            plt.text(i - width/2, results["exact"]["colors"][i], str(results["exact"]["colors"][i]),
                    ha='center', va='bottom')
            plt.text(i + width/2, results["approx"]["colors"][i], str(results["approx"]["colors"][i]),
                    ha='center', va='bottom')

        plt.xlabel('Test Cases', fontsize=12)
        plt.ylabel('Number of Colors Used', fontsize=12)
        plt.title('Color Usage Comparison: Exact vs Approximation Solution', fontsize=14)
        plt.legend(fontsize=10)
        plt.grid(True, alpha=0.3)

        # Set x-axis labels
        plt.xticks([i for i in x], [f"{case.split('_')[0]}\n{case.split('_')[1]}"
                                   for case in results["exact"]["details"]], rotation=0)

        # Add ratio text
        avg_ratio = sum(ratios) / len(ratios)
        plt.text(0.02, 0.98, f'Average approximation ratio: {avg_ratio:.2f}',
                transform=plt.gca().transAxes, fontsize=10,
                verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

        plot_path = os.path.join(output_dir, 'color_comparison.png')
        plt.savefig(plot_path, dpi=300, bbox_inches='tight')
        plt.close()

        print(f"\nPlot saved to: {plot_path}")
        print(f"Average approximation ratio: {avg_ratio:.2f}")
    else:
        print("\nInsufficient data to create plot!")

if __name__ == "__main__":
    analyze_values()