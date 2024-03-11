import torch
import torch.nn as nn
import torch.optim as optim

# Dane treningowe
x_train = torch.tensor([[1.0], [2.0], [3.0]])
y_train = torch.tensor([[2.0], [4.0], [6.0]])

# Model
class LinearRegressionModel(nn.Module):
    def __init__(self):
        super(LinearRegressionModel, self).__init__()
        self.linear = nn.Linear(1, 1)  # 1 wejście, 1 wyjście

    def forward(self, x):
        return self.linear(x)

model = LinearRegressionModel()

# Funkcja straty i optymalizator
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Trening modelu
epochs = 1000
for epoch in range(epochs):
    # Czyszczenie gradientów
    optimizer.zero_grad()

    # Przewidywanie
    y_pred = model(x_train)

    # Obliczanie straty
    loss = criterion(y_pred, y_train)

    # Wsteczna propagacja i aktualizacja wag
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 100 == 0:
        print(f'Epoch {epoch+1}/{epochs}, Loss: {loss.item()}')

# Testowanie modelu
x_test = torch.tensor([[4.0]])
predicted = model(x_test)
print(f'Przewidywana wartość dla x=4: {predicted.item()}')