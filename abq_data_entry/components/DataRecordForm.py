import tkinter as tk
from tkinter import ttk

from .LabelInput import LabelInput


class DataRecordForm(tk.Frame):
    """The input form for our widgets"""

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        # A dict to keep track of input widgets
        self.inputs = {}

        # Build the form
        # recordinfo section
        recordinfo = tk.LabelFrame(self, text="Record Information")

        # line 1
        self.inputs["Date"] = LabelInput(recordinfo, "Date", input_var=tk.StringVar())
        self.inputs["Date"].grid(row=0, column=0)
        self.inputs["Time"] = LabelInput(
            recordinfo,
            "Time",
            input_class=ttk.Combobox,
            input_var=tk.StringVar(),
            input_args={"values": ["8:00", "12:00", "16:00", "20:00"]},
        )
        self.inputs["Time"].grid(row=0, column=1)
        self.inputs["Technician"] = LabelInput(
            recordinfo, "Technician", input_var=tk.StringVar()
        )
        self.inputs["Technician"].grid(row=0, column=2)

        # line 2
        self.inputs["Lab"] = LabelInput(
            recordinfo,
            "Lab",
            input_class=ttk.Combobox,
            input_var=tk.StringVar(),
            input_args={"values": ["A", "B", "C", "D", "E"]},
        )
        self.inputs["Lab"].grid(row=1, column=0)
        self.inputs["Plot"] = LabelInput(
            recordinfo,
            "Plot",
            input_class=ttk.Combobox,
            input_var=tk.IntVar(),
            input_args={"values": list(range(1, 21))},
        )
        self.inputs["Plot"].grid(row=1, column=1)
        self.inputs["Seed sample"] = LabelInput(
            recordinfo, "Seed sample", input_var=tk.StringVar()
        )
        self.inputs["Seed sample"].grid(row=1, column=2)

        recordinfo.grid(row=0, column=0, sticky=(tk.W + tk.E))

        # Environment Data
        environmentinfo = tk.LabelFrame(self, text="Environment Data")
        self.inputs["Humidity"] = LabelInput(
            environmentinfo,
            "Humidity (g/m³)",
            input_class=tk.Spinbox,
            input_var=tk.DoubleVar(),
            input_args={"from_": 0.5, "to": 52.0, "increment": 0.01},
        )
        self.inputs["Humidity"].grid(row=0, column=0)
        self.inputs["Light"] = LabelInput(
            environmentinfo,
            "Light (klx)",
            input_class=tk.Spinbox,
            input_var=tk.DoubleVar(),
            input_args={"from_": 0, "to": 100, "increment": 0.01},
        )
        self.inputs["Light"].grid(row=0, column=1)
        self.inputs["Temperature"] = LabelInput(
            environmentinfo,
            "Temperature (°C)",
            input_class=tk.Spinbox,
            input_var=tk.DoubleVar(),
            input_args={"from_": 4, "to": 40, "increment": 0.01},
        )
        self.inputs["Temperature"].grid(row=0, column=2)
        self.inputs["Equipment Fault"] = LabelInput(
            environmentinfo,
            "Equipment Fault",
            input_class=ttk.Checkbutton,
            input_var=tk.BooleanVar(),
        )
        self.inputs["Equipment Fault"].grid(row=1, column=0, columnspan=3)
        environmentinfo.grid(row=1, column=0, sticky=(tk.W + tk.E))

        # Plant Data section
        plantinfo = tk.LabelFrame(self, text="Plant Data")

        self.inputs["Plants"] = LabelInput(
            plantinfo,
            "Plants",
            input_class=tk.Spinbox,
            input_var=tk.IntVar(),
            input_args={"from_": 0, "to": 20},
        )
        self.inputs["Plants"].grid(row=0, column=0)
        self.inputs["Blossoms"] = LabelInput(
            plantinfo,
            "Blossoms",
            input_class=tk.Spinbox,
            input_var=tk.IntVar(),
            input_args={"from_": 0, "to": 1000},
        )
        self.inputs["Blossoms"].grid(row=0, column=1)
        self.inputs["Fruit"] = LabelInput(
            plantinfo,
            "Fruit",
            input_class=tk.Spinbox,
            input_var=tk.IntVar(),
            input_args={"from_": 0, "to": 1000},
        )
        self.inputs["Fruit"].grid(row=0, column=2)

        # Height data
        self.inputs["Min Height"] = LabelInput(
            plantinfo,
            "Min Height (cm)",
            input_class=tk.Spinbox,
            input_var=tk.DoubleVar(),
            input_args={"from_": 0, "to": 1000, "increment": 0.01},
        )
        self.inputs["Min Height"].grid(row=1, column=0)
        self.inputs["Max Height"] = LabelInput(
            plantinfo,
            "Max Height (cm)",
            input_class=tk.Spinbox,
            input_var=tk.DoubleVar(),
            input_args={"from_": 0, "to": 1000, "increment": 0.01},
        )
        self.inputs["Max Height"].grid(row=1, column=1)
        self.inputs["Median Height"] = LabelInput(
            plantinfo,
            "Median Height (cm)",
            input_class=tk.Spinbox,
            input_var=tk.DoubleVar(),
            input_args={"from_": 0, "to": 1000, "increment": 0.01},
        )
        self.inputs["Median Height"].grid(row=1, column=2)

        plantinfo.grid(row=2, column=0, sticky=(tk.W + tk.E))

        # Notes section
        self.inputs["Notes"] = LabelInput(
            self, "Notes", input_class=tk.Text, input_args={"width": 75, "height": 10}
        )
        self.inputs["Notes"].grid(sticky=tk.W, row=3, column=0)

        # default the form
        self.reset()

    def get(self):
        """Retrieve data from form as a dict"""

        # We need to retrieve the data from Tkinter variables
        # and place it in regular Python objects

        data = {}
        for key, widget in self.inputs.items():
            data[key] = widget.get()
        return data

    def reset(self):
        """Resets the form entries"""

        # clear all values
        for widget in self.inputs.values():
            widget.set("")
