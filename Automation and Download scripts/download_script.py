import multiprocessing
import urllib.request

# --- Function Definitions ---

def perform_calculation(operation, a, b):
    """Performs basic math operations."""
    if operation == 'add':
        result = a + b
    elif operation == 'subtract':
        result = a - b
    elif operation == 'multiply':
        result = a * b
    elif operation == 'divide':
        if b != 0:
            result = a / b
        else:
            result = "Cannot divide by zero"
    else:
        result = "Invalid operation"
    
    print(f"Calc: {operation}({a}, {b}) = {result}")

def download_file(url, save_path):
    """Downloads a file from a URL."""
    try:
        urllib.request.urlretrieve(url, save_path)
        print(f"Downloaded: {url} -> {save_path}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

# --- Main Execution Block ---

if __name__ == "__main__":
    # 1. Setup Data for Calculations
    ops = ['add', 'subtract', 'multiply', 'divide']
    calc_values = [(10, 5), (15, 7), (8, 4), (12, 0)]
    
    # 2. Setup Data for Downloads
    urls = [
        "https://dox.abv.bg/download?id=363a4eca2e",
        "https://dox.abv.bg/download?id=968be12ebd",
        "https://dox.abv.bg/download?id=8411610d87"
    ]
    save_paths = ["file1.pdf", "file2.pdf", "file3.pdf"]

    processes = []

    print("--- Starting Calculations ---")
    for operation, (a, b) in zip(ops, calc_values):
        p = multiprocessing.Process(target=perform_calculation, args=(operation, a, b))
        processes.append(p)
        p.start()

    print("\n--- Starting Downloads ---")
    for url, path in zip(urls, save_paths):
        p = multiprocessing.Process(target=download_file, args=(url, path))
        processes.append(p)
        p.start()

    # Wait for all processes (both math and downloads) to finish
    for p in processes:
        p.join()

    print("\nAll tasks (calculations and downloads) completed.")