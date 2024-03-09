from BlurWindow.blurWindow import blur
import customtkinter as ctk
from PIL import Image, ImageTk
from ctypes import windll
import tkinter as tk

#FRESHGUI MODULE VERSION 0.4.2

projectName = 'FreshGUI'
projectVersion = '0.4.2'
projectAuthor = 'watakak'
githubRepo = f'https://github.com/{projectAuthor}/{projectName}'

root = tk.Tk()
buttons = []
dict = {}

def create(name='FreshGUI Window', size='400x300', icon='assets/FGUI.ico', resizable=True,
           transparency=False, focus=False, fullscreen=False):

    if logs:
        print(f'{projectName} | {projectVersion}\nMade by {projectAuthor}\n{githubRepo}\n')

    if icon == None:
        icon = 'assets/empty.ico'
    if name == None:
        name = ''

    root.title(name)
    root.geometry(size)
    root.resizable(width=resizable, height=resizable)
    root.iconbitmap(icon)
    root.config(background=themeBG)
    root.attributes('-topmost', focus, '-fullscreen', fullscreen)

    if transparency == True:
        window_blur = windll.user32.GetForegroundWindow()
        blur(window_blur, hexColor='#12121240')

def text(var='textVariable', text='FreshText', font=None, size=12, background=False, cornerRadius=5,
         position='center', up=0, down=0, left=0, right=0):
    if background == True:
        textColor = themeBG
        backgroundState = widgetsBG
    elif background == False:
        textColor = widgetsBG
        backgroundState = 'transparent'

    sizex = size / 0.3
    sizey = size / 0.6

    textLabel = ctk.CTkLabel(root, text=text, font=(font, size), width=sizex, height=sizey,
                             text_color=textColor, fg_color=backgroundState, corner_radius=cornerRadius)

    dict[var] = textLabel

    buttons.append((textLabel, position, {'up': up, 'down': down, 'left': left, 'right': right}))
    return textLabel

def button(var='buttonVariable', text='FreshButton', command=None, size=10, position='center',
           cursor='hand2', shape='rectangle', color=None, font=None, fontSize=12, image=None,
           imageResize=True, imagePlace='left', cornerRadius=7, borders=False,
           up=0, down=0, left=0, right=0, state='working'):

    if shape == 'rectangle':
        sizex = size / 0.06
        sizey = size / 0.265
    elif shape == 'square':
        sizex = size / 0.265
        sizey = size / 0.265
    else:
        if logs:
            print('FGUI ERROR: Shape must be "rectangle" or "square"')

    if image:
        image = tk.PhotoImage(file=image)

        if imageResize == True:
            reduction_factor = max(1, 2 ** ((image.width() * image.height()) // (120 * 120)))
            image = image.subsample(reduction_factor)

    if state == 'working':
        state = 'normal'
    elif state == 'disabled':
        cursor = 'arrow'

    if color == None:
        fgColor = widgetsBG
        hoverColor = activeWidgetsBG
    elif color == 'red':
        fgColor = '#D53D3D'
        hoverColor = '#CC2C2C'
    elif color == 'blue':
        fgColor = '#4E559A'
        hoverColor = '#3D4278'
    elif color == 'green':
        fgColor = '#2DB92D'
        hoverColor = '#28A528'
    else:
        fgColor = widgetsBG
        hoverColor = activeWidgetsBG

    button = ctk.CTkButton(root, text=text, width=sizex, height=sizey, corner_radius=cornerRadius,
                              cursor=cursor, image=image, state=state, compound=imagePlace,
                              border_width=borders, fg_color=fgColor, hover_color=hoverColor,
                              border_color=borderColor, text_color=textColor, font=(font, fontSize),
                              command=command)

    dict[var] = button

    buttons.append((button, position, {'up': up, 'down': down, 'left': left, 'right': right}))
    return button

def imageButton(var='buttonVariable', image=None, command=None, size=None, position='center',
                cursor='hand2', up=0, down=0, left=0, right=0, filtering='smooth',
                state='working'):
    if image == None:
        image = 'assets/FGUI.ico'
        size = 15

    image = Image.open(image)

    if filtering == 'smooth':
        imageFiltering = Image.BILINEAR
    elif filtering == 'pixel':
        imageFiltering = Image.NEAREST

    if size != None:
        imageSize = size / 0.265
        imageResolution = image.size

        new_size = (size * 2, size * 2)

        image = image.resize((int(imageSize), int(imageSize)), imageFiltering)
    elif size == None:
        imageSize = None

    photo = ImageTk.PhotoImage(image)

    if state == 'working':
        state = 'normal'
    elif state == 'disabled':
        cursor = 'arrow'

    button = tk.Button(root, image=photo, width=imageSize, height=imageSize, cursor=cursor,
                             state=state, command=command, bd=0, background=themeBG,
                             activebackground=themeBG)
    button.image = photo

    dict[var] = button

    buttons.append((button, position, {'up': up, 'down': down, 'left': left, 'right': right}))
    return button

def updateButtonPositions():
    new_width = root.winfo_width()
    new_height = root.winfo_height()

    for button, position, offsets in buttons:
        x_offset = offsets.get('right', 0) - offsets.get('left', 0)
        y_offset = offsets.get('down', 0) - offsets.get('up', 0)

        if 'center' in position:
            new_x = (new_width - button.winfo_reqwidth()) / 2 + x_offset
            new_y = (new_height - button.winfo_reqheight()) / 2 + y_offset
        elif 'topLeft' in position:
            new_x = 0 + x_offset
            new_y = 0 + y_offset
        elif 'topRight' in position:
            new_x = new_width - button.winfo_reqwidth() + x_offset
            new_y = 0 + y_offset
        elif 'bottomLeft' in position:
            new_x = 0 + x_offset
            new_y = new_height - button.winfo_reqheight() + y_offset
        elif 'bottomRight' in position:
            new_x = new_width - button.winfo_reqwidth() + x_offset
            new_y = new_height - button.winfo_reqheight() + y_offset
        elif 'left' in position:
            new_x = 0 + x_offset
            new_y = (new_height - button.winfo_reqheight()) / 2 + y_offset
        elif 'right' in position:
            new_x = new_width - button.winfo_reqwidth() + x_offset
            new_y = (new_height - button.winfo_reqheight()) / 2 + y_offset
        elif 'top' in position:
            new_x = (new_width - button.winfo_reqwidth()) / 2 + x_offset
            new_y = 0 + y_offset
        elif 'bottom' in position:
            new_x = (new_width - button.winfo_reqwidth()) / 2 + x_offset
            new_y = new_height - button.winfo_reqheight() + y_offset

        button.place(x=new_x, y=new_y)

def menu(var='menuVariable', options=1):
    dict[var] = tk.Menu(root)

    menu = tk.Menu(dict[var], tearoff=0)

    if options > 0:
        for i in range(1, options + 1):
            dict[var].add_cascade(label=f'Option{i}', menu=menu)

    root.config(menu=dict[var])

def settings(theme='Light', debug=False, language='English'):
    global themeBG, widgetsBG, activeWidgetsBG, borderColor, textColor
    global logs

    logs = debug

    if theme == 'Dark':
        themeBG = '#1F1F1F'
        widgetsBG = '#E0E0E0'
        activeWidgetsBG = '#BDBDBD'
        borderColor = '#868686'
        textColor = '#1F1F1F'
    elif theme == 'Light':
        themeBG = '#E0E0E0'
        widgetsBG = '#2E2E2E'
        activeWidgetsBG = '#1F1F1F'
        borderColor = '#868686'
        textColor = '#E0E0E0'
    else:
        print("This Theme doesn't exists!")

def exit():
    root.quit()

def run():
    root.mainloop()

settings()
root.bind("<Configure>", lambda event: updateButtonPositions())
