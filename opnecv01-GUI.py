import cv2
import numpy as np

# matplotlib是一个绘图库，彩色图像使用 OpenCV 加载时是 BGR 模式。但是 Matplotib 是 RGB模式。所以彩色图像如果已经被 OpenCV 读取，那它将不会被 Matplotib 正确显示


cv2.imread('1.jpg',0)
cv2.imshow('img',frame)
cv2.imwrite('img',img)
cv2.waitKey()  # 等待特定的几毫秒，看是否有键盘输入，如果设为0，会无限期的等待键盘输入
cv2.destroyAllWindows()  # 删除任何窗口
cv2.destroyWindow()   # 删除指定窗口

cv2.namedWindow('image',cv2.WINDOW_AUTOSIZE)  # 创建一个窗口，窗口大小不可调
        # cv2.WINDOW_AUTOSIZE :大小不可调
        # cv2.WINDOW_NORMAL:窗口大小可调
img = np.zeros((512,512,3), np.uint8)  # 画布


2.视频

cap = cv2.VideoCapture()  # 打开摄像头或者视频文件
ret,frame = cap.read()  # 返回一个布尔值，
cap.isOpened()  # 来判断窗口是否打开，
cap.open()
cap.get(pid)   # 0-18

    # CV_CAP_PROP_POS_MSEC视频文件的当前位置，以毫秒为单位或视频捕获时间戳。
    # CV_CAP_PROP_POS_FRAMES基于0的下一个要解码/捕获的帧的索引。
    # CV_CAP_PROP_POS_AVI_RATIO视频文件的相对位置：0-电影的开始，1-电影的结束。
    # CV_CAP_PROP_FRAME_WIDTH视频流中帧的宽度。
    # CV_CAP_PROP_FRAME_HEIGHT视频流中帧的高度。
    # CV_CAP_PROP_FPS帧频。
    # CV_CAP_PROP_FOURCC编解码器的4个字符的代码。
    # CV_CAP_PROP_FRAME_COUNT视频文件中的帧数。
    # CV_CAP_PROP_FORMAT由返回的Mat对象的格式retrieve()。
    # CV_CAP_PROP_MODE特定于后端的值，指示当前的捕获模式。
    # CV_CAP_PROP_BRIGHTNESS图像的亮度（仅适用于相机）。
    # CV_CAP_PROP_CONTRAST图像的对比度（仅适用于相机）。
    # CV_CAP_PROP_SATURATION图像的饱和度（仅适用于相机）。
    # CV_CAP_PROP_HUE图像的色相（仅适用于相机）。
    # CV_CAP_PROP_GAIN图像的增益（仅适用于相机）。
    # CV_CAP_PROP_EXPOSURE曝光（仅适用于相机）。
    # CV_CAP_PROP_CONVERT_RGB布尔型标志，指示是否应将图像转换为RGB。
    # CV_CAP_PROP_WHITE_BALANCE_U白平衡设置的U值（注意：当前仅由DC1394 v 2.x后端支持）
    # CV_CAP_PROP_WHITE_BALANCE_V白平衡设置的V值（注意：当前仅受DC1394 v 2.x后端支持）
    # CV_CAP_PROP_RECTIFICATION立体摄像机的纠正标志（注意：当前仅受DC1394 v 2.x后端支持）
    # CV_CAP_PROP_ISO_SPEED摄像机的ISO速度（注意：当前仅受DC1394 v 2.x后端支持）
    CV_CAP_PROP_BUFFERSIZE存储在内部缓冲存储器中的帧数（注意：当前仅受DC1394 v 2.x后端支持）

    注意：在播放每一帧时，使用 cv2.waiKey() 设置适当的持续时间。如果设置的太低视频就会播放的非常快，如果设置的太高就
    会播放的很慢（你可以使用这种方法控制视频的播放速度）。通常情况下 25 毫秒就可以了。

cv2.VideoWriter()   # 保存视频流、

cv2.VideoWriter_fourcc(*'XVID') # 视频的编码格式

    In Fedora: DIVX, XVID, MJPG, X264, WMV1, WMV2. (XVID is more preferable. MJPG results in high size video. X264 givesvery small size video)
    In Windows: DIVX (More to be tested and added)
    In OSX : (I don’t have access to OSX. Can some one fill this?)
    FourCC 码以下面的格式传给程序，以 MJPG 为例：
    cv2.cv.FOURCC('M','J','P','G') 或者 cv2.cv.FOURCC(*'MJPG')。

cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))  #1.保存视频流名称，编码格式，帧率，每一帧大小



3.绘图函数

cv2.line()
    cv2.line(img,(0,0),(511,511),(255,0,0),5)
cv2.circle()
    cv2.circle(img,(447,63), 63, (0,0,255), -1)
cv2.rectangle()  # 矩形
    cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
cv2.ellipse()
    cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
cv2.putText()
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

cv2.polylines()  # 画多边形
cv2.polylines(img,[pts],True,(0,255,255))  # pst是pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)pts = pts.reshape((-1,1,2))

    所需参数
        img：你想要绘制图形的那幅图像。
        color：形状的颜色。以 RGB 为例，需要传入一个元组，例如： （255,0,0 ）代表蓝色。对于灰度图只需要传入灰度值。
        thickness：线条的粗细。如果给一个闭合图形设置为 -1，那么这个图形就会被填充。默认值是 1.
        linetype：线条的类型，8 连接，抗锯齿等。默认情况是 8 连接。cv2.LINE_AA为抗锯齿，这样看起来会非常平滑。



把鼠标当笔

cv2.setMouseCallback()

用滑动条做调色板

cv2.getTrackbarPos()  # 获取滑动条的值
cv2.createTrackbar()  # 创建滑动条












