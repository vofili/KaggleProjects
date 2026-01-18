#boolean and conditionals

flag = True
print(type(flag))
#convert a variable to a bool
a= 4
base= ""
cat_name = "adam"
print(bool(a))
print(bool(base))
print(bool(cat_name))


#function to check if candidtate is old enough to run for president
def president_agecheck(age):
    min_age = 35
    return age >= min_age

print("A 40 year old can run for president: ",president_agecheck(40))
print("A 30 year old can run for president: ",president_agecheck(30))

#check if all conditions have been met for president

def president_check(age,born):
    return born and age >= 35

print("Person is 39 and Born in the US",president_check(49,True))
print("Person is 36 and NOT Born in the US",president_check(36,False))
print("Person is 20 and Born in the US",president_check(20,True))

#Write condition to check if weather is safe
def safe_to_go_out(umbrella,rain_level,hoodie,is_workday):
    have_hoodie=hoodie
    have_umbrella=umbrella
    rain_level=rain_level
    is_safe_to_go_out = have_umbrella or rain_level < 5 and have_hoodie or not (rain_level > 0) and is_workday
    return is_safe_to_go_out

print("Safe to go out:",safe_to_go_out(False,0,False,True))

user_name ="valentine"
pass_word =  "Passw0rd"

def check_user_creds(user_name,pass_word):
    if user_name == "valentine":
        if pass_word == "Passw0rd":
            print("User Authenticated")
            return True
        else:
            print("Password incorrect")
            return False

    elif(pass_word != "Passw0rd"):
        print("incorrect username and password")
        return False
    else:
        print("Incorrect Username")
        return False


print(int(False))

print("Check User valentine:",check_user_creds("1valentine","Passw0rd"))

print(False and False)