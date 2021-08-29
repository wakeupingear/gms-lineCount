import tkinter.filedialog
import tkinter as tk
import json5 as json

spriteKeys=["spr","s"]
objectKeys=["obj","o","npc"]
roomKeys=["room","r"]
soundKeys=["sound"]
scriptKeys=["script"]
fontKeys=["f"]
timelineKeys=["t"]
shaderKeys=["sh"]
pathKeys=["path"]
sequenceKeys=["seq"]

def isType(name,keys):
    for s in keys:
        if name.find(s)==0: return True
    return False

def open_file():
    filename = tkinter.filedialog.askopenfilename(
        initialdir=r"C:\Users\willf\Desktop\Outset Data\Builds\Outset.",
        title="Select a GameMaker Project",
        filetypes=[("2.0+ Project", "*.yyp")],
    )
    f=open(filename, "r")
    data=json.load(f)

    sprites=[]
    objects=[]
    rooms=[]
    paths=[]
    sounds=[]
    sequences=[]
    shaders=[]
    fonts=[]
    timelines=[]
    scripts=[]
    for (resource) in data["resources"]:
        arr=[resource["id"]["name"],resource["id"]["path"]]
        if isType(arr[0],soundKeys):
            sounds.append(arr)
        elif isType(arr[0],objectKeys):
            objects.append(arr)
        elif isType(arr[0],roomKeys):
            rooms.append(arr)
        elif isType(arr[0],scriptKeys):
            scripts.append(arr)
        elif isType(arr[0],fontKeys):
            fonts.append(arr)
        elif isType(arr[0],timelineKeys):
            timelines.append(arr)
        elif isType(arr[0],shaderKeys):
            shaders.append(arr)
        elif isType(arr[0],pathKeys):
            paths.append(arr)
        elif isType(arr[0],sequenceKeys):
            sequences.append(arr)
        elif isType(arr[0],spriteKeys):
            sprites.append(arr)
        else:
            print("Unknown type: "+arr[0])
    
    print("Sprites: "+str(len(sprites)))
    print("Objects: "+str(len(objects)))
    print("Rooms: "+str(len(rooms)))
    print("Paths: "+str(len(paths)))
    print("Sounds: "+str(len(sounds)))
    print("Sequences: "+str(len(sequences)))
    print("Shaders: "+str(len(shaders)))
    print("Fonts: "+str(len(fonts)))
    print("Timelines: "+str(len(timelines)))
    print("Scripts: "+str(len(scripts)))


def main():
    root = tk.Tk()
    root.title("GameMaker Line Counter")
    root.resizable(False, False)
    root.geometry("300x150")

    open_button = tk.Button(root, text="Open a File", command=open_file)
    open_button.pack(expand=True)

    root.mainloop()


if __name__ == "__main__":
    main()
