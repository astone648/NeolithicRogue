#This area holds the basic terrain and location of stuff for a displayed zone

class Area:
    def __init__(self, x, y, h, w, areaType, name, floorColor, objList = [], animalList = []):
        self.x = x
        self.y = y
        self.height = h
        self.width = w
        self.areaType = areaType
        self.name = name
        self.centerx = self.width//2
        self.centery = self.height//2
        self.floorColor = floorColor
        self.objList = objList
        self.animalList = animalList

    def draw(self, console, topx, topy, sw, sh):
        for drawx in range(0, sw):
            for drawy in range (0, sh):
                console.draw_char(drawx-topx, drawy-topy, ' ', bg=self.floorColor)
        for obj in self.objList:
            obj.draw(console, topx, topy, sw, sh)
        for animal in self.animalList:
            animal.draw(console, topx, topy, sw, sh)

    def clear(self, console, topx, topy, sw, sh, clearbg=None):
        for drawx in range(0, sw):
            for drawy in range (0, sh):
                console.draw_char(drawx-topx, drawy-topy, ' ', bg=clearbg)
        for obj in self.objList:
            obj.clear(console, topx, topy, sw, sh, clearbg)
        for animal in self.animalList:
            animal.clear(console, topx, topy, sw, sh, clearbg)