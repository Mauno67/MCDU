import tkinter as tk

ikkuna = tk.Tk()
ikkuna.title("MCDU simulaattori A320/MD-11")

current_menu = None
previous_menu = None
return_to = None
disabled_menus = {'CFDIUtest'}

function_names = []
main_menus = ['MCDU_MENU', 'ATC_MENU', 'SECFPLN_MENU',
 'FUEL_MENU',' RADNAV_MENU', 'FPLN_MENU', 'DATA_MENU',
 'INIT_MENU', 'PERF_MENU','PROG_MENU','DIR_MENU']

def get_current_menu():
    if function_names:
        return function_names[-1]
    return None

def check_current_menu():
    global current_menu
    if function_names:
        current_menu = get_current_menu()
        if current_menu == 'CFDIUtest':
            disable_return()
        else:
            enable_return()

    
    else:
        pass
    ikkuna.after(1000, check_current_menu)

# Määrittele Canvas-widget
canvas = tk.Canvas(ikkuna, width=800, height=480, bg="black")
canvas.grid(row=0, column=0, columnspan=10)

def update_display(text, positions):
    canvas.delete("all")  # Poista vanhat tekstit
    for (txt, pos) in zip(text, positions):
        canvas.create_text(pos[0], pos[1], text=txt, fill="green", font=("Courier", 12), anchor=pos[2])

# ------ Painikkeiden funktiot ------ #
def btn_dir():
    update_display(["DIR TO"], [(400, 40, "n")])
    function_names.clear()
    function_names.append("DIR_MENU")

def btn_prog():
    update_display(["PROG"], [(400, 40, "n")])
    function_names.clear()
    function_names.append("PROG_MENU")

def btn_perf():
    update_display(["PERFORMANCE"], [(400, 40, "n")])
    function_names.clear()
    function_names.append('PERF_MENU')

def btn_init():
    update_display(["INITIALIZATION"], [(400, 40, "n")])
    function_names.clear()
    function_names.append('INIT_MENU')

def btn_data():
    update_display(["DATA INDEX"], [(400, 40, "n")])
    function_names.clear()
    function_names.append('DATA_MENU')

def btn_fpln():
    update_display(["FLIGHT PLAN A"], [(400, 40, "n")])
    function_names.clear()
    function_names.append('FPLN_MENU')

def btn_radNav():
    update_display(["RADIO NAV"], [(400, 40, "n")])
    function_names.clear()
    function_names.append('RADNAV_MENU')

def btn_FuelPred():
    update_display(["FUEL PRED"], [(400, 40, "n")])
    function_names.clear()
    function_names.append('FUEL_MENU')

def btn_Secfpln():
    update_display(["SEC F-PLN"], [(400, 40, "n")])
    function_names.clear()
    function_names.append('SECFPLN_MENU')

def btn_atcComm_MENU():
    update_display(["ATC MENU"], [(400, 40, "n")])
    function_names.clear()
    function_names.append('ATC_MENU')

def btn_McduMenu_MENU():
    update_display(
        [
            "MCDU MENU", 
            "LSK1   <CFDS", 
            "LSK2   <ATSU", 
            "LSK3   <AIDS", 
            "LSK4   <FMGC"
        ],
        [(400, 40, "n"), (100, 100, "w"), (100, 150, "w"), (100, 200, "w"), (100, 250, "w")]
    )
    function_names.clear()
    if 'MCDU_MENU' not in function_names:
        function_names.append('MCDU_MENU')
#============== CFDS POLKU ==============#

def CFDS_MENU():
    update_display(
        [
            "CFDS INITIAL MENU", 
            "LSK1 <LRU FAULTS", 
            "LSK2 <LRU MAINTENANCE", 
            "LSK3 <ACARS FAULT LIST"
        ],
        [(400, 40, "n"), (100, 100, "w"), (100, 150, "w"), (100, 200, "w")]
    )
    if 'CFDS_MENU' not in function_names:
        function_names.append('CFDS_MENU')

## ## ##  LRU FAULTS ## ## ##

def LRUfault_MENU():
    update_display(
        [
            "CFDS LRE FAULTS", 
            "LRUS REPORTING", 
            "MAINT MEMORY FAULTS", 
            "NO FAULTS REPORTED", 
            "LSK6 <RETURN"
        ],
        [(400, 40, "n"), (400, 100, "n"), (400, 120, "n"), (400, 200, "n"), (100, 350, "w")]
    )
    
    if 'LRUfault_MENU' not in function_names:
        function_names.append("LRUfault_MENU")

## ## ##  LRU MAINTENANCE ## ## ## 

def LRUmaint_MENU():
    update_display(
        [
            "CFDS LRU MAINTENANCE",
            "LSK1 <ABSCU           BTTPU>  RSK1",
            "LSK2 <ACC-1           CFDIU>  RSK2",
            "LSK3 <ACC-2           CPC-1>  RSK3",
            "LSK4 <ACC-3           CPC-2>  RSK4",
            "LSK5 <ASCU            FCC-1>  RSK5",
            "LSK6 <RETURN    LRU ABBREVS>  RSK6"
        ],
        [
            (400, 40, "n"), (100, 100, "w"), (100, 150, "w"), (100, 200, "w"), 
            (100, 250, "w"), (100, 300, "w"), (100, 350, "w"),
            (700, 100, "e"), (700, 150, "e"), (700, 200, "e"), 
            (700, 250, "e"), (700, 300, "e"), (700, 350, "e")
        ]
    )
    
    if 'LRUmaint_MENU' not in function_names:
        function_names.append('LRUmaint_MENU')

################## CFDIU polku ####################
def SystemMaint_MENU(SysName):
    update_display(
        [
            f"{SysName} MAINTENANCE",
            "LSK1 <CURRENT FAULTS",
            "LSK2 <FAULT REVIEW",
            "LSK3 <RETURN-TO-SERVICE TEST",
            "LSK5 <ERASE MAINT MEMORY",
            "LSK6 <RETURN"
        ],
        [
            (400,40, "n"), (100,100, "w"), (100, 150, "w"), (100, 200, "w"), (100,300,"w"), (100, 350, "w")

        ]
    )
    if f'{SysName}maint_MENU' not in function_names:
        function_names.append(f'{SysName}maint_MENU')

def CURRENTfaults_CFDIU_MENU():
    update_display(
        [
            "CFDIU CURRENT FAULTS",
            "NO FAULTS",
            "LSK6 <RETURN"
        ],
    
        [
            (400,40, "n"), (400, 200, "n"), (100, 350, "w")
        ]
    )
    if 'CURRENTfaults_MENU' not in function_names:
        function_names.append('CURRENTfaults_MENU')

def CFDIUfaultReview_MENU():
    update_display(
        [
            "CFDIU FAULT REVIEW",
            "lSK1 <LEG 01   Faults  2",
            "LSK2 <LEG 03   Faults  1",
            "LSK6 <RETURN"
        ],
        [
            (400, 40, "n"), (100, 100, "w"), (100, 150, "w"), (100, 350, "w")
        ]
    )
    if 'CFDIUfaultReview_MENU' not in function_names:
        function_names.append('CFDIUfaultReview_MENU')


#////////////////////////////////////////////////////////////#
def test(SysName):
    update_display(
        [
            f"{SysName} CFDS R-T-S TEST",
            "AuTOMATIC TEST",
            "IN PROGRESS",
            "CFDIU ON 1234567-890",
            "CONFIG CODE",
            "ABCDE"
        ],
        [
            (400, 40, "n"), (400,60,"n"), (400, 150, "n"), (400, 180, "n"), (400, 210, "n"), (400, 240, "n")
        ]
    )
    disable_buttons()
    if f'{SysName}test' not in function_names:
        function_names.append(f'{SysName}test')
    ikkuna.after(5000, perform_test)
        
def perform_test():
    update_display(
        [
            "CFDIU CFDS R-T-S TEST",
            "ATOMATIC TEST",
            "PASSED",
            "CFDIU ON 1234567-890",
            "CONFIG CODE",
            "ABCDE",
            "CONTINUE> RSK6"
        ],
        [
            (400, 40, "n"), (400,60,"n"), (400, 150, "n"), (400, 180, "n"), (400, 210, "n"), (400, 240, "n"),(700, 350, "e")
        ]
    )

    enable_buttons()

def test2(SysName):
    update_display(
        [
            f"{SysName} CFDS R-T-S TEST",
            "AUTOMATIC TEST",
            "ALL",
            "TEST PASSED",
            "LSK6 <RETURN",
            "CONTINUE> RSK6"
        ],

        [
            (400, 40, "n"), (400,60, "n"), (400,150, "n"), (400, 180, "n"), (100, 350, "w"), (700,350, "e")
        ]
    )
    if f'{SysName}test2' not in function_names:
        function_names.append(f'{SysName}test2')

def test3(SysName):
    update_display(
        [
            f"{SysName} CFDS R-T-S TEST",
            "AUTOMATIC TEST",
            "R-T-S TEST COMPLETED",
            "LSK5 <MCDU KEYBOARD TEST",
            "LSK6 <RETURN"
        ],
        [(400,40,"n"), (400,60,"n"), (400,15,"n"), (100,300,"w"), (100,350,"w")]
    )
    if f'{SysName}test3' not in function_names:
        function_names.append(f'{SysName}test3')

########### FCC1 polku #############

def Systemmaint2_MENU(SysName):
    update_display(
        [
            f"{SysName} MAINTENANCE",
            "LSK1 <CURRENT FAULTS",
            "LSK2 <FAULT REVIEW",
            "LSK3 <RETURN-TO-SERVICE TEST",
            "LSK4 <SENSOR READOUT",
            "LSK5 <ERASE MAINT MEMORY",
            "LSK6 <RETURN",
            "HEX DATA> RSK6"
        ],
        [(400,40, "n"),(100,100, "w"), (100, 150, "w"), (100, 200, "w"), (100,250,"w"),(100,300,"w"), (100, 350, "w"), (700,350,"e")]
    )
    if f'{SysName}maint' not in function_names:
        function_names.append(f'{SysName}maint')
#============== ACARS POLKU ==============#

def ACARS_MENU():
    update_display(
        [
            "ACARS FAULT LIST", 
            "FAULTS REPORTED BY CFDS LRUS", 
            "LSK2 <SEND LIST TO ACARS", 
            "LSK3 <PREVIEW LIST", 
            "LSK6 <RETURN"
        ],
        [(400, 40, "n"), (400, 100, "n"), (100, 150, "w"), (100, 200, "w"), (100, 350, "w")]
    )
    if 'ACARSfault_MENU' not in function_names:
        function_names.append('ACARSfault_MENU')

 ## ## ## ACARS TRANSMISSION ## ## ##   

def ACARStrans():
    update_display(
        ["ACARS TRANSMISSION\nINITIATED\nWAIT FOR COMPLETION"], [(400, 200, "n")]
    )
    ikkuna.after(30, lambda: update_display(
        ["ACARS TRANSMISSION\nCOMPLETED", "LSK6 <RETURN"], [(400, 200, "n"), (100, 350, "w")]
    ))
    function_names.append('ACARStrans_MENU')

# --------- AIRPORT --------- #
def btn_AirPort():
    update_display("AIR PORT", "n")
    function_names.append('AIRPORT_MENU')


# --------- LSK nappulat --------- #
def handle_lsk_btn(btn_number):
    global current_menu
    current_menu = get_current_menu()
    print(f"Current menu: {current_menu}, Function Names: {function_names}")


    
    if current_menu == "MCDU_MENU":
        if btn_number == 1:
            CFDS_MENU()
        if btn_number == 2:
            pass
        if btn_number == 3:
            pass

        # Lisää tarvittaessa muita vaihtoehtoja tähän valikkoon

    elif current_menu == 'CFDS_MENU':
        if btn_number == 1:
            LRUfault_MENU()
        elif btn_number == 2:
            LRUmaint_MENU()
        elif btn_number == 3:
            ACARS_MENU()
        # Lisää muut valinnat
    
    elif current_menu == 'LRUmaint_MENU':
        if btn_number == 1:
            pass

    elif current_menu == 'CFDIUmaint_MENU':
        if btn_number == 1:
            CURRENTfaults_CFDIU_MENU() 
        elif btn_number == 2:
            CFDIUfaultReview_MENU()
        elif btn_number == 3:
            test('CFDIU')

        # Lisää muita vaihtoehtoja
    # Lisää muita valikkotarkastuksia

    # Paluu nappula
    if btn_number == 6:
        if current_menu in ['CFDIUtest2', 'CFDIUtest3']:
            palaa_valikkoon('CFDIUmaint_MENU')
        elif len(function_names) > 1:
            haku()  
        else:
            pass
        return
        
         


def handle_rsk_btn(btn_number):
    current_menu = get_current_menu()
    
    if current_menu == 'LRUmaint_MENU':
        if btn_number == 1:
            print("Nappia 1 painettu")
        elif btn_number == 2:
            SystemMaint_MENU('CFDIU')
            print("Nappia 2")
        elif btn_number == 5:
            Systemmaint2_MENU('FCC-1')
    elif current_menu == 'CFDIUtest':
        if btn_number == 6:
            test2('CFDIU')
    elif current_menu == 'CFDIUtest2':
        if btn_number == 6:
            test3('CFDIU')

# LSK namiskat
def lsk1_btn_act():
    handle_lsk_btn(1)

def lsk2_btn_act():
    handle_lsk_btn(2)

def lsk3_btn_act():
    handle_lsk_btn(3)

def lsk4_btn_act():
    handle_lsk_btn(4)

def lsk5_btn_act():
    handle_lsk_btn(5)

def lsk6_btn_act():
    handle_lsk_btn(6)


# RSK namiskat
def rsk1_btn_act():
    handle_rsk_btn(1)

def rsk2_btn_act():
    handle_rsk_btn(2)

def rsk3_btn_act():
    handle_rsk_btn(3)

def rsk4_btn_act():
    handle_rsk_btn(4)

def rsk5_btn_act():
    handle_rsk_btn(5)

def rsk6_btn_act():
    handle_rsk_btn(6)

# --------- Kirjasto funktioille + funktion haku --------- #

def haku():
    global previous_menu
    if len(function_names) > 1:
        function_names.pop()  # Poistetaan nykyinen menu
        previous_menu = function_names[-1]  # Edellinen menu
        siirry_valikkoon(previous_menu)  # Kutsutaan edellistä valikkoa
    else:
        print("ei edellistä valikkoa.")

def palaa_valikkoon(valikko_nimi):
    global function_names
    if valikko_nimi in function_names:
        # Palataan määriteltyyn valikkoon leikkaamalla pino
        function_names = function_names[:function_names.index(valikko_nimi) + 1]
        siirry_valikkoon(valikko_nimi)  # Kutsutaan haluttua valikkofunktiota
        print(f"Tämän hetkinen polku{function_names}")
    else:
        print(f"Valikkoa '{valikko_nimi}' ei löydy polusta.")  # Virheviesti

def siirry_valikkoon(valikko_nimi):
    if valikko_nimi in menu_functions:
        menu_functions[valikko_nimi]()
    else:
        print(f"Valikkoa {valikko_nimi} ei ole määritelty")

if function_names:
    last_function = function_names[-1] # Hakee listan viimeisen tiedon
    print(f"Viimeinen muuttuja on: {last_function}")
else:
    print("Lista on tyhjä")

menu_functions = {name: func for name, func in globals().items() if callable(func)and name.endswith("_MENU" or name.endswith("test"))}

menu_functions.update({
    
})




# --------- Painikkeet ylärivi --------- #

btn_dir = tk.Button(ikkuna, text="DIR", command=btn_dir)
btn_dir.grid(row=2, column=1, sticky="nsew")

btn_prog = tk.Button(ikkuna, text="PROG", command=btn_prog)
btn_prog.grid(row=2, column=2, sticky="nsew")

btn_perf = tk.Button(ikkuna, text="PERF", command=btn_perf)
btn_perf.grid(row=2, column=3, sticky="nsew")

btn_init = tk.Button(ikkuna, text="INIT", command=btn_init)
btn_init.grid(row=2, column=4, sticky="nsew")

btn_data = tk.Button(ikkuna, text="DATA", command=btn_data)
btn_data.grid(row=2, column=5, sticky="nsew")

empty_space = tk.Label(ikkuna, text="")
empty_space.grid(row=2, column=8, sticky="nsew")

# --------- Painikkeet keskirivi --------- #

btn_fpln = tk.Button(ikkuna, text="F-PLN", command=btn_fpln)
btn_fpln.grid(row=3, column=1, sticky="nsew")

btn_radNav = tk.Button(ikkuna, text="RAD \nNAV", command=btn_radNav)
btn_radNav.grid(row=3, column=2, sticky="nsew")

btn_FuelPred = tk.Button(ikkuna, text="FUEL \nPRED", command=btn_FuelPred)
btn_FuelPred.grid(row=3, column=3, sticky="nsew")

btn_Secfpln = tk.Button(ikkuna, text="SEC \nF-PLN", command=btn_Secfpln)
btn_Secfpln.grid(row=3, column=4, sticky="nsew")

btn_atcComm = tk.Button(ikkuna, text="ATC \nCOMM", command=btn_atcComm_MENU)
btn_atcComm.grid(row=3, column=5, sticky="nsew")

btn_McduMenu = tk.Button(ikkuna, text="MCDU \nMENU", command=btn_McduMenu_MENU)
btn_McduMenu.grid(row=3, column=6, sticky="nsew")


# --------- LSK nappulat --------- #
btn_lsk1 = tk.Button(ikkuna, text="lsk1", command=lambda: lsk1_btn_act())
btn_lsk1.grid(row=1, column=0, sticky="nsew")

btn_lsk2 = tk.Button(ikkuna, text="lsk2", command=lambda: lsk2_btn_act())
btn_lsk2.grid(row=2, column=0, sticky="nsew")

btn_lsk3 = tk.Button(ikkuna, text="lsk3", command=lambda: lsk3_btn_act())
btn_lsk3.grid(row=3, column=0, sticky="nsew")

btn_lsk4 = tk.Button(ikkuna, text="lsk4", command=lambda: lsk4_btn_act())
btn_lsk4.grid(row=4, column=0, sticky="nsew")

btn_lsk5 = tk.Button(ikkuna, text="lsk5", command=lambda: lsk5_btn_act())
btn_lsk5.grid(row=5, column=0, sticky="nsew")

btn_lsk6 = tk.Button(ikkuna, text="lsk6", command=lambda: lsk6_btn_act())
btn_lsk6.grid(row=6, column=0, sticky="nsew")

# --------- RSK nappulat --------- #
btn_rsk1 = tk.Button(ikkuna, text="RSK1", command=lambda: rsk1_btn_act())
btn_rsk1.grid(row=1, column=7, sticky="nsew")

btn_rsk2 = tk.Button(ikkuna, text="RSK2", command= lambda: rsk2_btn_act())
btn_rsk2.grid(row=2, column=7, sticky="nsew")

btn_rsk3 = tk.Button(ikkuna, text="RSK3", command=lambda: rsk3_btn_act())
btn_rsk3.grid(row=3, column=7, sticky="nsew")

btn_rsk4 = tk.Button(ikkuna, text="RSK4", command= lambda: rsk4_btn_act())
btn_rsk4.grid(row=4, column=7, sticky="nsew")

btn_rsk5 = tk.Button(ikkuna, text="RSK5", command= lambda: rsk5_btn_act())
btn_rsk5.grid(row=5, column=7, sticky="nsew")

btn_rks6 = tk.Button(ikkuna, text="RSK6", command=lambda: rsk6_btn_act())
btn_rks6.grid(row=6, column=7, sticky="nsew")


def disable_buttons():
    for button in all_buttons:
        button.config(state=tk.DISABLED)

def enable_buttons():
    for button in all_buttons:
        button.config(state=tk.NORMAL)


def disable_return():
    btn_lsk6.config(state=tk.DISABLED)

def enable_return():
    btn_lsk6.config(state=tk.NORMAL)



all_buttons = [btn_dir, btn_prog, btn_perf, btn_init, btn_data, btn_fpln, btn_radNav, btn_FuelPred, btn_Secfpln, btn_atcComm,
               btn_McduMenu, btn_lsk1, btn_lsk2,btn_lsk3,btn_lsk4,btn_lsk5,btn_lsk6,btn_rsk1,btn_rsk2,btn_rsk3,
               btn_rsk4,btn_rsk5,btn_rks6]
# --------- Sarakkeiden ja rivien venymä --------- #

for i in range(6):
    ikkuna.grid_rowconfigure(i, weight=1)

ikkuna.grid_rowconfigure(0, weight=1)
ikkuna.grid_rowconfigure(2, weight=1)
ikkuna.grid_rowconfigure(3, weight=1)

check_current_menu()
ikkuna.mainloop()