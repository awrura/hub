import logging
from datetime import datetime
from datetime import timedelta
from datetime import timezone
from typing import TypedDict

import jwt
from auth.action.interact.login import ITokenAuth
from auth.action.interact.login import Tokens
from config.auth import AuthTokenSettings
from jwt import PyJWTError

logger = logging.getLogger(__name__)


class TokenClaims(TypedDict):
    username: str


class JwtTokenAuth(ITokenAuth):
    def __init__(self, conf: AuthTokenSettings):
        self._conf = conf

    def decode(self, token: str) -> TokenClaims | None:
        try:
            return jwt.decode(
                token, self._conf.SECRET_KEY, algorithms=[self._conf.ALGORITHM]
            )
        except PyJWTError:
            logger.error('Unable to decode token')
            return None

    def renew(self, refresh_token: str) -> Tokens | None:
        claims = self.decode(refresh_token)
        if claims is None or 'access_token' not in claims:
            return None

        username = claims.get('username')
        return self.generate(username)

    def generate(self, username: str) -> Tokens:
        access_token = self._generate_token(
            username, self._conf.ACCESS_TOKEN_EXPIRE_MINUTES
        )
        refresh_token = self._generate_token(
            username, self._conf.REFRESH_TOKEN_EXPIRE_MINUTES, access_token=access_token
        )

        logger.info('Tokens generated successfully')
        return {'access_token': access_token, 'refresh_token': refresh_token}

    def _generate_token(self, username: str, expire_minutes: int, **kwargs) -> str:
        expire = datetime.now(timezone.utc) + timedelta(minutes=expire_minutes)
        to_encode = {
            'exp': expire,
            'sub': username,
            **kwargs,
        }
        encoded_jwt = jwt.encode(
            to_encode, self._conf.SECRET_KEY, algorithm=self._conf.ALGORITHM
        )
        return encoded_jwt
