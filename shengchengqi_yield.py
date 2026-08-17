import sys

# 1.传统的列表方式 （一次性全部加载到内存）
def read_huge_file_with_list(lines):
    data = []
    for i in range(lines):
        # 模拟读取每一行的数据
        data.append(f"这是第{i}行的超大文件数据】")
    return data

# 2.生成器方式（用 yield，读一行吐一行）
def read_huge_file_with_generator(lines):
    for i in range(lines):
        # yield 就像是暂停键，吐出当前数据，然后暂停，等待下一次被调用
        yield f"这是第{i}行的超大文件数据"

# 截下来测试
total_lines = 1000000
print("正在生成数据，请稍候")

# 实例化列表和生成器
list_data = read_huge_file_with_list(total_lines)
gen_data = read_huge_file_with_generator(total_lines)

# 核心对比：使用 sys.getsizeoof()查看占用内存大小（单位：字节）
print(f"传统列表占用内存：{sys.getsizeof(list_data)}字节")
print(f"生成器占用内存：{sys.getsizeof(gen_data)}字节")

# 如何使用生成器的数据？用 for 循环或者 next（)
print("\n测试打印生成器的前两行：")
print(next(gen_data))
print(next(gen_data))