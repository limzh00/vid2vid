import os
import sys
import argparse
import numpy as np
import cv2
import glob
if __name__ == '__main__':
    real_name = 'real_A_'
    fake_name = 'fake_B_'
    # ori path
    ori_path = '/data/limzh/vid2vid/results/edge2face_512/test_latest/0001'
    save_path = '/data/limzh/vid2vid/results/edge2face_512/test_latest/cat'
    
    imgs = os.listdir(ori_path)
    num = len(imgs) // 2
    for i in range(2, num+2):
        fake = os.path.join(ori_path, fake_name+f'{str(i).zfill(5)}.jpg')
        real = os.path.join(ori_path, real_name+f'{str(i).zfill(5)}.jpg')
        img_real, img_fake = cv2.imread(real), cv2.imread(fake)
        print(real, fake)
        cat = np.concatenate([img_real, img_fake], axis=1)
        cv2.imwrite(os.path.join(save_path, f'{str(i).zfill(5)}.jpg'), cat)

    video_ori_path = '/data/limzh/vid2vid/results/edge2face_512/test_latest/cat'
    video_writer = cv2.VideoWriter('demo_out_cat.avi', cv2.VideoWriter_fourcc(*'XVID'), 20, (1024, 512), True)
    
    video_ori_folder = sorted(glob.glob(os.path.join(video_ori_path, '*')))
    for frame in video_ori_folder:
        frame = cv2.imread(frame)
        video_writer.write(frame)
    video_writer.release()