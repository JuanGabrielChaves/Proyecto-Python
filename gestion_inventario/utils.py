import sys
from typing import Optional

try:
    from colorama import init, Fore, Style

    init(autoreset=True)
    COLORAMA_DISPONIBLE = True
except ImportError:
    COLORAMA_DISPONIBLE = False


def color_exito(texto: str) -> str:
    """Aplica color verde al texto si colorama está disponible."""
    if COLORAMA_DISPONIBLE:
        return f"{Fore.GREEN}{texto}{Style.RESET_ALL}"
    return texto


def color_error(texto: str) -> str:
    """Aplica color rojo al texto si colorama está disponible."""
    if COLORAMA_DISPONIBLE:
        return f"{Fore.RED}{texto}{Style.RESET_ALL}"
    return texto


def color_info(texto: str) -> str:
    """Aplica color cyan al texto si colorama está disponible."""
    if COLORAMA_DISPONIBLE:
        return f"{Fore.CYAN}{texto}{Style.RESET_ALL}"
    return texto


def color_titulo(texto: str) -> str:
    """Aplica color amarillo y negrita al texto si colorama está disponible."""
    if COLORAMA_DISPONIBLE:
        return f"{Fore.YELLOW}{Style.BRIGHT}{texto}{Style.RESET_ALL}"
    return texto


def color_menu(texto: str) -> str:
    """Aplica color magenta al texto si colorama está disponible."""
    if COLORAMA_DISPONIBLE:
        return f"{Fore.MAGENTA}{texto}{Style.RESET_ALL}"
    return texto
