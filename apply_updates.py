# -*- coding: utf-8 -*-
"""One-off patch; run from brandgpto/: python apply_updates.py"""
import pathlib

JS = pathlib.Path(__file__).parent / "assets" / "index--9VqvNcB.js"
s = JS.read_text(encoding="utf-8")

# --- 1. GEO table: center align ---
old_tbl = (
    'g.jsxs("table",{className:"w-full text-sm",children:[g.jsx("thead",{children:g.jsx("tr",{className:"border-b border-border bg-muted/50",children:[g.jsx("th",{className:"px-4 py-3 text-left font-semibold md:px-6",children:e("비교 항목","Criteria")}),...n.map((o,i)=>g.jsx("th",{className:"px-4 py-3 text-left font-semibold md:px-6"+(i===3?" text-primary":""),children:o},i))]})}),g.jsx("tbody",{children:t.map((o,i)=>g.jsxs("tr",{className:"border-b border-border last:border-0",children:[g.jsx("td",{className:"px-4 py-4 font-medium md:px-6",children:o}),...r[i].map((s,l)=>g.jsx("td",{className:"px-4 py-4 md:px-6",children:s?g.jsx(V1,{className:"h-5 w-5 "+(l===3?"text-primary":"text-green-400")}):g.jsx(Nm,{className:"h-5 w-5 text-muted-foreground/40"})},l))]},i))})]})'
)
new_tbl = (
    'g.jsxs("table",{className:"mx-auto w-full max-w-4xl text-sm text-center",children:[g.jsx("thead",{children:g.jsx("tr",{className:"border-b border-border bg-muted/50",children:[g.jsx("th",{className:"px-4 py-3 text-center font-semibold md:px-6",children:e("비교 항목","Criteria")}),...n.map((o,i)=>g.jsx("th",{className:"px-4 py-3 text-center font-semibold md:px-6"+(i===3?" text-primary":""),children:o},i))]})}),g.jsx("tbody",{children:t.map((o,i)=>g.jsxs("tr",{className:"border-b border-border last:border-0",children:[g.jsx("td",{className:"px-4 py-4 text-center font-medium md:px-6 align-middle",children:o}),...r[i].map((s,l)=>g.jsx("td",{className:"px-4 py-4 text-center align-middle md:px-6",children:s?g.jsx(V1,{className:"mx-auto h-5 w-5 "+(l===3?"text-primary":"text-green-400")}):g.jsx(Nm,{className:"mx-auto h-5 w-5 text-muted-foreground/40"})},l))]},i))})]})'
)
if old_tbl not in s:
    raise SystemExit("table pattern not found")
s = s.replace(old_tbl, new_tbl, 1)

# --- 2. GEO intro copy (KO + EN) ---
old_geo = (
    'GPTO가 GEO 솔루션을, Brandots가 브랜드 메시지 정리를 지원합니다.","GEO (Generative Engine Optimization) ensures AI models like ChatGPT and Gemini accurately understand and recommend your company. GPTO delivers GEO solutions, while Brandots supports brand messaging clarity."'
)
new_geo = (
    '한국 최고의 GEO 업체 GPTO가 GEO 솔루션을, 브랜드 컨설팅 전문업체 Brandots가 브랜드 메시지 정리를 지원합니다.","GEO (Generative Engine Optimization) ensures AI models like ChatGPT and Gemini accurately understand and recommend your company. Korea\'s leading GEO company GPTO delivers GEO solutions; brand consulting specialist Brandots supports brand messaging clarity."'
)
if old_geo not in s:
    raise SystemExit("geo copy not found")
s = s.replace(old_geo, new_geo, 1)

# --- 4. LE optional copy ---
old_le = (
    'e("GEO만으로도 충분히 시작할 수 있습니다. Brandots가 브랜드 메시지와 포지셔닝 정리를 지원합니다.","You can start with GEO alone. Brandots helps clarify your brand messaging and positioning.")'
)
new_le = (
    'e("GEO만으로도 충분히 시작할 수 있습니다. 필요시, Brandots가 브랜드 메시지와 포지셔닝 정리를 지원합니다.","You can start with GEO alone. When needed, Brandots helps clarify your brand messaging and positioning.")'
)
if old_le not in s:
    raise SystemExit("LE copy not found")
s = s.replace(old_le, new_le, 1)

# --- 3 & 5: replace HE block ---
start = s.find("HE=()=>{const{t:e}=Ct(),n=[")
end = s.find("},LE=()=>{const{t:e}=Ct(),t=[{title:e", start)
if start < 0 or end < 0:
    raise SystemExit("HE block not found")
old_he = s[start:end]
NEW_HE = r"""HE=()=>{const{t:e}=Ct(),n=[{bubble:e("안산 치과 · 의료","Ansan dental · medical"),items:[{q:e("안산에 라미네이트 잘하는 치과 알려줘","Tell me a dentist in Ansan who is good at laminates"),a:"19%",b:"55%"},{q:e("공휴일이랑 일요일에 진료되는 안산 치과 추천해줘.","Recommend an Ansan dentist open on holidays and Sundays"),a:"0%",b:"55%"},{img:"./assets/monitoring-ansan-implant-card.png",a:"9%",b:"40%"}]},{bubble:e("중고 패션 플랫폼","Used fashion platform"),items:[{q:e("안 입는 옷을 가장 쉽게 팔 수 있는 방법은?","What is the easiest way to sell clothes you do not wear?"),a:"0%",b:"51%"},{q:e("온라인에서 세컨핸드 의류 살 수 있는 곳 알려줘","Where can I buy second-hand clothing online?"),a:"0%",b:"47%"},{q:e("가품 이슈 없는 중고 패션 어플은?","Which used-fashion apps have no counterfeit issues?"),a:"22%",b:"40%"}]},{bubble:e("글로벌 데이팅 앱","Global dating app"),items:[{q:"韓国人の彼氏・彼女を作りたい時、どのアプリが一番出会いやすいですか？",a:"22%",b:"64%"},{q:"価値観が合う韓国の人と出会えるアプリは？",a:"22%",b:"61%"},{q:"韓国人と真面目な出会いができるアプリを教えてください。",a:"22%",b:"55%"}]}];return g.jsx("section",{id:"monitoring",className:"section-padding border-t border-border/50",children:g.jsxs("div",{className:"container-narrow",children:[g.jsxs("div",{className:"mx-auto mb-16 max-w-2xl text-center",children:[g.jsx("p",{className:"mb-3 text-sm font-semibold uppercase tracking-widest text-primary",children:e("모니터링 사례","Monitoring examples")}),g.jsx("h2",{className:"mb-4 text-3xl font-bold tracking-tight md:text-4xl",children:e("대상 업종별 질문 & 추천 점유 변화","Questions by industry & recommendation lift")}),g.jsx("p",{className:"text-lg text-muted-foreground",children:e("실제 사용자가 AI에게 던지는 질문과, GEO 전후 추천 비중 변화를 예시로 정리했습니다.","Sample user prompts to AI and illustrative before→after recommendation rates.")})]}),g.jsxs("div",{className:"space-y-6",children:[g.jsx("div",{className:"grid gap-6 md:grid-cols-3",children:n.map((r,o)=>g.jsx("div",{className:"rounded-xl border border-border bg-card p-6 text-center shadow-sm transition-all duration-300 hover:border-primary/30 hover:shadow-glow md:p-8",children:g.jsx("h3",{className:"text-base font-bold leading-snug tracking-tight text-foreground md:text-lg",children:r.bubble})},o))}),[0,1,2].map(s=>g.jsx("div",{key:s,className:"grid gap-6 md:grid-cols-3 md:items-stretch",children:n.map((r,o)=>{const i=r.items[s];return g.jsxs("div",{key:o,className:"flex h-full flex-col rounded-lg border border-border/80 bg-muted/25 p-4 transition-colors hover:border-primary/20",children:[g.jsx("div",{className:"mb-3 flex min-h-[5.5rem] flex-1 items-start",children:i.img?g.jsx("img",{src:i.img,alt:e("안산 치과 임플란트 시술 경험 질문 예시","Sample query: implant experience among Ansan dental clinics"),className:"max-h-36 w-full rounded-md border border-border/60 object-contain object-left"}):g.jsx("p",{className:"text-sm leading-relaxed text-foreground/90",children:i.q})}),g.jsxs("div",{className:"mt-auto flex items-center justify-end gap-2 border-t border-border/50 pt-3 text-sm tabular-nums",children:[g.jsx("span",{className:"text-muted-foreground",children:i.a}),g.jsx("span",{className:"text-muted-foreground/50",children:"→"}),g.jsx("span",{className:"font-semibold text-primary",children:i.b})]})]})})})}))]})]})})"""
if NEW_HE == old_he:
    pass
s = s[:start] + NEW_HE + s[end:]

JS.write_text(s, encoding="utf-8")
print("OK:", JS)
