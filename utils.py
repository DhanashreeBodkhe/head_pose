def get_direction(yaw):

    if yaw > 15:
        return "RIGHT"
    elif yaw < -15:
        return "LEFT"
    else:
        return "CENTER"