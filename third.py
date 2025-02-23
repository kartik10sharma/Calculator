import tkinter as tk
import subprocess


def run_script(script_name):
    """Function to execute a Python script."""
    try:
        subprocess.run(["python", script_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}: {e}")

def on_select(option):
    """Function to handle selection and show age options if needed."""
    if option == "User-Centric":
        age_window = tk.Toplevel(root)
        age_window.title("Select Age Group")
        age_window.geometry("300x250")

        tk.Label(age_window, text="Select Age Group:", font=("Arial", 12)).pack(pady=10)

        tk.Button(age_window, text="Age 10-20 yrs", command=lambda: [run_script("first.py"), age_window.destroy()]).pack(pady=5)
        tk.Button(age_window, text="Above 20 yrs", command=lambda: [run_script("sec.py"), age_window.destroy()]).pack(pady=5)
    
    elif option == "System-Centric":
        run_script("sec.py")


# Create the main window
root = tk.Tk()
root.title("Select Mode")
root.geometry("400x250")

# Create label
label = tk.Label(root, text="Choose an option:", font=("Arial", 12))
label.pack(pady=10)

# Create buttons
user_button = tk.Button(root, text="User-Centric", command=lambda: on_select("User-Centric"))
user_button.pack(pady=5)

system_button = tk.Button(root, text="System-Centric", command=lambda: on_select("System-Centric"))
system_button.pack(pady=5)

# Run the Tkinter main loop
root.mainloop()
