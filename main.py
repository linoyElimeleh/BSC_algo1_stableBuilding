import random


class Box:
    def __init__(self, height, width, length):
        self.height = height
        self.width = width
        self.length = length
        self.cubeVolume = width * length * height


# Sort box array by key
def sort_array(boxes_array):
    sorted(boxes_array, lambda b1, b2: b2.length * b2.width - b1.length * b1.width)


# Create one array of boxes from height, width and length arrays
def arrays_to_box(height, width, length):
    box_arr = []
    size = len(height)
    for i in range(size):
        box_arr.append(Box(height[i], width[i], length[i]))
    sort_array(box_arr)
    return box_arr


def find_highest_building(height, width, length):
    max_height = []
    result = []
    final_stable_tower = []

    # Create sorted boxes array
    box_arr = arrays_to_box(height, width, length)

    for i in range(len(box_arr)):
        max_height.append(box_arr[i].height)
        result.append(i)

    for i in range(len(box_arr)):
        for j in range(i):

            # Check if it is a stable building
            if box_arr[i].length < box_arr[j].length and box_arr[i].width < box_arr[j].width:

                # Check if the building have the highest size
                if max_height[j] + box_arr[i].height > max_height[i]:
                    max_height[i] = max_height[j] + box_arr[i].height

                    # Exchange results places
                    # temp = result[i]
                    result[i] = result[j]
                    # result[j] = temp

    max_index = 0
    for i in range(len(max_height)):
        if max_height[i] > max_height[max_index]:
            max_index = i

    new_t = max_index

    # Back through the array from the top box of the tower(maxIndex) to the Bottom of the tower
    while True:
        t = new_t
        final_stable_tower.append(box_arr[t])
        new_t = result[t]

        if t == new_t:
            break

    return box_arr, final_stable_tower


def initialize_arrays(height, width, length, size):
    for x in range(size):
        height.append(random.randint(1, 200))
        width.append(random.randint(1, 200))
        length.append(random.randint(1, 200))


def print_boxes_array(boxes_array):
    for x in range(len(boxes_array)):
        print "length: " + str(boxes_array[x].length) + " width: " + str(boxes_array[x].width) + " height: " + str(
            boxes_array[x].height)


if __name__ == '__main__':
    print ("*******  Example with 30 random boxes  *******\n")
    height30 = []
    width30 = []
    length30 = []

    initialize_arrays(height30, width30, length30, 30)

    box_array, max_array = find_highest_building(height30, width30, length30)

    print ("The 30 Boxes with their Dimensions are: ")
    print_boxes_array(box_array)

    print ("\nThe Highest Stable Tower of the 30 Boxes Sorted From Top to Bottom: ")
    print_boxes_array(max_array)
    max_height = 0
    for one_box in max_array:
        max_height += one_box.height

    print("\nThe Maximum Height of this Tower is: ")
    print (max_height)

    print ("*******  Example with 20 random boxes  *******\n")
    height20 = []
    width20 = []
    length20 = []

    initialize_arrays(height20, width20, length20, 20)
    box_array2, max_array2 = find_highest_building(height20, width20, length20)

    print ("The 20 Boxes with their Dimensions are: ")
    print_boxes_array(box_array2)

    print ("\nThe Highest Stable Tower of the 30 Boxes Sorted From Top to Bottom: ")
    print_boxes_array(max_array2)
    max_height2 = 0
    for one_box in max_array2:
        max_height2 += one_box.height

    print("\nThe Maximum Height of this Tower is: ")
    print (max_height2)
