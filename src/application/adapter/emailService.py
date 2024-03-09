"""adapter for server send email"""

import smtplib


class AdapterServerEmail:
    def __init__(self, host_, port_):
        self.server_ = smtplib.SMTP(host=host_, port=port_)

    def server(self):
        """return the server"""

        return self.server_
