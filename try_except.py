def load_image_safe(image_path):
    print(f"\n开始尝试读取图片：{image_path}")

    try:
        with open(image_path,'rb') as f:
            print("=>太棒了，图片读取成功！可以送入模型了。")

    except FileNotFoundError:
        print(f"=>[拦截成功]哎呀，找不到名为‘{image_path}’的图片！")
        print("=>系统自动跳过这张图，继续跑下一张……")

    except Exception as e:
        print(f"=>[未知错误]读取时发生意外崩溃，原因是：{e}")

    finally:
        print("---这次读取操作结束---")

# 测试环节
load_image_safe("fake_dog_image.jpg")
print("\n你看，虽然报错了，但程序没有中断，我这行代码还能继续打印!")

















