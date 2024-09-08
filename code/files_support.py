def read_tuples_from_file(file_path):
    tuples_set = set()
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 2:
                try:
                    num1 = int(parts[0])
                    num2 = int(parts[1])
                    tuples_set.add((num1, num2))
                except ValueError:
                    print(f"Skipping line due to non-integer values: {line.strip()}")
            else:
                print(f"Skipping line due to too many values: {line.strip()}")    
    return tuples_set

def write_tuples_to_file(tuples_set, file_path):
    with open(file_path, 'w') as file:
        for t in tuples_set:
            file.write(f"{t[0]},{t[1]}\n")

def file_exists(file_path):
    try:
        with open(file_path, 'r'):
            return True
    except FileNotFoundError:
        return False