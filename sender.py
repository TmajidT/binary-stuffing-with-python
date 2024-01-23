def divide_into_frames(bits, frame_size):
    frames = [bits[i:i+frame_size] for i in range(0, len(bits), frame_size)]
    return frames

def replace_100_and_101(frame):
    modified_frame = frame.replace('100', '100100').replace('101', '100101')
    return modified_frame

def add_101_to_start_and_end(frame):
    return '101' + frame + '101'