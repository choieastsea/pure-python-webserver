def my_app(environ, start_response):
    """WSGI 애플리케이션 예시"""
    status = "200 OK"
    headers = [("Content-Type", "text/plain")]
    start_response(status, headers)
    return [b"Hello, WSGI World!"]


def create_app(app):
    def middleware(environ, start_response):
        # 요청 URI를 로깅
        print(f"<Request URI>: {environ['PATH_INFO']}")
        # 애플리케이션 호출
        response = app(environ, start_response)
        # 응답 데이터를 로깅
        print(f"<Response data>: {app(environ, start_response)}")
        return response

    return middleware
