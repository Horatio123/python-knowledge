import numpy as np
from scipy.spatial.transform import Rotation

def test_numpy():
    a = np.array([1, 2, 3])
    print(a.shape)

def test_numpy_shape():
    a = np.array([[1, 2, 3], [4, 5, 6]])
    b = np.array([1, 2, 3, 4])
    c = b[np.newaxis, :]
    d = b[:, np.newaxis]
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")
    print(f"d: {d}")
    print(f"a.shape: {a.shape}")
    print(f"b.shape: {b.shape}")
    print(f"c.shape: {c.shape}")
    print(f"d.shape: {d.shape}")

def test_scipy():
    rot = np.array([0, 0, np.pi/2])
    r = Rotation.from_rotvec(rot)
    print(f"r.as_matrix(): {r.as_matrix()}")
    
    rots = np.array([[0, 0, np.pi/2], [0, np.pi/2, 0]])
    rs = Rotation.from_rotvec(rots)
    print(f"rs.as_matrix(): {rs.as_matrix()}")
    
def test_angular_velocity():
    #this will excess the 2*pi limit
    origin_rot = np.array([0, 0, 1])
    angular_velocity = np.array([0, 0, np.pi*2])
    now_rot = angular_velocity + origin_rot
    print(f"now_rot: {now_rot}")
    
    # this will not excess the 2*pi limit
    now_rot_matrix = Rotation.from_rotvec(angular_velocity).as_matrix() @ Rotation.from_rotvec(origin_rot).as_matrix()
    print(f"now_rot_matrix: {now_rot_matrix}")
    print(f"type(now_rot_matrix): {type(now_rot_matrix)}")
    now_rot_vec = Rotation.from_matrix(now_rot_matrix).as_rotvec()
    print(f"now_rot_vec: {now_rot_vec}")
    
if __name__ == '__main__':
    # test_numpy_shape()
    # test_scipy()
    test_angular_velocity()
