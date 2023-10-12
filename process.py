import imageio
import matplotlib.pyplot as plt
import numpy as np
import cv2
import pickle as pkl

# with open("./static/videos/ad.pkl", "rb") as f:
#     ad_vel = pkl.load(f)["vels"]
# with open("./static/videos/bl.pkl", "rb") as f:
#     bl_vel = pkl.load(f)["vels"]

# file = "./static/videos/switch.mp4"
# frames = []
# font_size = 0.7
# vid = imageio.get_reader(file)
# for i, frame in enumerate(vid):
#     frames.append(np.array(frame))
    
#     cv2.putText(
#         frames[-1], f'AlignDiff: {ad_vel[i]:.3f}', (10, 30), 
#         cv2.FONT_HERSHEY_SIMPLEX, font_size, (255,255,255), 2)
#     cv2.putText(
#         frames[-1], f'Baseline: {bl_vel[i]:.3f}', (266, 30), 
#         cv2.FONT_HERSHEY_SIMPLEX, font_size, (255,255,255), 2)

# writer = imageio.get_writer('./static/videos/switch_cap.mp4', fps=30)
# for frame in frames:
#     writer.append_data(frame)
# writer.close()


vid = imageio.get_reader("./static/videos/gap1-7.mp4")
frames = []
for i, frame in enumerate(vid):
    frames.append(np.array(frame))
    cap = ""
    if i < 20:
        cap = "Stride: 0.5"
    elif i >= 20 and i < 70:
        cap = "Stride: 1.0"
    elif i >= 70 and i < 90:
        cap = "Stride: 0.3"
    elif i >= 90 and i < 110:
        cap = "Stride: 0.6"
    elif i >= 110 and i < 145:
        cap = "Stride: 0.2"
    elif i >= 145 and i < 195:
        cap = "Stride: 0.6"
    elif i >= 195 and i < 210:
        cap = "Stride: 0.1"
    elif i >= 210 and i < 230:
        cap = "Stride: 0.5"
    elif i >= 230 and i < 255:
        cap = "Stride: 0.9"
    elif i >= 255 and i < 360:
        cap = "Stride: 0.6"
    elif i >= 360 and i < 375:
        cap = "Stride: 0.3"
    else:
        cap = "Stride: 0.6"
        
    cv2.putText(
        frames[-1], cap, (10, 30), 
        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)
    # cv2.putText(
    #     frames[-1], "2x", (10, 175), 
    #     cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)
    
writer = imageio.get_writer('./static/videos/gap_cap.mp4', fps=30)
for frame in frames:
    writer.append_data(frame)
writer.close()