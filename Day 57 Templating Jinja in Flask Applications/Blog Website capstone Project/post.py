class Post:
    def __init__(self, post_id, title, subtitle, body):
        self.id = post_id
        self.title = title
        self.subtitle = subtitle
        self.body = body

# Because the data is stored in object instances rather than standard Python dictionaries, you can access properties
# using dot notation inside your Jinja HTML templates:
#
# With post.py (Objects): {{ post.title }} and {{ post.id }}
#
# Without post.py (Raw JSON / Dicts): {{ post['title'] }} and {{ post['id'] }}
