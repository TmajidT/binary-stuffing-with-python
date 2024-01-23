def receiver(frames):
    stripped_frames = [frame[3:-3] for frame in frames]

    replaced_frames = [frame.replace('100100', '100').replace('100101', '101') for frame in stripped_frames]

    return replaced_frames

def concatenate_frames(received_frames):
    concatenated_string = ''.join(received_frames)
    return concatenated_string