"""adapter for server send email"""

import smtplib


class AdapterServerEmail:
    def __init__(self, host_, port_):
        try:
            self.server_ = smtplib.SMTP(host=host_, port=port_)
        except:
            self.server_ = ""

    def server(self):
        """return the server"""

        return self.server_
