# -*- coding: utf-8 -*-

import os
import matplotlib

def convert_circles(centre1, centre2, radius_ratio):
    """
    Create thee circles with which to start the Apollonian Gasket from a minimum spec.
    """
    
    # Make sure the radiuses are both positive
    if (radius_ratio<0) or (radius_ratio>1):
        raise ValueError("Radius ratio must be between 0 and 1.")
        
    # Make sure each centre has two coordinates
    if ((len(centre1)!=2) or (len(centre2)!=2)):
        raise TriangleError("Corners must have two coordinates")
    
    # Make numpy vectors for both centres
    c1_vector = np.array(centre1)
    c2_vector = np.array(centre2)
    
    # Find the centre of the big circle
    c3_vector = c1_vector*radius_ratio + c2_vector*(1-radius_ratio)
    
    # Find the radius of the big circle
    radius3 = np.linalg.norm(c2_vector-c1_vector)
    
    # Find the radiuses of the little circles
    radius1 = radius3*radius_ratio
    radius2 = radius3*(1-radius_ratio)
    
    # Make circles
    circle1 = Circle(tuple(centre1),radius1)
    circle2 = Circle(tuple(centre2),radius2)
    circle3 = Circle(tuple(c3_vector),radius3)
    
    return [circle3,circle1,circle2]

def circle_in_three_circles_with_one_inside_out(circ1, circ2, circ3, other_one=False):
    """
    Find the two Soddy circles for three existing circles, where the first one encloses all the others.
    """
    
    # Bends
    b1 = -1./circ1.rad
    b2 = 1./circ2.rad
    b3 = 1./circ3.rad
    
    # Solve Descartes circle theorem
    bs = b1 + b2 + b3 + 2*np.sqrt( b1*b2 + b2*b3 + b3*b1 )
    radius = 1./bs
    
    # Centre-bend products
    z1 = b1 * complex(circ1.cen[0],circ1.cen[1])
    z2 = b2 * complex(circ2.cen[0],circ2.cen[1])
    z3 = b3 * complex(circ3.cen[0],circ3.cen[1])
    
    # Solve complex Descartes circle theorem - two solutions
    zspos = z1 + z2 + z3 + 2*np.sqrt( z1*z2 + z2*z3 + z3*z1 )
    zsneg = z1 + z2 + z3 - 2*np.sqrt( z1*z2 + z2*z3 + z3*z1 )
    
    # Possible centres
    centrepos = zspos/bs
    centreneg = zsneg/bs
    
    # See which one is closer to fitting 
    errpos = abs(np.linalg.norm(np.array(circ2.cen)-np.array([centrepos.real,centrepos.imag]))-(radius+circ2.rad)) \
           + abs(np.linalg.norm(np.array(circ3.cen)-np.array([centrepos.real,centrepos.imag]))-(radius+circ3.rad))
    errneg = abs(np.linalg.norm(np.array(circ2.cen)-np.array([centreneg.real,centreneg.imag]))-(radius+circ2.rad)) \
           + abs(np.linalg.norm(np.array(circ3.cen)-np.array([centreneg.real,centreneg.imag]))-(radius+circ3.rad))
    
    # Choose one
    if not other_one:
        if errneg > errpos:
            centre = centrepos
        else:
            centre = centreneg    
    else:
        if errneg > errpos:
            centre = centreneq
        else:
            centre = centrepos
    
    # Make a circle object
    soddy_circle = Circle((centre.real,centre.imag),radius)
    
    return soddy_circle 
    
def pack_circles_in_circle(centre1, centre2, radius_ratio, radius_limit):
    """
    Recursively pack circles into a circle
    """
    
    # Convert the input parameters into three circles
    initial_circles = convert_circles(centre1, centre2, radius_ratio)
    
    # Create a circle list
    circle_list = list(initial_circles)
    
    # Handle the first iteration specially
    new_circle1 = circle_in_three_circles_with_one_inside_out(circle_list[0], circle_list[1], circle_list[2])
    new_circle2 = circle_in_three_circles_with_one_inside_out(circle_list[0], circle_list[1], circle_list[2],
                                                              other_one=True)
    circle_list.extend([new_circle1,new_circle2])
    
    # Create a to-do stack
    todo_list = deque([(0,1,3),(0,2,3),(1,2,3),(0,1,4),(0,2,4),(1,2,4)])
    counter = 4
    
    # Loop
    it = 0
    while todo_list:
        it += 1
        
        # What's next
        parents = todo_list.popleft()
        
        # Three circles
        circle1 = circle_list[parents[0]]
        circle2 = circle_list[parents[1]]
        circle3 = circle_list[parents[2]]
        
        # Is the first circle the big one?
        if parents[0]==0:
            
            # Modified Soddy circles
            new_circle = circle_in_three_circles_with_one_inside_out(circle1, circle2, circle3)
            
        else:
            
            # Ordinary Soddy circle
            new_circle = circle_in_three_circles(circle1, circle2, circle3)
        
        if new_circle.rad > radius_limit:
        
            # Add the new circle to the list
            circle_list.append(new_circle)
            counter += 1
            
            # Add a new parent combinations to the to-do stack
            todo_list.append((parents[0],parents[1],counter))
            todo_list.append((parents[0],parents[2],counter))
            todo_list.append((parents[1],parents[2],counter))
    
    return circle_list

def draw_circle_fractal(ax, centre1, centre2, radius_ratio, radius_limit,
                        bordercolour='k', circlecolour='b', linewidth=2):
    """
    Draw a circle and pack circles in it.
    """
    circle_list = pack_circles_in_circle(centre1, centre2, radius_ratio, radius_limit)
    
    draw_circle(ax, circle_list[0], colour=bordercolour, linewidth=linewidth)
    for circle in circle_list[1:]:
        draw_circle(ax, circle, colour=circlecolour, linewidth=linewidth)
    
    return

centre1 = (-1,0)
centre2 = (1,0)
radius_ratio = 0.5
radius_limit = 0.02
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(1,1,1)
ax.set_xlim((-3,3))
ax.set_ylim((-3,3))

draw_circle_fractal(ax, centre1, centre2, radius_ratio, radius_limit)

plt.show()

centre1 = (-1,-1)
centre2 = (1,1)
radius_ratio = 0.5
radius_limit = 0.002
fig = plt.figure(figsize=(16,16))
ax = fig.add_subplot(1,1,1)
ax.set_xlim((-3,3))
ax.set_ylim((-3,3))
ax.axis('off')

draw_circle_fractal(ax, centre1, centre2, radius_ratio, radius_limit, linewidth=1)

plt.show()

os.system("pause")