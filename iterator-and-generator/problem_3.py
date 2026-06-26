def read_large_file(filename):
    with open(filename, "r") as file:
        for line in file: # loads line by line
            yield line
        
        # yield from file #shorter version of reading line by line

        # for rl in file.readlines(): #this loads the entire file
        #     yield rl

for line in read_large_file("Iterator and Generator/sample.txt"):
    print(line)