import torch
import matplotlib.pyplot as plt
import os

# img = plt.imread(
#     'C:\\AI_Study\\YAI\\ToyProject\\datasets\\monet2photo\\trainA\\00001.jpg')

# train_monet = os.listdir(
#     'C:\\AI_Study\\YAI\\ToyProject\\datasets\\monet2photo\\trainA')
# train_photo = os.listdir(
#     'C:\\AI_Study\\YAI\\ToyProject\\datasets\\monet2photo\\trainB')
# test_monet = os.listdir(
#     'C:\\AI_Study\\YAI\\ToyProject\\datasets\\monet2photo\\testA')
# test_photo = os.listdir(
#     'C:\\AI_Study\\YAI\\ToyProject\\datasets\\monet2photo\\testB')


# print('train_monet:', len(train_monet))
# print('train_photo:', len(train_photo))
# print('test_monet:', len(test_monet))
# print('test_photo:', len(test_photo))

# print(len(train_monet) / len(test_monet))
# print(len(train_photo) / len(test_photo))

print(torch.cuda.is_available())
