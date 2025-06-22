from fastapi import FastAPI, UploadFile

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}


@app.get("/documentation")
def write_documentation(file: UploadFile, link: str):
    if file and link:
        return {"message": "Please pass only the url or zip of repository"}
    elif file and not link:

    elif not file and link:

    else:
        return {"message": "This is the documentation endpoint. You can add more details here."}

