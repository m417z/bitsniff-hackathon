import numpy as np
import math

k_fakes_num = 1000

# Return the similarity score for two time-series
def similarity(a, b):
    # return np.corrcoef(a, b)
    return np.trapz(a * b)

# Generate fake block time-series of given length
def generateFake(length):
    return np.zeros(length)

# Create bell shapes around blocks
def shapePredict(data):
    return data
    
# Calculate the probability of detection (in units of std)
def detect(traffic, blocks):
    if len(traffic) != len(block):
        print('Error: traffic/blocks length mismatch')
        return
    length = len(traffic)

    fake_results = np.zeros(k_fakes_num)
    for i in range(k_fakes_num):
        fake = generateFake(length)
        fake_results[i] = similarity(traffic, shapePredict(fake))

    real_result = similarity(traffic, shapePredict(blocks))

    fake_mean = np.mean(fake_results)
    fake_std = np.mean(fake_results)

    return (real_result - fake_mean) / fake_std