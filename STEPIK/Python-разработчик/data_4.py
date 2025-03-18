
from datetime import datetime
import pytz

def convert_timezone(input_datetime_str):
	input_dt=datetime.fromisoformat(input_datetime_str)
	input_tz=pytz.FixedOffset(4*60+40)
	input_dt=input_tz.localize(input_dt)
	#UTC
	output_tz1=pytz.FixedOffset(-(3*60+46))
	output_dt1=input_dt.astimezone(output_tz1)
	#Europe/Moscow
	output_tz2=pytz.timezone('Europe/Moscow')
	output_dt2=input_dt.astimezone(output_tz2)
	
	return output_dt1.isoformat(), output_dt2.isoformat()

t=input()

s=convert_timezone(t)
