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
siteName = ''
headerScr = ''

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
    if layer.name == 'SiteName':
        left = layer.bbox
        siteName = layer.text
        f = layer.bbox[3]- layer.bbox[1]
        top =layer.bbox[1]#(f/maxH)*100#-layer.bbox[1] str(layer.bbox[0]/2)
        padding = 'left: ' + str((layer.bbox[0]/maxW)*100) + '%;'
        headerScr = '<h1 style = \"font-size: 48px;position:fixed; '+ str(padding) + 'top: ' + str(top) + 'px; margin-top: ' + str(0) + 'px\">' + siteName + '</h1>'
        script += headerScr
        break
#/INIT



for layer in psd:
     if layer.kind == 'pixel' and layer.name.split(' ')[0] != 'Canvas': # Parse through images
            # save im loc
            layer_image = layer.composite()
            dir = 'Materials/Exit/%s.png' % imCnt#layer.name
            layer_image.save(dir)
            padding = ''
            #
            layerCtr = layer.bbox[0] + (layer.bbox[2] - layer.bbox[0]) # Center position of layer            
            # Get in which third the element is :)
            print(layerCtr)
            print(ctr - maxW/10)
            #top = layer.bbox[1]
            top = (layer.bbox[1]/maxH)*100
            print(top)
            #get posX
            padding = 'left: ' + str((layer.bbox[0]/maxW)*100) + '%;'
            if layer.name.split(' ')[0] != 'Header':
            #get width
                if maxW - layer.bbox[2] < 20 and layer.bbox[0] < 20:
                    width = 'width: 100%'
                else:
                    PercAll = ((layer.bbox[2] - layer.bbox[0])/maxW)*100
                    width = 'min-width: ' + str(PercAll - PercAll/3) + '%; max-width: ' + str(PercAll + PercAll/3) + '%;'
                if 'Button' in layer.name: #This is a fucking abomination, not sure how to replace :/
                    script += '<a href = \"https://www.abv.bg/\" >\n'
                script += '<img src = \"../Materials/Exit/' + str(imCnt) + '.png\" alt = \"img\" style = \" position: absolute; ' + padding + ' top: ' + str(top) + '%; ' +width + '\">\n'
                if 'Button' in layer.name: #This is a fucking abomination, not sure how to replace :/
                    script += '</a>\n'
            else:
                height = layer.bbox[3]/2
                script += '<div style = \"padding:' + str(height) + 'px; margin-top: 0px; background: #' +  layer.name.split(' ')[1] + ';\">\n'
                #script += headerScr
                script += '</div>'
      #          script += SiteName
                
                #script += '<h1 style = \ font-size:large;\">' + siteName + '</h1>'
                #class = \"header\"
            imCnt +=1
            
script += """</body>
</html>""" 
print(script)
f = open("Materials/test.html", "w")
f.write(script)
f.close()
os.system(r"D:\GameJams\psdWebReader\PythonApplication1\Materials\test.html")

