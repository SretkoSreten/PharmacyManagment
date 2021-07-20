from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

app = Tk()

class App:
    def __init__(self, root):
        self.root = root
        self.root.config(bg = 'skyblue')
        self.width = 1400
        self.height = 900
        self.root.title("Hospital Managment System")
        self.root.resizable(False, False)
        self.root.geometry("1300x800")
        #============= variables start 

        self.name_of_tablets = StringVar()
        self.ref_no = StringVar()
        self.dose = StringVar()
        self.no_tablets = StringVar()
        self.lot = StringVar()
        self.issused_data = StringVar()
        self.exp_data = StringVar()
        self.daily_dose = StringVar()
        self.side_effects = StringVar()
        self.further_info = StringVar()
        self.storage_advice = StringVar()
        self.driving_machine = StringVar()
        self.medication = StringVar()
        self.patient_id = StringVar()
        self.nhs_number = StringVar()
        self.patient_name = StringVar()
        self.patient_address = StringVar()
        self.data_birth = StringVar()

        #==============variables end

        #------------ header draw start ---------------

        header_title = Label(self.root, text = "Hospital Managment System",
        bd = 10, relief = GROOVE, font = ('times new roman', 40, 'bold'),
        bg = 'white', fg = 'red')
        header_title.pack(side = TOP, fill = X)

        #------------- header draw end -----------

        main_frame = Frame(self.root, bd = 10, relief = RIDGE, bg = 'white')
        main_frame.place(x = 0, y = 85, width = self.width, height = 470)
        #============main========#
        
        width = self.width - 100
        height = self.height / 2

        left_frame_container = Frame(main_frame, bd = 10, relief = RIDGE, bg = 'white', 
        width = width / 2, height = height)
        left_frame_container.grid(row = 0, column = 0, pady = 10, padx = 25)

        right_frame_container = Frame(main_frame, bd = 10, relief = RIDGE, bg = 'white',
        width = width, height = height)
        right_frame_container.grid(row = 0, column = 1, padx = 10, pady = 20)

        self.right_frame_container = right_frame_container
        self.left_frame_container = left_frame_container

        #============main========#

        fontEntrySize = 13
        fontSize = 11
        pady_ = 7
        padx_ = 5

        #============ left start

        name_of_tablets = Label(left_frame_container, text = "Name of tablets: ", fg = "black", 
        font = ("times new roman",fontSize, "bold"))
        name_of_tablets.grid(row = 0, column = 0, pady = pady_, padx = padx_, sticky = 'w')
        name_of_tablets_choose = ttk.Combobox(left_frame_container, textvariable = self.name_of_tablets, 
        font = ("times new roman", fontEntrySize, "bold"))
        name_of_tablets_choose['values'] = ('brufen', 'aspirin', 'paracetamol', 'propolis')
        name_of_tablets_choose.grid(row = 0, column = 1, pady = pady_, padx = padx_, sticky = 'w')


        entry_of_tablets = Entry(left_frame_container, textvariable = self.name_of_tablets, 
        relief = GROOVE, bd = 5, font = ("times new roman",fontEntrySize, "bold"))
        entry_of_tablets.grid(row = 0, column = 1, pady = pady_, padx = padx_, sticky = 'w')


        reference_no_name = Label(left_frame_container, text = "Reference No: ", fg = "black", font = ("times new roman",fontSize, "bold"))
        reference_no_name.grid(row = 1, column = 0, pady = pady_, padx = padx_, sticky = 'w')
        reference_no_entry = Entry(left_frame_container, textvariable = self.ref_no,
        relief = GROOVE, bd = 5, font = ("times new roman",fontEntrySize, "bold"))
        reference_no_entry.grid(row = 1, column = 1, pady = pady_, padx = padx_, sticky = 'w')


        dose_name = Label(left_frame_container, text = "Dose: ", fg = "black", font = ("times new roman",fontSize, "bold"))
        dose_name.grid(row = 2, column = 0, pady = pady_, padx = padx_, sticky = 'w')
        entry_dose = Entry(left_frame_container, textvariable = self.dose, 
        relief = GROOVE, bd = 5, font = ("times new roman",fontEntrySize, "bold"))
        entry_dose.grid(row = 2, column = 1, pady = pady_, padx = padx_, sticky = 'w')


        no_tablets_name = Label(left_frame_container, text = "No.of Tablets: ", fg = "black", font = ("times new roman",fontSize, "bold"))
        no_tablets_name.grid(row = 3, column = 0, pady = pady_, padx = padx_, sticky = 'w')
        entry_no_tablets = Entry(left_frame_container, textvariable = self.no_tablets,
         relief = GROOVE, bd = 5, font = ("times new roman", fontEntrySize, "bold"))
        entry_no_tablets.grid(row = 3, column = 1, pady = pady_, padx = padx_, sticky = 'w')

        lot_name = Label(left_frame_container, text = "Lot: ", fg = "black", font = ("times new roman", fontSize, "bold"))
        lot_name.grid(row = 4, column = 0, pady = pady_, padx = padx_, sticky = 'w')
        entry_lot = Entry(left_frame_container, relief = GROOVE, textvariable = self.lot, 
        bd = 5, font = ("times new roman",fontEntrySize, "bold"))
        entry_lot.grid(row = 4, column = 1, pady = pady_, padx = padx_, sticky = 'w')


        issused_data_name = Label(left_frame_container, text = "Issused data: ", fg = "black", font = ("times new roman",fontSize, "bold"))
        issused_data_name.grid(row = 5, column = 0, pady = pady_, padx = padx_, sticky = 'w')
        entry_issused = Entry(left_frame_container, textvariable = self.issused_data, 
        relief = GROOVE, bd = 5, font = ("times new roman",fontEntrySize, "bold"))
        entry_issused.grid(row = 5, column = 1, pady = pady_, padx = padx_, sticky = 'w')

        exp_date_name = Label(left_frame_container, text = "Exp Date: ", fg = "black", font = ("times new roman",fontSize, "bold"))
        exp_date_name.grid(row = 6, column = 0, pady = pady_, padx = padx_, sticky = 'w')
        exp_entry = Entry(left_frame_container, textvariable = self.exp_data, 
        relief = GROOVE, bd = 5, font = ("times new roman",fontEntrySize, "bold"))
        exp_entry.grid(row = 6, column = 1, pady = pady_, padx = padx_, sticky = 'w')

        daily_dose_name = Label(left_frame_container, text = "Daily Dose: ", fg = "black", font = ("times new roman",fontSize, "bold"))
        daily_dose_name.grid(row = 7, column = 0, pady = pady_, padx = padx_, sticky = 'w')
        entry_dose = Entry(left_frame_container, textvariable = self.daily_dose, 
        relief = GROOVE, bd = 5, font = ("times new roman",fontEntrySize, "bold"))
        entry_dose.grid(row = 7, column = 1, pady = pady_, padx = padx_, sticky = 'w')

        side_effects_name = Label(left_frame_container, text = "Side Effects: ", fg = "black", font = ("times new roman",fontSize, "bold"))
        side_effects_name.grid(row = 8, column = 0, pady = pady_, padx = padx_, sticky = 'w')
        entry_side_effects = Entry(left_frame_container, textvariable = self.side_effects, 
        relief = GROOVE, bd = 5, font = ("times new roman",fontEntrySize, "bold"))
        entry_side_effects.grid(row = 8, column = 1, pady = pady_, padx = padx_, sticky = 'w')

        #=========== left end

        #============right start

        further_info_name = Label(left_frame_container, text = "Further Information: ", fg = "black", font = ("times new roman",fontSize, "bold"))
        further_info_name.grid(row = 0, column = 2, pady = pady_, padx = padx_, sticky = 'w')
        entry_further_info = Entry(left_frame_container, textvariable = self.further_info, relief = GROOVE, bd = 5, font = ("times new roman",fontEntrySize, "bold"))
        entry_further_info.grid(row = 0, column = 3, pady = pady_, padx = padx_, sticky = 'w')


        storage_advice_name = Label(left_frame_container, text = "Storage Advice: ", fg = "black", font = ("times new roman",fontSize, "bold"))
        storage_advice_name.grid(row = 1, column = 2, pady = pady_, padx = padx_, sticky = 'w')
        entry_storage_advice = Entry(left_frame_container, textvariable = self.storage_advice, relief = GROOVE, bd = 5, font = ("times new roman",fontEntrySize, "bold"))
        entry_storage_advice.grid(row = 1, column = 3, pady = pady_, padx = padx_, sticky = 'w')

        driving_machine_name = Label(left_frame_container, text = "Driving Machines: ", fg = "black", font = ("times new roman",fontSize, "bold"))
        driving_machine_name.grid(row = 2, column = 2, pady = pady_, padx = padx_, sticky = 'w')
        entry_driving_machine = Entry(left_frame_container, textvariable = self.driving_machine, relief = GROOVE, bd = 5, font = ("times new roman",fontEntrySize, "bold"))
        entry_driving_machine.grid(row = 2, column = 3, pady = pady_, padx = padx_, sticky = 'w')

        medic_name = Label(left_frame_container, text = "Medication: ", fg = "black", font = ("times new roman",fontSize, "bold"))
        medic_name.grid(row = 3, column = 2, pady = pady_, padx = padx_, sticky = 'w')
        entry_medic = Entry(left_frame_container, textvariable = self.medication, relief = GROOVE, bd = 5, font = ("times new roman",fontEntrySize, "bold"))
        entry_medic.grid(row = 3, column = 3, pady = pady_, padx = padx_, sticky = 'w')

        patient_id = Label(left_frame_container, text = "Patient Id: ", fg = "black", font = ("times new roman",fontSize, "bold"))
        patient_id.grid(row = 4, column = 2, pady = pady_, padx = padx_, sticky = 'w')
        entry_patient = Entry(left_frame_container, textvariable = self.patient_id, relief = GROOVE, bd = 5, font = ("times new roman",fontEntrySize, "bold"))
        entry_patient.grid(row = 4, column = 3, pady = pady_, padx = padx_, sticky = 'w')

        nhs_number = Label(left_frame_container, text = "NHS Number: ", fg = "black", font = ("times new roman",fontSize, "bold"))
        nhs_number.grid(row = 5, column = 2, pady = pady_, padx = padx_, sticky = 'w')
        entry_nhs_number = Entry(left_frame_container, textvariable = self.nhs_number, relief = GROOVE, bd = 5, font = ("times new roman",fontEntrySize, "bold"))
        entry_nhs_number.grid(row = 5, column = 3, pady = pady_, padx = padx_, sticky = 'w')

        patient_name = Label(left_frame_container, text = "Patient Name: ", fg = "black", font = ("times new roman",fontSize, "bold"))
        patient_name.grid(row = 6, column = 2, pady = pady_, padx = padx_, sticky = 'w')
        entry_patient_name = Entry(left_frame_container, textvariable = self.patient_name, relief = GROOVE, bd = 5, font = ("times new roman",fontEntrySize, "bold"))
        entry_patient_name.grid(row = 6, column = 3, pady = pady_, padx = padx_, sticky = 'w')

        date_birth = Label(left_frame_container, text = "Date of Birth: ", fg = "black", font = ("times new roman",fontSize, "bold"))
        date_birth.grid(row = 7, column = 2, pady = pady_, padx = padx_, sticky = 'w')
        entry_date = Entry(left_frame_container, textvariable = self.data_birth, relief = GROOVE, bd = 5, font = ("times new roman",fontEntrySize, "bold"))
        entry_date.grid(row = 7, column = 3, pady = pady_, padx = padx_, sticky = 'w')

        patient_address = Label(left_frame_container, text = "Patient Address: ", fg = "black", font = ("times new roman",fontSize, "bold"))
        patient_address.grid(row = 8, column = 2, pady = pady_, padx = padx_, sticky = 'w')
        entry_patient_address = Entry(left_frame_container, textvariable = self.patient_address, relief = GROOVE, bd = 5, font = ("times new roman",fontEntrySize, "bold"))
        entry_patient_address.grid(row = 8, column = 3, pady = pady_, padx = padx_, sticky = 'w')

        #=============== right end

        #=========== inspection start

        width_insp = width / 2 - 150
        height_insp = height - 50

        # inspection_container = Frame(self.right_frame_container, bd = 2, relief = RIDGE, bg = 'white',
        # width = width_insp, height = height_insp)
        # inspection_container.grid(row = 0, column = 0, padx = 20, pady = 20)

        self.show_inspection()

        #============ inspection btns end

        btnFontSize = 10
        btn_font = ('arial', 15, 'bold')
        btn_pad_x = 60
        btn_pad_y = 15

        btns_frame = Frame(self.root, bd = 10, relief = RIDGE, bg = 'white')
        btns_frame.place(x = 0, y = 560, width = self.width, height = 100)

        add_btn = Button(btns_frame, text = "Update", width = 10, font = btn_font, command = self.update)
        add_btn.grid(row = 0, column = 1, padx = btn_pad_x, pady = btn_pad_y)

        update_btn = Button(btns_frame, text = "Add", width = 10, font = btn_font, command = self.add)
        update_btn.grid(row = 0, column = 2, padx = btn_pad_x, pady = btn_pad_y)

        delete_btn = Button(btns_frame, text = "Delete", width = 10, font = btn_font, command = self.delete)
        delete_btn.grid(row = 0, column = 3, padx = btn_pad_x, pady = btn_pad_y)

        clear_btn = Button(btns_frame, text = "Reset", width = 10, font = btn_font, command = self.reset)
        clear_btn.grid(row = 0, column = 4, padx = btn_pad_x, pady = btn_pad_y)

        exit_btn = Button(btns_frame, text = "Exit", width = 10, font = btn_font, command = self.quit_)
        exit_btn.grid(row = 0, column = 5, padx = btn_pad_x, pady = btn_pad_y)

        #===================inspetion btns end

        #=================== table start

        column_width = 80

        TABLE_Frame = Frame(self.root, bd = 10, relief = RIDGE, bg = 'white')
        TABLE_Frame.place(x = 0, y = 670, width = self.width - 90, height = 130)

        scroll_x = Scrollbar(TABLE_Frame, orient = HORIZONTAL)
        scroll_y = Scrollbar(TABLE_Frame, orient = VERTICAL)

        self.table = ttk.Treeview(TABLE_Frame, 
        column = ('name_tablets', 'ref_no', 'no_tablets', 'lot', 'issused_data', 'exp_data', 'exp_data',
        'daily_dose', 'storage_adv', 'nhs_number', 'patient_name', 'dob', 'address', 'dose'), 
        xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)
        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)

        scroll_x.config()
        scroll_y.config()

        self.table.heading('name_tablets', text = 'Name of tablets')
        self.table.heading('ref_no', text = 'Reference No.')
        self.table.heading('dose', text = 'Doseage')
        self.table.heading('no_tablets', text = 'No. of tablets')
        self.table.heading('lot', text = 'Lot')
        self.table.heading('issused_data', text = 'Issused Date')
        self.table.heading('exp_data', text = 'Exp. Date')
        self.table.heading('daily_dose', text = 'Daily Dose')
        self.table.heading('storage_adv', text = 'Storage Adv.')
        self.table.heading('nhs_number', text = 'NHS Number')
        self.table.heading('patient_name', text = 'Patient Name')
        self.table.heading('dob', text = 'DOB')
        self.table.heading('address', text = 'Address')

        self.table['show'] = 'headings'

        self.table.column('name_tablets', width = column_width)
        self.table.column('ref_no', width = column_width)
        self.table.column('dose', width = column_width)
        self.table.column('no_tablets', width = column_width)
        self.table.column('lot', width = column_width)
        self.table.column('issused_data', width = column_width)
        self.table.column('exp_data', width = column_width)
        self.table.column('daily_dose', width = column_width)
        self.table.column('storage_adv', width = column_width)
        self.table.column('nhs_number', width = column_width)
        self.table.column('patient_name', width = column_width)
        self.table.column('dob', width = column_width)
        self.table.column('address', width = column_width)

        self.table.pack(fill = BOTH, expand = 1)

        #============== table end

    def quit_(self):
        self.root.destroy()

    def reset(self):
        self.name_of_tablets.set('')
        self.ref_no.set('')
        self.dose.set('')
        self.no_tablets.set('')
        self.lot.set('')
        self.issused_data.set('')
        self.exp_data.set('')
        self.daily_dose.set('')
        self.side_effects.set('')
        self.further_info.set('')
        self.storage_advice.set('')
        self.driving_machine.set('')
        self.medication.set('')
        self.patient_id.set('')
        self.nhs_number.set('')
        self.patient_name.set('')
        self.patient_address.set('')
    
    def show_inspection(self):

        width = self.width - 100
        height = self.height / 2

        width_insp = width / 2 - 150
        height_insp = height

        fontEntrySize = 13
        fontSize = 11
        pady_ = 7
        padx_ = 5

        inspection_container = Frame(self.right_frame_container, bd = 2, relief = RIDGE, bg = 'white',
        width = width_insp, height = height_insp)
        inspection_container.grid(row = 0, column = 0, padx = 20, pady = 20)


        insp_tablets = Label(inspection_container, text = "Name of tablets: ", fg = "black", font = ("times new roman",fontSize, "bold"))
        insp_tablets.grid(row = 0, column = 0, padx = padx_, sticky = 'w')
        label_insp_tablets = Label(inspection_container, textvariable = self.name_of_tablets, text = "", font = ("times new roman",fontEntrySize, "bold"))
        label_insp_tablets.grid(row = 0, column = 1, padx = padx_, sticky = 'w')

        insp_no_name = Label(inspection_container, text = "Reference No: ", fg = "black", font = ("times new roman",fontSize, "bold"))
        insp_no_name.grid(row = 1, column = 0, padx = padx_, sticky = 'w')
        insp_no_entry = Label(inspection_container, bd = 5, textvariable = self.ref_no, font = ("times new roman",fontEntrySize, "bold"))
        insp_no_entry.grid(row = 1, column = 1, padx = padx_, sticky = 'w')


        insp_dose_name = Label(inspection_container, text = "Dose: ", fg = "black", font = ("times new roman",fontSize, "bold"))
        insp_dose_name.grid(row = 2, column = 0, padx = padx_, sticky = 'w')
        insp_entry_dose = Label(inspection_container ,textvariable = self.dose, bd = 5, font = ("times new roman",fontEntrySize, "bold"))
        insp_entry_dose.grid(row = 2, column = 1, padx = padx_, sticky = 'w')


        insp_tablets_name = Label(inspection_container, text = "Number of tablets: ", fg = "black", font = ("times new roman",fontSize, "bold"))
        insp_tablets_name.grid(row = 3, column = 0, padx = padx_, sticky = 'w')
        insp_no_tablets = Label(inspection_container, textvariable = self.no_tablets, bd = 5, font = ("times new roman", fontEntrySize, "bold"))
        insp_no_tablets.grid(row = 3, column = 1, padx = padx_, sticky = 'w')

        insp_lot_name = Label(inspection_container, text = "Lot: ", fg = "black", font = ("times new roman", fontSize, "bold"))
        insp_lot_name.grid(row = 4, column = 0,  padx = padx_, sticky = 'w')
        insp_entry_lot = Label(inspection_container, textvariable = self.lot, bd = 5, font = ("times new roman",fontEntrySize, "bold"))
        insp_entry_lot.grid(row = 4, column = 1,  padx = padx_, sticky = 'w')


        insp_issused_data_name = Label(inspection_container, text = "Issused data: ", fg = "black", font = ("times new roman",fontSize, "bold"))
        insp_issused_data_name.grid(row = 5, column = 0, padx = padx_, sticky = 'w')
        insp_entry_issused = Label(inspection_container, textvariable = self.issused_data, bd = 5, font = ("times new roman",fontEntrySize, "bold"))
        insp_entry_issused.grid(row = 5, column = 1,  padx = padx_, sticky = 'w')

        insp_exp_date_name = Label(inspection_container, text = "Exp Date: ", fg = "black", font = ("times new roman",fontSize, "bold"))
        insp_exp_date_name.grid(row = 6, column = 0,  padx = padx_, sticky = 'w')
        insp_exp_entry = Label(inspection_container, textvariable = self.exp_data, bd = 5, font = ("times new roman",fontEntrySize, "bold"))
        insp_exp_entry.grid(row = 6, column = 1, padx = padx_, sticky = 'w')

        insp_daily_dose_name = Label(inspection_container, text = "Daily Dose: ", fg = "black", font = ("times new roman",fontSize, "bold"))
        insp_daily_dose_name.grid(row = 7, column = 0, padx = padx_, sticky = 'w')
        insp_entry_dose = Label(inspection_container, textvariable = self.daily_dose, bd = 5, font = ("times new roman",fontEntrySize, "bold"))
        insp_entry_dose.grid(row = 7, column = 1, padx = padx_, sticky = 'w')


        insp_side_effect_name = Label(inspection_container, text = "Posible Effects: ", fg = "black", font = ("times new roman",fontSize, "bold"))
        insp_side_effect_name.grid(row = 8, column = 0,  padx = padx_, sticky = 'w')
        insp_side_effect_entry = Label(inspection_container, textvariable = self.side_effects, bd = 5, font = ("times new roman",fontEntrySize, "bold"))
        insp_side_effect_entry.grid(row = 8, column = 1,  padx = padx_, sticky = 'w')

        insp_further_info_name = Label(inspection_container, text = "Further Information: ", fg = "black", font = ("times new roman",fontSize, "bold"))
        insp_further_info_name.grid(row = 9, column = 0,  padx = padx_, sticky = 'w')
        insp_further_info_entry = Label(inspection_container, textvariable = self.further_info, bd = 5, font = ("times new roman",fontEntrySize, "bold"))
        insp_further_info_entry.grid(row = 9, column = 1,  padx = padx_, sticky = 'w')

        insp_storage_advice_name = Label(inspection_container, text = "Storage Advice: ", fg = "black", font = ("times new roman",fontSize, "bold"))
        insp_storage_advice_name.grid(row = 10, column = 0,  padx = padx_, sticky = 'w')
        insp_storage_advice_entry = Label(inspection_container, textvariable = self.storage_advice, bd = 5, font = ("times new roman",fontEntrySize, "bold"))
        insp_storage_advice_entry.grid(row = 10, column = 1,  padx = padx_, sticky = 'w')

        insp_driving_name = Label(inspection_container, text = "Driving or Using Machines: ", fg = "black", font = ("times new roman",fontSize, "bold"))
        insp_driving_name.grid(row = 11, column = 0,  padx = padx_, sticky = 'w')
        insp_driving_entry = Label(inspection_container, textvariable = self.driving_machine, bd = 5, font = ("times new roman",fontEntrySize, "bold"))
        insp_driving_entry.grid(row = 11, column = 1,  padx = padx_, sticky = 'w')

    def add(self):
        name_of_tablets = self.name_of_tablets.get()
        ref_no = self.ref_no.get()
        dose = self.dose.get()
        no_tablets = self.no_tablets.get()
        lot = self.lot.get()
        issused_data = self.issused_data.get()
        exp_data = self.exp_data.get()
        daily_dose = self.daily_dose.get()
        side_effects = self.side_effects.get()
        further_info = self.further_info.get()
        storage_advice = self.storage_advice.get()
        driving_machine = self.driving_machine.get()
        medication = self.medication.get()
        patient_id = self.patient_id.get()
        nhs_number = self.nhs_number.get()
        patient_name = self.patient_name.get()
        patient_address = self.patient_address.get()
        data_birth = self.data_birth.get()

        if name_of_tablets == "":
            MessageBox.showinfo('Add Error Status', "Fileds must be filled")   
        else:         
            con = mysql.connect(
                host = "localhost",
                user = "root",
                password = '',
                database = "hospital db"
            )
            custor = con.cursor()
            sql = "insert into tablet (name_of_tablets, ref_no, dose, no_tablets, lot, issused_data, exp_date, daily_dose, side_effects, further_info, storage_advice, driving_machines, medication, patient_id, nhs_number, patient_name, patient_address, date_of_birth) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            custor.execute(sql, (name_of_tablets, ref_no, dose, no_tablets, lot, issused_data, exp_data, daily_dose, side_effects, further_info, storage_advice, driving_machine, medication, patient_id, nhs_number, patient_name, patient_address, data_birth))
            custor.execute('commit')

            MessageBox.showinfo('Add Status', "Document successfully inserted")

            self.show()

    def show(self):
        con = mysql.connect(
            host = "localhost",
            user = "root",
            password = '',
            database = "hospital db"
        )
        custor = con.cursor()
        custor.execute('select * from tablet')
        tablets = custor.fetchall()

        if len(tablets) > 0:
            self.table.delete(*self.table.get_children())
            for tablet in tablets:
                self.table.insert('', END, values = tablet)
            con.commit()
        con.close() 


    def delete(self):
        if self.patient_id.get() == "":
            MessageBox.showinfo('Remove Error Status', "Roll must be filled")   
        else:
            tablet_id = self.patient_id.get()

            con = mysql.connect(
                host = "localhost",
                user = "root",
                password = '',
                database = "hospital db"
            )

            custor = con.cursor()
            custor.execute("delete from tablet where id = '" + tablet_id + "'")
            con.commit()
            con.close()

            self.show()

            MessageBox.showinfo('Remove Status', "Remove successfully")

    def update(self):
        name_of_tablets = self.name_of_tablets.get()
        ref_no = self.ref_no.get()
        dose = self.dose.get()
        no_tablets = self.no_tablets.get()
        lot = self.lot.get()
        issused_data = self.issused_data.get()
        exp_data = self.exp_data.get()
        daily_dose = self.daily_dose.get()
        side_effects = self.side_effects.get()
        further_info = self.further_info.get()
        storage_advice = self.storage_advice.get()
        driving_machine = self.driving_machine.get()
        medication = self.medication.get()
        patient_id = self.patient_id.get()
        nhs_number = self.nhs_number.get()
        patient_name = self.patient_name.get()
        patient_address = self.patient_address.get()
        data_birth = self.data_birth.get()

        _id = self.patient_id.get()

        if _id == "":
            MessageBox.showinfo('Add Error Status', "Fileds must be filled")   
        else:         
            con = mysql.connect(
                host = "localhost",
                user = "root",
                password = '',
                database = "hospital db"
            )
            custor = con.cursor()
            sql = "update tablet set name_of_tablets = '"+name_of_tablets+"', ref_no = '"+ref_no+"', dose = '"+dose+"', no_tablets = '"+no_tablets+"', lot = '"+lot+"', issused_data = '"+issused_data+"', exp_date = '"+exp_data+"', daily_dose = '"+daily_dose+"', side_effects = '"+side_effects+"', further_info = '"+further_info+"', storage_advice = '"+storage_advice+"', driving_machines = '"+driving_machine+"', medication = '"+medication+"', patient_id = '"+patient_id+"', nhs_number = '"+nhs_number+"', patient_name = '"+patient_name+"', patient_address = '"+patient_address+"', date_of_birth = '"+data_birth+"' where id = '"+_id+"'"
            custor.execute(sql)
            custor.execute('commit')

            MessageBox.showinfo('Add Status', "Document successfully updated")

            self.show()

app_ = App(app)
app_.show()

app.mainloop()