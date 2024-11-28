import csv

def read_users(file_name:str)->dict:
    ''' Read users from a file, then users as dict '''
    users = {}
    with open(file_name) as file_object:
        csv_reader = csv.DictReader(file_object)

        for line in csv_reader:
            user = {'username':line['username'], 'password':line['password'], 'is_logged_in':line['is_logged_in']}
            users[line['email']] = user
        
    return users

def write(file_name:str, data:dict, fieldnames:list)->None:
    ''' Write the data to the file. '''
    with open(file_name, 'a') as file_object:
        csv_writer = csv.DictWriter(file_object, fieldnames=fieldnames)

        csv_writer.writerow(data)

def list_blogs(file_name:str)->list[dict]:
    ''' List all blogs from the file '''
    with open(file_name) as file_object:
        csv_reader = csv.DictReader(file_object)
        blogs = [{'title': blog['title'], 'created_by':blog['created_by'],'created_at':blog['created_at'], 'updated_at':blog['updated_at']} for blog in csv_reader]

        return blogs
    
def update_blog(file_name:str, new_blog:dict, fieldnames:list)->None:
    ''' Remove previous version of file and update entire file. '''
    blogs = list_blogs('blogs.csv')

    for i in  range(len(blogs)):
        if blogs[i].title == new_blog.title and blogs[i].created_by == new_blog.created_by:
            blogs[i] = new_blog

    with open(file_name) as file_object:
        csv_writer = csv.DictWriter(file_object, fieldnames=fieldnames)

        csv_writer.writerows(blogs)

    
def read_blog(file_name:str, title:str, created_by:str)->dict:
    ''' Read a blog '''
    with open(file_name) as file_object:
        csv_reader = csv.DictReader

        for blog in csv_reader:
            if blog['title'] == title and blog['created_by'] == created_by:
                return blog
        
        return None