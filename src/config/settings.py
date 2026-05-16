from distutils.util import strtobool
from loguru import logger
from typing import Dict
import os


__all__ = [
    "Settings"
]

class Settings:
    
    class appSettings:
        debug_mode: bool = bool(strtobool(os.getenv("DEBUG_MODE", "False")))
        additional_settings: Dict = {}
        
        def __init__(self) -> None:
            logger.debug(f"DEBUG_MODE: {os.getenv('DEBUG_MODE')}")
            if not self.debug_mode:
                # Disable doc endpoints in non-debug mode
                self.additional_settings.update({
                    "docs_url": None,
                    "redoc_url": None,
                    "openapi_url": None,
                })
