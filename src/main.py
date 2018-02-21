from tinydb import TinyDB,Query
import os
import json
import statistics

'''DB FETCH'''
db_patient =TinyDB('/home/mssprrg/BGProject/src/db/db_schema/PATIENT_DATA.json')
db_bg=TinyDB('/home/mssprrg/BGProject/src/db/db_schema/BG_VALUES.json')
db_lifestyle=TinyDB('/home/mssprrg/BGProject/src/db/db_schema/LIFESTYLE.json')
db_hour_values=TinyDB('/home/mssprrg/BGProject/src/db/db_schema/BG_VALUES_HOUR.json')

'''QUERY OBJECT'''
DB_Query=Query()

'''GLOBAL VARIABLE'''


'''BG_VALUES OPERATIONS '''
def bg_operation():
	if (not os.path.exists('/home/mssprrg/BGProject/src/db/db_schema/BG_VALUES.json')):
		try:
			raise Exception('BG_VALUE FILE inconsistent')
		except Exception as error:
			print(error)
			main()
	#Insert from Monitoring Device  --later implementation move this function to diff file
	bg_value=int(input("Enter the BG Value : "))
	bg_time=input('Enter the time :')
	insert_values=json.loads('{"TimeStamp" : "'+str(bg_time)+'","Bg_Value":'+str(bg_value)+'}')
	print(insert_values)
	#db_bg.insert(insert_values)
	
	#Check for necesaary calculation according to timestamp
	
	if(bg_time[-2:] != "00"):
		#get the LL and UL values from Lifestyle
		print(" ")
	else:
		bg_list=db_bg.all()
		bg_hour_list=bg_list[-4:]
		bg_hour_tot=0
		bg_values_list=[]
		for bg_entry in bg_hour_list:
			bg_values_list.append(bg_entry.get("Bg_Value"))
		bg_hour_avg=sum(bg_values_list)/len(bg_values_list)
		bg_hour_std=statistics.stdev(bg_values_list)
		print(str(bg_hour_avg)+"Total bg "+str(sum(bg_values_list)))
		insert_hour_bg={"TimeStamp":bg_time,"Bg_Value":bg_value,"Bg_Hour_Avg":bg_hour_avg,"Bg_Hour_Std":bg_hour_std}
		print(insert_hour_bg)
		db_hour_values.insert(insert_hour_bg)
		
'''MAIN DRIVING FUNCTION'''
def main():
	
	'''Check for Patient Details '''
	#check for FTU
	patient_exist=db_patient.search(DB_Query['Name'].exists())

	if len(patient_exist) == 1 :
		#Not FTU, do the bg_operations required
		bg_operation()
	else:
		#Yes FTU
		try:
			raise Exception('You Have Not registered! ')
		except Exception as error:
			print(error)
if __name__=='__main__':
	main()
