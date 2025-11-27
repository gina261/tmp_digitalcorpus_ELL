from pathlib import Path
import streamlit as st

def _read_text(path: str) -> str:
    p = Path(path)
    return p.read_text(encoding="utf-8")

@st.cache_data(show_spinner=False)
def load_css_text(path: str, _mtime: float) -> str:
    # 캐시 키에 파일 수정시간을 섞어서, 파일 바뀌면 자동 갱신
    return _read_text(path)

def inject_css(path: str):
    p = Path(path)
    css = load_css_text(str(p), p.stat().st_mtime)
    st.markdown(f"<style>\n{css}\n</style>", unsafe_allow_html=True)

def inject_css_bundle(paths: list[str]):
    parts = []
    for path in paths:
        p = Path(path)
        parts.append(load_css_text(str(p), p.stat().st_mtime))
    st.markdown("<style>\n" + "\n\n".join(parts) + "\n</style>", unsafe_allow_html=True)