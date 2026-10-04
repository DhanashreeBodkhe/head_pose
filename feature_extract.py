import cv2
import numpy as np

MODEL_POINTS = np.array([
    (0.0, 0.0, 0.0),          
    (0.0, -330.0, -65.0),     
    (-225.0, 170.0, -135.0),  
    (225.0, 170.0, -135.0),   
    (-150.0, -150.0, -125.0), 
    (150.0, -150.0, -125.0)   
], dtype=np.float64)


def get_head_pose(landmarks, img_w, img_h):

    image_points = np.array([
        (landmarks[1].x * img_w, landmarks[1].y * img_h),
        (landmarks[152].x * img_w, landmarks[152].y * img_h),
        (landmarks[33].x * img_w, landmarks[33].y * img_h),
        (landmarks[263].x * img_w, landmarks[263].y * img_h),
        (landmarks[61].x * img_w, landmarks[61].y * img_h),
        (landmarks[291].x * img_w, landmarks[291].y * img_h)
    ], dtype=np.float64)

    focal_length = img_w
    center = (img_w / 2, img_h / 2)

    camera_matrix = np.array([
        [focal_length, 0, center[0]],
        [0, focal_length, center[1]],
        [0, 0, 1]
    ], dtype="double")

    dist_coeffs = np.zeros((4, 1))

    _, rotation_vector, translation_vector = cv2.solvePnP(
        MODEL_POINTS,
        image_points,
        camera_matrix,
        dist_coeffs,
        flags=cv2.SOLVEPNP_ITERATIVE
    )

    rmat, _ = cv2.Rodrigues(rotation_vector)

    sy = np.sqrt(rmat[0, 0]**2 + rmat[1, 0]**2)

    if sy < 1e-6:
        yaw = np.degrees(np.arctan2(-rmat[2, 0], sy))
    else:
        yaw = np.degrees(np.arctan2(-rmat[2, 0], sy))

    return yaw