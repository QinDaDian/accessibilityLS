from django.shortcuts import render


# 登录身份验证，取session值
def authentication(func):
    def wrapper(*args, **kwargs):
        if args[0].session.get('username', False) is False:  # if can't find username, return False
            return render(args[0], 'error.html')
        else:
            return func(*args, **kwargs)
    return wrapper
