import datetime
import json
import numpy
import sys

# Parse the arguments - must be a json dict object
args = mldb.script.args
if type(args) != dict and not (type(args) == list and len(args) == 0):
    print "The current arguments are: ", args
    print
    print "Usage is %%mldb py <gist://rest of the gist_url> {json with the params}"
    print "The parameter fields are:"
    print '    "id":   str (default value = "2d_problem")'
    print '    "size": int (default value = 2000)'
    sys.exit(1)

# 1. Data set name
try:
    id_ds = str(mldb.script.args['id'])
except:
    print 'Missing "id" field, using default value "2d_problem"'
    id_ds = "2d_problem"
    
# 2. Number of samples (default = 2000)
try:
    size_ds = int(mldb.script.args['size'])
except:
    print 'Missing "size" field, using default value 2000'
    size_ds = 2000

print
print "Parameters used:"
print "    ID:  ", id_ds
print "    Size:", size_ds, "samples"

# Get the config of the data set
datasetConfig = {
        "type": "mutable",
        "id": id_ds
    }
dataset = mldb.create_dataset(datasetConfig)

# Record the rows
ts = datetime.datetime.now()
for i in range(0, size_ds):
    an_id = 'id_' + str(i)
    offset = float(i%2) / 2
    x, y = numpy.random.normal(0.25 + offset, 0.25, 2)
    features = [['x', x, ts], ['y', y, ts], ['label', str(i%2), ts]]
    dataset.record_row(an_id, features)

# commit the dataset
dataset.commit()
