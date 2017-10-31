from ..abstract import Resource


class AppStore(Resource):
    resource = 'app_store'

    def balance(self, app_uid, email):
        return self.get(
            'balance',
            app_uid=app_uid, email=email
            )

    def use(self, app_uid, email, num_credits):
        return self.post(
            'use',
            app_uid=app_uid, email=email, num_credits=num_credits
            )
