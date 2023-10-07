import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime

# Create a connection to the SQLite database
conn = sqlite3.connect('jobs.db')
c = conn.cursor()

# Create jobs table if it doesn't exist
c.execute('''
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        options TEXT,
        company_name TEXT,
        location TEXT,
        contact_person TEXT,
        contact_method TEXT,
        job_title TEXT
    )
''')
conn.commit()

# Function to handle new job entry
def enter_job():
    date = entry_date.get()
    options = ', '.join([var_options[i].get() for i in range(len(options_list)) if var_options[i].get() != 0])
    company_name = entry_company_name.get()
    location = entry_location.get()
    contact_person = entry_contact_person.get()
    contact_method = ', '.join([var_contact_method[i].get() for i in range(len(contact_method_list)) if var_contact_method[i].get() != 0])
    job_title = entry_job_title.get()
    
    if not date or not options or not company_name or not location or not contact_person or not contact_method or not job_title:
        messagebox.showerror('Error', 'All fields are required!')
    else:
        c.execute('INSERT INTO jobs (date, options, company_name, location, contact_person, contact_method, job_title) VALUES (?, ?, ?, ?, ?, ?, ?)',
                  (date, options, company_name, location, contact_person, contact_method, job_title))
        conn.commit()
        messagebox.showinfo('Success', 'Job entry added successfully!')
        clear_entries()

# Function to clear input fields
def clear_entries():
    entry_date.delete(0, tk.END)
    entry_company_name.delete(0, tk.END)
    entry_location.delete(0, tk.END)
    entry_contact_person.delete(0, tk.END)
    entry_job_title.delete(0, tk.END)
    for i in range(len(options_list)):
        var_options[i].set(0)
    for i in range(len(contact_method_list)):
        var_contact_method[i].set(0)

# Main function to create GUI
def main():
    global entry_date, entry_company_name, entry_location, entry_contact_person, entry_job_title
    global var_options, var_contact_method, options_list, contact_method_list
    
    root = tk.Tk()
    root.title('Job Tracker')
    
    options_list = ['Application', 'Resume', 'Cover letter', 'Interview', 'Test/exam', 'Job board', 'Referral', 'Networking', 'Reemployment service', 'Skill development', 'Other']
    contact_method_list = ['In person', 'Phone/fax', 'Mail', 'Email', 'Web']
    
    var_options = [tk.StringVar() for _ in range(len(options_list))]
    var_contact_method = [tk.StringVar() for _ in range(len(contact_method_list))]

    label_date = tk.Label(root, text='Date (YYYY-MM-DD):')
    label_date.pack()
    entry_date = tk.Entry(root)
    entry_date.pack()

    label_options = tk.Label(root, text='Options:')
    label_options.pack()
    for i in range(len(options_list)):
        checkbox = tk.Checkbutton(root, text=options_list[i], variable=var_options[i], onvalue=options_list[i])
        checkbox.pack()

    label_company_name = tk.Label(root, text='Company Name:')
    label_company_name.pack()
    entry_company_name = tk.Entry(root)
    entry_company_name.pack()

    label_location = tk.Label(root, text='Location:')
    label_location.pack()
    entry_location = tk.Entry(root)
    entry_location.pack()

    label_contact_person = tk.Label(root, text='Contact Person:')
    label_contact_person.pack()
    entry_contact_person = tk.Entry(root)
    entry_contact_person.pack()

    label_contact_method = tk.Label(root, text='Contact Method:')
    label_contact_method.pack()
    for i in range(len(contact_method_list)):
        checkbox = tk.Checkbutton(root, text=contact_method_list[i], variable=var_contact_method[i], onvalue=contact_method_list[i])
        checkbox.pack()

    label_job_title = tk.Label(root, text='Job Title:')
    label_job_title.pack()
    entry_job_title = tk.Entry(root)
    entry_job_title.pack()

    button_enter_job = tk.Button(root, text='Enter Job', command=enter_job)
    button_enter_job.pack()

    button_clear = tk.Button(root, text='Clear Entries', command=clear_entries)
    button_clear.pack()

    # Function to handle job search by date range
    def search_jobs_by_date_range():
        start_date = entry_start_date.get()
        end_date = entry_end_date.get()
        if not start_date or not end_date:
            messagebox.showerror('Error', 'Please enter both start and end dates.')
        else:
            # Perform database query to get jobs within the specified date range
            c.execute('SELECT * FROM jobs WHERE date BETWEEN ? AND ?', (start_date, end_date))
            jobs = c.fetchall()
            display_search_results(jobs)

    # Function to display search results in a new window
    def display_search_results(jobs):
        results_window = tk.Toplevel()
        results_window.title('Search Results')

        if not jobs:
            label_no_results = tk.Label(results_window, text='No jobs found within the specified date range.')
            label_no_results.pack()
        else:
            for job in jobs:
                label_job_info = tk.Label(results_window, text=f"Date: {job[1]}, Options: {job[2]}, Company: {job[3]}, Location: {job[4]}, Contact Person: {job[5]}, Contact Method: {job[6]}, Job Title: {job[7]}")
                label_job_info.pack()


    # Add a button to initiate the job search by date range
    button_search_jobs = tk.Button(root, text='Search Jobs by Date Range', command=search_jobs_by_date_range)
    button_search_jobs.pack()
    
    # Add entry fields for start and end dates in the main window
    label_start_date = tk.Label(root, text='Start Date (YYYY-MM-DD):')
    label_start_date.pack()
    entry_start_date = tk.Entry(root)
    entry_start_date.pack()

    label_end_date = tk.Label(root, text='End Date (YYYY-MM-DD):')
    label_end_date.pack()
    entry_end_date = tk.Entry(root)
    entry_end_date.pack()


    root.mainloop()

if __name__ == '__main__':
    main()