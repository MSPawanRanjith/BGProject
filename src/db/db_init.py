from tinydb import TinyDB

'''Initializing db files'''

db_patient =TinyDB('/home/mssprrg/BGProject/src/db/db_schema/PATIENT_DATA.json')
print("Initialized Patient files..")

db_doctor =TinyDB('/home/mssprrg/BGProject/src/db/db_schema/DOCTOR_DATA.json')
print("Initialized Doctor files..")

db_bg_values=TinyDB('/home/mssprrg/BGProject/src/db/db_schema/BG_VALUES.json')
print("Initialized BG_Values files..")

db_lifestyle=TinyDB('/home/mssprrg/BGProject/src/db/db_schema/LIFESTYLE.json')
print("Initialized LIFESTYLE files..")

db_hour_values=TinyDB('/home/mssprrg/BGProject/src/db/db_schema/BG_VALUES_HOUR.json')
print("Initialized BG_VALUES_HOUR files..")
