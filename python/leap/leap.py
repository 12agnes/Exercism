def is_leap_year(year):
   if ((year % 4 == 0) or (year % 400 == 0) and  (year % 100 != 0 )):
   	return (is_leap_year(year))
   else:
	return (is_leap_year(year))