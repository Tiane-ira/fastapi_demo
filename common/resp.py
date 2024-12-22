class Resp:
    def __init__(self, code: int = 0, msg: str = '', data: any = None):
        self.code = code
        self.msg = msg
        self.data = data


def success(msg: str = 'Success', data: any = None):
    return Resp(0, msg, data)
