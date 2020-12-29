import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image,ImageTk,ImageEnhance, ImageFilter, ImageDraw
from tkinter import messagebox as mb

#CREATE MAIN WINDOW
window = tk.Tk()
window.title("Picturesque - Photo Editor")
window.configure(bg="lightcyan")
window.rowconfigure(2, minsize=600, weight=1)
window.columnconfigure(1, minsize=600, weight=1)
window.state('zoomed') #Fullscreen

#TOOLBAR
toolbar = tk.Frame(window, relief=tk.RAISED, bd=2)
toolbar.grid(row=0, column =0, padx = 4, sticky="ew", columnspan=400)

#FRAME - RIGHT
fr_filters = tk.Frame(window, relief=tk.RAISED, bd=2, width=100, height=100)
fr_filters.grid(column =2, row=1, padx = 4, sticky="ns", rowspan=2)

#FRAME - LEFT
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2, width =100, height=100, background = '#36CFC5')
fr_buttons.grid(column=0, row=1, sticky="ns", rowspan=2)

#MESSAGE YOU GET WHEN YOU HOVER OVER AN ICON
class CreateToolTip(object):
	def __init__(self, widget, text='widget info'):
		self.widget = widget
		self.text = text
		self.widget.bind("<Enter>", self.enter)
		self.widget.bind("<Leave>", self.close)
	def enter(self, event=None):
		x = y = 0
		x, y, cx, cy = self.widget.bbox("insert")
		x += self.widget.winfo_rootx() + 25
		y += self.widget.winfo_rooty() + 38
		self.tw = tk.Toplevel(self.widget) #Creates a toplevel window
		self.tw.wm_overrideredirect(True) #Leaves only the label and removes the app window
		self.tw.wm_geometry("+%d+%d" % (x, y))
		label = tk.Label(self.tw, text=self.text, justify='left', relief='solid', borderwidth=1, font=("tahoma", "10", "normal"))
		label.pack(ipadx=1)
	def close(self, event=None):
		if self.tw:
			self.tw.destroy()


#OPEN IMAGE FROM SYSTEM
def open_file():
	global my_image
	global y
	window.filename=askopenfilename(initialdir="/Users/sohamjain/Desktop",title="Select a file", filetypes=[("jpeg files","*.jpeg"),("jpg files","*.jpg"),("png files","*.png"),("All Files","*.*")])
	my_image=ImageTk.PhotoImage(Image.open(window.filename))
	my_image_label=tk.Label(window,image=my_image, background="lightcyan")
	my_image_label.grid(row=2,column=1,sticky="nsew")
	y=window.filename

img = Image.open("Icon_open.jpg")
open_img = ImageTk.PhotoImage(img)
OpenButton = Button(toolbar, image=open_img, relief=FLAT, command=open_file)
OpenButton.grid(row=0, column=0, ipadx=5, sticky="nsew")
CreateToolTip(OpenButton, text = ' Open a new image')


#SAVE CHANGES TO IMAGE	
def save():
	im2=Image.open("enhanced.sample5.png")
	im2.save(str(y))

img = Image.open("Icon_save.jpg")
save_img = ImageTk.PhotoImage(img)
SaveButton = Button(toolbar, image=save_img, relief=FLAT, command=save)
SaveButton.grid(row=0, column=1, sticky="nsew", ipadx=5)
CreateToolTip(SaveButton, text = 'Save changes')


#SAVE MODIFIED IMAGE AS A NEW FILE IN THE SYSTEM
def save_file():
	filepath = asksaveasfilename(
		defaultextension="txt",
		filetypes=[("Png Files", "*.png"), ("All Files", "*.*")],
	)
	im2=Image.open(str(y))
	im2.save(str(filepath))

img = Image.open("Icon_saveas.jpg")
saveas_img = ImageTk.PhotoImage(img)
SaveAsButton = Button(toolbar, image=saveas_img, relief=FLAT, command=save_file)
SaveAsButton.grid(row=0, column=2, sticky="nsew", ipadx=5)
CreateToolTip(SaveAsButton, text = 'Save as')


#DISPLAY CHANGES MADE ON TO THE SCREEN
def display():
	global path
	global img
	img = ImageTk.PhotoImage(Image.open("enhanced.sample5.png"))
	panel = tk.Label(window, image = img, background="lightcyan")
	panel.grid(row=2,column=1,sticky="nsew")

#BRIGHTEN THE IMAGE
def brighten():
	global im
	global enhancer_im
	global enhancer
	im = Image.open(str(y))
	enhancer = ImageEnhance.Brightness(im)
	enhanced_im = enhancer.enhance(horizontal_bri.get())
	enhanced_im.save("enhanced.sample5.png")
	display()

bri_label=Label(fr_buttons, text="BRIGHTNESS:", background="#36CFC5", font=('tahoma',10,'bold'))
bri_label.grid(row=4)
horizontal_bri=tk.Scale(fr_buttons,from_=0.0, to=2.0, resolution=0.1, orient= HORIZONTAL)
bright= tk.Button(fr_buttons,text="Brighten",command=brighten,highlightbackground='lavender')
horizontal_bri.grid(row=5,column=0,sticky="ew",padx=5,pady=5)
bright.grid(row=6, column=0, sticky="ew", padx=5,pady=5)


#APPLY CONTRAST TO THE IMAGE
def contras():
	global im
	global enhancer_im
	global enhancer
	im = Image.open(str(y))
	enhancer = ImageEnhance.Contrast(im)
	enhanced_im = enhancer.enhance(horizontal_con.get())
	enhanced_im.save("enhanced.sample5.png")
	display()

cont_label=Label(fr_buttons, text="CONTRAST:", background="#36CFC5", font=('tahoma',10,'bold'))
cont_label.grid(row=8)
horizontal_con=tk.Scale(fr_buttons,from_=0.0, to=2.0, resolution=0.1, orient= HORIZONTAL)
contrast=tk.Button(fr_buttons,text="Contrast",command=contras,highlightbackground='lavender')
horizontal_con.grid(row=9,column=0,sticky="ew",padx=5,pady=5)
contrast.grid(row=10, column=0, sticky="ew", padx=5,pady=5)


#SHARPEN THE IMAGE
def sharpen():
	global im
	global enhancer_im
	global enhancer
	im = Image.open(str(y))
	enhancer = ImageEnhance.Sharpness(im)
	enhanced_im = enhancer.enhance(horizontal_sha.get())
	enhanced_im.save("enhanced.sample5.png")
	display()

sharp_label=Label(fr_buttons, text="SHARPEN:", background="#36CFC5", font=('tahoma',10,'bold'))
sharp_label.grid(row=12)
horizontal_sha=tk.Scale(fr_buttons,from_=-4.0, to=4.0, resolution=0.5, orient= HORIZONTAL,highlightbackground='lavender')
sharp=tk.Button(fr_buttons,text="Sharpen",command=sharpen,highlightbackground='lavender')
horizontal_sha.grid(row=13,column=0,sticky="ew",padx=5,pady=5)
sharp.grid(row=14, column=0, sticky="ew", padx=5,pady=5)


#CROP AN IMAGE
def opencrop():
	global i
	top=tk.Toplevel()
	top.title("Crop Preview")
	def exitt():
		display()
		save()
		top.destroy()
	def callback():
	    if mb.askyesno('!', 'Save Changes?'):
	        mb.showwarning('Yes', 'Changes saved')
	        exitt()
	    else:
	        mb.showinfo('No', 'Exiting...')
	        top.destroy()
	def display1():
		global imgg
		imgg = ImageTk.PhotoImage(Image.open("enhanced.sample5.png"))
		panel = tk.Label(top, image = imgg)
		panel.grid(row=0,column=1,sticky="nsew")
		callback()
	def get_crop_start_xy(event):
		global x1,y1
		x1=event.x
		y1=event.y
	def get_crop_end_xy(event):
	    global x2,y2
	    x2=event.x
	    y2=event.y
	    crop()
	def crop():
		imageObject  = Image.open(str(y))
		cropped     = imageObject.crop((x1,y1,x2,y2))
		cropped.save("enhanced.sample5.png")
		display1()
	i=ImageTk.PhotoImage(Image.open(str(y)))
	my_image_lab=tk.Label(top,image=i)
	my_image_lab.grid(row=0,column=1,sticky="nsew")
	my_image_lab.bind("<Button-1>", get_crop_start_xy)
	my_image_lab.bind("<ButtonRelease-1>",get_crop_end_xy)


crop_button=tk.Button(fr_buttons,text="Crop Image",command=opencrop,highlightbackground='lavender')
crop_button.grid(row=16, column=0, sticky="ew", padx=5,pady=5)


#ROTATE CLOCKWISE - ROTATE RIGHT
def clockrotate():
	colorImage=Image.open(str(y))
	rotated     = colorImage.rotate(270,expand=1)
	rotated.save("enhanced.sample5.png")
	display()
	save()

clock_rotate_button=tk.Button(fr_buttons,text="Rotate Right",command=clockrotate,highlightbackground='lavender')
clock_rotate_button.grid(row=18,column=0,sticky="ew",padx=5,pady=5)


#ROTATE ANTI-CLOCKWISE - ROTATE LEFT
def antirotate():
	colorImage=Image.open(str(y))
	rotated     = colorImage.rotate(90,expand=1)
	rotated.save("enhanced.sample5.png")
	display()
	save()

anti_rotate_button= tk.Button(fr_buttons,text="Rotate Left",command=antirotate,highlightbackground='lavender')
anti_rotate_button.grid(row=17,column=0,sticky="ew",padx=5,pady=5)


#RESIZE IMAGE
def opensize():
	global i
	top=tk.Toplevel()
	top.title("Size Toolbar")
	def size(var):
		color_image = Image.open(str(y))
		im1 = color_image.resize((horizontal_size_width.get(),horizontal_size_height.get())) 
		im1.save("enhanced.sample5.png")
		display()
	i=Image.open(str(y))
	
	horizontal_size_width=tk.Scale(top,from_=0, to=i.width+200, resolution=5, orient= HORIZONTAL,command=size)
	horizontal_size_height=tk.Scale(top,from_=0, to=i.height+200, resolution=5, orient= HORIZONTAL,command=size)
	horizontal_size_width.set(i.width)
	horizontal_size_height.set(i.height)
	horizontal_size_width.grid(row=1,column=0,sticky="ew",padx=5,pady=5)
	horizontal_size_height.grid(row=2,column=0,sticky="ew",padx=5,pady=5)

resize_button=tk.Button(fr_buttons,text="Resize",command=opensize,highlightbackground='lavender')
resize_button.grid(row=19,column=0,sticky="ew",padx=5,pady=5)

#FILTERS
filters_label=Label(fr_filters, text="FILTERS", font=('tahoma',10,'bold'))
filters_label.grid(row=0)

#GRAYSCALE FILTER
def bw():
	color_image = Image.open(str(y))
	bw = color_image.convert('L')
	bw.save("enhanced.sample5.png")
	display()

img = Image.open("Filter_bw.jpg")
bw_img = ImageTk.PhotoImage(img)
bw_button = Button(fr_filters, image=bw_img, relief=FLAT, command=bw)
bw_button.grid(row=4, column=0, sticky="nsew", ipadx=5)
grayscale_label=Label(fr_filters, text="GRAYSCALE", font=('tahoma',10,'bold'))
grayscale_label.grid(row=8)


#SEPIA FILTER
def sepia():
    global img
    global enhancer_im
    global enhancer
    img = Image.open(str(y))
    width, height = img.size

    pixels = img.load() # create the pixel map

    for py in range(height):
        for px in range(width):
            r, g, b = img.getpixel((px, py))

            tr = int(0.393 * r + 0.769 * g + 0.189 * b)
            tg = int(0.349 * r + 0.686 * g + 0.168 * b)
            tb = int(0.272 * r + 0.534 * g + 0.131 * b)

            if tr > 255:
                tr = 255

            if tg > 255:
                tg = 255

            if tb > 255:
                tb = 255

            pixels[px, py] = (tr,tg,tb)
    img.save("enhanced.sample5.png")
    display()

img = Image.open("Filter_sepia.jpg")
sepia_img = ImageTk.PhotoImage(img)
sepia_button = Button(fr_filters, image=sepia_img, relief=FLAT, command=sepia)
sepia_button.grid(row=10, column=0, sticky="nsew", ipadx=5)
sepia_label=Label(fr_filters, text="SEPIA", font=('tahoma',10,'bold'))
sepia_label.grid(row=14)


#DEHAZE FILTER
def blur():
	im1 = Image.open(str(y))
	blurim = im1.filter(ImageFilter.BLUR) 
	blurim.save("enhanced.sample5.png")
	display()

img = Image.open("Filter_blur.jpg")
dehaze_img = ImageTk.PhotoImage(img)
dehaze_button = Button(fr_filters, image=dehaze_img, relief=FLAT, command=blur)
dehaze_button.grid(row=16, column=0, sticky="nsew", ipadx=5)
dehaze_label=Label(fr_filters, text="DEHAZE", font=('tahoma',10,'bold'))
dehaze_label.grid(row=20)


#CONTOUR FILTER
def contour():
	im1 = Image.open(str(y))
	blurim = im1.filter(ImageFilter.CONTOUR) 
	blurim.save("enhanced.sample5.png")
	display()

img = Image.open("Filter_contour.jpg")
contour_img = ImageTk.PhotoImage(img)
contour_button = Button(fr_filters, image=contour_img, relief=FLAT, command=contour)
contour_button.grid(row=22, column=0, sticky="nsew", ipadx=5)
contour_label=Label(fr_filters, text="CONTOUR", font=('tahoma',10,'bold'))
contour_label.grid(row=26)



#HELP WINDOW
def help_index():
	HelpWindow = Toplevel()
	HelpWindow.title("Help")
	HelpWindow.resizable(width="False", height="False")
	image = ImageTk.PhotoImage(Image.open('Menu_help.png'))
	panel = Label(HelpWindow, image=image)
	panel.image = image
	panel.pack()

img = Image.open("Icon_help.jpg")
help_img = ImageTk.PhotoImage(img)
HelpButton = Button(toolbar, image=help_img, relief=FLAT, command=help_index)
HelpButton.grid(row=0, column=3, sticky="nsew", ipadx=5)
CreateToolTip(HelpButton, text = 'Help')


#ABOUT WINDOW
def About():
	AboutWindow = Toplevel()
	AboutWindow.title("About Picturesque")
	AboutWindow.resizable(width="False", height="False")
	image = ImageTk.PhotoImage(Image.open('Menu_about.png'))
	panel = Label(AboutWindow, image=image)
	panel.image = image
	panel.pack()

img = Image.open("Icon_about.jpg")
about_img = ImageTk.PhotoImage(img)
AboutButton = Button(toolbar, image=about_img, relief=FLAT, command=About)
AboutButton.grid(row=0, column=4, sticky="nsew", ipadx=5)
CreateToolTip(AboutButton, text = 'About')


#TEST - IGNORE
def donothing():
	filewin = Toplevel(window)
	button = Button(filewin, text="Do nothing button")
	button.pack()


#MENU
menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="Save as", command=save_file)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=help_index)
helpmenu.add_command(label="About...", command=About)
menubar.add_cascade(label="Help", menu=helpmenu)

window.config(menu=menubar)


#EMPTY LABELS

#BUTTONS
empty_label=Label(fr_buttons, background="#36CFC5", font=('tahoma',10,'bold'))
empty_label.grid(row=7)

empty_label=Label(fr_buttons, background="#36CFC5", font=('tahoma',10,'bold'))
empty_label.grid(row=11)

empty_label=Label(fr_buttons, background="#36CFC5", font=('tahoma',10,'bold'))
empty_label.grid(row=15)

#FILTERS
empty_label=Label(fr_filters, font=('tahoma',10,'bold'))
empty_label.grid(row=2)

empty_label=Label(fr_filters, font=('tahoma',10,'bold'))
empty_label.grid(row=9)

empty_label=Label(fr_filters, font=('tahoma',10,'bold'))
empty_label.grid(row=15)

empty_label=Label(fr_filters, font=('tahoma',10,'bold'))
empty_label.grid(row=21)

window.mainloop()
