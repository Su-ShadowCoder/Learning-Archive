import pyjokes
from tkinter import ttk


window_name = (" Joke-Generator")

import tkinter as tk
# Create the main window
root = tk.Tk()
root.title(f"🤡{window_name}")


#height and width
window_width = 900
window_height = 400

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width // 2 - window_width / 2)
center_y = int(screen_height // 2 - window_height/ 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# icon
root.icon_image = tk.PhotoImage(file="jester2.png")
root.iconphoto(True, root.icon_image)

# Add a label to the window
label = tk.Label(root, text="Asalaam alaykum.\n\nPeace be upon you.")
label.pack(pady=20)

#  press button for joke. the button is the image of the justerhat. 



def joke_button():
    joke = pyjokes.get_joke()
    return label.config(text=f"{joke}")

# print(joke_button())


joke_button = tk.Button(root, text="Click for joke", command= joke_button)

joke_button.pack(ipadx=5, ipady=5, expand=True)




exit_button = tk.Button(
    root,
    text="Stop joking    (exit)",
    command=lambda: root.quit()
)

exit_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

# Start the Tkinter event loop
root.mainloop()



