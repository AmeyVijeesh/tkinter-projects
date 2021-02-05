from tkinter import *
from tkinter import messagebox
from covid import Covid


def get_country():
    country = country_var.get()

    if country == '':
        messagebox.showerror(
            "Blank Country name",
            "Please enter the country name and try again.",
            icon='error'
        )

    else:
        try:
            Covid().get_status_by_country_name(country)

            status_top_level = Toplevel()
            status_top_level.config(bg='white')
            status_top_level.geometry("200x200")
            status_top_level.resizable(False, False)
            status_top_level.title(f"{country} Covid 19 Stats")

            country_data = Covid().get_status_by_country_name(country)

            confirmed = str(country_data['confirmed'])
            recovered = str(country_data['recovered'])
            active = str(country_data['active'])
            deaths = str(country_data['deaths'])

            country_label = Label(status_top_level, text=f'{country.capitalize()} Data', fg='black', bg='white',
                                  font=('Calibri', 15, 'bold'))
            country_label.place(x=40, y=10)

            confirmed_label1 = Label(status_top_level, text=f'Confirmed: {confirmed}', fg='black', bg='white',
                                     font=('Calibri', 12))
            confirmed_label1.place(x=25, y=50)

            active_label1 = Label(status_top_level, text=f'Active: {deaths}', fg='black', bg='white',
                                  font=('Calibri', 12))
            active_label1.place(x=25, y=75)

            deaths_label1 = Label(status_top_level, text=f'Deaths: {active}', fg='black', bg='white',
                                  font=('Calibri', 12))
            deaths_label1.place(x=25, y=100)

            recovered_label1 = Label(status_top_level, text=f'Recovered: {recovered}', fg='black', bg='white',
                                     font=('Calibri', 12))
            recovered_label1.place(x=25, y=125)

        except ValueError:
            messagebox.showerror(
                "Invalid Country",
                f"'{country}' is not a valid country. Please enter a valid one and try again.",
                icon='error'
            )



root = Tk()
root.geometry("500x300")
root.resizable(False, False)
root.configure(bg='white')
root.title("CoronaVirus Tracker")

frame = Frame(root, bd=3, bg='white', highlightbackground='black', highlightthickness=4)
frame.place(relx=0.5, rely=0.12, relwidth=0.85, relheight=0.85, anchor='n')

world_confirmed = Covid().get_total_confirmed_cases()
world_deaths = Covid().get_total_deaths()
world_active = Covid().get_total_active_cases()
world_recovered = Covid().get_total_recovered()

data = Covid().get_status_by_country_name("us")
usa_confirmed = str(data['confirmed'])
usa_deaths = str(data['deaths'])
usa_active = str(data['active'])
usa_recovered = str(data['recovered'])

print(Covid().list_countries())

world_label = Label(frame, text='World Data', fg='black', bg='white', font=('Calibri', 15, 'bold'))
world_label.place(x=25, y=30)

confirmed_label = Label(frame, text=f'Confirmed: {world_confirmed}', fg='black', bg='white', font=('Calibri', 12))
confirmed_label.place(x=25, y=75)

active_label = Label(frame, text=f'Active: {world_deaths}', fg='black', bg='white', font=('Calibri', 12))
active_label.place(x=25, y=100)

deaths_label = Label(frame, text=f'Deaths: {world_active}', fg='black', bg='white', font=('Calibri', 12))
deaths_label.place(x=25, y=125)

recovered_label = Label(frame, text=f'Recovered: {world_recovered}', fg='black', bg='white', font=('Calibri', 12))
recovered_label.place(x=25, y=150)

usa_label = Label(frame, text='USA Data', fg='black', bg='white', font=('Calibri', 15, 'bold'))
usa_label.place(x=250, y=30)

confirmed_label = Label(frame, text=f'Confirmed: {usa_confirmed}', fg='black', bg='white', font=('Calibri', 12))
confirmed_label.place(x=240, y=75)

active_label = Label(frame, text=f'Active: {usa_deaths}', fg='black', bg='white', font=('Calibri', 12))
active_label.place(x=240, y=100)

deaths_label = Label(frame, text=f'Deaths: {usa_active}', fg='black', bg='white', font=('Calibri', 12))
deaths_label.place(x=240, y=125)

recovered_label = Label(frame, text=f'Recovered: {usa_recovered}', fg='black', bg='white', font=('Calibri', 12))
recovered_label.place(x=240, y=150)

country_var = StringVar()
country_entry = Entry(frame, highlightbackground='black', highlightthickness=4, textvariable=country_var)
country_entry.place(x=100, y=200)

country_button = Button(frame, text='Get Results', bg='black', fg='white', relief=FLAT, command=get_country)
country_button.place(x=250, y=200)

root.mainloop()
