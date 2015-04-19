import datetime
mldb_url = "http://localhost:80"
rest_root = mldb_url + "/v1"
datasetConfig = {
        "type": "mutable",
        "id": "superheroes_and_villains",
        "address": "superheroes_and_villains.beh.gz"
    }

dataset = mldb.create_dataset(datasetConfig)
ts = datetime.datetime.now().isoformat(' ')
def record(name, **kwargs):
    global ts
    global dataset
    cols = []
    for key, val in kwargs.items():
        cols.append([key, val, ts])

    dataset.record_row(name, cols)

record("Zatanna", Gender="Female", Height=67, Weight=127, Eyes="Blue", Hair="Black", Good=True, Bad=False)
record("Nightwing", Gender="Male", Height=70, Weight=175, Eyes="Blue", Hair="Black", Good=True, Bad=False)
record("Batman", Gender="Male", Height=74, Weight=210, Eyes="Blue", Hair="Black", Good=True, Bad=False)
record("Green Lantern", Gender="Male", Height=72, Weight=200, Eyes="Brown", Hair="Brown", Good=True, Bad=False)
record("Superman", Gender="Male", Height=75, Weight=235, Eyes="Blue", Hair="Black", Good=True, Bad=False)
record("The Flash", Gender="Male", Height=72, Weight=195, Eyes="Blue", Hair="Blond", Good=True, Bad=False)
record("Aquaman", Gender="Male", Height=73, Weight=325, Eyes="Blue", Hair="Blond", Good=True, Bad=False)
record("Catwoman", Gender="Female", Height=67, Weight=133, Eyes="Green", Hair="Black", Good=True, Bad=True)
record("Wonder Woman", Gender="Female", Height=72, Weight=130, Eyes="Blue", Hair="Black", Good=True, Bad=False)
record("The Joker", Gender="Male", Height=72, Weight=160, Eyes="Green", Hair="Green", Skin="White", Good=False, Bad=True)
record("Harley Quinn", Gender="Female", Height=67, Weight=140, Eyes="Blue", Hair="Blond", Good=False, Bad=True)
record("Power Girl", Gender="Female", Height=71, Weight=180, Eyes="Blue", Hair="Blond", Good=True, Bad=False)
record("Supergirl", Gender="Female", Height=65, Weight=135, Eyes="Blue", Hair="Blond", Good=True, Bad=False)
record("Batwoman", Gender="Female", Height=66, Weight=123, Eyes="Blue", Hair="Black", Good=True, Bad=False)
record("Oracle", Gender="Female", Height=67, Weight=126, Eyes="Blue", Hair="Red", Good=True, Bad=False)
record("Black Canary", Gender="Female", Height=67, Weight=130, Eyes="Blue", Hair="Blond", Good=True, Bad=False)

dataset.commit()