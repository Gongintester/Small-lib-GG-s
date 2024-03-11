'''
if __name__ == '__main__':

    import multiprocessing

    multiprocessing.freeze_support()
'''
#does not work this shit !

import json 
from utlixation_token import tokenize, stem, all_words_fun
import numpy
import os
import matplotlib.pyplot
from see import plot

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

from model import NeuralNet

with open("intents/intents.json", "r") as f:
    intinets = json.load(f)

#print(intinets) test

#Data for info
clear = lambda: os.system('cls')
version_program = 0.001

#Data fro ai 
all_words = []
tags = []
xy = []
for intinent in intinets['intemts']:
    tag = intinent ['tag']
    tags.append(tag)
    for pattern in intinent['patterns']:
        w = tokenize(pattern)
        all_words.extend(w) #Adding to all_words
        xy.append((w, tag))


ignore_words = ['?', '!', '.', ',']
all_words = [stem(w) for w in all_words if w not in ignore_words ] #Removing special symobls 
all_words = sorted(set(all_words)) #set is list where cant be any dublicate 
tags = sorted(set(tags))
#print(tags)

x_train = []
y_train = []

for (pattern_sentece, tag) in xy: #EIiR = Enter Information RUn
    bag = all_words_fun(pattern_sentece, all_words)
    x_train.append(bag)

    label = tags.index(tag) #Label is the number of tag in list of tags 
    y_train.append(label) #Adding tags to train data 
    #Cross Entropy Loss


x_train = numpy.array(x_train)
y_train = numpy.array(y_train)

class ChatDataSet(Dataset):
    def __init__(self):
        self.n_sample = len(x_train)
        self.x_data = x_train
        self.y_data = y_train

    #data set [idx]
    def __getitem__(self, index):
        return (self.x_data[index], self.y_data[index])
    
    def __len__(self):
        return self.n_sample
    
#Static Seters
dataset = ChatDataSet()

#HyoerSeters
batch_size = 16
learning_rate = 0.001
hidden_size = 16
output_size = len(tags)
input_size = len(x_train[0])
num_epochs = 30000
#maby someting other

#print(input_size, len(all_words))
#print(output_size, tags)

#File Sizes
#Train_Loder = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True)  
Train_Loder =  DataLoader(dataset = dataset, batch_size=batch_size, shuffle=True) #<-- remove this ) hif you want to # try to make this one work#, num_workers = 2)  

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = NeuralNet(input_size, hidden_size, output_size).to(device)

#loss and optimizer
creterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

#test
plot_scores = []
plot_mean_scores = []


clear() #Clear before function
#traning
for epoch in range(num_epochs):
    for (words, labels) in Train_Loder:
        words = words.to(device)
        labels = labels.to(device, dtype=torch.int64)

        # forward
        outputs = model(words)
        loss = creterion(outputs, labels)

        # backward and optimizer step  
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()


    

    if ( epoch + 1) % 100 == 0:
        clear()
        print(f'epoch {epoch+1}/{num_epochs}, loss={loss.item():.16f}')
        print(f'{loss.item():.16f}')
        plot_scores.append(epoch + 1)
        plot(plot_scores, plot_mean_scores)



        
        
print(f'final loss, loss={loss.item():.16f}')

data = {
    "model": model.state_dict(),                    #model c
    "model_version_program": version_program,       #model c
    "input_size": input_size,                       #neutral net
    "output_size": output_size,                     #neutral net
    "hidden_size": hidden_size,                     #neutral net
    "epoch": epoch,                                 #neutral net        
    "all_words": all_words,                         #data c
    "all_tags": tags                                #data c
}

FILE = "data.pth"
torch.save(data, FILE)
print(f"traning complete. file saved to {FILE}")
