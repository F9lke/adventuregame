class Functions:

    @staticmethod
    def list_to_dict(l: list):
        return dict(zip(l[::2], l[1::2]))
