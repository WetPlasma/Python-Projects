import tkinter

window = tkinter.Tk()
window.title("Distance Converter")
convert = int(0)


def convertit():
    convert = float(inputmile.get()) * 1.6093
    output_label.config(text=f"{convert} Km")


# entry
inputmile = tkinter.Entry()
inputmile.grid(row=0, column=1)
miles_label = tkinter.Label(text="miles")
miles_label.grid(row=0, column=2)
equalto_laber = tkinter.Label(text="is equal to:")
equalto_laber.grid(row=1, column=0)
output_label = tkinter.Label(text="0 Km")
output_label.grid(row=1, column=1)
button = tkinter.Button(text="Calculate", command=convertit)
button.grid(row=2, column=1)


window.mainloop()
