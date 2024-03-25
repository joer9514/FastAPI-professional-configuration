"""
Module for Trusted Host Middleware Setup.

This module provides a middleware class for managing HOST header injection.
"""

from settings.project import WHITELIST_OF_HOSTS


class TrustedHOSTMiddlewareSetup:
    """Middleware for HOST Header Injection management"""

    def __init__(self):
        self.__whitelist_of_hosts = WHITELIST_OF_HOSTS.split(", ")

        self.config = {
            "allowed_hosts": self.__whitelist_of_hosts,
        }


TrustedHostMiddlewareSetup = TrustedHOSTMiddlewareSetup().config
