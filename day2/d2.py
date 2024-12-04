import sys
    
def main():
    path = sys.argv[1] #input file. don't need argparse ArgumentParser and allat lol
    reports = read_input(path)
    count = 0
    for level in reports:
        if safe(level):
            count += 1
    print("# safe levels: ", count)                 

def read_input(path):
    with open(path, 'r') as file:
        return [line.split() for line in file]

def safe(level) -> bool:
    d = {True: 0, False: 0}
    for i in range(len(level)-1):
        j = i+1 
        diff = int(level[j]) - int(level[i])
        d[diff > 0] += 1
        if abs(diff) < 1 or abs(diff) > 3:
            return False #failed condition
    if 0 in d.values():
        return True #all (+) or (-)

if __name__ == "__main__":
    main()