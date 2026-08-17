import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)

        end_time = time.time()
        cost_time = end_time - start_time

        print(f"[性能测试]函数 '{func.__name__}' 总耗时: {cost_time:.4f} 秒")
        return result
    return wrapper

# 测试环节
@timer
def simulate_model_inference():
    print("\n[模型]RT-DETR正在努力提取特征……")
    time.sleep(1.5)
    print("[模型]目标检测完成！找到 3 只猫。")
    return "Detection Result"

@timer
def simulate_data_loading():
    print("\n[数据]正在从硬盘疯狂加载 1000张图片……")
    time.sleep(0.8)
    print("[数据]加载完毕。")

result = simulate_model_inference()
simulate_data_loading()