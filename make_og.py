from PIL import Image, ImageDraw, ImageFont
import random
W,H=1200,630
img=Image.new("RGB",(W,H),"#1f2a24")
d=ImageDraw.Draw(img)
# subtle gradient
for y in range(H):
    t=y/H
    c=(int(31+12*t),int(42+10*t),int(36+6*t))
    d.line([(0,y),(W,y)],fill=c)
def font(sz,bold=False):
    for p in (["/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"] if bold else ["/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]):
        try: return ImageFont.truetype(p,sz)
        except OSError: pass
    return ImageFont.load_default()
# shelf of books at the bottom
random.seed(7)
pal=["#c8553d","#f2a65a","#e9d8a6","#588157","#3a7ca5","#8d5a97","#d9a441","#b5838d","#6b9080","#a44a3f"]
shelf_y=560; x=60
while x<W-60:
    w=random.randint(26,52); h=random.randint(130,200)
    if False:
        # leaning book
        poly=[(x,shelf_y),(x+w,shelf_y),(x+w+h*0.35,shelf_y-h*0.94),(x+h*0.35,shelf_y-h*0.94)]
        d.polygon(poly,fill=random.choice(pal)); x+=int(w+h*0.35)+6; continue
    col=random.choice(pal)
    d.rectangle([x,shelf_y-h,x+w,shelf_y],fill=col)
    d.rectangle([x+4,shelf_y-h+14,x+w-4,shelf_y-h+20],fill="#00000033" if False else "#2b2b2b")
    d.rectangle([x+4,shelf_y-30,x+w-4,shelf_y-25],fill="#2b2b2b")
    x+=w+3
d.rectangle([40,shelf_y,W-40,shelf_y+18],fill="#8b5e34")
d.rectangle([40,shelf_y+18,W-40,shelf_y+24],fill="#5e3f22")
# text panel
d.rounded_rectangle([60,50,W-60,330],radius=28,fill="#fbf7ef")
d.text((100,82),"Book Catalog",font=font(84,True),fill="#1f2a24")
tf=font(36)
d.text((102,200),"Take a photo of your shelf and get a",font=tf,fill="#3d4a42")
d.text((102,248),"cataloged, valued, searchable library.",font=tf,fill="#3d4a42")
# badge
bf=font(24)
t="A Grok Bot template"; tw=d.textlength(t,font=bf)
d.rounded_rectangle([W-100-tw-40,86,W-100,128],radius=21,fill="#c8553d")
d.text((W-100-tw-20,93),t,font=bf,fill="#ffffff")
img.save("og-image.png",optimize=True)
print(img.size)
