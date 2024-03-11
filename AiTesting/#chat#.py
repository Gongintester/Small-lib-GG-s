import random
import json 
import torch
from model import NeuralNet
from utlixation_token import all_words_fun, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open("intents/intents.json", "r") as f:
    intinets = json.load(f)

FILE = "data.pth"
data = torch.load("data.pth")

input_size = data["input_size"]
output_size = data["output_size"]         
hidden_size = data["hidden_size"]
all_words = data["all_words"]
all_tags = data["all_tags"]
model = data["model"]


model_working = NeuralNet(input_size, hidden_size, output_size).to(device)
model_working.load_state_dict(model)
model_working.eval()

NameBot = "Atlas"
print("I am " + NameBot)
print("#-->Stop to Exit<--#")


while True:
    message = input("Me: ")
    if message == "Stop":
        break

    message = tokenize(message)
    Use = all_words_fun(message, all_words)
    Use = Use.reshape(1, Use.shape[0])
    Use = torch.from_numpy(Use).to(device)

    output = model_working(Use).to(device)
    #output.load_state_dict(torch.load('data.pth'))# 
    _, predicted = torch.max(output, dim=1)
    tag = all_tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.05:
        for intinet in intinets["intemts"]:
            if tag == intinet["tag"]:
                print(f"{NameBot}: {random.choice(intinet['responses'])}")
    else:
        print(f'{NameBot}: I do not understand THIS SHIT...')