from datetime import datetime


def visitor_cookie_handler(request, response):
    # cookie values are returned as strings
    visits_cookie = int(request.COOKIES.get('visits_cookie', '1'))

    last_visit_cookie = request.COOKIES.get('last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')

    if (datetime.now() - last_visit_time).days > 0:
        visits_cookie += 1
        response.set_cookie('last_visit', str(datetime.now()))
    else:
        response.set_cookie('last_visit', last_visit_cookie)

    response.set_cookie('visits_cookie', visits_cookie)
