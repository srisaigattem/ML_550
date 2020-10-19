import json
def get_nme():
    nme=input("Hi, i'm query bot may i know your good nme please..?\n")
    return nme
def get_inp():
    try:
        return int(input())
    except:
        print("Enter number b/w 1-3")
def emer_number():
    dict = {"Ambulance":108,"Police":100,"Fire":104}
    return dict 
def pharma_number():
    dict = {"Apolo pharmacy":+918814286610 ,"med PLus":+918814286650,"BAlaji medicals":+91881148610}
    return dict 
def hospital_number():
    dict = {"PHC":+91881456245,"multispeciality hospital" :+9183535632200,"orthopedic hospital":+913567669225}
    return dict 
def Hotels_number():
    dict = {"Suprabath":+91882624583,"Chandrika":+918816254947,"sitayya grand":+9188164542578,"Ananda Inn":+918816545514}
    return dict 
def bakeries_number():
    dict = {"Bombay sweets and Bakeries":+918816454550,"Sri ramu":+9188162251548,"Hotlines":+918816455482,"Chocodew":+918821664485}
    return dict 
def groceries_number():
    dict = {"Reliance fresh mart":+9171882128708,"Spencers":+917548481100,"More":+9188456494104,"tatwarti":+91534779657}
    return dict 
def Elsectricians_number():
    dict = {"Ram":+918814656108,"venkat":+91882266100,"kondal rao":+916487846496}
    return dict 
def maids_number():
    dict = {"Lakshmi":+91848783854,"Pavani":+9174584644,"fathima":+91487844825,"Devi":+917445416484,"savitri":+9178548973348}
    return dict 
def plumbers_number():
    dict = {"ramesh":+91874569258,"suresh":+918878497946,"gopal":+918784993344,"trivikram":+9187854796248,"edukondalu":+9187841484353}
    return dict 
def cableservice_number():
    dict = {"Tata sky":+914477745845,"VCV":+9187846499,"BCN":+917866796104,"Airtel":+917849449794}
    return dict 
def intereservice_number():
    dict = {"Apple fibernet":+9188144548544,"Excell":+918814254100,"JIO fibernet":+918826488104}
    return dict
def prit_nums(dc):
    for key in dc:
        print(key," : ",dc[key])
        print()

def other_numbers(n,nme):
    if(n==1):
        print(nme," these Are some Pharmacy NUmbers: \n")
        op=pharma_number()
        prit_nums(op)
    if(n==2):
        print(nme," these Are some Hospital NUmbers: \n")
        op=hospital_number()
        prit_nums(op)
    if(n==3):
        print(nme," these Are some Hotels NUmbers: \n")
        op=Hotels_number()
        prit_nums(op)
    if(n==4):
        print(nme," these Are some Groceries stores NUmbers: \n")
        op=groceries_number()
        prit_nums(op)
    if(n==5):
        print(nme," these Are some Bakeries  NUmbers: \n")
        op=bakeries_number()
        prit_nums(op)
    if(n==6):
        print(nme," these Are some Electricians  NUmbers: \n")
        op=Elsectricians_number()
        prit_nums(op)
    if(n==7):
        print(nme," these Are some Maids  NUmbers: \n")
        op=maids_number()
        prit_nums(op)
    if(n==8):
        print(nme," these Are some Plumbers  NUmbers: \n")
        op=plumbers_number()
        prit_nums(op)
    if(n==9):
        print(nme," these Are some Cableservice providers NUmbers: \n")
        op=cableservice_number()
        prit_nums(op)
    if(n==10):
        print(nme," these Are some Internet service Providers NUmbers: \n")
        op=intereservice_number()
        prit_nums(op)

def chat_box(n,nme):
    3

    if(n!=3):
        if(n==1):
            print(nme,"here are emergency number: \n")
            op=emer_number()
            prit_nums(op)
            
        else:
            print("Do you Want..? \n 1 .Pharmacy numbers \n 2 .Hospitals \n 3 .hotels numbers \n 4 .groceries \n 5 .Bakeries \n 6 .Electricians \n 7 .Maid \n 8 .Plumbers \n 9 .Cable network \n 10 .Internet service provider \n ----------------\n Please select an option...?:")
            n=get_inp()
            print("------------------\n")
            if(n<=10 and n>=1):
                other_numbers(n,nme)
            else:
                print("sorry "+nme+" i didn't get you please enter crct value..:) \n-----------------\n",end="\n")
                
    else:
        print("OK,Bye "+nme+" Thank you:)")
        #break
def strt():
    nme = get_nme()
    n=0
    while(n!=3):
        print("Hi, "+nme+" what contacts do you want in 'BHIMAVARAM'..?","1 .emergency number","2 .other Numbers ","3 .Quit.","please select option:",sep='\n')
        n=get_inp()
        
        if(n<=3 and n>=0):
            print("------------\n")
            chat_box(n,nme)
        else:
            print("------------\n")
            print("sorry "+nme+" i didn't get you \n-----------------\n",end="\n")
    
     
strt() 