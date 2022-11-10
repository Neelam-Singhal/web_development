'''

>>> db.create_all()
>>> from flaskblog import User, Post
>>> user_1 = User(username='Neelam', email='ns@gmail.com', password='pass')
## add only tells db that a change is expected. It dosen't make an actual change.
>>> db.session.add(user_1) 
>>> user_2 = User(username='Dhaiv', email='dm@gmail.com', password='pass')  
>>> db.session.add(user_2)
>>> db.session.commit()


# Now, we can query the SQLite DB:
>>> User.query.all()
[User('Neelam', ns@gmail.com',default.jpg'), User('Dhaiv', dm@gmail.com',default.jpg')]
>>> User.query.first()  
User('Neelam', ns@gmail.com',default.jpg')

>>> User.query.filter_by(username='Neelam')
<flask_sqlalchemy.BaseQuery object at 0x000001D385D87A00>
>>> User.query.filter_by(username='Neelam').first()
User('Neelam', ns@gmail.com',default.jpg')
>>> user = User.query.filter_by(username='Neelam').first()
>>> user
User('Neelam', ns@gmail.com',default.jpg')
>>> user.id
1
>>> User.query.get(1)
User('Neelam', ns@gmail.com',default.jpg')

>>> user.posts
[]
>>> post_1 = Post(title='Blog_1', content='first blog post', user_id = user.id)
>>> post_2 = Post(title='Blog_2', content='second blog post', user_id = user.id) 
>>> db.session.add(post_1)
>>> db.session.add(post_2)
>>> db.session.commit()

>>> user.posts
[Post('Blog_1', 2022-11-09 11:35:09.833438'), Post('Blog_2', 2022-11-09 11:35:09.865383')]


>>> for post in user.posts:
...     print(post)
... 
Post('Blog_1', 2022-11-09 11:35:09.833438')
Post('Blog_2', 2022-11-09 11:35:09.865383')
>>> for post in user.posts:
...     print(post.title)
... 
Blog_1
Blog_2


>>> post = Post.query.first()
>>> post
Post('Blog_1', 2022-11-09 11:35:09.833438')
>>> post.user_id
1

>>> post.author
User('Neelam', ns@gmail.com',default.jpg')

##To drop the table
>>> db.drop_all()
>>> db.create_all()
>>> User.query.all()
[]
>>> Post.query.all()
[]


'''