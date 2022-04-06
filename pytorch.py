import torch
import pandas as pd

x = torch.rand(1234, 123456)
y = torch.rand(1234, 123456)
y.add_(x)
print(x)
print(y)
g = pd.DataFrame(y)
cities = pd.DataFrame(g, columns=['State'])
cities.to_csv('cities.csv')