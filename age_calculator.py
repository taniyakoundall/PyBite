print("welcome to age calculator")
age=input("enter your current age: ")
ext_age=input("enter the age till which you want to calculate: ")
ext_age_days=int(ext_age)*365
ext_age_weeks=int(ext_age)*52
ext_age_months=int(ext_age)*12

age_days=int(age)*365
age_weeks=int(age)*52
age_months=int(age)*12

left_days=int(ext_age_days)-int(age_days)
left_weeks=int(ext_age_weeks)-int(age_weeks)
left_months=int(ext_age_months)-int(age_months)

print("you have ",int(left_days)," days, ",int(left_weeks)," weeks and ",int(left_months)," left.")