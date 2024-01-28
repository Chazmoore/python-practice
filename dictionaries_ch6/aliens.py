# alien_0 = {'color': 'green', 'points': 5}

# print(alien_0['color'])
# print(alien_0['points'])


# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0['color'])

# alien_0 = {'color': 'green', 'points': 5}

# new_points = alien_0['points']
# print(f"You just earned {new_points}!")

# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)

# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# alien_0 = {}

# alien_0['color'] = 'green'
# alien_0['points'] = 5

# print(alien_0)

# alien_0 = {'color' : 'green'}
# print(f"The alien is {alien_0['color']}.")

# alien_0['color'] = 'yellow'
# print(f"The alien is now {alien_0['color']}.")

# alien_0 = {'x_posistion': 0, 'y_posistion': 25, 'speed': 'medium'}
# print(f"Original posistion: {alien_0['x_posistion']}")

# # move the alien to the right.
# # Determine how far to move the alien based on its current speed.

# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:

#     # This must be a fast alien
#     x_increment = 3

# # the new posistion is the old posistion plus the increment.
# alien_0['x_posistion'] = alien_0['x_posistion'] + x_increment

# print(f"New posistion: {alien_0['x_posistion']}")

# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)

# del alien_0['points']
# print(alien_0)

alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'Not point value assigned')
print(point_value)