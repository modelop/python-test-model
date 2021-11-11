#fastscore.schema.0: input_schema.avsc

#fastscore.schema.1: output_schema.avsc

import json
import math

print("Starting program", flush=True)

#adding comment 11-10-2021 08:36pm MST
#adding comment 11-10-2021 09:10pm MST
#adding comment 11-10-2021 09:28pm MST
#adding comment 11-11-2021 10:24am MST
#adding comment 11-11-2021 02:43pm MST
#adding comment 11-11-2021 02:51pm MST
#adding comment 11-11-2021 03:06pm MST
#adding comment 11-11-2021 03:19pm MST
#adding comment 11-11-2021 03:28pm MST

#modelop.init
def begin():
    global coefs
    coefs = json.load(open('external_file_asset.json', 'r'))
    print("pass", flush=True)
    pass

#modelop.score
def action(datum):
    prediction = compute_prediction(datum)
    print("Can you hear me now?", flush=True)
    yield prediction

def compute_prediction(datum):
    x_score = coefs['x']*datum['x'] 
    y_score = coefs['y']*datum['y'] 
    prediction = x_score + y_score + coefs['intercept']
    return prediction

#modelop.metrics
def metrics(data):
    actuals = data.z.tolist()
    data = data.to_dict(orient='records')
    predictions = list(map(compute_prediction, data))
    diffs = [x[0] - x[1] for x in zip(actuals, predictions)]
    rmse = math.sqrt(sum(list(map(lambda x: x**2, diffs)))/len(diffs))
    mae = sum(list(map(abs, diffs)))/len(diffs)
    yield dict(MAE=mae, RMSE=rmse)

