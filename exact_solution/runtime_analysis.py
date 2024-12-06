import matplotlib.pyplot as plt
import subprocess
import time
import os
import numpy as np


def run_algorithm(input_file):
    """Run exact algorithm and measure its execution time"""
    try:
        start_time = time.time()
        process = subprocess.run(['python', 'cs412_mingraphcolor_exact_file.py', input_file],
                                 capture_output=True, text=True)
        end_time = time.time()
        execution_time = end_time - start_time

        if process.returncode == 0:
            return execution_time
        else:
            print(f"Error running algorithm: {process.stderr}")
            return None

    except Exception as e:
        print(f"Error running on {input_file}: {e}")
        return None


def analyze_runtimes():
    # Create required directories
    script_dir = os.path.dirname(os.path.abspath(__file__))
    test_cases_dir = os.path.join(script_dir, "test_cases")
    output_dir = os.path.join(script_dir, "analysis_results")
    os.makedirs(output_dir, exist_ok=True)

    # Define test cases using your existing files
    test_files = [
        "graph_small.txt",
        "graph_medium.txt",
        "large_graph2.txt"  # Excluding graph_large.txt as it might take too long
    ]

    results = {"sizes": [], "times": [], "details": []}

    def get_graph_size(file_path):
        try:
            with open(file_path, 'r') as f:
                edges = int(f.readline().strip())
                vertices = set()
                for _ in range(edges):
                    u, v = f.readline().strip().split()
                    vertices.add(u)
                    vertices.add(v)
            return len(vertices)
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")
            return None

    # Run tests and collect data
    for file in test_files:
        file_path = os.path.join(test_cases_dir, file)
        print(f"\nTesting graph: {file}")

        graph_size = get_graph_size(file_path)
        if graph_size is None:
            continue

        print(f"Graph size: {graph_size} vertices")

        # Run multiple times for better average
        num_runs = 3
        times = []
        for i in range(num_runs):
            print(f"Run {i + 1}/{num_runs}...")
            runtime = run_algorithm(file_path)
            if runtime is not None:
                times.append(runtime)

        if times:
            avg_time = sum(times) / len(times)
            results["sizes"].append(graph_size)
            results["times"].append(avg_time)
            results["details"].append(file)
            print(f"Average time: {avg_time:.4f} seconds")

    # Create runtime plot
    if results["sizes"]:
        plt.figure(figsize=(10, 6))
        plt.scatter(results["sizes"], results["times"], marker='o', color='red', s=100)

        # Add trend line
        if len(results["times"]) > 1:
            z = np.polyfit(results["sizes"], results["times"], 2)
            p = np.poly1d(z)
            x = np.linspace(min(results["sizes"]), max(results["sizes"]), 100)
            plt.plot(x, p(x), 'r--', alpha=0.5, label='Trend (Polynomial)')

        plt.xlabel('Number of Vertices', fontsize=12)
        plt.ylabel('Runtime (seconds)', fontsize=12)
        plt.title('Exact Solution Runtime Analysis', fontsize=14)
        plt.legend(fontsize=10)
        plt.grid(True, alpha=0.3)
        plt.yscale('log')

        plot_path = os.path.join(output_dir, 'runtime_comparison.png')
        plt.savefig(plot_path, dpi=300, bbox_inches='tight')
        plt.close()

        # Print results
        print("\nRuntime Analysis Results:")
        print("========================")
        for i in range(len(results["sizes"])):
            print(f"{results['details'][i]}: {results['times'][i]:.4f}s ({results['sizes'][i]} vertices)")

        print(f"\nPlot saved to: {plot_path}")
    else:
        print("\nNo data collected to create plot!")


if __name__ == "__main__":
    analyze_runtimes()