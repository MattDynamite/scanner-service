from fastapi import FastAPI
import uvicorn
from loguru import logger
from models import ScannerType, TCPScanner, HTTPScanner

app = FastAPI()


@app.get("/scan")
def scan_ports():
    scanner = None
    scanner_type: str = ScannerType.TCP.value
    if scanner_type == ScannerType.TCP:
        scanner = TCPScanner()
    elif scanner_type == ScannerType.HTTP:
        scanner = HTTPScanner()

    if not scanner:
        return {"message": "Invalid scanner type"}

    ports = scanner.scan()
    return {"ports": ports}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
