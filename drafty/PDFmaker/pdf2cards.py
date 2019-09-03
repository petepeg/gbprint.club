from pdf2image import convert_from_path
from PIL import Image
import glob
#import sys than use sys.argv[i] i0 is the script name

#converts pdf into jpg, assigns pages to a list
#images are 1375x1875, whole card should be 2626,1876. 62 pixels are trimmed off front right and back left

source_files = glob.glob("./source_pdfs/*.pdf")
for path in source_files:
    guild_name = path[20:-10]
    pages = convert_from_path(path, 500)

    blank_card = Image.new('RGB', (2626,1875), color=0)

#crop, paste onto template, print to file
    j = 0
    for i, page in enumerate(pages) :
        if i % 2 == 0:
            page_crop = page.crop((64,0,1375,1875))
            #cards_back.append(page_crop)
            blank_card.paste(page_crop,(1314,0))
        else:
            page_crop = page.crop((0,0,1313,1875))
            #cards_front.append(page_crop)
            blank_card.paste(page_crop,(0,0))
            path = './Cards/' + guild_name + str(j) + '.jpg'
            blank_card.save(path, 'JPEG')
            j += 1