from psd_tools import PSDImage
from PIL import Image

#INIT
script = '' #HTML code, components will be added later in code
pathf = 'Materials/test.psd'    #temp path value
psd = PSDImage.open(pathf)
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
            layer_image = layer.composite()
            dir = 'Materials/Exit/%s.png' % layer.name
            layerCtr = (layer.bbox[2] - layer.bbox[0])/2 # Center position of layer
            # Get in which third the element is :)
            if layerCtr < ctr + maxW/10 and layerCtr > ctr - maxW/10:
                pos = 'middle' #width: 50%
            elif layerCtr > ctr + maxW/10:
                pos = 'right' #right: pix diff
            elif layerCtr > ctr - maxW/10:
                pos = 'left' #left: pix diff
            # /Get third

            
         
