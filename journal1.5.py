import numpy as np 

def generate_table(start, end, num_entries):
    step_size = (end - start) / (num_entries - 1)
    
    # Print table header
    print(f"{'x':<10}{'sin(x)':<10}")
    
    # Generate and print table entries
    for i in range(num_entries):
        x = start + i * step_size
        sin_x = np.sin(x)
        print(f"{x:<10.4f}{sin_x:<10.4f}")

def main():     #Define main program
    start_value = 0
    end_value = 2
    num_entries = 1000
    
    generate_table(start_value, end_value, num_entries)

#if the main program exists, run it
if __name__ == "__main__":
    main()
