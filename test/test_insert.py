from tinydb import *

db_patient =TinyDB('/home/mssprrg/BGProject/src/db/db_schema/PATIENT_DATA.json')
db_lifestyle=TinyDB('/home/mssprrg/BGProject/src/db/db_schema/LIFESTYLE.json')
Patient=Query()

#db_patient.insert({"Name":"TEST","AGE":45})
#db_find=db_patient.search(Patient['Name'].exists())

#db_lifestyle.insert({"TimeStamp":"0900","LL":90,"UL":105})
#db_lifestyle.insert({"TimeStamp":"1300","LL":90,"UL":105})
#db_lifestyle.insert({"TimeStamp":"2000","LL":90,"UL":105})

#db_values=db_lifestyle.all()
#print(db_values)

#bg_time=input('Enter the time :')
#print(bg_time[-2:])
bg_time="00"
bg_value=10
bg_hour_std=10.8
bg_hour_avg=12.5
insert_hour_bg={"TimeStamp":bg_time,"Bg_Value":bg_value,"Bg_Hour_Avg":bg_hour_avg,"Bg_Hour_Std":bg_hour_std}
print(insert_hour_bg)
		
#db_id=db_patient.get(doc_id="1")
#print(db_id)
#if len(db_find)==1 :
	#print("NOT FTU")
#else:
	#print("FTU")
