from typing import List
import socket
import requests

from pydantic import BaseModel
import enum
from loguru import logger


class Port(BaseModel):
    number: int
    is_exposed: bool


class ScannerType(str, enum.Enum):
    HTTP = "http_scanner"
    TCP = "tcp_scanner"
    EVENTBRIDGE = "eventbridge_scanner"


class BaseScanner:
    _type: ScannerType

    def scan(self) -> List[Port]:
        raise NotImplementedError


class TCPScanner(BaseScanner):
    _type = ScannerType.TCP

    def scan(self) -> List[Port]:
        open_ports = []
        for port in range(1000, 10000):
            logger.info(f"Scanning port number {port}")
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex(('localhost', port))
            if result == 0:
                is_exposed = True
            else:
                is_exposed = False

            open_ports.append(Port(number=port, is_exposed=is_exposed))
            if is_exposed:
                logger.info(f"port {port} is open")

            sock.close()
        return open_ports


class HTTPScanner(BaseScanner):
    _type = ScannerType.HTTP

    def scan(self) -> List[Port]:
        open_ports = []
        for port in range(1, 65536):
            is_exposed = False
            try:
                logger.info(f"Scanning port number {port}")
                response = requests.get(f"http://localhost:{port}", timeout=1)
                if response.status_code == 200:
                    is_exposed = True
                else:
                    is_exposed = False
            except requests.exceptions.RequestException:
                is_exposed = False
            finally:
                open_ports.append(Port(number=port, is_exposed=is_exposed))
                logger.info(f"Conclusion is {is_exposed=}")
        return open_ports
