import requests
# golbal variables
api_key = "RGAPI-3d99aa08-0398-4ce2-9937-3fb0459298b6"


def summoner_data(region, summoner_name, API_key):
    URL = "https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={API_key}".format(
        region=region, summoner_name=summoner_name, API_key=api_key)

    response = requests.get(URL)
    return response.json()


summoner_info = summoner_data("na1", "SWWHYY", api_key)
print(summoner_info)


def summoner_rank(region, id, API_key):
    id = "Yyjj6n0R1NB_NtlkAXX5QCRnVrAm5t7DbiRX_vYF2099lJHw"
    URL = "https://{region}.api.riotgames.com/lol/league/v4/entries/by-summoner/{id}?api_key={API_key}".format(
        region=region, id=id, API_key=api_key)
    response = requests.get(URL)
    return response.json()


summoner_rank_info = summoner_rank("na1", id, api_key)
print(summoner_rank_info)


# def matches(region, id, )
