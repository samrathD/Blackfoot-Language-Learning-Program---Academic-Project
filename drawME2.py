# Your header

import cmpt120image
import random
apple = cmpt120image.getImage("images/apples.png")
bread = cmpt120image.getImage("images/bread.png")
burger = cmpt120image.getImage("images/burger.png")
child = cmpt120image.getImage("images/child.png")
coffee = cmpt120image.getImage("images/coffee.png")
dog = cmpt120image.getImage("images/dog.png")
door = cmpt120image.getImage("images/door.png")
egg = cmpt120image.getImage("images/eggs.png")
fish = cmpt120image.getImage("images/fish.png")
orange = cmpt120image.getImage("images/oranges.png")
salt = cmpt120image.getImage("images/salt.png")
tipi = cmpt120image.getImage("images/tipi.png")

canvas = cmpt120image.getWhiteImage(400,300)

#Recolor Image
def isBlack(pixel):
    r = pixel[0]
    g = pixel[1]
    b = pixel[2]
    return r<200 and g<200 and b<200
def recolorImage(img,color):
    #image = cmpt120image.getImage(img)
    height = len(img)
    width = len(img[0])
    
    for row in range(height):
        for col in range (width):
            if isBlack(img[row][col]):
                img[row][col] = color
          
    return img

#colour_burger = recolorImage(burger,[210,170,10])
#cmpt120image.showImage(colour_burger)

#Minify Item
def minify(img):
    height = len(img)
    width = len(img[0])

    new_img = cmpt120image.getBlackImage(width//2,height//2)
    new_height = height//2
    new_width = width//2

    for row in range(0,height,2):
        for col in range(0,width,2):

            pixel1 = img[row][col]
            pixel2 = img[row][col + 1]
            pixel3 = img[row + 1][col]
            pixel4 = img[row + 1][col + 1]

            r_avg = (pixel1[0] + pixel2[0] + pixel3[0] + pixel4[0])/4
            g_avg = (pixel1[1] + pixel2[1] + pixel3[1] + pixel4[1])/4
            b_avg = (pixel1[2] + pixel2[2] + pixel3[2] + pixel4[2])/4

            new_img[row//2][col//2] = [r_avg,g_avg,b_avg]
                                       

    return new_img

#small_burger = minify(burger)
#cmpt120image.showImage(small_burger)

#Mirror Item
def mirror(img):
    height = len(img)
    width = len(img[0])
    canvas = cmpt120image.getBlackImage(height,width)
    for row in range(height):
        for col in range(width):
            canvas[row][col] = img[row][-col]
    return canvas

#rev_child = mirror(child)
#cmpt120image.showImage(rev_child)

#Draw Item
def isNotwhite(pixel):
    r = pixel[0]
    g = pixel[1]
    b = pixel[2]


    return r != 255 and g != 255 and b != 255
def drawItem(canvas,item,row,col):

    item_height = len(item)
    item_width = len(item[0])
    

    for item_row in range(item_height):
        for item_column in range(item_width):
            if isNotwhite(item[item_row][item_column]):
                canvas[item_row +  row][item_column + col] = item[item_row][item_column]
    return canvas

#rand_burger = drawItem(canvas,burger,150,150)
#cmpt120image.showImage(rand_burger)

#Distributing Items
def distributeItems(canvas,item,n):
    canvas_height = len(canvas)
    canvas_width = len(canvas[0])

    item_height = len(item)
    item_width = len(item[0])

    for i in range(n):
        row = random.randint(0, canvas_height - item_height)
        col = random.randint(0, canvas_width - item_width)
        drawItem(canvas,item,row,col)

    return canvas

fishes = distributeItems(canvas,fish,8)
cmpt120image.showImage(fishes)

