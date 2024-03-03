file=open("vlan-database.txt","a")
   
while True:
    dataVLAN = input("Input data VLAN baru (y/t)?")
    if dataVLAN =='y' :
        print("*****************************")
        x = input("Masukkan VLAN ID: ")
        y = input("Masukkan Nama VLAN: ")
        file.write("VLAN ID: "+ x +" , Nama: "+ y + "\n")
        print("-----------------------------")
    else : 
        break
    
file.close()
vlan=open("vlan-database.txt","r")
for item in vlan:
     item=item.strip()
     print(item)
vlan.close()