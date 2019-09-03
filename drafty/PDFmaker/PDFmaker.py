from PIL import Image
import random
def makePDF(player_list):
    template = Image.open('./drafty/PDFmaker/pageTemplate.jpg')
    blank_card = Image.new('RGB', (2626,1875), color=(255,255,255))
    opened_list = []
    pages = []
    #test_list = ['Masons1','Masons2','Masons3','Masons4','Masons5']
    filename = 'output' + str(random.randrange(100,999)) + str(random.randrange(100,999)) + '.pdf'

    for i in player_list:
        opened_list.append(Image.open('./drafty/PDFmaker/Cards/' + i + '.jpg'))

    def page_maker(cards):
        #global pages
        #global template
        i = 0

        while len(cards) % 4 != 0:
            cards.append(blank_card)

        for card in cards:
            if i == 0:
                template.paste(card, (305,198))
            elif i == 1:
                template.paste(card, (3041,198))
            elif i == 2:
                template.paste(card, (305,2185))
            elif i == 3:
                template.paste(card, (3041,2185))

            i += 1

            if i > 3:
                pages.append(template.copy())
                i = 0


    page_maker(opened_list)
    pages[0].save('./drafty/download/' + filename, save_all=True, resolution=500, append_images=pages[1:])

    return filename

         