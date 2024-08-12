import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from scipy.io import loadmat
from sklearn.preprocessing import OneHotEncoder

# 设定随机种子以保证结果可复现
torch.manual_seed(42)


# 定义模型
class NumberNet(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(NumberNet, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)  # 第一层全连接层
        self.relu = nn.ReLU()  # ReLU 激活函数
        self.fc2 = nn.Linear(hidden_size, output_size)  # 第二层全连接层

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x


def calculate_accuracy(nn_pred, y):
    y_pred = np.array(np.argmax(nn_pred, axis=1) + 1)
    # print(y_pred.shape)
    y = y.ravel()
    # print(y.shape)

    # 使用 == 运算符进行逐元素比较
    comparison_result = (y_pred == y)

    # 将布尔值转换为整数 (True -> 1, False -> 0)
    result = comparison_result.astype(int)

    accuracy = float(np.sum(result)) / float(result.shape[0])
    return accuracy


if __name__ == '__main__':
    data = loadmat('./ex4data1.mat')
    a1_data = data['X']
    a1_tensor = torch.from_numpy(a1_data).float()
    y_origin_data = data['y']
    print(f'a1_data type is {type(a1_data)}, a1_data.shape: {a1_data.shape}')
    print(f'y_origin_data type is {type(y_origin_data)}, y_origin_data.shape: {y_origin_data.shape}')

    encoder = OneHotEncoder(sparse_output=False)
    y_data = encoder.fit_transform(y_origin_data)
    y_tensor = torch.from_numpy(y_data).float()
    print(f'y_data.shape: {y_data.shape}')
    print(f'y_origin_data[10]: {y_origin_data[10]}')
    print(f'y_data[10]: {y_data[10]}')

    # 初始化设置
    input_size = 400
    hidden_size = 25
    num_labels = 10
    output_size = 10  # 输出类别数
    learning_rate = 1  # 学习率
    num_epochs = 1000

    # 创建模型实例
    model = NumberNet(input_size, hidden_size, output_size)

    # 定义损失函数和优化器
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=learning_rate)

    # 训练模型
    for epoch in range(num_epochs):
        # 前向传播
        outputs = model(a1_tensor)

        # 计算损失
        loss = criterion(outputs, y_tensor)

        # 反向传播
        optimizer.zero_grad()
        loss.backward()

        # 更新权重
        optimizer.step()

        if (epoch + 1) % 10 == 0:
            accuracy_rate = calculate_accuracy(outputs.detach().numpy(), y_origin_data)
            print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}, Accuracy is {accuracy_rate * 100}%')

    print('Training finished.')



