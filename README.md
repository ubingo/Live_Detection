#### 一、简介
- 基于dlib；
- 基于OpenCV；
- 依赖于shape_predictor_68_face_landmarks.dat（用于人脸68个关键点检测的dat模型库）
- 实现实时活体检测功能，包含眨眼检测、张嘴检测、摇头检测、点头检测；

#### 二、人脸68个特征点分布图
![image](https://github.com/echo1118/Live_Detection/blob/master/image/人脸68个特征点分布图.jpeg)

#### 三、功能实现

- 眨眼检测：基于计算眼睛纵横比；
- 张嘴检测：基于计算嘴唇纵横比；
- 摇头检测：基于计算鼻子到面部轮廓的距离对比；
- 点头检测：基于计算左眉毛与左右脸轮廓的欧氏距离(两边之和是否小于或等于第三边+阈值)；

#### 四、参考资料
- 参考资料： https://developer.aliyun.com/article/336184


网友改造成api调用的网文参考：
https://blog.csdn.net/weixin_53742691/article/details/136610143

![image](https://github.com/user-attachments/assets/8c3a2d1f-3155-4a4e-976f-debfac6d4a18)

![image](https://github.com/user-attachments/assets/eb509de1-0139-4f76-87c1-85354bc99788)
