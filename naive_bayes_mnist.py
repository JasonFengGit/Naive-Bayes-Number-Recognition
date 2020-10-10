import random
from collections import defaultdict

train_data = [list(map(int, line.strip().split(","))) for line in open("mnist_train.csv").read().strip().split("\n")]
train_data, validate_data = train_data[:50000], train_data[50000:]

def normalize(probs):
    sum_probs = sum(probs)
    if sum_probs == 0:
        return normalize([1 for each in probs])
    return [each/sum_probs for each in probs]

def normalize_dict(d):
    total = sum(d.values())
    for each in d:
        d[each] /= total
    return d

def train():
    # returns a belief
    prior = defaultdict(int)
    counter = {i: {x: [0, 0] for x in range(10)} for i in range(784)}
    for data in train_data:
        data = convert_data(data)
        label = data[0]
        pixels = data[1:]
        prior[label] += 1
        for i in range(len(pixels)):
            counter[i][label][pixels[i]] += 1
    prior = normalize_dict(prior)
    for i in range(784):
        for x in range(10):
            counter[i][x] = normalize(counter[i][x])
    return prior, counter

def argmax(l):
    maximum = 0
    result = None
    for i in range(len(l)):
        if l[i] > maximum:
            maximum = l[i]
            result = i
    return result

# data: 1D array of 28x28=784 grayscale pixels. Each pixel ranges from 0-255
# returns int
def predict(data):
    global belief, prior
    probs = [prior[x] for x in range(10)]
    data = convert_data(data)
    for i in range(len(data)):
        for x in range(10):
            probs[x] *= belief[i][x][data[i]]
        probs = normalize(probs)
    return argmax(probs)

def convert_data(data):
    return [data[0]] + [1 if each > 0 else 0 for each in data[1:]]

def convert_1d_2d(arr1d, col=28):
    result = []
    for start in range(0, len(arr1d), col):
        result.append(arr1d[start:start+col])
    return result

def show_image(pixels):
    pixels = convert_1d_2d(pixels)
    ASCII = " .:-=+*#%@"
    MAGIC = 256//len(ASCII)+1
    art = "\n".join(["".join([ASCII[item//MAGIC] for item in row]) for row in pixels])
    print(art)

def run_test(auto=False, no_graphics=False, validating=False):
    
    if validating:
        data = validate_data

    else:
        data = [list(map(int, line.strip().split(","))) for line in open("mnist_test.csv").read().strip().split("\n")]
    right = 0

    for i in range(len(data)):
        row = data[i]
        label = row[0]
        pixels = row[1:]
        prediction = predict(pixels)

        if label==prediction:
            right+=1

        print("NO.{}\npredict: {}\nactual: {}\naccumulative precision: {}".format(i, prediction, label, right/(i+1)))
        if not no_graphics: show_image(pixels)
        if not auto: input("press Enter to continue")

if __name__=="__main__":
    prior, belief = train()
    run_test(auto=False, no_graphics=False, validating=False)
