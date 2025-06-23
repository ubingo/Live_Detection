import base64
from flask import Flask, request
import numpy as np
import cv2
import imutils
import dlib
from imutils import face_utils

import DynamicRecognition

app = Flask(__name__)

@app.route('/process_video', methods=['GET'])
def process_video():

    # 从前端获取视频文件地址
    file_path = request.args.get('file_path')

    # 视频分析
    DynamicRecognition.Face_Recognize(file_path)

    # 返回处理后的结果（可以是JSON格式）
    return {"result": "Processed successfully"}

if __name__ == '__main__':
    app.run(debug=True)
#     版权声明：本文为博主原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接和本声明。                       
# 原文链接：https://blog.csdn.net/weixin_53742691/article/details/136610143
