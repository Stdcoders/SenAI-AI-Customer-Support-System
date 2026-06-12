import re
import uuid
from dataclasses import dataclass

from app.rag.loader import Document


MIN_TOKENS = 300
MAX_TOKENS = 500
OVERLAP_TOKENS = 50


@dataclass(slots=True)
class Chunk:

    id: str

    source: str

    section_title: str

    policy_id: str | None

    chunk_index: int

    text: str

    token_count: int


class SemanticChunker:

    """
    Semantic markdown chunker.

    Strategy:

    Markdown

    →

    Heading Sections

    →

    Merge small sections

    →

    Split large sections

    →

    Return 300–500 token chunks
    """

    def estimate_tokens(
        self,
        text: str,
    ) -> int:

        return int(len(text.split()) * 1.3)

    def extract_policy_id(
        self,
        text: str,
    ) -> str | None:

        match = re.search(

            r"Policy ID:\s*([A-Z0-9\-_]+)",

            text,

            re.IGNORECASE,

        )

        if match:

            return match.group(1)

        return None

    def split_into_sections(

        self,

        document: Document,

    ):

        pattern = r"(?=^#)"

        parts = re.split(

            pattern,

            document.content,

            flags=re.MULTILINE,

        )

        sections = []

        for part in parts:

            part = part.strip()

            if not part:

                continue

            title = part.splitlines()[0].replace("#", "").strip()

            sections.append(

                {

                    "title": title,

                    "text": part,

                }

            )

        return sections

    def merge_small_sections(

        self,

        sections,

    ):

        merged = []

        buffer = ""

        buffer_title = ""

        for section in sections:

            token_count = self.estimate_tokens(

                section["text"]

            )

            if not buffer:

                buffer = section["text"]

                buffer_title = section["title"]

                continue

            if self.estimate_tokens(buffer) < MIN_TOKENS:

                buffer += "\n\n" + section["text"]

            else:

                merged.append(

                    {

                        "title": buffer_title,

                        "text": buffer,

                    }

                )

                buffer = section["text"]

                buffer_title = section["title"]

        if buffer:

            merged.append(

                {

                    "title": buffer_title,

                    "text": buffer,

                }

            )

        return merged

    def split_large_section(

        self,

        source,

        title,

        policy_id,

        text,

    ):

        words = text.split()

        chunks = []

        start = 0

        chunk_index = 0

        approx_words = int(MAX_TOKENS / 1.3)

        overlap_words = int(OVERLAP_TOKENS / 1.3)

        while start < len(words):

            end = start + approx_words

            chunk_words = words[start:end]

            chunk_text = " ".join(chunk_words)

            chunks.append(

                Chunk(

                    id=str(uuid.uuid4()),

                    source=source,

                    section_title=title,

                    policy_id=policy_id,

                    chunk_index=chunk_index,

                    text=chunk_text,

                    token_count=self.estimate_tokens(

                        chunk_text

                    ),

                )

            )

            chunk_index += 1

            start = end - overlap_words

        return chunks

    def chunk(

        self,

        document: Document,

    ):

        sections = self.split_into_sections(

            document

        )

        sections = self.merge_small_sections(

            sections

        )

        chunks = []

        for section in sections:

            policy_id = self.extract_policy_id(

                section["text"]

            )

            tokens = self.estimate_tokens(

                section["text"]

            )

            if tokens <= MAX_TOKENS:

                chunks.append(

                    Chunk(

                        id=str(uuid.uuid4()),

                        source=document.source,

                        section_title=section["title"],

                        policy_id=policy_id,

                        chunk_index=0,

                        text=section["text"],

                        token_count=tokens,

                    )

                )

            else:

                chunks.extend(

                    self.split_large_section(

                        source=document.source,

                        title=section["title"],

                        policy_id=policy_id,

                        text=section["text"],

                    )

                )

        return chunks


semantic_chunker = SemanticChunker()