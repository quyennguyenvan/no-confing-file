import json

#load from source repo
# data_key = json.load(open("config.json"))["data_key"]

#load from docker volume mount:

data_key = json.load(open("/config/config.json"))["data_key"]

if __name__ == "__main__":

    print(data_key)
    # while True:
        # print("helo")