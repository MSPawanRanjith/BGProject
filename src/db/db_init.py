from tinydb import TinyDB
import config
'''Initializing db files'''

db_patient =TinyDB(config.DB_PATIENT)
print("Initialized Patient files..")

db_doctor =TinyDB(config.DB_DOCTOR)
print("Initialized Doctor files..")

db_bg_values=TinyDB(config.DB_BG_VALUES)
print("Initialized BG_Values files..")

db_lifestyle=TinyDB(config.DB_LIFESTYLE)
print("Initialized LIFESTYLE files..")

db_hour_values=TinyDB(config.DB_HOUR_VALUES)
print("Initialized BG_VALUES_HOUR files..")
