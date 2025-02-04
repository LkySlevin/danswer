from enum import Enum

DOCUMENT_ID = "document_id"
CHUNK_ID = "chunk_id"
BLURB = "blurb"
CONTENT = "content"
SOURCE_TYPE = "source_type"
SOURCE_LINKS = "source_links"
SOURCE_LINK = "link"
SEMANTIC_IDENTIFIER = "semantic_identifier"
TITLE = "title"
SECTION_CONTINUATION = "section_continuation"
EMBEDDINGS = "embeddings"
ALLOWED_USERS = "allowed_users"
ACCESS_CONTROL_LIST = "access_control_list"
DOCUMENT_SETS = "document_sets"
TIME_FILTER = "time_filter"
METADATA = "metadata"
MATCH_HIGHLIGHTS = "match_highlights"
# stored in the `metadata` of a chunk. Used to signify that this chunk should
# not be used for QA. For example, Google Drive file types which can't be parsed
# are still useful as a search result but not for QA.
IGNORE_FOR_QA = "ignore_for_qa"
GEN_AI_API_KEY_STORAGE_KEY = "genai_api_key"
PUBLIC_DOC_PAT = "PUBLIC"
PUBLIC_DOCUMENT_SET = "__PUBLIC"
QUOTE = "quote"
BOOST = "boost"
DOC_UPDATED_AT = "doc_updated_at"  # Indexed as seconds since epoch
PRIMARY_OWNERS = "primary_owners"
SECONDARY_OWNERS = "secondary_owners"
RECENCY_BIAS = "recency_bias"
HIDDEN = "hidden"
SCORE = "score"
ID_SEPARATOR = ":;:"
DEFAULT_BOOST = 0
SESSION_KEY = "session"


class DocumentSource(str, Enum):
    SLACK = "slack"
    WEB = "web"
    GOOGLE_DRIVE = "google_drive"
    GITHUB = "github"
    GURU = "guru"
    BOOKSTACK = "bookstack"
    CONFLUENCE = "confluence"
    SLAB = "slab"
    JIRA = "jira"
    PRODUCTBOARD = "productboard"
    FILE = "file"
    NOTION = "notion"
    ZULIP = "zulip"
    LINEAR = "linear"
    HUBSPOT = "hubspot"
    DOCUMENT360 = "document360"
    GONG = "gong"
    GOOGLE_SITES = "google_sites"
    ZENDESK = "zendesk"


class DocumentIndexType(str, Enum):
    COMBINED = "combined"  # Vespa
    SPLIT = "split"  # Typesense + Qdrant


class AuthType(str, Enum):
    DISABLED = "disabled"
    BASIC = "basic"
    GOOGLE_OAUTH = "google_oauth"
    OIDC = "oidc"
    SAML = "saml"


class QAFeedbackType(str, Enum):
    LIKE = "like"  # User likes the answer, used for metrics
    DISLIKE = "dislike"  # User dislikes the answer, used for metrics


class SearchFeedbackType(str, Enum):
    ENDORSE = "endorse"  # boost this document for all future queries
    REJECT = "reject"  # down-boost this document for all future queries
    HIDE = "hide"  # mark this document as untrusted, hide from LLM
    UNHIDE = "unhide"


class MessageType(str, Enum):
    # Using OpenAI standards, Langchain equivalent shown in comment
    SYSTEM = "system"  # SystemMessage
    USER = "user"  # HumanMessage
    ASSISTANT = "assistant"  # AIMessage
    DANSWER = "danswer"  # FunctionMessage
