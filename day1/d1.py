import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="aoc input files")
    parser.add_argument('-f', '--file', help="input file", required=True)
    return parser.parse_args()
    
def main():
    args = parse_arguments()
    l1, l2 = read_input(args.file)
    
    sum = 0
    
    for a, b in zip(l1, l2):
        sum += abs(int(a)-int(b))  
    print(f"Sum is: {sum}")
    return 
    
def read_input(path):
    l1, l2 = [], [] #lists of location ids
    
    with open(path, 'r') as file:
        for line in file:
            stripped = line.split()
            l1.append(int(stripped[0]))
            l2.append(int(stripped[1]))
            
    return sorted(l1), sorted(l2)

if __name__ == '__main__':
    main()
    