from PIL import Image

food = ['bone.png', 'cheese.png', 'peanutbutter.png', 'salmon.png', 'strawberry.png', 'watermelon.png']
dogs = ['carson.png', 'celeste.png', 'jonathan.png', 'marlin.png', 'tildy.png', 'wonton.png']

basewidth = 50
for pic in food:
    img = Image.open(f'./photos/{pic}')
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img.save(f'./resized_photos/food/{pic}')

basewidth = 100
for pic in dogs:
    img = Image.open(f'./photos/{pic}')
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img.save(f'./resized_photos/dogs/{pic}')

# baseheight = 50
# for pic in food:
#     img = Image.open(f'./photos/{pic}')
#     hpercent = (baseheight / float(img.size[1]))
#     wsize = int((float(img.size[0]) * float(hpercent)))
#     img = img.resize((wsize, baseheight), Image.ANTIALIAS)
#     img.save(f'./resized_photos/food/{pic}')

# baseheight = 100
# for pic in dogs:
#     img = Image.open(f'./photos/{pic}')
#     hpercent = (baseheight / float(img.size[1]))
#     wsize = int((float(img.size[0]) * float(hpercent)))
#     img = img.resize((wsize, baseheight), Image.ANTIALIAS)
#     img.save(f'./resized_photos/dogs/{pic}')