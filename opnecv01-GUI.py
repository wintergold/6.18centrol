import cv2
import numpy as np

# matplotlib��һ����ͼ�⣬��ɫͼ��ʹ�� OpenCV ����ʱ�� BGR ģʽ������ Matplotib �� RGBģʽ�����Բ�ɫͼ������Ѿ��� OpenCV ��ȡ�����������ᱻ Matplotib ��ȷ��ʾ


cv2.imread('1.jpg',0)
cv2.imshow('img',frame)
cv2.imwrite('img',img)
cv2.waitKey()  # �ȴ��ض��ļ����룬���Ƿ��м������룬�����Ϊ0���������ڵĵȴ���������
cv2.destroyAllWindows()  # ɾ���κδ���
cv2.destroyWindow()   # ɾ��ָ������

cv2.namedWindow('image',cv2.WINDOW_AUTOSIZE)  # ����һ�����ڣ����ڴ�С���ɵ�
        # cv2.WINDOW_AUTOSIZE :��С���ɵ�
        # cv2.WINDOW_NORMAL:���ڴ�С�ɵ�
img = np.zeros((512,512,3), np.uint8)  # ����


2.��Ƶ

cap = cv2.VideoCapture()  # ������ͷ������Ƶ�ļ�
ret,frame = cap.read()  # ����һ������ֵ��
cap.isOpened()  # ���жϴ����Ƿ�򿪣�
cap.open()
cap.get(pid)   # 0-18

    # CV_CAP_PROP_POS_MSEC��Ƶ�ļ��ĵ�ǰλ�ã��Ժ���Ϊ��λ����Ƶ����ʱ�����
    # CV_CAP_PROP_POS_FRAMES����0����һ��Ҫ����/�����֡��������
    # CV_CAP_PROP_POS_AVI_RATIO��Ƶ�ļ������λ�ã�0-��Ӱ�Ŀ�ʼ��1-��Ӱ�Ľ�����
    # CV_CAP_PROP_FRAME_WIDTH��Ƶ����֡�Ŀ�ȡ�
    # CV_CAP_PROP_FRAME_HEIGHT��Ƶ����֡�ĸ߶ȡ�
    # CV_CAP_PROP_FPS֡Ƶ��
    # CV_CAP_PROP_FOURCC���������4���ַ��Ĵ��롣
    # CV_CAP_PROP_FRAME_COUNT��Ƶ�ļ��е�֡����
    # CV_CAP_PROP_FORMAT�ɷ��ص�Mat����ĸ�ʽretrieve()��
    # CV_CAP_PROP_MODE�ض��ں�˵�ֵ��ָʾ��ǰ�Ĳ���ģʽ��
    # CV_CAP_PROP_BRIGHTNESSͼ������ȣ����������������
    # CV_CAP_PROP_CONTRASTͼ��ĶԱȶȣ����������������
    # CV_CAP_PROP_SATURATIONͼ��ı��Ͷȣ����������������
    # CV_CAP_PROP_HUEͼ���ɫ�ࣨ���������������
    # CV_CAP_PROP_GAINͼ������棨���������������
    # CV_CAP_PROP_EXPOSURE�ع⣨���������������
    # CV_CAP_PROP_CONVERT_RGB�����ͱ�־��ָʾ�Ƿ�Ӧ��ͼ��ת��ΪRGB��
    # CV_CAP_PROP_WHITE_BALANCE_U��ƽ�����õ�Uֵ��ע�⣺��ǰ����DC1394 v 2.x���֧�֣�
    # CV_CAP_PROP_WHITE_BALANCE_V��ƽ�����õ�Vֵ��ע�⣺��ǰ����DC1394 v 2.x���֧�֣�
    # CV_CAP_PROP_RECTIFICATION����������ľ�����־��ע�⣺��ǰ����DC1394 v 2.x���֧�֣�
    # CV_CAP_PROP_ISO_SPEED�������ISO�ٶȣ�ע�⣺��ǰ����DC1394 v 2.x���֧�֣�
    CV_CAP_PROP_BUFFERSIZE�洢���ڲ�����洢���е�֡����ע�⣺��ǰ����DC1394 v 2.x���֧�֣�

    ע�⣺�ڲ���ÿһ֡ʱ��ʹ�� cv2.waiKey() �����ʵ��ĳ���ʱ�䡣������õ�̫����Ƶ�ͻᲥ�ŵķǳ��죬������õ�̫�߾�
    �Ქ�ŵĺ����������ʹ�����ַ���������Ƶ�Ĳ����ٶȣ���ͨ������� 25 ����Ϳ����ˡ�

cv2.VideoWriter()   # ������Ƶ����

cv2.VideoWriter_fourcc(*'XVID') # ��Ƶ�ı����ʽ

    In Fedora: DIVX, XVID, MJPG, X264, WMV1, WMV2. (XVID is more preferable. MJPG results in high size video. X264 givesvery small size video)
    In Windows: DIVX (More to be tested and added)
    In OSX : (I don��t have access to OSX. Can some one fill this?)
    FourCC ��������ĸ�ʽ���������� MJPG Ϊ����
    cv2.cv.FOURCC('M','J','P','G') ���� cv2.cv.FOURCC(*'MJPG')��

cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))  #1.������Ƶ�����ƣ������ʽ��֡�ʣ�ÿһ֡��С



3.��ͼ����

cv2.line()
    cv2.line(img,(0,0),(511,511),(255,0,0),5)
cv2.circle()
    cv2.circle(img,(447,63), 63, (0,0,255), -1)
cv2.rectangle()  # ����
    cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
cv2.ellipse()
    cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
cv2.putText()
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

cv2.polylines()  # �������
cv2.polylines(img,[pts],True,(0,255,255))  # pst��pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)pts = pts.reshape((-1,1,2))

    �������
        img������Ҫ����ͼ�ε��Ƿ�ͼ��
        color����״����ɫ���� RGB Ϊ������Ҫ����һ��Ԫ�飬���磺 ��255,0,0 ��������ɫ�����ڻҶ�ͼֻ��Ҫ����Ҷ�ֵ��
        thickness�������Ĵ�ϸ�������һ���պ�ͼ������Ϊ -1����ô���ͼ�ξͻᱻ��䡣Ĭ��ֵ�� 1.
        linetype�����������ͣ�8 ���ӣ�����ݵȡ�Ĭ������� 8 ���ӡ�cv2.LINE_AAΪ����ݣ�������������ǳ�ƽ����



����굱��

cv2.setMouseCallback()

�û���������ɫ��

cv2.getTrackbarPos()  # ��ȡ��������ֵ
cv2.createTrackbar()  # ����������












