import os
import re

# 定义要处理的文件夹路径
folder_path = 'namePlates'

# 检查文件夹是否存在
if not os.path.exists(folder_path):
    print(f"文件夹 {folder_path} 不存在")
    exit()

# 遍历文件夹内的所有文件
for filename in os.listdir(folder_path):
    # 使用正则表达式匹配文件名中 " (数字)" 的部分
    new_filename = re.sub(r' \(\d+\)', '', filename)
    
    # 如果文件名有变化，进行重命名操作
    if new_filename != filename:
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_filename)
        
        # 检查目标文件是否已存在，如果存在则添加唯一标识符
        counter = 1
        base_name, extension = os.path.splitext(new_filename)
        while os.path.exists(new_file):
            new_file = os.path.join(folder_path, f"{base_name}_{counter}{extension}")
            counter += 1
        
        # 重命名文件
        os.rename(old_file, new_file)
        print(f"已将 {filename} 重命名为 {new_file}")

print("文件重命名完成")
