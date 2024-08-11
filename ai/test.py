from sklearn.preprocessing import OneHotEncoder
import numpy as np


def test_oneshot():
    # 创建一个示例数据集
    data = np.array([
        [5],
        [7],
        [1],
        [3],
        [2],
        [1]
    ])

    # 初始化 OneHotEncoder
    encoder = OneHotEncoder(sparse_output=False)  # 设置 sparse_output=False 以获得 NumPy 数组而不是稀疏矩阵

    # 拟合并转换数据
    encoded_data = encoder.fit_transform(data)

    # 打印编码后的数据
    print("Encoded Data:")
    print(encoded_data)


def test_array():
    a = np.ones((1, 2))
    print()
    print(a)
    b = np.ones((2, 1)) * np.array([2, 3])
    print(b)

    c = np.zeros(b.shape)
    print(c)


def test_random():
    a = np.random.random((2, 3))
    print()
    print(a)
    print(a.shape)
    print(a.ravel())
    print(a.ravel().shape)


def test_compare_ndarray():
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([1, 2, 6, 4, 7])

    print(type(arr1))
    print(type(arr2))
    print(arr1.shape)
    print(arr2.shape)
    # 使用 == 运算符进行逐元素比较
    comparison_result = (arr1 == arr2)

    # 将布尔值转换为整数 (True -> 1, False -> 0)
    result = comparison_result.astype(int)

    print(result)

    accuracy = np.sum(result) / result.shape[0]
    print(accuracy)
