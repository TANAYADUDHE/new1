import tkinter as tk

root = tk.Tk()
root.title("Birthday Surprise 🎉")
root.geometry("700x450")
root.configure(bg="#4ADFD0")  # 🌸 Soft Peach Pink

current_slide = 0
frames = []

def show_slide(index):
    for frame in frames:
        frame.pack_forget()
    frames[index].pack(fill="both", expand=True)

# -------- Slide 1 --------
slide1 = tk.Frame(root, bg="#8FEAE3")
tk.Button(slide1, text="🎁 Tap to Open 🎁",
          font=("Arial", 18), bg="#8FEAE3", fg="#4A4E69",
          command=lambda: next_slide()).pack(expand=True)
frames.append(slide1)

# -------- Slide 2 --------
slide2 = tk.Frame(root, bg="#F295AE")
tk.Label(slide2, text="Hey You 💖\nSomething Special Awaits...",
         font=("Arial", 20), fg="#4A4E69", bg="#F295AE").pack(expand=True)
tk.Button(slide2, text="Next ➡",
          bg="#FFB3C6", fg="#4A4E69",
          command=lambda: next_slide()).pack(pady=20)
frames.append(slide2)

# -------- Slide 3 --------
slide3 = tk.Frame(root, bg="#F295AE")
tk.Label(slide3,
         text="You make every moment beautiful 🌸\nStay happy always!",
         font=("Arial", 18), fg="#4A4E69", bg="#F295AE").pack(expand=True)
tk.Button(slide3, text="Next ➡",
          bg="#FFB3C6", fg="#4A4E69",
          command=lambda: next_slide()).pack(pady=20)
frames.append(slide3)

# -------- Slide 4 --------
slide4 = tk.Frame(root, bg="#F295AE")
text_label = tk.Label(slide4, text="", font=("Courier", 14),
                      fg="#070A18", bg="#F295AE",
                      wraplength=600, justify="left")
text_label.pack(pady=40)

message = """Dear Special Person 💖,

Happy Birthday Dambo🐣!!! 🎂✨

You are truly amazing and bring so much joy to everyone.
May your life be filled with happiness and smiles 😊 & 
Thank you for always suporting me  

Stay amazing always 💫
Lots of Loveeeeeee & happiness💕
"""

def type_text(index=0):
    if index < len(message):
        text_label.config(text=message[:index+1])
        root.after(30, type_text, index+1)

tk.Button(slide4, text="Show Letter 💌",
          bg="#EFA939", fg="#4A4E69",
          command=lambda: type_text()).pack(pady=10)

tk.Button(slide4, text="Next ➡",
          bg="#EFA939", fg="#4A4E69",
          command=lambda: next_slide()).pack()

frames.append(slide4)

# -------- Slide 5 --------
slide5 = tk.Frame(root, bg="#E1F295")
tk.Label(slide5,
         text="🎉 HAPPY BIRTHDAY ADITYA🎉\nHave an amazing day!",
         font=("Arial", 24, "bold"),
         fg="#4A4E69", bg="#E1F295").pack(expand=True)

frames.append(slide5)

# -------- Navigation --------
def next_slide():
    global current_slide
    current_slide += 1
    if current_slide < len(frames):
        show_slide(current_slide)

show_slide(0)
root.mainloop()
