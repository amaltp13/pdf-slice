
import PyPDF2
import os
import tkinter as tk

from tkinter import filedialog

from tkinter import messagebox
from tkinter import ttk
from tkinter import Entry
from ttkbootstrap import Style

class pdf_merger:
    def __init__(self, root):
        self.root = root
        self.flag_ok = 2
        self.root.geometry("650x450")

        self.root.title("PDF Combine")

        self.agreement1 = tk.StringVar()
        self.agreement2 = tk.StringVar()
        self.agreement3 = tk.StringVar()
        self.agreement4 = tk.StringVar()
        self.agreement5 = tk.StringVar()
        self.filename = ["a","b","c","d","e","f"]
        print(f"f[0] contains  {self.filename[0]}")
        print(f"f[1] contains  {self.filename[1]}")
        print(f"f[2] contains  {self.filename[2]}")
        print(f"f[3] contains  {self.filename[3]}")
        print(f"f[4] contains  {self.filename[4]}")
        self.style = Style(theme='sandstone')
        self.set_up_gui()

    def pre_check(self):
        flag_check =0
        flag_check_2 = 0
        if self.p1s1.get() and not self.p1e1.get():
            print("inside")
            flag_check = 1
        if self.p2s1.get() and not self.p2e1.get():
            print("inside")
            flag_check = 1
        if self.p3s1.get() and not self.p3e1.get():
            print("inside")
            flag_check = 1
        if self.p1s2.get() and not self.p1e2.get():
            print("inside")
            flag_check = 1
        if self.p2s2.get() and not self.p2e2.get():
            print("inside")
            flag_check = 1
        if self.p3s2.get() and not self.p3e2.get():
            print("inside")
            flag_check = 1
        if self.p1s3.get() and not self.p1e3.get():
            print("inside")
            flag_check = 1
        if self.p2s3.get() and not self.p2e3.get():
            print("inside")
            flag_check = 1
        if self.p3s3.get() and not self.p3e3.get():
            print("inside")
            flag_check = 1
        if self.p1s4.get() and not self.p1e4.get():
            print("inside")
            flag_check = 1
        if self.p2s4.get() and not self.p2e4.get():
            print("inside")
            flag_check = 1
        if self.p3s4.get() and not self.p3e4.get():
            print("inside")
            flag_check = 1
        if self.p1s5.get() and not self.p1e5.get():
            print("inside")
            flag_check = 1
        if self.p2s5.get() and not self.p2e5.get():
            print("inside")
            flag_check = 1
        if self.p3s5.get() and not self.p3e5.get():
            print("inside")
            flag_check = 1
        if not self.output_file.get():
            print("Output file not specified")
            messagebox.showerror('File Error', 'Output file not specified')
            flag_check = 1
        if  self.filename[5]=="f":
            print("Output file not specified")
            messagebox.showerror('File Error', 'Output file not specified')
            flag_check = 1

        if self.p1s1.get() > self.p1e1.get():
            print("Value error")
            flag_check_2 = 1
        if self.p2s1.get() > self.p2e1.get():
            print("Value error")
            flag_check_2 = 1
        if self.p3s1.get() > self.p3e1.get():
            print("Value error")
            flag_check_2 = 1
        if self.p1s2.get() > self.p1e2.get():
            print("Value error")
            flag_check_2 = 1
        if self.p2s2.get() > self.p2e2.get():
            print("Value error")
            flag_check_2 = 1
        if self.p3s2.get() > self.p3e2.get():
            print("Value error")
            flag_check_2 = 1
        if self.p1s3.get() > self.p1e3.get():
            print("Value error")
            flag_check_2 = 1
        if self.p2s3.get() > self.p2e3.get():
            print("Value error")
            flag_check_2 = 1
        if self.p3s3.get() > self.p3e3.get():
            print("Value error")
            flag_check_2 = 1
        if self.p1s4.get() > self.p1e4.get():
            print("Value error")
            flag_check_2 = 1
        if self.p2s4.get() > self.p2e4.get():
            print("Value error")
            flag_check_2 = 1
        if self.p3s4.get() > self.p3e4.get():
            print("Value error")
            flag_check_2 = 1
        if self.p1s5.get() > self.p1e5.get():
            print("Value error")
            flag_check_2 = 1
        if self.p2s5.get() > self.p2e5.get():
            print("Value error")
            flag_check_2 = 1
        if self.p3s5.get() > self.p3e5.get():
            print("Value error")
            flag_check_2 = 1
        if flag_check:
            print("Please fill all required values")
            messagebox.showerror('Value Error', 'Please fill all required values !')
        if flag_check_2:
            print("Start value greater than end value")
            messagebox.showerror('Value Error', 'Start value greater than end value !')

    def set_up_gui(self):
        self.file_1_btn = ttk.Button(self.root, text="Select File 1", command= lambda: self.open_file_front(0) )
        self.file_1_btn.place(x=20, y=100)
        self.file_2_btn = ttk.Button(self.root, text="Select File 2",command= lambda:self.open_file_front(1))
        self.file_2_btn.place(x=20, y=150)
        self.file_3_btn = ttk.Button(self.root, text="Select File 3",command= lambda:self.open_file_front(2))
        self.file_3_btn.place(x=20, y=200)
        self.file_4_btn = ttk.Button(self.root, text="Select File 4",command= lambda:self.open_file_front(3))
        self.file_4_btn.place(x=20, y=250)
        self.file_5_btn = ttk.Button(self.root, text="Select File 5",command= lambda:self.open_file_front(4))
        self.file_5_btn.place(x=20, y=300)

        self.start_btn = ttk.Button(self.root, text="Start Combining",command= lambda:self.start())
        self.start_btn.place(x=450, y=380, height = 45)
        self.folder_btn = ttk.Button(self.root, text="Select folder", command= lambda:self.open_folder())
        self.folder_btn.place(x=35, y=380, height=30)


        self.p1s1 = Entry(self.root, width=5, background="gray71", foreground="#fff", font=('Calibri', 12))
        self.p1s1.place(x=150, y=100, height=26)
        self.p1e1 = Entry(self.root, width=5, background="gray71", foreground="#fff", font=('Calibri', 12))
        self.p1e1.place(x=210, y=100, height=26)
        self.p2s1 = Entry(self.root, width=5, background="gray71", foreground="#fff", font=('Calibri', 12))
        self.p2s1.place(x=300, y=100, height=26)
        self.p2e1 = Entry(self.root, width=5, background="gray71", foreground="#fff", font=('Calibri', 12))
        self.p2e1.place(x=360, y=100, height=26)
        self.p3s1 = Entry(self.root, width=5, background="gray71", foreground="#fff", font=('Calibri', 12))
        self.p3s1.place(x=450, y=100, height=26)
        self.p3e1 = Entry(self.root, width=5, background="gray71", foreground="#fff", font=('Calibri', 12))
        self.p3e1.place(x=510, y=100, height=26)

        self.p1s2 = Entry(self.root, width=5, background="gray71", foreground="#fff", font=('Calibri', 12))
        self.p1s2.place(x=150, y=150, height=26)
        self.p1e2 = Entry(self.root, width=5, background="gray71", foreground="#fff", font=('Calibri', 12))
        self.p1e2.place(x=210, y=150, height=26)
        self.p2s2 = Entry(self.root, width=5, background="gray71", foreground="#fff", font=('Calibri', 12))
        self.p2s2.place(x=300, y=150, height=26)
        self.p2e2 = Entry(self.root, width=5, background="gray71", foreground="#fff", font=('Calibri', 12))
        self.p2e2.place(x=360, y=150, height=26)
        self.p3s2 = Entry(self.root, width=5, background="gray71", foreground="#fff", font=('Calibri', 12))
        self.p3s2.place(x=450, y=150, height=26)
        self.p3e2 = Entry(self.root, width=5, background="gray71", foreground="#fff", font=('Calibri', 12))
        self.p3e2.place(x=510, y=150, height=26)

        self.p1s3 = Entry(self.root, width=5, background="gray71", foreground="#fff", font=('Calibri', 12))
        self.p1s3.place(x=150, y=200, height=26)
        self.p1e3 = Entry(self.root, width=5, background="gray71", foreground="#fff", font=('Calibri', 12))
        self.p1e3.place(x=210, y=200, height=26)
        self.p2s3 = Entry(self.root, width=5, background="gray71", foreground="#fff", font=('Calibri', 12))
        self.p2s3.place(x=300, y=200, height=26)
        self.p2e3 = Entry(self.root, width=5, background="gray71", foreground="#fff", font=('Calibri', 12))
        self.p2e3.place(x=360, y=200, height=26)
        self.p3s3 = Entry(self.root, width=5, background="gray71", foreground="#fff", font=('Calibri', 12))
        self.p3s3.place(x=450, y=200, height=26)
        self.p3e3 = Entry(self.root, width=5, background="gray71", foreground="#fff", font=('Calibri', 12))
        self.p3e3.place(x=510, y=200, height=26)

        self.p1s4 = Entry(self.root, width=5, background="gray71", foreground="#fff", font=('Calibri', 12))
        self.p1s4.place(x=150, y=250, height=26)
        self.p1e4 = Entry(self.root, width=5, background="gray71", foreground="#fff", font=('Calibri', 12))
        self.p1e4.place(x=210, y=250, height=26)
        self.p2s4 = Entry(self.root, width=5, background="gray71", foreground="#fff", font=('Calibri', 12))
        self.p2s4.place(x=300, y=250, height=26)
        self.p2e4 = Entry(self.root, width=5, background="gray71", foreground="#fff", font=('Calibri', 12))
        self.p2e4.place(x=360, y=250, height=26)
        self.p3s4 = Entry(self.root, width=5, background="gray71", foreground="#fff", font=('Calibri', 12))
        self.p3s4.place(x=450, y=250, height=26)
        self.p3e4 = Entry(self.root, width=5, background="gray71", foreground="#fff", font=('Calibri', 12))
        self.p3e4.place(x=510, y=250, height=26)

        self.p1s5 = Entry(self.root, width=5, background="gray71", foreground="#fff", font=('Calibri', 12))
        self.p1s5.place(x=150, y=300, height=26)
        self.p1e5 = Entry(self.root, width=5, background="gray71", foreground="#fff", font=('Calibri', 12))
        self.p1e5.place(x=210, y=300, height=26)
        self.p2s5 = Entry(self.root, width=5, background="gray71", foreground="#fff", font=('Calibri', 12))
        self.p2s5.place(x=300, y=300, height=26)
        self.p2e5 = Entry(self.root, width=5, background="gray71", foreground="#fff", font=('Calibri', 12))
        self.p2e5.place(x=360, y=300, height=26)
        self.p3s5 = Entry(self.root, width=5, background="gray71", foreground="#fff", font=('Calibri', 12))
        self.p3s5.place(x=450, y=300, height=26)
        self.p3e5 = Entry(self.root, width=5, background="gray71", foreground="#fff", font=('Calibri', 12))
        self.p3e5.place(x=510, y=300, height=26)

        self.output_file = Entry(self.root, width=25, background="gray71", foreground="#fff", font=('Calibri', 12))
        self.output_file .place(x=200, y=380, height=30)

        self.labl11 = ttk.Label(self.root, text="Output Folder", font=('Calibri', 12))
        self.labl11.place(x=40, y=350)
        self.labl12 = ttk.Label(self.root, text="Output File Name", font=('Calibri', 12))
        self.labl12.place(x=240, y=350)

        self.labl1 = ttk.Label(self.root, text="P1s", font=('Calibri', 12))
        self.labl1.place(x=160, y=70)
        self.labl2 = ttk.Label(self.root, text="P1e", font=('Calibri', 12))
        self.labl2.place(x=220, y=70)
        self.labl3 = ttk.Label(self.root, text="P2s", font=('Calibri', 12))
        self.labl3.place(x=310, y=70)
        self.labl4 = ttk.Label(self.root, text="P2e", font=('Calibri', 12))
        self.labl4.place(x=370, y=70)
        self.labl5 = ttk.Label(self.root, text="P3s", font=('Calibri', 12))
        self.labl5.place(x=460, y=70)
        self.labl6 = ttk.Label(self.root, text="P3e", font=('Calibri', 12))
        self.labl6.place(x=520, y=70)

        self.labl6 = ttk.Label(self.root, text="All Pages", font=('Calibri', 12))
        self.labl6.place(x=580, y=70)

        self.labl7 = ttk.Label(self.root, text="#PDF Combiner", font=('Calibri', 20))
        self.labl7.place(x=50, y=10)

        cb1 = ttk.Checkbutton(root,text='',variable=self.agreement1,onvalue='agree',offvalue='disagree')
        cb1.place(x=600,y=102)
        cb2 = ttk.Checkbutton(root, text='', variable=self.agreement2, onvalue='agree', offvalue='disagree')
        cb2.place(x=600, y=152)
        cb3 = ttk.Checkbutton(root, text='', variable=self.agreement3, onvalue='agree', offvalue='disagree')
        cb3.place(x=600, y=202)
        cb4 = ttk.Checkbutton(root, text='', variable=self.agreement4, onvalue='agree', offvalue='disagree')
        cb4.place(x=600, y=252)
        cb5 = ttk.Checkbutton(root, text='', variable=self.agreement5, onvalue='agree', offvalue='disagree')
        cb5.place(x=600, y=302)

    def merge_pdfs(self,pdf1_path, pdf2_path, start_page, end_page):
        # Create a PdfFileReader object for the first PDF or create a new one if it doesn't exist
        start_page =int(start_page)
        end_page =int(end_page)
        pdf2 = PyPDF2.PdfReader(open(pdf2_path, 'rb'))
        try:

            pdf1 = PyPDF2.PdfReader(open(pdf1_path, 'rb'))
            print(f"Size pf pdf2 = {len(pdf2.pages)}")
            if(start_page > len(pdf2.pages)) or (end_page > len(pdf2.pages)):
                print("size error")
                self.flag_ok = 0
                messagebox.showerror('size error', 'Size of PDF is lesser then index value !')
        except FileNotFoundError:

            pdf1 = PyPDF2.PdfReader(open(pdf2_path, 'rb'))

            pdf1_writer = PyPDF2.PdfWriter()

            with open(pdf1_path, 'wb') as pdf1_file:

                pdf1_writer.write(pdf1_file)

            pdf1 = PyPDF2.PdfReader(open(pdf1_path, 'rb'))

        # Create a PdfFileReader object for the second PDF



        # Create a PdfFileWriter object to write the output

        pdf_writer = PyPDF2.PdfWriter()

        # Add pages from the first PDF

        for page_num in range(len(pdf1.pages)):
            page = pdf1.pages[page_num]

            pdf_writer.add_page(page)

        # Add pages from the second PDF between start_page and end_page

        for page_num in range(start_page - 1, end_page):
            page = pdf2.pages[page_num]

            pdf_writer.add_page(page)

        # Write the combined PDF back to the first PDF file

        with open(pdf1_path, 'wb') as pdf1_file:

            pdf_writer.write(pdf1_file)
            self.flag_ok =1

    def start(self):
        self.pre_check()
        print(self.agreement1.get())
        print(self.output_file.get())
        a= f"{self.filename[5]}/{self.output_file.get()}.pdf"

        print(a)
        self.flag_ok = 2
        if (self.agreement1.get() != 'agree') and self.filename[0] != "a":
            print(f"f[0] contains  {self.filename[0]}")
            if not (self.p1s1.get() or self.p1e1.get()):
                print("No index given")
                self.flag_ok = 0
                messagebox.showerror('Index Error', 'index not given !')
            else:
                #a=r"C:\Users\556521\Downloads\first_pdf.pdf"
                self.merge_pdfs(a,self.filename[0],self.p1s1.get(),self.p1e1.get())

            if self.p2s1.get():
                self.merge_pdfs(a, self.filename[0], self.p2s1.get(), self.p2e1.get())

            if self.p3s1.get():
                self.merge_pdfs(a, self.filename[0], self.p3s1.get(), self.p3e1.get())

        elif self.filename[0] != "a":
            print("abc")
            print(f"f[0] contains  {self.filename[0]}")
            pdf2 = PyPDF2.PdfReader(open(self.filename[0], 'rb'))

            len_of_pdf = len(pdf2.pages)
            print(len_of_pdf)
            self.merge_pdfs(a, self.filename[0],1,len_of_pdf)

        if (self.agreement2.get() != 'agree') and self.filename[1] != 'b':
            print("abc")
            print(f"f[1] contains  {self.filename[1]}")
            if not (self.p1s2.get() or self.p1e2.get()):
                print("No index given")
                messagebox.showerror('Index Error', 'index not given !')
                self.flag_ok = 0
            else:
                # a=r"C:\Users\556521\Downloads\first_pdf.pdf"
                self.merge_pdfs(a, self.filename[1], self.p1s2.get(), self.p1e2.get())

            if self.p2s2.get():
                self.merge_pdfs(a, self.filename[1], self.p2s2.get(), self.p2e2.get())

            if self.p3s2.get():
                self.merge_pdfs(a, self.filename[1], self.p3s2.get(), self.p3e2.get())

        elif self.filename[1] != "b":
            print("abc")
            print(f"f[1] contains  {self.filename[1]}")
            pdf2 = PyPDF2.PdfReader(open(self.filename[1], 'rb'))

            len_of_pdf = len(pdf2.pages)
            print(len_of_pdf)
            self.merge_pdfs(a, self.filename[1], 1, len_of_pdf)

        if (self.agreement3.get() != 'agree') and self.filename[2] != 'c':
            print("abc")
            print(f"f[2] contains  {self.filename[2]}")
            if not (self.p1s3.get() or self.p1e3.get()):
                print("No index given")
                self.flag_ok = 0
                messagebox.showerror('Index Error', 'index not given !')
            else:
                # a=r"C:\Users\556521\Downloads\first_pdf.pdf"
                self.merge_pdfs(a, self.filename[2], self.p1s3.get(), self.p1e3.get())

            if self.p2s3.get():
                self.merge_pdfs(a, self.filename[2], self.p2s3.get(), self.p2e3.get())

            if self.p3s3.get():
                self.merge_pdfs(a, self.filename[2], self.p3s3.get(), self.p3e3.get())

        elif self.filename[2] != "c":
            print("abc")
            print(f"f[2] contains  {self.filename[2]}")
            pdf2 = PyPDF2.PdfReader(open(self.filename[2], 'rb'))

            len_of_pdf = len(pdf2.pages)
            print(len_of_pdf)
            self.merge_pdfs(a, self.filename[2], 1, len_of_pdf)

        if (self.agreement4.get() != 'agree') and self.filename[3] != 'd':
            print("abc")
            print(f"f[3] contains  {self.filename[3]}")
            if not (self.p1s4.get() or self.p1e4.get()):
                print("No index given")
                self.flag_ok = 0
                messagebox.showerror('Index Error', 'index not given !')
            else:
                # a=r"C:\Users\556521\Downloads\first_pdf.pdf"
                self.merge_pdfs(a, self.filename[3], self.p1s4.get(), self.p1e4.get())

            if self.p2s4.get():
                self.merge_pdfs(a, self.filename[3], self.p2s4.get(), self.p2e4.get())

            if self.p3s4.get():
                self.merge_pdfs(a, self.filename[3], self.p3s4.get(), self.p3e4.get())

        elif self.filename[3] != "d":
            print("abc")
            print(f"f[3] contains  {self.filename[3]}")
            pdf2 = PyPDF2.PdfReader(open(self.filename[3], 'rb'))

            len_of_pdf = len(pdf2.pages)
            print(len_of_pdf)
            self.merge_pdfs(a, self.filename[3], 1, len_of_pdf)

        if (self.agreement5.get() != 'agree') and self.filename[4] != 'e':
            print("abc")
            print(f"f[4] contains  {self.filename[4]}")
            if not (self.p1s5.get() or self.p1e5.get()):
                print("No index given")
                self.flag_ok = 0
                messagebox.showerror('Index Error', 'index not given !')
            else:
                # a=r"C:\Users\556521\Downloads\first_pdf.pdf"
                self.merge_pdfs(a, self.filename[4], self.p1s1.get(), self.p1e1.get())

            if self.p2s5.get():
                self.merge_pdfs(a, self.filename[4], self.p2s1.get(), self.p2e1.get())

            if self.p3s5.get():
                self.merge_pdfs(a, self.filename[4], self.p3s1.get(), self.p3e1.get())

        elif self.filename[4] != "e":
            print("abc")
            print(f"f[4] contains  {self.filename[4]}")
            pdf2 = PyPDF2.PdfReader(open(self.filename[4], 'rb'))

            len_of_pdf = len(pdf2.pages)
            print(len_of_pdf)
            self.merge_pdfs(a, self.filename[4], 1, len_of_pdf)

        if(self.flag_ok==1):
            messagebox.showinfo("Finished", "PDF Activity Finished")
    def open_folder(self):
        folder_location = filedialog.askdirectory()
        self.filename[5] = folder_location
        print(self.filename[5])
        self.folder_btn.config(text = os.path.basename(folder_location))
    def open_file_front(self,number):
        print(number)
        print(self.p2s5.get())

        file = filedialog.askopenfilename(initialdir="/",
                                              title="Select a File",
                                              filetypes=[("PDF Files", "*.pdf")])
        print(file)

        match number:
            case 0:
                self.file_1_btn.config(text=os.path.basename(file))
                self.filename[0]= file
                print(self.filename[0])
            case 1:
                self.file_2_btn.config(text=os.path.basename(file))
                #self.filename.insert(1, file)
                self.filename[1] = file
                print(self.filename[1])
            case 2:
                self.file_3_btn.config(text=os.path.basename(file))
                #self.filename.insert(2, file)
                self.filename[2] = file
                print(self.filename[2])
            case 3:
                self.file_4_btn.config(text=os.path.basename(file))
                #self.filename.insert(3, file)
                self.filename[3] = file
                print(self.filename[3])
            case 4:
                self.file_5_btn.config(text=os.path.basename(file))
                #self.filename.insert(4, file)
                self.filename[4] = file
                print(self.filename[4])



if __name__ == "__main__":
    root = tk.Tk()

    app = pdf_merger(root)

    root.mainloop()