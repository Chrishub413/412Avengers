import matplotlib.pyplot as plt
import subprocess
import time
import os
import numpy as np

def run_algorithm(algorithm_path, input_file):
    """Run algorithm and measure its execution time"""
    try:
        start_time = time.time()
        process = subprocess.run(['python', algorithm_path, input_file],
                               capture_output=True, text=True)
        end_time = time.time()
        execution_time = end_time - start_time

        # Check if the program executed successfully
        if process.returncode == 0:
            return execution_time
        else:
            print(f"Error running algorithm: {process.stderr}")
            return None

    except Exception as e:
        print(f"Error running {algorithm_path} on {input_file}: {e}")
        return None

def analyze_runtimes():
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
        ],
        "large": [
            os.path.join(comparison_dir, "large_optimal.txt"),
            os.path.join(comparison_dir, "large_nonoptimal.txt")
        ]
    }

    results = {
        "exact": {"sizes": [], "times": [], "details": []},
        "approx": {"sizes": [], "times": [], "details": []}
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
            print(f"\nTesting {size} graph: {file_name}")

            graph_size = get_graph_size(file)
            if graph_size is None:
                continue

            print(f"Graph size: {graph_size} vertices")

            # Run approximation algorithm for all sizes
            print("Running approximation algorithm...")
            approx_time = run_algorithm(approx_path, file)
            if approx_time is not None:
                results["approx"]["sizes"].append(graph_size)
                results["approx"]["times"].append(approx_time)
                results["approx"]["details"].append(f"{size}_{file_name}")
                print(f"Approximation time: {approx_time:.4f} seconds")

            # Run exact algorithm only for small and medium sizes
            if size != "large":
                print("Running exact algorithm...")
                num_runs = 3
                times = []
                for i in range(num_runs):
                    print(f"Run {i+1}/{num_runs}...")
                    exact_time = run_algorithm(exact_path, file)
                    if exact_time is not None:
                        times.append(exact_time)

                if times:
                    avg_time = sum(times) / len(times)
                    results["exact"]["sizes"].append(graph_size)
                    results["exact"]["times"].append(avg_time)
                    results["exact"]["details"].append(f"{size}_{file_name}")
                    print(f"Exact time (average of {num_runs} runs): {avg_time:.4f} seconds")

    # Create runtime comparison plot
    if results["approx"]["sizes"]:  # Only require approximation results to create plot
        plt.figure(figsize=(12, 8))

        # Plot exact solution data if available
        if results["exact"]["sizes"]:
            plt.scatter(results["exact"]["sizes"], results["exact"]["times"],
                      label='Exact Solution', marker='o', color='red', s=100)

            # Add trend line for exact solution if we have multiple points
            if len(results["exact"]["times"]) > 1:
                z_exact = np.polyfit(results["exact"]["sizes"], results["exact"]["times"], 2)
                p_exact = np.poly1d(z_exact)
                x_exact = np.linspace(min(results["exact"]["sizes"]), max(results["exact"]["sizes"]), 100)
                plt.plot(x_exact, p_exact(x_exact), 'r--', alpha=0.5,
                        label='Exact Trend (Polynomial)')

        # Plot approximation data
        plt.scatter(results["approx"]["sizes"], results["approx"]["times"],
                   label='Approximation', marker='s', color='blue', s=100)

        # Add trend line for approximation
        if len(results["approx"]["times"]) > 1:
            z_approx = np.polyfit(results["approx"]["sizes"], results["approx"]["times"], 1)
            p_approx = np.poly1d(z_approx)
            x_approx = np.linspace(min(results["approx"]["sizes"]), max(results["approx"]["sizes"]), 100)
            plt.plot(x_approx, p_approx(x_approx), 'b--', alpha=0.5,
                    label='Approximation Trend (Linear)')

        plt.xlabel('Number of Vertices', fontsize=12)
        plt.ylabel('Runtime (seconds)', fontsize=12)
        plt.title('Runtime Comparison: Exact vs Approximation Solution', fontsize=14)
        plt.legend(fontsize=10)
        plt.grid(True, alpha=0.3)

        # Add log scale for better visualization
        plt.yscale('log')

        plot_path = os.path.join(output_dir, 'runtime_comparison.png')
        plt.savefig(plot_path, dpi=300, bbox_inches='tight')
        plt.close()

        # Print results
        print("\nRuntime Analysis Results:")
        print("========================")

        if results["exact"]["sizes"]:
            print("\nExact Solution:")
            for i in range(len(results["exact"]["sizes"])):
                print(f"{results['exact']['details'][i]}: {results['exact']['times'][i]:.4f}s ({results['exact']['sizes'][i]} vertices)")

        print("\nApproximation Solution:")
        for i in range(len(results["approx"]["sizes"])):
            print(f"{results['approx']['details'][i]}: {results['approx']['times'][i]:.4f}s ({results['approx']['sizes'][i]} vertices)")

        print(f"\nPlot saved to: {plot_path}")
    else:
        print("\nNo data collected to create plot!")

if __name__ == "__main__":
    analyze_runtimes()