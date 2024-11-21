import file_operation
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

    file_operation.write('blogs.csv', blog, blog.keys())

    return blog