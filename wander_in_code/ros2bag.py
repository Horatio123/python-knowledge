import json
from rosbags.rosbag2 import Reader
from rosbags.serde import deserialize_cdr

def ros2bag_to_json(bag_path, output_json):
    """
    将ROS2 bag文件中的topic信息转换为JSON格式
    
    参数:
        bag_path: ROS2 bag文件夹路径
        output_json: 输出的JSON文件路径
    """
    result = {}
    
    # 打开ROS2 bag文件
    with Reader(bag_path) as reader:
        # 获取所有连接(connection)信息
        connections = [conn for conn in reader.connections]
        
        # 遍历每个连接
        for conn in connections:
            topic_name = conn.topic
            msg_type = conn.msgtype
            
            # 初始化该topic的数据列表
            if topic_name not in result:
                result[topic_name] = {
                    'msg_type': msg_type,
                    'messages': []
                }
            
            # 读取该topic的所有消息
            for _, _, raw_data in reader.messages([conn]):
                # 反序列化消息
                msg = deserialize_cdr(raw_data, conn.msgtype)
                
                # 将消息转换为字典格式
                msg_dict = msg_to_dict(msg)
                
                # 添加到结果中
                result[topic_name]['messages'].append(msg_dict)
    
    # 将结果写入JSON文件
    with open(output_json, 'w') as f:
        json.dump(result, f, indent=4)

def msg_to_dict(msg):
    """
    将ROS2消息对象转换为字典
    
    参数:
        msg: ROS2消息对象
    
    返回:
        字典格式的消息数据
    """
    if hasattr(msg, '__slots__'):
        # 如果是ROS2消息类型
        return {slot: msg_to_dict(getattr(msg, slot)) for slot in msg.__slots__}
    elif isinstance(msg, (list, tuple)):
        # 如果是列表或元组
        return [msg_to_dict(item) for item in msg]
    elif isinstance(msg, dict):
        # 如果是字典
        return {k: msg_to_dict(v) for k, v in msg.items()}
    else:
        # 基本类型直接返回
        return msg

if __name__ == '__main__':
    # 使用示例
    bag_path = '/home/ros/bags/joy.bag'  # 替换为你的ROS2 bag文件夹路径
    output_json = '/home/ros/bags/output.json'  # 替换为你想保存的JSON文件路径
    
    ros2bag_to_json(bag_path, output_json)
    print(f"转换完成，结果已保存到 {output_json}")