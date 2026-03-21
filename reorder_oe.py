# -*- coding: utf-8 -*-
import pathlib

p = pathlib.Path(__file__).parent / "assets" / "index--9VqvNcB.js"
s = p.read_text(encoding="utf-8")

old = (
    'OE=()=>{const{t:e}=Ct(),t=[{icon:ew,title:e("검색 1위인데 AI에선 없다","Ranked #1 on Google, Invisible to AI"),desc:e("SEO에 투자했지만, ChatGPT나 Gemini에게 물어보면 경쟁사만 나옵니다.","You\'ve invested in SEO, but when people ask ChatGPT or Gemini, only your competitors show up.")},'
    '{icon:B1,title:e("고객이 AI에게 묻는 시대","Customers Now Ask AI"),desc:e(\'"강남 피부과 추천해줘", "주말에 남친이랑 데이트할 때 입을 코디 추천" — 검색창이 아니라 AI에게 묻습니다.\',\'"Best dermatologist in Gangnam", "Outfit ideas for a weekend date with my boyfriend" — they ask AI, not Google.\')},'
    '{icon:ow,title:e("기존 광고의 한계","Traditional Ads Hit Their Ceiling"),desc:e("네이버 키워드 광고, SNS 광고, 블로그 SEO — AI 추천 시대엔 충분하지 않습니다.","Keyword ads, social ads, blog SEO — they\'re not enough in the age of AI recommendations.")}];return'
)

new = (
    'OE=()=>{const{t:e}=Ct(),t=[{icon:B1,title:e("고객이 AI에게 묻는 시대","Customers Now Ask AI"),desc:e(\'"강남 피부과 추천해줘", "주말에 남친이랑 데이트할 때 입을 코디 추천" — 검색창이 아니라 AI에게 묻습니다.\',\'"Best dermatologist in Gangnam", "Outfit ideas for a weekend date with my boyfriend" — they ask AI, not Google.\')},'
    '{icon:ew,title:e("검색 1위인데 AI에선 없다","Ranked #1 on Google, Invisible to AI"),desc:e("SEO에 투자했지만, ChatGPT나 Gemini에게 물어보면 경쟁사만 나옵니다.","You\'ve invested in SEO, but when people ask ChatGPT or Gemini, only your competitors show up.")},'
    '{icon:ow,title:e("기존 광고의 한계","Traditional Ads Hit Their Ceiling"),desc:e("네이버 키워드 광고, SNS 광고, 블로그 SEO — AI 추천 시대엔 충분하지 않습니다.","Keyword ads, social ads, blog SEO — they\'re not enough in the age of AI recommendations.")}];return'
)

if old not in s:
    raise SystemExit("pattern not found")
p.write_text(s.replace(old, new, 1), encoding="utf-8")
print("OK")
