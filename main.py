import auth
import blog
import file_operations

users = file_operations.read_users('users.csv')
email=None

# Sign in/ Log in
options = '''1. Sign in
2. Log in
3. List all blogs
4. Read the blog
5. Create a blog
6. Update a blog
7. Delete a blog
'''
print(options)
option = int(input('Option: '))
if option == 1:
    ''' Sig in '''
    email = auth.create_user(users)
    user = users[email]
    username = user['username']
    password = user['password']

    data = {
        'email':email, 'username':username, 'password':password, 'is_logged_in':False
    }

    file_operations.write('users.csv', data, fieldnames=data.keys())

elif option == 2:
    ''' Log in '''
    email = input('Enter your email: ')
    password = input('Enter your password: ')

    is_login = auth.login_user(email, password, users)

    if is_login:
        print('You have logged in.')
    
elif option == 3:
    ''' List all blogs '''
    blogs = file_operations.list_blogs('blogs.csv')

    for blog in blogs:
        title = blog['title']
        if len(title) > 56:
            title = title[:53]
            title+='...'

        print('-' * 60)
        print('|',title, ' ' * 60 - 2 - 2 - len(title),'|')
        print('|','Author:',blog['created_by'], ' ' * (60 - 2 - 2 - len(blog['created_by'])), '|')
        print('|','Updated at/Created at:',f'{blog['updated_at']}/{blog['created_at']}', (60 - 2 - 2 -1 - len(blog['created_at'] - len(blog['updated_at']))), '|')
        print('-' * 60)

elif option == 4:
    ''' Read the blog '''
    title = input('Title: ')
    created_by = input('Author: ')
    
    blog = file_operations.read_blog('blogs.csv', title, created_by)

    if blog is not None:
        print(blog['title'])
        print('Created At/Updated_at', f'{blog['created_at']}/{blog["updated_at"]}')
        print(blog['content'])
        print('Author:',blog['created_by'])


elif option == 5:
    ''' Create a blog '''
    created_blog = blog.create(email)

    print(f'Blog "{blog.title}" was created')

elif option == 6:
    ''' Update a blog '''