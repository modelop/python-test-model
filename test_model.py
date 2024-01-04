#fastscore.schema.0: input_schema.avsc

#fastscore.schema.1: output_schema.avsc

import json
import math

print("Starting program", flush=True)

# add comments below
# comment 2024-01-04 22:15:09.616119
# comment 2024-01-03 22:14:08.357225
# comment 2024-01-02 22:15:18.610725
# comment 2023-12-21 22:53:22.397632
# comment 2023-12-20 22:15:37.947909
# comment 2023-12-19 22:15:33.885130

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
