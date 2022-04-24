import requests


# AUTHOR : Belgrobin/Belgobrine/florian-bougeatre

# Get ids from file
# If file not exist, create it
# Return ids array
def get_ids():
    filepath_in = "./ids.txt"
    try:
        ids = [line.removesuffix('\n') for line in open(filepath_in).readlines() if not line.startswith('#')]
    except FileNotFoundError:
        open(filepath_in, "w").write("#Start writing the ids to test below\n#Exemple :\nBelgobrine\nBelgrobrin")
        ids = [line.removesuffix('\n') for line in open(filepath_in).readlines() if not line.startswith('#')]
    finally:
        return ids


# Write the output array to file
def output(output_arr):
    filepath_out = "./out.txt"
    open(filepath_out, "a").writelines(output_arr)


# Iterate over ids array
# Verify the ids on Origin
# Write the result out array
def verify_ids(ids_arr):
    url = "https://signin.ea.com/p/ajax/user/checkOriginId?requestorId=portal&originId="
    out = []
    for id in ids_arr:
        json = requests.get(url + id).json()
        status, message = json["status"], json["message"]
        print(id, status, message)
        if status:
            out.append(f"{id} IS VALID\n")
        elif message == "origin_id_duplicated":
            out.append(f"{id} IS DUPLICATED\n")
        elif message == "origin_id_not_allowed":
            out.append(f"{id} IS NOT ALLOWED\n")
        else:
            out.append(f"{id} IS OTHER : {message}\n")
    return out


# Gets the ids
# Verify the ids
# Sends the results array to output function
output(verify_ids(get_ids()))
