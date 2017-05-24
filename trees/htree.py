'''
H-Tree Construction

An H-tree is a geometric shape that consists of a repeating pattern resembles the letter “H”.

It can be constructed by starting with a line segment of arbitrary length,
drawing two segments of the same length at right angles to the first through its endpoints, and continuing in the same vein,
reducing (dividing) the length of the line segments drawn at each stage by √2.


Write a function drawHTree that constructs an H-tree, given its center (x and y coordinates), a starting length, and depth. Assume that the starting line is parallel to the X-axis.

Use the function drawLine provided to implement your algorithm. In a production code, a drawLine function would render a real line between two points. However, this is not a real production environment, so to make things easier, implement drawLine such that it simply prints its arguments (the print format is left to your discretion).

Analyze the time and space complexity of your algorithm. In your analysis, assume that drawLine's time and space complexities are constant, i.e. O(1).

Time => O(4^D)
Space => O(D)
'''


# drawLine provided
# line/sqrt(2)
# 4 way tree

# drawHTree():
     if curr_depth == depth:
        return
#    drawHTree(LT)
#    drawHTree(RT)
#    drawHTree(BL)
#    drawHTree(BR)
        drawLine(x,y)

# H (0, 0)
# l = 2 ()
# L ( -L/2,0)
# R (L/2,0)
# LT -L/2, -L/2
# RB -L/2, L/2
# RT 1,-1
# RB 1, 1


def drawLine(x1, y1, x2, y2):
    # draws line, assume implementation available

def drawHTree(x, y, length, depth):
  if depth <= 0:
    return
 
  drawHTree(x-length/2, y-length/2, length/math.sqrt(2), depth-1) # LT
  drawHTree(x-length/2, y+length/2, length/math.sqrt(2), depth-1) # RB
  drawHTree(x+length/2, y-length/2, length/math.sqrt(2), depth-1) # RT
  drawHTree(x+length/2, y+length/2, length/math.sqrt(2), depth-1) # RB
  start = (-length/2, -length/2)
  # Left line
  start_l = (x+length/2, y-length/2)
  end_l = (x-length/2, y+length/2)
  drawLine(start_l,end_l)
  # Right Line
  start_r = (x+length/2, y-length/2)
  end_r = (x+length/2, y+length/2)
  drawLine(start_r,end_r)
  # Horiz line
  start = (end_l - start_l)/2
  end = (end_r - start_r)/2
  drawLine(start,end)
  
  drawLine(start,end)                    
