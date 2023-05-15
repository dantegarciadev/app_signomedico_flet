import flet

app = flet.FletApp(__name__)

def upload():
    # Get the uploaded file.
    file = request.files["file"]

    # Save the file to a directory.
    with open("uploads/" + file.filename, "wb") as f:
        f.write(file.read())

    # Display a message to the user indicating that the file has been uploaded successfully.
    return "File uploaded successfully!"

app.add_route("/upload", methods=["POST"], view=upload)

# Create a button to allow users to select a file to upload.
button = flet.Button(
    text="Upload File",
    onclick=lambda: app.post("/upload", files={"file": flet.FileInput()})
)

# Add the button to the page.
app.add_element(button)

if __name__ == "__main__":
    app.run(debug=True)
