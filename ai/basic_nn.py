import numpy as np
from scipy.io import loadmat
from sklearn.preprocessing import OneHotEncoder
from ai_log import logger


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def sigmoid_gradient(z):
    return sigmoid(z) * (1 - sigmoid(z))


def forward_propagate(a1, w1, w2, b1, b2):
    num = a1.shape[0]
    z1 = a1 @ w1.T + np.ones((num, 1)) * b1

    a2 = sigmoid(z1)
    z2 = a2 @ w2.T + np.ones((num, 1)) * b2

    h = sigmoid(z2)

    return z1, a2, z2, h


def cost(h, y):
    num = h.shape[0]
    J = 0
    for i in range(num):
        first_term = np.multiply(-y[i, :], np.log(h[i, :]))
        second_term = np.multiply((1 - y[i, :]), np.log(1 - h[i, :]))
        J += np.sum(first_term - second_term)

    J = J / num

    return J


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
    # print(f'accuracy = {accuracy * 100}%')


def back_propagate(a1, w1, w2, b1, b2, y, learning_rate):
    z1, a2, z2, h = forward_propagate(a1, w1, w2, b1, b2)
    num = a1.shape[0]
    delta_w1 = np.zeros(w1.shape)
    delta_w2 = np.zeros(w2.shape)
    delta_b1 = np.zeros(b1.shape)
    delta_b2 = np.zeros(b2.shape)

    for t in range(num):
        a1t = a1[t, :].reshape((1, -1))
        z1t = z1[t, :].reshape((1, -1))
        a2t = a2[t, :].reshape((1, -1))
        z2t = z2[t, :].reshape((1, -1))
        ht = h[t, :].reshape((1, -1))
        yt = y[t, :].reshape((1, -1))

        delta_z2 = (ht - yt) * sigmoid_gradient(z2t)
        delta_w2 = delta_w2 + (delta_z2.T * a2t)
        delta_b2 = delta_b2 + delta_z2

        delta_z1 = delta_z2 @ w2 * sigmoid_gradient(z1t)
        delta_w1 = delta_w1 + delta_z1.T * a1t
        delta_b1 = delta_b1 + delta_z1

    j = cost(h, y)
    delta_w1 = delta_w1 / num
    delta_w2 = delta_w2 / num
    delta_b1 = delta_b1 / num
    delta_b2 = delta_b2 / num

    return j, h, w1 - delta_w1 * learning_rate, w2 - delta_w2 * learning_rate, \
        b1 - delta_b1 * learning_rate, b2 - delta_b2 * learning_rate


if __name__ == '__main__':
    data = loadmat('./ex4data1.mat')

    a1_data = data['X']
    y_origin_data = data['y']
    print(f'a1_data type is {type(a1_data)}, a1_data.shape: {a1_data.shape}')
    print(f'y_origin_data type is {type(y_origin_data)}, y_origin_data.shape: {y_origin_data.shape}')

    encoder = OneHotEncoder(sparse_output=False)
    y_data = encoder.fit_transform(y_origin_data)
    print(f'y_data.shape: {y_data.shape}')
    print(f'y_origin_data[10]: {y_origin_data[10]}')
    print(f'y_data[10]: {y_data[10]}')

    # 初始化设置
    input_size = 400
    hidden_size = 25
    num_labels = 10
    learning_rate = 5

    weight1 = (np.random.random((hidden_size, input_size)) - 0.5) * 0.25
    bias1 = (np.random.random((1, hidden_size)) - 0.5) * 0.25
    weight2 = (np.random.random((num_labels, hidden_size)) - 0.5) * 0.25
    bias2 = (np.random.random((1, num_labels)) - 0.5) * 0.25

    for i in range(10001):
        j, h, weight1, weight2, bias1, bias2 = \
            back_propagate(a1_data, weight1, weight2, bias1, bias2, y_data, learning_rate)

        if i % 10 == 0:
            accuracy_rate = calculate_accuracy(h, y_origin_data)
            logger.info(f'iteration {i}, cost is {j} accuracy is {accuracy_rate * 100}%')
            # print(bias2)

