import csv

with open('users.csv', 'a') as file_obj:

    csv_file_reader = csv.DictReader(file_obj)
    csv_file_writer = csv.DictWriter(file_obj, fieldnames=['username', 'email', 'password'])

    for line in csv_file_reader:
        print(line)


    user = {'username':'fazil', 'email':'fazil@example.com', 'password':'126'}

    csv_file_writer.writerow(user)