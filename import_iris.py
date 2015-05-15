import requests
import datetime

datasetConfig = {
        "type": "beh.mutable",
        "id": "iris_dataset"
    }

dataset = mldb.create_dataset(datasetConfig)
ts = datetime.datetime.now().isoformat(' ')

response = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
split = response.content.decode('utf-8').split('\n')

for i, line in enumerate(split):
    cols = []
    line_split = line.split(',')
    if len(line_split) != 5:
        continue
    cols.append(["sepal length", float(line_split[0]), ts])
    cols.append(["sepal width", float(line_split[1]), ts])
    cols.append(["petal length", float(line_split[2]), ts])
    cols.append(["petal width", float(line_split[3]), ts])
    cols.append(["class", line_split[4], ts])
    dataset.record_row(str(i+1), cols)

dataset.commit()
