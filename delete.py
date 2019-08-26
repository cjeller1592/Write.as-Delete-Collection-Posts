import writeas

# PUT IN VALUES BEFORE RUNNING SCRIPT
# Username and password for Write.as account
username = ''
password = ''
# The Write.as slug for your blog - ex: write.as/matt -> 'matt'
collection = ''


# Instanciate Write.as Client
c = writeas.client()

# Log in with Write.as
user = c.login(username, password)
c.setToken(user['access_token'])

list = []

# I assume 500 posts is more than generous!
for i in range(1,50):
# Iterate through the pages
  cposts = c.retrieveCPosts('feed-test', i)
  
  posts = cposts['posts']
    # If the posts are not an empty list, take each post and put it in a list!
    # That way it catches pages that don't have 10 posts
  if posts != []:
     for post in posts:
    # Append to the list of posts
     list.append(post)

  else:
    break

for p in list:
# Grab the id of the post
  id = p['id']
# Feed it into the delete post method to delete
  c.deletePost(id)

# Fin
print('All done! Posts deleted!')
