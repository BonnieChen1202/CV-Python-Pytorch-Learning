class BaseVisionModel:
    def __init__(self , name):
        self.model_name = name
        print(f"[系统提示]成功创建了基础视觉模型：{self.model_name}")

    def log(self , message):
        print(f"[{self.model_name}日志] -> {message}")


class SwinTransformer(BaseVisionModel):
    def __init__(self, name, window_size):
        super().__init__(name)

        self.window_size = window_size
        self.log(f"窗口大小(window size) 已设置为：{self.window_size}")

    def forward(self, input_image):
        self.log("正在接收输入图像数据")
        self.log("正在执行 Shifted Window Attention 计算")

        output = f"提取完毕的图像特征（基于{self.window_size}x{self.window_size}窗口）"
        return output


if __name__ == "__main__":
    print("---步骤 A：实例化模型---")
    my_model = SwinTransformer(name="Swin-Tiny-V1",window_size=7)

    print("\n---步骤 B：模拟数据输入---")
    dummy_image = "一张 224x224的测试图片"

    result = my_model.forward(dummy_image)

    print("\n---步骤 C：查看输出结果---")
    print(f"最终输出：{result}")

