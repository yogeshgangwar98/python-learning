from constants import BASE_URL


def read_data(filename):
    with open(filename,"r") as file:
        # content = file.readlines()
        # lines = len(content)
        # words = sum(len(line.split()) for line in content)
        # character = sum(len(line) for line in content)

        content = file.read()
        lines = len(content.splitlines())
        words = len(content.split())
        character = len(content)
        return {"line":lines, "words":words, "character": character}

print(read_data(BASE_URL+"sample.txt"))