import tkinter as tk
from tkinter import filedialog, Tk, messagebox
import os

class To_do_List:

    #this is the constructor of the window
    def __init__(self, main):
        self.main = main
        self.main.title("To-Do-List")
        self.main.geometry("500x500") #This will be the size of the main window
        self.lists = {}
        self.main_menu()

    #main menu function
    def main_menu(self):
        #Paste the directory path here in which you want to save your lists
        directory_path = "C:/Users/HRISHIKESH/OneDrive/Desktop/Raj Folder/Secure Folder/Private/Python_Internship/"
        for widget in self.main.winfo_children():  # This for loop is used for creating multiple windows inside of a parent window without disrupting the widgets of
            widget.destroy()                                                                #parent and nor child window. It uses the winfo_children() method in tkinter library
                                                                                            
        tk.Label(self.main, text="To-Do-List", font=("Helvetica ", 20)).pack(pady=10)  #Here the font and font size are placed in the font= ()       
        tk.Button(self.main, text="Create New List", command=self.create_new_list, height = 2, width = 15).pack(pady=10)
        tk.Button(self.main, text="View Lists", command=lambda path=directory_path: self.view_lists(path), height=2, width=15).pack(pady=10)
        tk.Button(self.main, text="Close", command=self.main.quit, height=2, width=15).pack(pady=10)
    
    def create_new_list(self):
        for widget in self.main.winfo_children():
            widget.destroy()
        
        tk.Label(self.main, text="Create New List", font=("Helvetica", 16)).pack(pady=10)
        
        name_label = tk.Label(self.main, text="List Name:") 
        name_label.pack(pady=5)
        
        name_entry = tk.Entry(self.main) #takes the name of the file input here...
        name_entry.pack(pady=5)
        
        items_label = tk.Label(self.main, text="Items (separated by commas):") 
        items_label.pack(pady=5)
        
        items_entry = tk.Entry(self.main) #Here goes the elements of your list...
        items_entry.pack(pady=5) #(.pack) function places the widget in the center of the window by default...
        
        save_button = tk.Button(self.main, text="Save List", command=lambda: self.save_list(name_entry.get(), items_entry.get()))
        save_button.pack(pady=10)

        back_button = tk.Button(self.main, text="Back to Main Menu", command=self.main_menu) 
        back_button.pack(pady=10)
    
    def save_list(self, name, items):
        if name and items:
            items = [item.strip() for item in items.split(",")] #separates the items received from the items_entry variables with comma(,) using for loop
            self.lists[name] = items
            self.view_list(name)

    def save_list_as_text_file(self, name): #this funtion initiates the filedialog and saves the list created on this app as text file 
        print(f"Saving list: {name}")
        if name in self.lists:
            print(f"List found: {self.lists[name]}")
            root = Tk()
            root.withdraw() #This line calls the withdraw() method on the root window to hide it from view. This is done because we only need to display the file dialog, not the main window itself.
            file_path = filedialog.asksaveasfilename(initialdir="C:/Users/HRISHIKESH/OneDrive/Desktop/Raj Folder/Secure Folder/Private/Python_Internship/", title="Save as Text File",initialfile=name, filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")), defaultextension=".txt")
           #This line calls the asksaveasfilename() function from the filedialog module to display a file dialog that allows the user to choose where to save the text file. #
           #The function takes several options that control its behavior, 
           #such as initialdir, which sets the initial directory displayed in the dialog, title, which sets the title of the dialog window, filetypes, which sets the types of files that can be selected, 
           #and defaultextension, which sets the default extension for the saved file. 
           #The function returns the path chosen by the user or an empty string if they canceled or closed the dialog.

            print(f"File path: {file_path}") 
            if file_path:
                with open(file_path, "w") as f:
                    for i, item in enumerate(self.lists[name]):
                        f.write(f"{i+1}. {item}\n")
                        
    def view_lists(self, directory_path):
        for widget in self.main.winfo_children():
            widget.destroy()

        tk.Label(self.main, text="View Lists", font=("Helvetica", 16)).pack(pady=10)

        items = os.listdir(directory_path)

        for item in items:
            full_path = os.path.join(directory_path, item)
            if os.path.isfile(full_path) and item.endswith('.txt'):
                frame = tk.Frame(self.main)
                frame.pack(anchor="w", padx=20, pady=5)

                tk.Label(frame, text=item).pack(side="left")
                tk.Button(frame, text="View File", command=lambda path=full_path: self.view_file(path), height=1, width=10).pack(side="left", padx=2)
                tk.Button(frame, text="Edit File", command=lambda path=full_path: self.edit_file(path), height=1, width=10).pack(side="left", padx=2)
                tk.Button(frame, text="Delete File", command=lambda path=full_path: self.delete_file(path), height=1, width=10).pack(side="left", padx=2)

        back_button = tk.Button(self.main, text="Back to Main Menu", command=self.main_menu, height=2, width=20)
        back_button.pack(pady=10)

    def view_list(self, name):
        for widget in self.main.winfo_children():
            widget.destroy()
    
        tk.Label(self.main, text=name, font=("Helvetica", 16)).pack(pady=10)
    
        if name in self.lists:
            for i, item in enumerate(self.lists[name]):
                tk.Label(self.main, text=f"{i+1}. {item}").pack(anchor="w")

        edit_button = tk.Button(self.main, text="Edit List", command=lambda: self.edit_list(name))
        edit_button.pack(pady=10)

        save_button = tk.Button(self.main, text="Save List as text file", command=lambda: self.save_list_as_text_file(name)) #This line executes the Save the list as text file function
        save_button.pack(pady=10)
    
        back_button = tk.Button(self.main, text="Back to Main Menu", command=self.main_menu, height=2, width=20) #This button is used to get back to the main menu
        back_button.pack(pady=10)

 
    def view_file(self, file_path):
        for widget in self.main.winfo_children():
            widget.destroy()

        tk.Label(self.main, text=f"View File: {os.path.basename(file_path)}", font=("Helvetica", 16)).pack(pady=10)

        frame = tk.Frame(self.main)
        frame.pack(anchor="w", padx=20, pady=5)

        tk.Label(frame, text="Status:", font=("Helvetica", 12)).grid(row=0, column=0, padx=10)
        tk.Label(frame, text="Remaining", font=("Helvetica", 12)).grid(row=0, column=1, padx=10)
        tk.Label(frame, text="Active", font=("Helvetica", 12)).grid(row=0, column=2, padx=10)
        tk.Label(frame, text="Complete", font=("Helvetica", 12)).grid(row=0, column=3, padx=10)

        check_vars = []

        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                file_content = file.readlines()

            for i, line in enumerate(file_content):
                parts = line.strip().split(',')
                item = parts[0]
                states = list(map(int, parts[1:])) if len(parts) > 1 else [0, 0, 0]

                # Ensure we have exactly 3 states
                if len(states) < 3:
                    states += [0] * (3 - len(states))

                tk.Label(frame, text=item).grid(row=i+1, column=0, padx=10)

                var1 = tk.IntVar(value=states[0])
                var2 = tk.IntVar(value=states[1])
                var3 = tk.IntVar(value=states[2])
                check_vars.append((item, var1, var2, var3))

                tk.Checkbutton(frame, variable=var1).grid(row=i+1, column=1, padx=10)
                tk.Checkbutton(frame, variable=var2).grid(row=i+1, column=2, padx=10)
                tk.Checkbutton(frame, variable=var3).grid(row=i+1, column=3, padx=10)

        def save_checks():
            with open(file_path, 'w') as file:
                for item, var1, var2, var3 in check_vars:
                    file.write(f"{item},{var1.get()},{var2.get()},{var3.get()}\n")

        save_button = tk.Button(self.main, text="Save Checks", command=save_checks)
        save_button.pack(pady=10)

        back_button = tk.Button(self.main, text="Back to List", command=lambda: self.view_lists(os.path.dirname(file_path)), height=2, width=20)
        back_button.pack(pady=10)



    def edit_list(self, name):
        for widget in self.main.winfo_children():
            widget.destroy()
    
        tk.Label(self.main, text=f"Edit List: {name}", font=("Helvetica", 16)).pack(pady=10)
    
        if name in self.lists:
            items = self.lists[name]
            item_vars = []
            for i, item in enumerate(items):  #eumerate function iterates over the lists and its items
                item_var = tk.StringVar(value=item)
                item_vars.append(item_var)
                tk.Entry(self.main, textvariable=item_var).pack(anchor="w")
        
            def save_changes():
                new_items = [item_var.get() for item_var in item_vars]
                self.lists[name] = new_items
                self.view_list(name)
        
            save_button = tk.Button(self.main, text="Save Changes", command=save_changes)
            save_button.pack(pady=10)
    
        back_button = tk.Button(self.main, text="Back to Main Menu", command=self.main_menu, height=2, width=20)
        back_button.pack(pady=10)
    
 
    def edit_file(self, file_path):
        for widget in self.main.winfo_children():
            widget.destroy()

        tk.Label(self.main, text=f"Edit File: {os.path.basename(file_path)}", font=("Helvetica", 16)).pack(pady=10)

        item_vars = []

        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                file_content = file.readlines()

            for line in file_content:
                item_var = tk.StringVar(value=line.strip().split(',')[0])
                item_vars.append(item_var)
                tk.Entry(self.main, textvariable=item_var).pack(anchor="w")

        add_button = tk.Button(self.main, text="+", command=None)
        add_button.pack(anchor="w", pady=5, padx=5)  # Initial placement

        def add_entry():
            item_var = tk.StringVar(value="")
            item_vars.append(item_var)
            new_entry = tk.Entry(self.main, textvariable=item_var)
            new_entry.pack(anchor="w", before=add_button, pady=2, padx=5)
            # Repack the add button below the new entry
            add_button.pack_forget()
            add_button.pack(anchor="w", pady=5, padx=5)

        add_button.config(command=add_entry)

        def save_changes():
            new_content = [item_var.get() + ',0,0,0\n' for item_var in item_vars]
            with open(file_path, 'w') as file:
                file.writelines(new_content)
            self.view_lists(os.path.dirname(file_path))

        save_button = tk.Button(self.main, text="Save Changes", command=save_changes)
        save_button.pack(pady=10)

        back_button = tk.Button(self.main, text="Back to List", command=lambda: self.view_lists(os.path.dirname(file_path)), height=2, width=20)
        back_button.pack(pady=10)

    def delete_file(self, file_path):
            if messagebox.askokcancel("Delete", f"Are you sure you want to delete {os.path.basename(file_path)}?"):
                try:
                    os.remove(file_path)
                    messagebox.showinfo("Deleted", f"{os.path.basename(file_path)} has been deleted.")
                    self.view_lists(os.path.dirname(file_path))
                except Exception as e:
                    messagebox.showerror("Error", f"An error occurred while deleting the file: {e}")


        
root = tk.Tk() #Tkinter library expressed as Tk and is stored here in the root variable...
app = To_do_List(root) 
root.mainloop()

