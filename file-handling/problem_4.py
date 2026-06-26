from constants import BASE_URL

def log_analyzer(filename):
    with open(filename,"r") as file:
        return_dict = {"INFO": 0,"ERROR": 0,"WARNING": 0,"error_messages": []}
        for line in file:
            split_word = line.split(':', 1)
            logger = split_word[0]
            return_dict[logger] += 1

            if logger == "ERROR":
                return_dict["error_messages"].append(split_word[1].strip()) # .strip() here removes spaces and \n

        return return_dict

print(log_analyzer(BASE_URL+"sample.log"))