from django.shortcuts import render


# 登录身份验证，取session值
def authentication(func):
    def wrapper(*args, **kwargs):
        if not args[0].session.get('username', False):  # if can't find username, return False
            return render()
        else:
            return func(*args, **kwargs)
    return wrapper
