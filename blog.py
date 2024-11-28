import file_operations
from datetime import date

def create(user:str)->dict:
    ''' Creating a new blog '''
    title = input('Title: ')
    content = input('Content:\n')

    title_len = len(title)
    content_len = len(content)
    
    while title_len == 0 or content_len == 0:
        if title_len == 0:
            title = input('Title: ')
        else:
            content = input('Content:\n')

    words_in_title = title.split()
    if len(words_in_title)>20:
        title = ' '.join(words_in_title[:20])

    # Preparing the blog
    blog = {
        'title':title,
        'content': content,
        'created_by': user,
        'created_at': date.today(),
        'updated_at': date.today()
    }

    file_operations.write('blogs.csv', blog, blog.keys())

    return blog

def get_blog_for_update(user:str)->dict:
    ''' Get blog to update '''
    
    title = input('Enter the title of the blog: ')
    return file_operations.read_blog('blogs.csv', title, user)

def can_update(blog:dict, user:str)->bool:
    ''' Check user has an access to update the blog. '''
    return blog.created_by == user

def update(user:str,title:str|None=None, content:str|None=None)->bool:
    ''' Update a blog then return it. '''

    blog = get_blog_for_update(user)

    if blog is not None:
        if can_update(blog, user):
            if title is not None:
                blog.title = title
            if content is not None:
                blog.content = content
            return True
        blog.update_at = date.today()

        file_operations.update_blog('blogs.csv', blog, ['title','content', 'created_by', 'created_at', 'updated_at'])

    return False