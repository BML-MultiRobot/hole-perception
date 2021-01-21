#basic script to solve width given depth
import numpy as np
import rospy
import math

ANGLE = ...


def calcWidth(m):
    return (math.cos(ANGLE) * m, math.sin(ANGLE) * m)
