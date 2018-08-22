from guizero import App, PushButton

# method to set the key or combination for each button
def map_key(keynumber):
    print(keynumber)

app = App(title="Keypad example", width=200, height=90, layout="grid")
button1 = PushButton(app, command=map_key, args=[1], text="1", grid=[0,0])
button2 = PushButton(app, command=map_key, args=[2], text="2", grid=[1,0])
button3 = PushButton(app, command=map_key, args=[3], text="3", grid=[2,0])
button4 = PushButton(app, command=map_key, args=[4], text="4", grid=[3,0])
button5 = PushButton(app, command=map_key, args=[5], text="5", grid=[0,1])
button6 = PushButton(app, command=map_key, args=[6], text="6", grid=[1,1])
button7 = PushButton(app, command=map_key, args=[7], text="7", grid=[2,1])
button8 = PushButton(app, command=map_key, args=[8], text="8", grid=[3,1])
app.display()