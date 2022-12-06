#this script is to group the total population based on age
#Adult population
adult_pop = 0
adult_male_pop = 0
adult_female_pop = 0
#youth population
youth_pop = 0
youth_male_pop = 0
youth_female_pop = 0
#children population
child_pop = 0
child_M_pop = 0
child_F_pop = 0

user_name = str(input("Please, what is your name: "))
user_age = int(input("Please, what is your age: "))
user_sex = str(input("Please, what is your sex "))
if user_age >= 50:
    adult_pop += 1
    if user_sex =="male" or user_sex == "M":
        print("Thanks you ", user_name, " your data is been recorded " )
        adult_male_pop += 1
    elif user_sex == "female" or user_sex == "F":
        print("Thanks ", user_name, "your data is been recorded")
        adult_female_pop += 1
    else:
         print("invalid data")
#youth population         
elif user_age >=17 :
    youth_pop += 1
    if user_sex == "male" or user_sex =="M":
        youth_male_pop += 1
        print("Thanks ", user_name, "your data is been recorded")
    elif user_sex == "female" or user_sex == "F":
       youth_female_pop += 1
       print("Thanks ", user_name, "Your data is been recorded") 
    else:
        print("invalid data, please update data")
#children population
elif user_age <=16:
    child_pop += 1
    if user_sex == "male" or user_sex == "M":
        child_M_pop += 1
        print("Thanks ", user_name, "Your data is been recorded")
    elif user_sex == "female" or user_sex=="F":
        child_F_pop += 1
        print("Thanks ", user_name, "Your data is been recorded")
    else:
        print("invalid data, please update data")

else:
    print("invalid, please update")

 
#total sum of all the population
total_pop = adult_pop + youth_pop + child_pop
print("Total Population", total_pop,": ", "             Male population (adult) =", adult_male_pop, "   Female population (female) =", adult_female_pop, "  Male population (youth) =", youth_pop, "  Female population (youth) =", youth_female_pop, " Male population (children) =", child_M_pop, "    Female population (children) =", child_F_pop )