import enum


class ServerMessage(enum.Enum):
    LOGIN_ERROR_MESSAGE = "YOU HAVE NOT LOGGED INTO THE SERVER. RERUN THE EXECUTABLE FILE"
    SUCCESSFUL_LOGIN_MESSAGE = "YOU HAVE SUCCESSFULLY LOGGED IN"
    DISCONNECT_MESSAGE = "YOU HAVE SUCCESSFULLY DISCONNECTED FROM THE SERVER"
