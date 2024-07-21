import requests


def get_posts(top: int) -> list:
    """Get top n posts."""
    result = requests.get('https://jsonplaceholder.typicode.com/posts')
    return result.json()[:top]

def get_comments(post_id: int) -> list:
    """Get comments for a specific a post."""
    result = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}/comments')
    return result.json()

def get_users() -> list:
    """Get a list of users inluding information like addess, phone number, ..."""
    result = requests.get('https://jsonplaceholder.typicode.com/users')
    return result.json()
