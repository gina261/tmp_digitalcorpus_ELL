import streamlit as st
import re
import nltk
from spellchecker import SpellChecker
from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer

# ============== NLTK & SpellChecker Setup ==============
def load_resources():
    """NLTK 데이터와 SpellChecker를 한 번만 로드합니다."""
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt', quiet=True)
    
    spell = SpellChecker(language='en')
    return spell

spell_checker = load_resources()

# ============== Logic from spelling_counter.py ==============
def tokenize_text(text: str):
    return word_tokenize(text)

def is_candidate_word(tok: str) -> bool:
    if not isinstance(tok, str):
        return False
    # 알파벳과 따옴표만 허용
    if not re.match(r"^[A-Za-z']+$", tok):
        return False
    # 2글자 이하 제외
    if len(tok) <= 2:
        return False
    # 전체 대문자(약어 등) 제외
    if tok.isupper():
        return False
    return True

def analyze_and_correct(text: str, spell: SpellChecker):
    """
    텍스트를 분석하여 교정된 텍스트와 에러 목록을 반환합니다.
    """
    detok = TreebankWordDetokenizer()
    tokens = tokenize_text(text)
    
    candidate_indices = [i for i, t in enumerate(tokens) if is_candidate_word(t)]
    candidate_words = [tokens[i].lower() for i in candidate_indices]
    
    # 한 번에 오타 찾기
    misspelled = spell.unknown(candidate_words)
    
    corrections_log = {}
    error_count = 0
    
    # 교정 로직
    for i, lw in zip(candidate_indices, candidate_words):
        if lw in misspelled:
            orig = tokens[i]
            suggestion = spell.correction(lw)
            
            if not suggestion:
                continue
                
            # 로그 저장
            if orig not in corrections_log:
                corrections_log[orig] = suggestion
                error_count += 1
            
            # 대소문자 보존 처리
            if orig.istitle():
                suggestion = suggestion.capitalize()
            elif orig.isupper():
                suggestion = suggestion.upper()
                
            tokens[i] = suggestion
            
    corrected_text = detok.detokenize(tokens)
    return corrected_text, corrections_log, error_count

# ============== 챗봇 응답 생성 함수 ==============
def generate_spelling_response(text):
    corrected_text, corrections, count = analyze_and_correct(text, spell_checker)
    
    response_md = ""
    
    if count == 0:
        response_md += "**오타가 발견되지 않았습니다.**\n\n완벽한 문장이네요!"
    else:
        response_md += f"🔍 **총 {count}개의 오타를 발견하여 수정했습니다.**\n\n"
        response_md += "---\n"
        response_md += "**수정된 문장:**\n"
        response_md += f"> {corrected_text}\n\n"
        response_md += "---\n"
        response_md += "**상세 수정 내역:**\n"
        for original, fixed in corrections.items():
            response_md += f"- `{original}` → **{fixed}**\n"
            
    return response_md