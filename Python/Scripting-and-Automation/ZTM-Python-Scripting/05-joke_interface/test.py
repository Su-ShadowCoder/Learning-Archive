# import tkinter as tk

# root = tk.Tk()
# root.title("Interactive Example")

# # 1. Create a label to display a message
# message_label = tk.Label(root, text="Initial Message")
# message_label.pack(pady=20)

# # 2. Define the event handler function
# def update_message():
#     message_label.config(text="Button Clicked! Label Updated.") # Use .config() to change options

# # 3. Create the button and link the handler
# update_button = tk.Button(root, text="Update Text", command=update_message)
# update_button.pack()



# root.mainloop()

import pyjokes



print(pyjokes.get_joke())