import random


def phone_Maker():
    phone = "+569"+str(random.randrange(10000000,99999999,1))
    return phone


def RUT_CHOICE():
    for rut in RUT_Dict:
        if RUT_Dict[rut]["Used"] == False:
            RUT_Dict[rut]["Used"] = True
            return rut
    
def Motivos():
    Dict = {}
    motivoFile = open("Files\Motivos.txt")
    Motivos = motivoFile.read().split(",")
    motivoFile.close()
    for motivo in Motivos:
        if motivo[0] == "0":
            Dict[motivo[1:]] = {"Llamada Realizada": False}
        else:
            Dict[motivo[1:]] = {"Llamada Realizada": True}
    return Dict

def Motivo_Choice(Realizada):
    motivos = Motivos()
    lista = []
    for key in motivos:
        if motivos[key]["Llamada Realizada"] == Realizada:
            lista.append(key)
    return random.choice(lista)
                


def Llamadas(Fechas):
    
    Duraciones = Duracion()
    llamadasDict = {}
    idLlamada = 0 #O-L
    rutClientes = []
    for rut in Clientes:
        rutClientes.append(rut)
    for idT in Tennants:
        for idA in Agentes:
            if Agentes[idA]["Tennant"] == idT:
                genteLlamada = []
                for llamada in range(10):
                    while True:
                        persona = random.choice(rutClientes)
                        if not(persona in genteLlamada and genteLlamada <7):
                            break
                    
                    realizada = random.choice([True, False])
                    motivo = Motivo_Choice(realizada)
                    llamadasDict[str(idLlamada)]= {
                            "Realizada": realizada,"Nombre archivo": "archivo"+str(idLlamada),
                            "Fecha llamada": Fechas[idLlamada], "Duracion": Duraciones[idLlamada], "Transcripcion":"Dato"+str(idLlamada),
                            "Motivo": motivo, "RUT Cliente": persona, "ID Agente": idA, "ID Supervisor": "null",
                            "ID Campaña": "null"
                            }
                    idLlamada += 1
                     
    return llamadasDict
   
def Fecha_Llamada():
    date = ""
    dates = []
    meses = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    for years in range(2017,2020):
        for mes in meses:
            for i in range(random.randint(1,500)):
                day = random.randint(1, meses[mes])
                date += str(day)+"/"+str(mes)+"/"+str(years)
                dates.append(date)
                date = ""
    return dates


        
def Fecha_Campaña():
    dates = []
    date = ""
    meses = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    for years in range(2017,2020):
        for mes in meses:
            for i in range(1):
                date += str(1)+"/"+str(mes)+"/"+str(years)
                dates.append(date)
                date = ""
    return dates
        
    

def Duracion():
    duraciones = []
    for i in range(6000):
        duraciones.append(str(random.randint(0,1))+":"+str(random.randint(0,59))+":"+str(random.randint(0,59)))
    return duraciones
    
                

    

def Supervisado():
    for idS in Supervisores:
        supervisar = [True, False]*10
        for idA in Agentes:
            if len(supervisar)!=0:
                for idL in llamadas:
                    if Agentes[llamadas[idL]["ID Agente"]]["Tennant"] == Supervisores[idS]["Tennant"] and len(supervisar)!=0 and llamadas[idL]["ID Supervisor"] == "null":
                        choice = random.choice(supervisar)
                        supervisar.remove(choice)
                        if choice:
                            llamadas[idL]["ID Supervisor"] = idS

def Campaign_Reader():
    campList = []
    campFile = open("Files\Campañas.txt")
    Campaign = campFile.read().split(",")
    campFile.close()
    for item in range(len(Campaign)):
        campList.append(Campaign[item])

    return campList


def Tipificaciones_Reader():
    tipiDict = {}
    tipiFile = open("Files\Tipificaciones.txt")
    Tipificaciones = tipiFile.read().split(",")
    tipiFile.close()
    idP = 0
    cont = 0
    for item in range(len(Tipificaciones)):
        if cont == 1:
            tipiDict[str(idP)] = {"Type": Tipificaciones[item-1], "Pregunta asociada":Tipificaciones[item]}
            cont = 0
            idP += 1
        else:
            cont += 1
    return tipiDict
      
    

def Campaign():
    tipsDict = {}
    idCampaña = 0
    dates = Fecha_Campaña()
    fechaMes = 0
    for idT in Tennants:
        total = Campaign_Reader()
        for i in range(5):
            choice = random.choice(total)
            total.remove(choice)
            tipsDict[str(idCampaña)] = {"Fecha inicio": dates[fechaMes], "Fecha termino": dates[fechaMes+1], "Nombre": choice}
            idCampaña += 1
        fechaMes += 1
    return tipsDict

def Campaign_Tipificaciones():
    tipiCamp = []
    campañas = Campaign()
    tipificaciones = Tipificaciones_Reader()
    tipList = []
    for idT in tipificaciones:
        tipList.append(idT) #pozo
    for idC in campañas:
        temp = []
        cont = 0
        for i in range(4):
            choice= random.choice(tipList[cont*4:4*(cont+1)])
            if [idC,choice] not in tipiCamp:
                temp.append([int(idC), int(choice)])
                cont +=1 
        tipiCamp.append(temp)
            
    return tipiCamp
#######################################################3
def Campaign_Final():
    campaigns = Campaign()
    for idT in Tennants:
        for camp in campaigns:
            cont = 0
            for idL in llamadas:
                if cont < 20:
                    if True:
                        if Agentes[llamadas[idL]["ID Agente"]]["Tennant"] == idT and llamadas[idL]["ID Campaña"] == "null" and llamadas[idL]["Realizada"]:
                            if campaigns[camp]["Fecha inicio"].split("/")[1] == llamadas[idL]["Fecha llamada"].split("/")[1] and campaigns[camp]["Fecha inicio"].split("/")[2] == llamadas[idL]["Fecha llamada"].split("/")[2]:
                                cont +=1
                                llamadas[idL]["ID Campaña"] = camp


def Respuestas_Tipificaciones():
    answers = ["Respuesta 1", "Respuesta 2", "Respuesta 3"]
    total = []
    CampPre = Campaign_Tipificaciones()

    for idL in llamadas:
        for campaign in CampPre:

            for subcampaign in campaign:
                
                if str(subcampaign[0]) == llamadas[idL]["ID Campaña"]:
                    total.append([idL, subcampaign[1], random.choice(answers)])
    return total

####################################################################  
def RUT_GENERATOR():
    
    listRUT = {}
    characters = [0, 1,2,3,4,5,6,7,8,9,"k"]
    for i in range(1000):
        RUT = ""
        lengthRUT = random.choice([8,9])
        if lengthRUT == 8:
            RUT += str(random.choice(characters[7:9]))
        else:
            RUT += str(random.choice(characters[1:2]))
        for num in range(lengthRUT-2):
            RUT += str(random.choice(characters[0:9]))
        RUT += "-"+str(random.choice(characters[1:11]))
        listRUT[RUT] = {"Used": False}
    return listRUT

def City_Maker():
    city = open("Files\City.txt")
    cities = city.read().split()
    city.close()
    return random.choice(cities)

def Name_Maker():
    names = open("Files\\Names.txt")
    Names = names.read().split(",")
    names.close()
    Name = random.choice(Names)
    return Name[1:]

def Last_Name_Maker():
    lastNames = open("Files\Last Names.txt")
    LastNames = lastNames.read().split()
    lastNames.close()
    return random.choice(LastNames)+"_"+random.choice(LastNames)
    
def Streets_Maker():
    streets = open("Files\Streets.txt")
    Streets = streets.read().split()
    streets.close()
    return random.choice(Streets)

def Street_Num_Maker():
    return str(random.randrange(1,1000,1))
    
def People_Maker():
    Gente = {}
    for i in range(70):
        Gente[RUT_CHOICE()] = {
                "Name": Name_Maker(),
                "Last Names": Last_Name_Maker(),
                "City": City_Maker(),
                "Streets": Streets_Maker(),
                "Street Num": Street_Num_Maker(),
                "Phone": phone_Maker()
                }
        """
        if Name[0]== "0":
            People[rut]["Gender"] = "Hombre"
        else:
            People[rut]["Gender"] = "Mujer"
        """
    return Gente

def Company_Maker():
    file = open("Files\Tennants.txt")
    data = file.read().split(",")
    file.close()
    TID = 0
    AID = 0
    SID = 0
    Tennants = {}
    Agentes = {}
    Supervisores = {}
    
    for T in range(20): #Num of tennnants
        Tennants[str(TID)] = {"Nombre": data[T]}
        for A in range(30): # Num of Agents
            Agentes[str(AID)] = {
                    "RUT": RUT_CHOICE(), "Tennant": str(TID), 
                    "Nombre": Name_Maker(), "Apellido": Last_Name_Maker(),
                    "Ciudad": City_Maker(), "Calle": Streets_Maker(),
                    "Numero": Street_Num_Maker(), "Telefono": phone_Maker()}
            AID +=1
        for S in range(5): #Num of Supervisors
            Supervisores[str(SID)] = {"RUT": RUT_CHOICE(), "Tennant": str(TID), 
                    "Nombre": Name_Maker(), "Apellido": Last_Name_Maker(),
                    "Ciudad": City_Maker(), "Calle": Streets_Maker(),
                    "Numero": Street_Num_Maker(), "Telefono": phone_Maker()
                         }
            SID += 1
        TID +=1
    return Tennants, Agentes, Supervisores

################################################################ FUNCIONES IMPRIMIR
    
def Main():
    file = open("Files\Secuencias SQL.txt", "w")
    Create_table_Tennant(file)
    Create_table_Cliente(file)
    Create_table_Agente(file)
    Create_table_Supervisor(file)
    Create_table_Campaña(file)
    Create_table_llamadas(file)
    Create_table_Supervision(file)
    Create_table_tipificacion(file)
    Create_table_Respuestas_tipificaciones(file)
    Create_table_Tipificaciones_Campaña(file)
    ###############################################TABLAR INSERTAR
    for idT in Tennants:
        Insert_table_Tennant(file, idT, Tennants[idT]["Nombre"])
    #file.write("\n")
    for rut in Clientes:
        Insert_table_Cliente(file, rut, Clientes[rut]["Name"], Clientes[rut]["Last Names"], Clientes[rut]["City"], Clientes[rut]["Streets"], Clientes[rut]["Street Num"], Clientes[rut]["Phone"])
    #file.write("\n")
    for idA in Agentes:
        Insert_table_Agente(file, idA, Agentes[idA]["Tennant"], Agentes[idA]["RUT"], Agentes[idA]["Nombre"], Agentes[idA]["Apellido"], Agentes[idA]["Ciudad"], Agentes[idA]["Calle"], Agentes[idA]["Numero"], Agentes[idA]["Telefono"])
    #file.write("\n")
    for idS in Supervisores:
        Insert_table_Supervisor(file, idS, Supervisores[idS]["Tennant"], Supervisores[idS]["RUT"], Supervisores[idS]["Nombre"], Supervisores[idS]["Apellido"], Supervisores[idS]["Ciudad"], Supervisores[idS]["Calle"], Supervisores[idS]["Numero"], Supervisores[idS]["Telefono"])
    #file.write("\n")
    #file.write("\n")
    for idC in campaigns:
        Insert_tabla_Campaña(file, idC, campaigns[idC]["Fecha inicio"], campaigns[idC]["Fecha termino"], campaigns[idC]["Nombre"])
    for idL in llamadas:
        Insert_tabla_Llamadas(file, idL, llamadas[idL]["Realizada"], llamadas[idL]["Nombre archivo"], llamadas[idL]["Fecha llamada"], llamadas[idL]["Duracion"], llamadas[idL]["Transcripcion"], llamadas[idL]["Motivo"], llamadas[idL]["RUT Cliente"], llamadas[idL]["ID Agente"], llamadas[idL]["ID Supervisor"], llamadas[idL]["ID Campaña"])
    for idP in tipificaciones:
        Insert_tabla_tipificacion(file, idP, tipificaciones[idP]["Type"], tipificaciones[idP]["Pregunta asociada"])
    
    for idL in llamadas:
        if llamadas[idL]["ID Supervisor"] != "null":
            Insert_table_Supervision(file,idL, llamadas[idL]["ID Supervisor"], random.choice([True,False]))


    for lista in resp:
        Insert_table_Respuestas_Tipificaciones(file, lista[0], lista[1], lista[2])

    
    for lista in tipiCamp:
        for item in range(len(lista)):
            Insert_tabla_tipificaciones_campaña(file,lista[item][0], lista[item][1])

    
    
    
    file.close()
    
def Create_table_Tennant(file):
    return file.write("CREATE TABLE Tennant(ID_Tennant integer PRIMARY KEY, Nombre varchar(30) NOT NULL);")

def Create_table_Cliente(file):
    return file.write("CREATE TABLE Cliente(RUT varchar(10) PRIMARY KEY, Nombre varchar(30) , Apellido varchar(30), Ciudad varchar(40), Calle varchar(60), Numero integer, Telefono varchar(15));")

def Create_table_Agente(file):
    return file.write("CREATE TABLE Agente(ID_Agente integer PRIMARY KEY, ID_Tennant integer NOT NULL, RUT varchar(10), Nombre varchar(30), Apellido varchar(30), Ciudad varchar(40), Calle varchar(60), Numero integer, Telefono varchar(15), FOREIGN KEY (ID_Tennant) REFERENCES Tennant(ID_Tennant));")

def Create_table_Supervisor(file):
    return file.write("CREATE TABLE Supervisor(ID_Supervisor integer PRIMARY KEY, ID_Tennant integer NOT NULL, RUT varchar(10), Nombre varchar(30), Apellido varchar(30), Ciudad varchar(40), Calle varchar(60), Numero integer, Telefono varchar(15), FOREIGN KEY (ID_Tennant) REFERENCES Tennant(ID_Tennant));")

def Create_table_Campaña(file):
    return file.write("CREATE TABLE Campaña(ID_Campaña integer PRIMARY KEY, Fecha_inicio varchar(20), Fecha_termino varchar(20), Nombre varchar(30));")

def Create_table_llamadas(file):
    return file.write("CREATE TABLE Llamadas(ID_Llamada integer PRIMARY KEY, Realizada bool NOT NULL, Nombre_Archivo varchar(30) NOT NULL, Fecha_Llamada varchar(20), Duracion varchar(15), Transcripcion varchar(15), Motivo varchar(30), RUT varchar(10) NOT NULL, ID_Agente integer NOT NULL, ID_Supervisor integer, ID_Campaña integer, FOREIGN KEY (RUT) REFERENCES Cliente(RUT), FOREIGN KEY (ID_Agente) REFERENCES Agente(ID_Agente), FOREIGN KEY (ID_Supervisor) REFERENCES Supervisor(ID_Supervisor), FOREIGN KEY (ID_Campaña) REFERENCES Campaña(ID_Campaña));")
    
def Create_table_Supervision(file):
    return file.write("CREATE TABLE Supervision(ID_Llamada integer NOT NULL, ID_Supervisor integer NULL, Aprovado bool NOT NULL, FOREIGN KEY (ID_Llamada) REFERENCES Llamadas(ID_Llamada), FOREIGN KEY (ID_Supervisor) REFERENCES Supervisor(ID_Supervisor), CONSTRAINT Super PRIMARY KEY (ID_Llamada, ID_Supervisor));")

def Create_table_Respuestas_tipificaciones(file):
    return file.write("CREATE TABLE Respuestas_Tipificaciones(ID_Llamada integer NOT NULL, ID_Pregunta integer NOT NULL, Respuesta varchar(30), FOREIGN KEY (ID_Llamada) REFERENCES Llamadas(ID_Llamada), FOREIGN KEY (ID_Pregunta) REFERENCES Tipificacion(ID_Pregunta), CONSTRAINT Resp_Tip PRIMARY KEY (ID_Llamada, ID_Pregunta));")

def Create_table_tipificacion(file):
    return file.write("CREATE TABLE Tipificacion(ID_Pregunta integer PRIMARY KEY, Tipo_Dato varchar(30), Pregunta_Asociada varchar(40));")

def Create_table_Tipificaciones_Campaña(file):
    return file.write("CREATE TABLE Tipificaciones_Campaña(ID_Campaña integer NOT NULL, ID_Pregunta integer NOT NULL, FOREIGN KEY (ID_Campaña) REFERENCES Campaña(ID_Campaña), FOREIGN KEY (ID_Pregunta) REFERENCES Tipificacion(ID_Pregunta), CONSTRAINT Tip_Camp PRIMARY KEY (ID_Campaña, ID_Pregunta));")
#######################################################
def Insert_table_Tennant(file, idT, Nombre):
    return file.write("INSERT INTO Tennant (ID_Tennant, Nombre) VALUES ("+str(idT)+ ",'" +str(Nombre)+"');")

def Insert_table_Cliente(file, rut, Nombre, Apellido, Ciudad, Calle, Numero, Telefono):
    return file.write("INSERT INTO Cliente (RUT, Nombre, Apellido, Ciudad, Calle, Numero, Telefono) VALUES ('"+str(rut)+ "','" +str(Nombre)+"','"+ str(Apellido) +"','"+ str(Ciudad)+"','"+str(Calle)+"','"+str(Numero)+"','"+str(Telefono)+"');")

def Insert_table_Agente(file, idA, idT, rut, Nombre, Apellido, Ciudad, Calle, Numero, Telefono):
    return file.write("INSERT INTO Agente (ID_Agente, ID_Tennant, RUT, Nombre, Apellido, Ciudad, Calle, Numero, Telefono) VALUES ("+str(idA)+","+ str(idT)+",'"+str(rut)+ "','" +str(Nombre)+"','"+ str(Apellido) +"','"+ str(Ciudad)+"','"+str(Calle)+"','"+str(Numero)+"','"+str(Telefono)+"');")

def Insert_table_Supervisor(file, idS, idT, rut, Nombre, Apellido, Ciudad, Calle, Numero, Telefono):
    return file.write("INSERT INTO Supervisor (ID_Supervisor, ID_Tennant, RUT, Nombre, Apellido, Ciudad, Calle, Numero, Telefono) VALUES ("+str(idS)+","+ str(idT)+",'"+str(rut)+ "','" +str(Nombre)+"','"+ str(Apellido) +"','"+ str(Ciudad)+"','"+str(Calle)+"','"+str(Numero)+"','"+str(Telefono)+"');")

def Insert_tabla_Llamadas(file, idL, Realizada, NombreArchivo, Fecha, Duracion, Transcripcion, Motivo, RUT, idA, idS, idC):
    
    if idS == "null" and idC == "null":
        return file.write("INSERT INTO Llamadas(ID_Llamada, Realizada, Nombre_Archivo, Fecha_Llamada, Duracion, Transcripcion, Motivo, RUT, ID_Agente, ID_Supervisor, ID_Campaña) VALUES ("+str(idL)+","+ str(Realizada)+",'"+str(NombreArchivo)+ "','" +str(Fecha)+"','"+ str(Duracion) +"','"+ str(Transcripcion)+"','"+str(Motivo)+"','"+str(RUT)+"',"+str(idA)+", NULL,NULL);")
    if idS == "null":
        return file.write("INSERT INTO Llamadas(ID_Llamada, Realizada, Nombre_Archivo, Fecha_Llamada, Duracion, Transcripcion, Motivo, RUT, ID_Agente, ID_Supervisor, ID_Campaña) VALUES ("+str(idL)+","+ str(Realizada)+",'"+str(NombreArchivo)+ "','" +str(Fecha)+"','"+ str(Duracion) +"','"+ str(Transcripcion)+"','"+str(Motivo)+"','"+str(RUT)+"',"+str(idA)+",NULL,"+str(idC)+");")
    if idC == "null":
        return file.write("INSERT INTO Llamadas(ID_Llamada, Realizada, Nombre_Archivo, Fecha_Llamada, Duracion, Transcripcion, Motivo, RUT, ID_Agente, ID_Supervisor, ID_Campaña) VALUES ("+str(idL)+","+ str(Realizada)+",'"+str(NombreArchivo)+ "','" +str(Fecha)+"','"+ str(Duracion) +"','"+ str(Transcripcion)+"','"+str(Motivo)+"','"+str(RUT)+"',"+str(idA)+","+str(idS)+",NULL);")
    else:    
        return file.write("INSERT INTO Llamadas(ID_Llamada, Realizada, Nombre_Archivo, Fecha_Llamada, Duracion, Transcripcion, Motivo, RUT, ID_Agente, ID_Supervisor, ID_Campaña) VALUES ("+str(idL)+","+ str(Realizada)+",'"+str(NombreArchivo)+ "','" +str(Fecha)+"','"+ str(Duracion) +"','"+ str(Transcripcion)+"','"+str(Motivo)+"','"+str(RUT)+"',"+str(idA)+","+str(idS)+","+str(idC)+");")

def Insert_tabla_Campaña(file, idC, FI, FT, Nombre):
    return file.write("INSERT INTO Campaña(ID_Campaña, Fecha_inicio, Fecha_termino, Nombre) VALUES ("+str(idC)+",'"+ str(FI)+"','"+str(FT)+ "','" +str(Nombre)+"');")

def Insert_tabla_tipificaciones_campaña(file,idC, idP):
    return file.write("INSERT INTO Tipificaciones_Campaña(ID_Campaña, ID_Pregunta) VALUES ("+str(idC)+","+str(idP)+");")

def Insert_tabla_tipificacion(file, idP, Dato, Pregunta):
    return file.write("INSERT INTO Tipificacion(ID_Pregunta, Tipo_Dato, Pregunta_Asociada) VALUES ("+str(idP)+",'"+str(Dato)+"','"+str(Pregunta)+"');")

def Insert_table_Supervision(file,idL, idS, Aprovado):
    return file.write("INSERT INTO Supervision(ID_Llamada, ID_Supervisor, Aprovado) VALUES ("+str(idL)+","+str(idS)+","+str(Aprovado)+");")

def Insert_table_Respuestas_Tipificaciones(file, idL, idP, Respuesta):
    return file.write("INSERT INTO Respuestas_Tipificaciones(ID_Llamada, ID_Pregunta, Respuesta) VALUES ("+str(idL)+","+str(idP)+",'"+str(Respuesta)+"');")



if __name__=="__main__":
    
    RUT_Dict = RUT_GENERATOR()

    Clientes = People_Maker()

    Tennants, Agentes, Supervisores = Company_Maker() 
    Fechas = Fecha_Llamada()
    llamadas = Llamadas(Fechas)
    Supervisado() 
    Campaign_Final()  
    campaigns = Campaign()
    tipificaciones = Tipificaciones_Reader()
    
    resp =  Respuestas_Tipificaciones()
    
    tipiCamp = Campaign_Tipificaciones()
    Main()
    