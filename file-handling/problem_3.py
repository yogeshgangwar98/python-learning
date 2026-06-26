from constants import BASE_URL

def copy_file(source, destination):
    with open(source,"rb") as s_file, open(destination, "wb") as d_file:
        # for line in s_file:
        #     d_file.write(line)

        while chunk := s_file.read(4096): # reads only 4 kb at a time
            d_file.write(chunk)

copy_file(BASE_URL+"source.txt", BASE_URL+"destination.txt")

# := is walrus operator means chunk = s_file.read() and then return chunk