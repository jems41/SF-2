def covers(platform, horizontal_pos):
    '''
    :param platform: a platform as defined by the input of the question
    :param horizonal_pos: an integer
    :return : True if platform covers horizontal_post; False otherwise. 
    '''
    return platform[1] <= horizontal_pos <= platform[2]  # Fix the condition to check if horizontal_pos is between start and end of the platform

def pillar_from(platforms, height, horizontal_pos):
    '''
    :param platforms: a list of platforms (as lists)
    :param height: vertical position
    :param horizontal_pos: horizontal position
    :return : minimum length of pillar from height and horizontal_pos to the platform/ground below
    '''
    bottom = 0
    for platform in platforms:        
        if (platform[0] < height and covers(platform, horizontal_pos)):
            bottom = max(bottom, platform[0])  # Fix to correctly identify the bottom of the platform
    return height - bottom

n = int(input())

platforms = []

for i in range(n):
    platform = list(map(int, input().split())) 
    platforms.append(platform)

print(platforms)

total = 0

for platform in platforms: 
    total = total + pillar_from(platforms, platform[0], platform[1])
    total = total + pillar_from(platforms, platform[0], platform[2])

print(total)
