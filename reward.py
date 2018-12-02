def reward_function(on_track, x, y, distance_from_center, car_orientation, progress, steps, throttle, steering, track_width, waypoints, closest_waypoint):

    import math

    reward = 1e-3

    marker_2 = 0.33 * track_width

    if distance_from_center > marker_2:
        reward = 1e-3 # probably not gonna be able to turn
    else:
        reward = 1        

    reward += progress
    # Smooth steering
    # ABS_STEERING_THRESHOLD = 0.5
    # if abs(steering) > ABS_STEERING_THRESHOLD:
    #     reward *= 0.8

    #Penalize going too slow
    THROTTLE_THRESHOLD = 0.5
    if throttle < THROTTLE_THRESHOLD:
        reward *= 0.8

    return float(reward)
