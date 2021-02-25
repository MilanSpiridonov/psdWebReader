from psd_tools import PSDImage
from PIL import Image
import os

#INIT
script = '' #HTML code, components will be added later in code #aligncenter
script += """<!DOCTYPE html>
<html>
<head>
<style>
.aligncenter{
text-align: center;}
</style>
<title> Landing Page </title>
<head>
<body>
"""

pathf = 'Materials/test.psd'    #temp path value
psd = PSDImage.open(pathf)
imCnt = 0
#/INIT

for layer in psd:
     if layer.name.split(' ')[0] == 'Canvas': #There's one layer named 'Canvas', where we get different info on positions and stuff
        ctr = layer.bbox[2]/2 # Center of the canvas
        maxW = layer.bbox[2] # Max Width
        maxH = layer.bbox[3] - 1 # Max Height
        try: #This sets background color
            bgColor = layer.name.split(' ')[1]
            if bgColor == 'White':
                pColor = 'Black'
            else:
                pColor = 'White'
        except: 
            print('No background color given')
     if layer.kind == 'pixel' and layer.name.split(' ')[0] != 'Canvas': # Parse through images
            # save im loc
            layer_image = layer.composite()
            dir = 'Materials/Exit/%s.png' % imCnt#layer.name
            layer_image.save(dir)
            #
            layerCtr = layer.bbox[0] + (layer.bbox[2] - layer.bbox[0])/2 # Center position of layer            
            # Get in which third the element is :)
            print(layerCtr)
            print(ctr - maxW/10)
            if layerCtr < ctr + maxW/10 and layerCtr > ctr - maxW/10:
                pos = 'middle' #width: 50%                
                #script += '<img src = \"../Materials/Exit/'+str(imCnt)+'.png\" alt = \"img\" style = \" position: fixed;right:100px; left: 50%\" >\n </img>'                
            elif layerCtr > ctr + maxW/10:
                pos = 'right' #right: % diff # calc the distance from border :)
            elif layerCtr > ctr - maxW/10:
                pos = 'left' #left: % diff   # calc the distance from border :)sf
            # /Get third
            imCnt +=1
            
script += """</body>
</html>""" 
print(script)
f = open("Materials/test.html", "w")
f.write(script)
f.close()
os.system(r"D:\GameJams\psdWebReader\PythonApplication1\Materials\test.html")

