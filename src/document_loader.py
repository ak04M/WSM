from pathlib import Path


def load_documents(folder_path):

    folder = Path(folder_path)

    documents = {}
    filenames = {}

    files = sorted(
        folder.glob("data*.txt"),
        key=lambda file: int(file.stem.replace("data", ""))
    )

    for file in files:
        doc_id = int(file.stem.replace("data", ""))

        with open(file, "r", encoding="utf-8") as f:
            documents[doc_id] = f.read()

        filenames[doc_id] = file.name

    return documents, filenames