import os
import cv2
import torch
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms


# ==========================================
# 第一部分：定义“仓库管理员” (自定义 Dataset)
# ==========================================
class MyVisionDataset(Dataset):

    # 魔法方法 1：__init__ (初始化，拿登记造册的清单)
    def __init__(self, image_folder_path):
        """
        初始化函数，当创建这个类的实例时最先运行。
        通常在这里读取文件列表，但不把图片全部读进内存（否则内存会爆）。
        """
        self.image_folder = image_folder_path
        # 获取文件夹下所有的图片名字存入列表，比如 ['dog.jpg', 'cat.jpg', ...]
        self.image_names = os.listdir(image_folder_path)

        # 定义一个转换工具：把普通的 NumPy 数组转成 PyTorch 需要的 Tensor
        self.transform = transforms.ToTensor()

    # 魔法方法 2：__len__ (告诉系统总共有多少条数据)
    def __len__(self):
        """
        DataLoader 会调用这个方法，来知道总共有多少个批次可以拉取。
        """
        return len(self.image_names)

    # 魔法方法 3：__getitem__ (核心！根据索引拿货，并做预处理)
    def __getitem__(self, idx):
        """
        当 DataLoader 要求取第 idx 张图片时，会自动调用这个方法。
        """
        # 1. 根据索引拿到当前图片的名字和完整路径
        current_image_name = self.image_names[idx]
        image_path = os.path.join(self.image_folder, current_image_name)

        # 2. 用 OpenCV 读取图片 (读出来是 H, W, C 格式的 NumPy 数组，且颜色空间是 BGR)
        img_bgr = cv2.imread(image_path)

        # 防御性编程：如果图片损坏读不到，抛出异常
        if img_bgr is None:
            raise ValueError(f"无法读取图片: {image_path}")

        # 3. 将 OpenCV 的 BGR 格式转换为模型最常用的 RGB 格式
        img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

        # 4. 关键转换：NumPy 数组 -> PyTorch Tensor
        # transforms.ToTensor() 偷偷帮我们做了两件极其重要的事情：
        #   (a) 维度转换：把 (Height, Width, Channels) 变成了 PyTorch 需要的 (Channels, Height, Width)
        #   (b) 归一化：把 0~255 的像素值，除以 255 变成了 0.0~1.0 的浮点数 (Float32)
        img_tensor = self.transform(img_rgb)

        # 5. 生成对应的标签 (这里为了演示简化，我们直接把图片名字当作标签返回)
        # 在真实的分类任务中，这里返回的通常是 0, 1, 2 这样的类别索引 Tensor
        label = current_image_name

        # 一定要返回图片 Tensor 和 对应的标签
        return img_tensor, label


# ==========================================
# 第二部分：测试与使用“货车司机” (DataLoader)
# ==========================================
if __name__ == "__main__":
    # 假设你的电脑同一目录下有一个叫 'my_images' 的文件夹，里面放了几张测试图片
    folder_path = "./my_images"

    # 为了测试代码，如果文件夹不存在，咱们用 Python 先创建一个空文件夹避免报错
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"提示: 请往刚才新建的 {folder_path} 文件夹里放几张 jpg 图片再运行！")
        exit()

    # 1. 实例化我们的仓库管理员
    my_dataset = MyVisionDataset(image_folder_path=folder_path)
    print(f"仓库里总共有 {len(my_dataset)} 张图片。")

    # 2. 实例化货车司机 (DataLoader)
    # batch_size=2 表示每次拉 2 张图；shuffle=True 表示每次训练前把数据打乱
    my_dataloader = DataLoader(dataset=my_dataset, batch_size=2, shuffle=True)

    # 3. 模拟深度学习训练过程，遍历 DataLoader 开始“拉货”
    for batch_idx, (batch_images, batch_labels) in enumerate(my_dataloader):
        print(f"\n=== 当前正在拉取第 {batch_idx + 1} 批次 (Batch) ===")
        # 打印这一批次图片张量的形状 (Shape)
        print(f"这一批图片的 Tensor 形状是: {batch_images.shape}")
        print(f"对应的标签是: {batch_labels}")

        # 测试一圈就够了，直接 break 退出循环
        break