from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class Document:
    """
    Represents a single knowledge document.
    """

    source: str
    content: str


class KnowledgeLoader:
    """
    Loads all markdown knowledge documents from disk.

    Responsibility:
    - discover files
    - read content
    - create Document objects

    It DOES NOT:
    - chunk
    - embed
    - retrieve
    """

    def __init__(self, knowledge_path: str = "knowledge"):

        if knowledge_path is None:

            self.knowledge_path = (
                Path(__file__).resolve().parent.parent / "knowledge"
        )

        else:

            self.knowledge_path = Path(knowledge_path)

    def load_documents(self) -> list[Document]:

        documents: list[Document] = []

        if not self.knowledge_path.exists():

            raise FileNotFoundError(
                f"Knowledge directory not found: {self.knowledge_path}"
            )

        markdown_files = sorted(
            self.knowledge_path.glob("*.md")
        )

        for file in markdown_files:

            content = file.read_text(
                encoding="utf-8"
            )

            documents.append(

                Document(

                    source=file.name,

                    content=content,

                )

            )

        return documents


knowledge_loader = KnowledgeLoader()