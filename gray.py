import cv2

# 任务一：读取与显示图片
image_path = "person_dog.png"
img = cv2.imread(image_path)

if img is None:
    print(f"报错：找不到图片‘{image_path}’,请检查路径！")
    exit()

# 打印出来的 shape 通常是（高度，宽度，3），3是 BGR 三个颜色通道
print(f"图片读取成功！这张图片的矩阵形状是：{img.shape}")

cv2.imshow("1.Original BGR Image", img)

# 任务二：色彩空间转换与保存
# 1.转换为灰度图（Grayscale）
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("2.Grayscale Image",gray_img)

# 2.转换为 HSV 色彩空间（Hue 色调，Saturation 饱和度，Value 明度）
# 作用：HSV 比 BGR 更接近人类视觉对颜色的感知，在做“特定颜色追踪”（比如追踪红色的球）时极其好用，因为它不受光照忽明忽暗的影响。
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("3.HSV Image",hsv_img)

# 3.将处理后的图片保存到硬盘
cv2.imwrite("result_gray.jpg",gray_img)
cv2.imwrite("result_hsv.jpg",hsv_img)
print("灰度图和 HSV 图已成功保存到本地！")

# 任务三：切片提取感兴趣区域（ROI-Region of Interest）
# 数学坐标系是 (x, y)，即 (水平, 垂直)。
# 但是！图片在计算机里是矩阵，矩阵是按 [行, 列] 索引的。
# 所以代码里必须是 img[y的范围, x的范围] 也就是 img[高度范围, 宽度范围]！
y_start, y_end = 50,300
x_start, x_end = 100,400

roi_img = img[y_start:y_end, x_start:x_end]

cv2.imshow("4.Cropped ROI",roi_img)

# 让窗口停留在屏幕上，等待按键关闭
print("\n👉 请在弹出的图片窗口上按下键盘任意键，即可关闭所有图片程序。")

# cv2.waitKey(0) 表示无限期等待键盘敲击；如果不写这句，图片窗口闪一下就没了。
cv2.waitKey(0)






















