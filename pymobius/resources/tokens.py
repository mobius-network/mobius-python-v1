from ..abstract import Resource


class Tokens(Resource):
    resource = 'tokens'

    def register(self, token_type, name, symbol, issuer):
        return self.post(
            'register',
            token_type=token_type, name=name, symbol=symbol, issuer=issuer
            )

    def create_address(self, token_uid):
        return self.post(
            'create_address',
            token_uid=token_uid
            )

    def register_address(self, token_uid, address):
        return self.post(
            'register_address',
            token_uid=token_uid, address=address
            )

    def balance(self, token_uid, address):
        return self.get(
            'balance',
            token_uid=token_uid, address=address
            )

    def transfer_managed(self, token_address_uid, address_to, num_tokens):
        return self.post(
            'transfer/managed',
            token_address_uid=token_address_uid, address_to=address_to, num_tokens=num_tokens
            )

    def transfer_info(self, token_address_transfer_uid):
        return self.get(
            'transfer/info',
            token_address_transfer_uid=token_address_transfer_uid
            )
