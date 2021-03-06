# from keyring import delete_password


class Credentials:
    def __init__(self, page, credential):
        self.page = page
        self.credential = credential

    user_credentials = []

    def save_page(self):
        Credentials.user_credentials.append(self)
    def delete_page(self):
        Credentials.user_credentials.remove(self)

    @classmethod
    def find_by_page(cls, pager):
        for pagy in cls.user_credentials:
            if pagy.page == pager:
                return pagy

    @classmethod
    def page_present(cls,pager):
        for pagy in cls.user_credentials:
            if pagy.page == pager:
                return pagy
        return False