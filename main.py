from tkinter import *
from tkinter import filedialog

from commads import *

def main():
    root = Tk()
    root.title('TEDITOR -- yeffEJ')
    root.geometry("1000x600")
    # root.minsize()
    # root.maxsize()
    # root.iconbitmap('')

    text = Text(root, width=1000, height=600)
    text.pack()

    menu_bar = Menu(root)
    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label='open file', command=open_file)
    file_menu.add_command(label='new file', command=new_file)
    file_menu.add_command(label='save file', command=save_file)
    file_menu.add_command(label='save file as', command=save_file_as)
    file_menu.add_separator()
    file_menu.add_command(label='quit', command=root.quit)
    menu_bar.add_cascade(label='menu', menu=file_menu)

    root.config(menu=menu_bar)
    root.mainloop()


if __name__ == '__main__':
    main()