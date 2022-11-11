
#Task 1

first_group = "January",  "March", "May", "Julay", "Augest","October","December"
secent_group = "April", "Juna", "September", "November"
therte_group = "February"

mount_name = str.capitalize(input("Ogrenmek Istediginiz Ay`in Ismini Giriniz : "))

if mount_name in first_group:
    print("31")
elif mount_name in secent_group:
    print("30")
else:
    print("28/29")
