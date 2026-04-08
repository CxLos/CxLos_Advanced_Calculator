
# =========== Imports =========== #

import uvicorn
import logging
from pathlib import Path

from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.exceptions import RequestValidationError

from pydantic import BaseModel, Field, field_validator  # Use @validator for Pydantic 1.x
from app.operations import add, subtract, multiply, divide  # Ensure correct import path

# ----- Colorama ----- #

import colorama
from colorama import Fore, Back, Style, init
init(autoreset=True) # Automatically reset color after each print

for color_name in dir(colorama.Fore):
    if not color_name.startswith('_'): # Skip private attributes
        color = getattr(colorama.Fore, color_name) # Get the actual color code
        # print(f"{color}{color_name}{colorama.Style.RESET_ALL}") # Print color name in its own color
    # print('\n')

# print(Fore.BLACK + '-' * 200, '\n')

# =========== Get cwd =========== #

# Get current file path
# print(f"Current file path: {Path(__file__).resolve()}")

# =========== Main Code =========== #

# Seting up logging configuration for the application. This will allow us to log important information and errors during the execution of the application, which is crucial for debugging and monitoring purposes.
logging.basicConfig(
    level=logging.INFO # Set the logging level to INFO, which means that all messages at this level and above (WARNING, ERROR, CRITICAL) will be logged.
)

# Create a logger instance for this module. This allows us to log messages with the context of this specific module, making it easier to identify where logs are coming from when analyzing logs from the entire application.
logger = logging.getLogger(__name__)

# Create an instance of the FastAPI application
app = FastAPI()

# Mount the static files directory to serve CSS, JavaScript, and other static assets. This allows the application to serve files from the "assets" directory when requested by the client, making it possible to include stylesheets and scripts in the web pages.
BASE_DIR = Path(__file__).parent
app.mount("/assets", StaticFiles(directory=BASE_DIR / "assets"), name="assets")

# Setup templates directory
templates = Jinja2Templates(directory=BASE_DIR / "templates")

# Pydantic model for request data
class OperationRequest(BaseModel):
    a: float = Field(..., description="The first number")
    b: float = Field(..., description="The second number")

    # field_validator is used to validate the input data for both 'a' and 'b'. It checks if the values are either integers or floats. If not, it raises a ValueError with a descriptive message. This ensures that the API receives valid numerical input for the operations.
    @field_validator('a', 'b')  # Correct decorator for Pydantic 1.x
    def validate_numbers(cls, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Both a and b must be numbers.')
        return value

# Pydantic model for successful response
class OperationResponse(BaseModel):
    result: float = Field(..., description="The result of the operation")

# Pydantic model for error response
class ErrorResponse(BaseModel):
    error: str = Field(..., description="Error message")

# Custom Exception Handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    logger.error(f"HTTPException on {request.url.path}: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail},
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # Extracting error messages
    error_messages = "; ".join([f"{err['loc'][-1]}: {err['msg']}" for err in exc.errors()])
    logger.error(f"ValidationError on {request.url.path}: {error_messages}")
    return JSONResponse(
        status_code=400,
        content={"error": error_messages},
    )

@app.get("/")
async def read_root(request: Request):
    """
    Serve the index.html template.
    """
    return templates.TemplateResponse(request, "index.html")

@app.get("/health")
async def health_check():
    """
    Health check endpoint used by Docker to verify the container is running correctly.
    Returns a simple JSON response indicating the service is healthy.
    """
    return {"status": "healthy"}

@app.post("/add", response_model=OperationResponse, responses={400: {"model": ErrorResponse}})
async def add_route(operation: OperationRequest):
    """
    Add two numbers.
    """
    try:
        result = add(operation.a, operation.b)
        return OperationResponse(result=result)
    except Exception as e:
        logger.error(f"Add Operation Error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/subtract", response_model=OperationResponse, responses={400: {"model": ErrorResponse}})
async def subtract_route(operation: OperationRequest):
    """
    Subtract two numbers.
    """
    try:
        result = subtract(operation.a, operation.b)
        return OperationResponse(result=result)
    except Exception as e:
        logger.error(f"Subtract Operation Error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/multiply", response_model=OperationResponse, responses={400: {"model": ErrorResponse}})
async def multiply_route(operation: OperationRequest):
    """
    Multiply two numbers.
    """
    try:
        result = multiply(operation.a, operation.b)
        return OperationResponse(result=result)
    except Exception as e:
        logger.error(f"Multiply Operation Error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/divide", response_model=OperationResponse, responses={400: {"model": ErrorResponse}})
async def divide_route(operation: OperationRequest):
    """
    Divide two numbers.
    """
    try:
        result = divide(operation.a, operation.b)
        return OperationResponse(result=result)
    except ValueError as e:
        logger.error(f"Divide Operation Error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Divide Operation Internal Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# ========== Run Application ========== #

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)