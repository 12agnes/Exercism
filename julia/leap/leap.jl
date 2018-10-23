function is_leap_year(year::Int)
	if year % 4 != 0 
           return false
	elseif year % 4 == 0 && year % 100 != 0
	   return true
	elseif year % 100 ==0 && year % 400 != 0
	   return false
	else year % 400 == 0
	   return true
	end
end

