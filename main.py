import random

import sender
import receiver

def generate_random_bits(length):
    return ''.join(random.choice(['0', '1']) for _ in range(length))


def main():
    random_bits = generate_random_bits(1000)
    print("Random Bits:", random_bits)
    print()
    frames = sender.divide_into_frames(random_bits, 10)
    modified_frames = [sender.replace_100_and_101(frame) for frame in frames]
    modified_frames = [sender.add_101_to_start_and_end(frame) for frame in modified_frames]
    for i, frame in enumerate(modified_frames):
        print(f"Modified Frame {i+1}: {frame}")


    received_frames = receiver.receiver(modified_frames)
    print("\nReceived Frames:")

    for i, frame in enumerate(received_frames):
        print(f"Frame {i+1}: {frame}")

    final_string = receiver.concatenate_frames(received_frames)
    print()
    print("Final String:")
    print(final_string)

if __name__ == '__main__':
    main()
