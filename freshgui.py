from BlurWindow.blurWindow import blur
import customtkinter as ctk
from PIL import Image, ImageTk
from ctypes import windll
import tkinter as tk

#FRESHGUI MODULE VERSION 0.8.6

projectName = 'FreshGUI'
projectVersion = '0.8.6'
projectAuthor = 'watakak'
githubRepo = f'https://github.com/{projectAuthor}/{projectName}'

root = tk.Tk()
buttons = []
labels = []
dict = {}

root.title('FreshGUI Window')
root.geometry('400x300')
root.iconbitmap('assets/FGUI.ico')

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

def textWidget(bg=None, fg=None, font='Consolas', size=16, cursor=None, insertBlink=True, state='enabled',
               insertWidth=None, spacing=None, bordersWidth=2, scroll=False):
    bg = themeBG
    fg = activeWidgetsBG

    if insertBlink == True:
        insertBlink = 600
    elif insertBlink == False:
        insertBlink = 0
    else:
        insertBlink = insertBlink

    if scroll == True:
        print(True)

    text_area = tk.Text(wrap="word")
    text_area.config(background=bg, foreground=fg, font=(font, size), cursor=cursor, relief='flat',
                     insertofftime=insertBlink, insertontime=insertBlink, selectbackground=selectBG,
                     selectforeground=fg, insertbackground=fg, insertwidth=insertWidth, spacing3=spacing,
                     padx=bordersWidth, pady=bordersWidth)
    text_area.pack(expand=True, fill="both")

def text(var='textVariable', text='FreshText', font=None, size=12, color='themed',
         background=False, cornerRadius=5, position='center', up=0, down=0, left=0, right=0):
    if background == True:
        textColor = themeBG
        backgroundState = mainTextColor
    elif background == False:
        textColor = mainTextColor
        backgroundState = 'transparent'

    if color == 'themed':
        textColor = mainTextColor
    elif color == 'gray':
        textColor = '#868686'

    #Fonts
    #SF Pro Text Bold - Bold
    #SF Pro Text - Regular
    #SF Pro Text Regular - Thin

    sizex = size / 0.3
    sizey = size / 0.6

    textLabel = ctk.CTkLabel(root, text=text, font=(font, size), width=sizex, height=sizey,
                             text_color=textColor, fg_color=backgroundState, corner_radius=cornerRadius)

    dict[var] = textLabel

    buttons.append((textLabel, position, {'up': up, 'down': down, 'left': left, 'right': right}))
    return textLabel

def button(var='buttonVariable', text='FreshButton', command=None, size=10, position='center',
           cursor='hand2', shape='rectangle', color=None, font=None, fontSize=12, image=None,
           imageResize=True, imagePlace='left', imageSize=10, cornerRadius=7, borders=False,
           up=0, down=0, left=0, right=0, active=True, width=False, height=False):

    if shape == 'rectangle':
        sizex = size / 0.06
        sizey = size / 0.265
    elif shape == 'square':
        sizex = size / 0.265
        sizey = size / 0.265
    else:
        if logs:
            print('FGUI ERROR: Shape must be "rectangle" or "square"')

    if width and height:
        sizex = width
        sizey = height

    if image:
        image = tk.PhotoImage(file=image)

        if imageResize:
            max_width, max_height = sizex / 1.5, sizey / 1.5
            scale_factor = max(image.width() / max_width, image.height() / max_height, 1)
            reduction_factor = int(scale_factor)
            reduction_factor = max(1, reduction_factor)
            image = image.subsample(reduction_factor)

    if active == True:
        state = 'normal'
    else:
        state = 'disabled'
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
                active=True):
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

    if active == True:
        state = 'normal'
    else:
        state = 'disabled'
        cursor = 'arrow'

    button = tk.Button(root, image=photo, width=imageSize, height=imageSize, cursor=cursor,
                             state=state, command=command, bd=0, background=themeBG,
                             activebackground=themeBG)
    button.image = photo

    dict[var] = button

    buttons.append((button, position, {'up': up, 'down': down, 'left': left, 'right': right}))
    return button

def input(var='inputVariable', text='FreshInput', font=None, size=16, state='normal',
          show=None, position='center', up=0, down=0, left=0, right=0, cornerRadius=5, bordersWidth=2):

    entry = ctk.CTkEntry(root, font=(font, size), fg_color=mainTextColor,
                         text_color=themeBG, placeholder_text=text, placeholder_text_color='#868686',
                         corner_radius=cornerRadius, border_width=bordersWidth, state=state, show=show)

    dict[var] = entry

    buttons.append((entry, position, {'up': up, 'down': down, 'left': left, 'right': right}))
    return entry

def checkBox(var='checkBoxVariable', text='FreshCheckBox', position='center', up=0, down=0, left=0,
             right=0, command=None, size=10, cornerRadius=6, borderWidth=2):
    size = size * 2.5

    checkbox = ctk.CTkCheckBox(root, text=text, onvalue='on', offvalue='off', command=command,
                               checkbox_width=size, checkbox_height=size, corner_radius=cornerRadius,
                               border_width=borderWidth, fg_color=widgetsBG, border_color=widgetsBG,
                               hover_color=activeWidgetsBG, text_color=widgetsBG, checkmark_color=themeBG)

    dict[var] = checkbox

    buttons.append((checkbox, position, {'up': up, 'down': down, 'left': left, 'right': right}))
    return checkbox

def checkBoxState(var='checkBoxVariable'):
    # Assuming dict is accessible here
    if var in dict:
        checkbox = dict[var]
        state = checkbox.get()  # Assuming your checkbox widget has a get() method
        if state == 'on':
            return True
        else:
            return False
    else:
        print('Checkbox variable', var, 'not found.')
        return None

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

def scene(scene='scene'):
    print(scene)

def settings(theme='light', debug=False, language='English'):
    global themeBG, widgetsBG, activeWidgetsBG, borderColor, textColor, selectBG, mainTextColor
    global logs

    logs = debug

    if theme == 'dark':
        themeBG = '#1F1F1F'
        widgetsBG = '#E0E0E0'
        mainTextColor = '#E0E0E0'
        activeWidgetsBG = '#BDBDBD'
        borderColor = '#868686'
        textColor = '#1F1F1F'
        selectBG = '#191919'
    elif theme == 'light':
        themeBG = '#E0E0E0'
        widgetsBG = '#2E2E2E'
        mainTextColor = '#2E2E2E'
        activeWidgetsBG = '#1F1F1F'
        borderColor = '#868686'
        textColor = '#E0E0E0'
        selectBG = '#C7C7C7'
    elif theme == 'default':
        themeBG = '#FFFFFF'
        widgetsBG = '#9E9E9E'
        mainTextColor = '#000000'
        activeWidgetsBG = '#757575'
        borderColor = '#868686'
        textColor = '#000000'
        selectBG = '#C7C7C7'
    else:
        print("This Theme doesn't exists!")

def exit():
    root.quit()

def run():
    root.mainloop()

settings()
root.bind("<Configure>", lambda event: updateButtonPositions())