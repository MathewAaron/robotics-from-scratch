import numpy as np
from scipy.spatial.transform import Rotation as rotation

def get_rotation_matrix(angle:float,degrees = False)->np.array:
    """
    Function to create a 2D rotation matrix from a given angle.
    Angle can be set to degrees by setting degrees = True

    Parameters:
        Angles -> float
        degrees -> bool
    Returns
        2x2 np.array
    """
    
    return np.array(rotation.from_euler('z', angle,degrees=degrees).as_matrix()[0:2,0:2])

