import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="aoc input files")
    parser.add_argument('-f', '--file', help="input file", required=True)
    return parser.parse_args()
    
def main():
    args = parse_arguments()
    l1, l2 = read_input(args.file)
    
    #--part 1--
    dist = 0
    for a, b in zip(l1, l2):
        dist += abs(int(a)-int(b))  
    print(f"Distance sum is: {dist}")
    
    #--part 2--
    hashmap = {int(k):0 for k in l1}
    for loc in l2:
        try:
            hashmap[int(loc)] += 1
        except KeyError: #not in l1
            continue
    
    total_similarity = sum(int(k) * int(v) for k, v in zip(hashmap.keys(), hashmap.values()))
    print("Total Similarity Score", total_similarity)
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
    