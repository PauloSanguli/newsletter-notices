from src.infra.models import Newspapper, Emails


class Formater:
    @staticmethod
    def email(datas: any) -> list:
        """formater for emails"""
        emails = list()

        for __email in datas:
            m = Emails(
                id=__email.id,
                email=__email.email
            )
            emails.append(m.dict())
        return emails

    @staticmethod
    def newspapper(datas: any) -> list:
        """formater for newspapper"""
        newspapper = list()

        for __news in datas:
            m = Newspapper(
                id=__news.id,
                content=__news.content,
                header=__news.header,
                category=__news.header,
                date_publish=__news.date_publish,
                img=__news.img
            )
            newspapper.append(m.dict())
        return newspapper