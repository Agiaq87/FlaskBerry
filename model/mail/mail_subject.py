class MailSubject:
    def __init__(self, subject_mail: str):
        self.subject = subject_mail

    @classmethod
    def validate_mail(cls, mail: str) -> __init__:
        # TODO check for validation
        return MailSubject(mail)
