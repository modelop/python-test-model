#fastscore.schema.0: input_schema.avsc

#fastscore.schema.1: output_schema.avsc

import json
import math

print("Starting program", flush=True)

# add comments below
# comment 2024-01-17 22:16:05.278122
# added other commit
# second commit after reset
# commit after reset jp

#modelop.init
def begin():
    global coefs
    coefs = json.load(open('external_file_asset.json', 'r'))
    print("pass", flush=True)
    pass

#modelop.score
def action(datum):
    prediction = compute_prediction(datum)
    # a new comment
    print("Can you hear me now?", flush=True)
    yield prediction

def compute_prediction(datum):
    # commit after reset
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
