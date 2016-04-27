# -*- coding: utf-8 -*-

import os
import matplotlib

class TriangleError(ValueError):
    """
    Invalid triangle specification
    """

def convert_triangle(triangle):
    """
    Convert a list of three 2D points representing a triangle into a set of sides.
    Raise an error if the triangle is not a triangle.
    """
    
    # Make sure it has exactly three corners
    if len(triangle) != 3:
        raise TriangleError("Triangle must have three corners")
    
    # Get corners
    a = triangle[0]
    b = triangle[1]
    c = triangle[2]
    
    # Make sure each corner has two coordinates
    if ((len(a)!=2) or (len(b)!=2) or (len(c)!=2)):
        raise TriangleError("Corners must have two coordinates")
        
    try:
        # Make sides from corners, taking care of the sign
        if ( (b[0]-a[0])*(c[1]-b[1]) - (b[1]-a[1])*(c[0]-b[0]) ) < 0:
            line1 = Line(a,b)
            line2 = Line(b,c)
            line3 = Line(c,a)
        else:
            line1 = Line(a,c)
            line2 = Line(c,b)
            line3 = Line(b,a)
            
    except TypeError:
        raise TriangleError("Corners are not valid numbers")
        

    sides = [line1,line2,line3]
    
    return sides

from collections import deque

def pack_circles_in_triangle(triangle, radius_limit):
    """
    Recursively pack circles into a triangle
    """
    
    # Convert triangle (3 points) into a set of side
    sides = convert_triangle(triangle)
    
    # Create a circle list
    circle_list = list(sides)
    counter = 2
    
    # Create a to-do stack
    todo_list = deque([(0,1,2)])
    
    # Loop
    it = 0
    while todo_list:
        it += 1
        
        # What's next
        parents = todo_list.popleft()
        
        # How many lines are present
        num_lines = 0
        for ii in range(3):
            if parents[ii] < 3:
                num_lines += 1
        
        # Switch on number of lines
        if num_lines == 0:
            
            # Three circles
            circle1 = circle_list[parents[0]]
            circle2 = circle_list[parents[1]]
            circle3 = circle_list[parents[2]]
            
            # Spawn a new circle
            new_circle = circle_in_three_circles(circle1, circle2, circle3)
            
        elif num_lines == 1:
            
            # Two circles, one line
            line1 = circle_list[parents[0]]
            circle1 = circle_list[parents[1]]
            circle2 = circle_list[parents[2]]
            
            # Spawn a new circle
            new_circle = circle_in_two_circles_and_a_line(circle1, circle2, line1)
            
        elif num_lines == 2:
            
            # Two lines, one circle
            line1 = circle_list[parents[0]]
            line2 = circle_list[parents[1]]
            circle1 = circle_list[parents[2]]
            
            # Spawn a new circle
            new_circle = circle_in_two_lines_and_a_circle(line1, line2, circle1)
            
        elif num_lines == 3:
            
            # Three line
            line1 = circle_list[parents[0]]
            line2 = circle_list[parents[1]]
            line3 = circle_list[parents[2]]
            
            # Spawn a new circle
            new_circle = circle_in_three_lines(line1, line2, line3)
            
        else:
            raise ValueError
        
        if new_circle.rad > radius_limit:
        
            # Add the new circle to the list
            circle_list.append(new_circle)
            counter += 1
            
            # Add a new parent combinations to the to-do stack
            todo_list.append((parents[0],parents[1],counter))
            todo_list.append((parents[0],parents[2],counter))
            todo_list.append((parents[1],parents[2],counter))
    
    
    # Remove the three lines from the list
    circle_list[:3] = []
    
    return sides,circle_list

def draw_triangle_fractal(ax, triangle, radius_limit, linecolour='k', circlecolour='b', linewidth=2):
    """
    Draw a triangle and pack circles in it.
    """
    sides,circle_list = pack_circles_in_triangle(triangle, radius_limit)
    
    for ii in range(3):
        draw_line(ax, sides[ii], colour=linecolour, linewidth=linewidth)
    
    for circle in circle_list:
        draw_circle(ax, circle, colour=circlecolour, linewidth=linewidth)
    
    return

triangle = [(-2,-2),(0,2),(2,0)]
radius_limit = 0.005
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(1,1,1)
ax.set_xlim((-3,3))
ax.set_ylim((-3,3))

draw_triangle_fractal(ax, triangle, radius_limit)

plt.show()

h = 0.02
triangle_list = [[(-2,-2-h),(0,0-h),(2,-2-h)],
                 [(-2,2+h) ,(0,0+h),(2,2+h) ],
                 [(-2-h,-2),(-2-h,2),(0-h,0)],
                 [(2+h,-2) ,(2+h,2), (0+h,0)]  ]

radius_limit = 0.005
fig = plt.figure(figsize=(16,16))
ax = fig.add_subplot(1,1,1)
ax.set_xlim((-3,3))
ax.set_ylim((-3,3))
ax.axis('off')

for triangle in triangle_list:
    draw_triangle_fractal(ax, triangle, radius_limit, linewidth=1)

plt.show()
    
os.system("pause")