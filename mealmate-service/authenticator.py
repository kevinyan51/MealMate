import os
from fastapi import Depends
from jwtdown_fastapi.authentication import Authenticator
from queries.users import UserQueries, UserOut, UserOutWithPassword


class UserAuthenticator(Authenticator):
    async def get_account_data(self, username: str, accounts: UserQueries):
        return accounts.get(username)

    def get_account_getter(self, accounts: UserQueries = Depends()):
        return accounts

    def get_hashed_password(self, account: UserOutWithPassword):
        return account.hashed_password

    def get_account_data_for_cookie(self, account: UserOut):
        return account.username, UserOut(**account.dict())


authenticator = UserAuthenticator(os.environ.get("SIGNING_KEY"))
