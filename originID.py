import requests


# Refactored in case of integration with the NRU bot
def get_ids():
    ids = []
    filepath_in = "./ids.txt"
    try:
        file = open(filepath_in)
        for line in file.readlines():
            if not line.startswith('#'):
                ids.append(line.removesuffix('\n'))
    except FileNotFoundError:
        file = open(filepath_in, "w")
        file.write("#Start writing the ids to test below\n#Exemple :\nBelgobrine\nBelgrobrin")
    finally:
        return ids


# Refactored in case of integration with the NRU bot
def output(output_arr):
    filepath_out = "./out.txt"
    out = open(filepath_out, "a")
    out.writelines(output_arr)


# Refactored in case of integration with the NRU bot
def verify_ids():
    url = "https://signin.ea.com/p/ajax/user/checkOriginId?requestorId=portal&originId=@"
    out = []
    for id in get_ids():
        if not id.startswith('#'):
            json = requests.get(url.replace('@', id)).json()
            status = json["status"]
            message = json["message"]
            print(id, status, message)

            if status:
                out.append(id + " IS VALID\n")
            elif message == "origin_id_duplicated":
                out.append(id + " IS DUPLICATED\n")
            elif message == "origin_id_not_allowed":
                out.append(id + " IS NOT ALLOWED\n")
    output(out)


# Calling main function
verify_ids()
