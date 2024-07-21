def get_posts(top: int) -> list:
    """Get top n posts."""
    return [
        {
            "title": "Post 1",
            "content": "lorem ispum"
        },
        {
            "title": "Post 2",
            "content": "lorem ispum"
        },
        {
            "title": "Post 3",
            "content": "lorem ispum"
        },
        {
            "title": "Post 4",
            "content": "lorem ispum"
        },
        {
            "title": "Post 5",
            "content": "lorem ispum"
        }
    ]

def get_comments(post_id: int) -> list:
    """Get comments for a specific a post."""
    return [
        {
            "author": "John",
            "comment": "lorem ispum"
        },
        {
            "author": "Jane",
            "comment": "lorem ispum"
        }
    ]

def get_users() -> list:
    """Get a list of users."""
    return [
        {
            "name": "John Doe",
            "email": "john@doe.com"
        },
        {
            "name": "Jane Doe",
            "email": "jane@doe.com"
        }
    ]
