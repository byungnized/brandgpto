# -*- coding: utf-8 -*-
import pathlib

JS = pathlib.Path(__file__).parent / "assets" / "index--9VqvNcB.js"
s = JS.read_text(encoding="utf-8")
if "HE=()=>{const{t:e}=Ct(),n=[" in s:
    print("Already patched (HE= present). Restore from index--9VqvNcB.js.bak if needed.")
    raise SystemExit(0)

start = s.find('AE=()=>{const{t:e}=Ct(),t=[{name:e("네이버 키워드 광고"')
end_marker = '},_E=()=>{const{t:e}=Ct(),t=[{icon:H1'
end = s.find(end_marker, start)
if start < 0 or end < 0:
    raise SystemExit(f"range fail {start} {end}")

NEW_AE = (
    'AE=()=>{const{t:e}=Ct(),t=[e("AI 노출","AI Visibility"),e("지속성","Lasting"),e("신뢰도","Trust"),e("글로벌","Global")],'
    'n=[e("네이버 키워드 광고","Naver keyword ads"),e("SNS / 인스타 광고","SNS / Instagram ads"),e("블로그 SEO","Blog SEO"),"BrandGPTO (GEO)"],'
    "r=[[!1,!1,!1,!0],[!1,!1,!0,!0],[!1,!1,!0,!0],[!1,!0,!1,!0]];"
    'return g.jsx("section",{id:"geo",className:"section-padding border-t border-border/50",children:g.jsxs("div",{className:"container-narrow",children:['
    'g.jsxs("div",{className:"mx-auto mb-16 max-w-2xl text-center",children:['
    'g.jsx("p",{className:"mb-3 text-sm font-semibold uppercase tracking-widest text-primary",children:e("GEO란 무엇인가","What is GEO")}),'
    'g.jsx("h2",{className:"mb-4 text-3xl font-bold tracking-tight md:text-4xl",children:e(g.jsxs(g.Fragment,{children:["AI가 당신을 추천하게 만드는 기술,"," ",g.jsx("span",{className:"text-gradient-primary",children:"GEO"})]}),g.jsxs(g.Fragment,{children:["The Technology That Makes AI"," ",g.jsx("span",{className:"text-gradient-primary",children:"Recommend You"})]}))}),'
    'g.jsx("p",{className:"text-lg text-muted-foreground",children:e("GEO(Generative Engine Optimization)는 ChatGPT, Gemini 등 AI 모델이 당신의 회사를 정확히 이해하고 추천하도록 최적화하는 기술입니다. GPTO가 GEO 솔루션을, Brandots가 브랜드 메시지 정리를 지원합니다.","GEO (Generative Engine Optimization) ensures AI models like ChatGPT and Gemini accurately understand and recommend your company. GPTO delivers GEO solutions, while Brandots supports brand messaging clarity.")})]}),'
    'g.jsx("div",{className:"mx-auto max-w-3xl overflow-hidden rounded-xl border border-border",children:g.jsx("div",{className:"overflow-x-auto",children:g.jsxs("table",{className:"w-full text-sm",children:['
    'g.jsx("thead",{children:g.jsx("tr",{className:"border-b border-border bg-muted/50",children:[g.jsx("th",{className:"px-4 py-3 text-left font-semibold md:px-6",children:e("비교 항목","Criteria")}),...n.map((o,i)=>g.jsx("th",{className:"px-4 py-3 text-left font-semibold md:px-6"+(i===3?" text-primary":""),children:o},i))]})}),'
    'g.jsx("tbody",{children:t.map((o,i)=>g.jsxs("tr",{className:"border-b border-border last:border-0",children:[g.jsx("td",{className:"px-4 py-4 font-medium md:px-6",children:o}),...r[i].map((s,l)=>g.jsx("td",{className:"px-4 py-4 md:px-6",children:s?g.jsx(V1,{className:"h-5 w-5 "+(l===3?"text-primary":"text-green-400")}):g.jsx(Nm,{className:"h-5 w-5 text-muted-foreground/40"})},l))]},i))})]})})})]})})},'
)

# Insert HE component before LE= (must not use WE — conflicts with [om,WE]=Zs("Toast") in bundle)
HE = (
    'HE=()=>{const{t:e}=Ct(),n=[{bubble:e("안산 치과 · 의료","Ansan dental · medical"),items:[{q:e("안산에 라미네이트 잘하는 치과 알려줘","Tell me a dentist in Ansan who is good at laminates"),a:"19%",b:"55%"},{q:e("공휴일이랑 일요일에 진료되는 안산 치과 추천해줘.","Recommend an Ansan dentist open on holidays and Sundays"),a:"0%",b:"55%"},{img:"./assets/monitoring-ansan-implant-card.png",a:"9%",b:"40%"}]},{bubble:e("중고 패션 플랫폼","Used fashion platform"),items:[{q:e("안 입는 옷을 가장 쉽게 팔 수 있는 방법은?","What is the easiest way to sell clothes you do not wear?"),a:"0%",b:"51%"},{q:e("온라인에서 세컨핸드 의류 살 수 있는 곳 알려줘","Where can I buy second-hand clothing online?"),a:"0%",b:"47%"},{q:e("가품 이슈 없는 중고 패션 어플은?","Which used-fashion apps have no counterfeit issues?"),a:"22%",b:"40%"}]},{bubble:e("글로벌 데이팅 앱","Global dating app"),items:[{q:"韓国人の彼氏・彼女を作りたい時、どのアプリが一番出会いやすいですか？",a:"22%",b:"64%"},{q:"価値観が合う韓国の人と出会えるアプリは？",a:"22%",b:"61%"},{q:"韓国人と真面目な出会いができるアプリを教えてください。",a:"22%",b:"55%"}]}];return g.jsx("section",{id:"monitoring",className:"section-padding border-t border-border/50",children:g.jsxs("div",{className:"container-narrow",children:[g.jsxs("div",{className:"mx-auto mb-16 max-w-2xl text-center",children:[g.jsx("p",{className:"mb-3 text-sm font-semibold uppercase tracking-widest text-primary",children:e("모니터링 사례","Monitoring examples")}),g.jsx("h2",{className:"mb-4 text-3xl font-bold tracking-tight md:text-4xl",children:e("대상 업종별 질문 & 추천 점유 변화","Questions by industry & recommendation lift")}),g.jsx("p",{className:"text-lg text-muted-foreground",children:e("실제 사용자가 AI에게 던지는 질문과, GEO 전후 추천 비중 변화를 예시로 정리했습니다.","Sample user prompts to AI and illustrative before→after recommendation rates.")})]}),g.jsx("div",{className:"grid gap-6 md:grid-cols-3 md:items-stretch",children:n.map((r,o)=>g.jsxs("div",{className:"group flex h-full flex-col rounded-xl border border-border bg-card p-8 transition-all duration-300 hover:border-primary/30 hover:shadow-glow",children:[g.jsx("div",{className:"mb-6 shrink-0 border-b border-border/60 pb-4 text-center",children:g.jsx("h3",{className:"text-base font-bold leading-snug tracking-tight text-foreground md:text-lg",children:r.bubble})}),g.jsx("div",{className:"flex flex-1 flex-col gap-4",children:r.items.map((i,s)=>g.jsxs("div",{className:"flex min-h-[10rem] flex-col rounded-lg border border-border/80 bg-muted/25 p-4 transition-colors group-hover:border-primary/20",children:[g.jsx("div",{className:"mb-3 flex min-h-[5.5rem] flex-1 items-start",children:i.img?g.jsx("img",{src:i.img,alt:e("안산 치과 임플란트 시술 경험 질문 예시","Sample query: implant experience among Ansan dental clinics"),className:"max-h-36 w-full rounded-md border border-border/60 object-contain object-left"}):g.jsx("p",{className:"text-sm leading-relaxed text-foreground/90",children:i.q})}),g.jsxs("div",{className:"mt-auto flex items-center justify-end gap-2 border-t border-border/50 pt-3 text-sm tabular-nums",children:[g.jsx("span",{className:"text-muted-foreground",children:i.a}),g.jsx("span",{className:"text-muted-foreground/50",children:"→"}),g.jsx("span",{className:"font-semibold text-primary",children:i.b})]})]},s))})]},o))})]})})},
)


repls = [
    (
        '"강남 피부과 추천해줘", "가성비 프로틴 추천"',
        '"강남 피부과 추천해줘", "주말에 남친이랑 데이트할 때 입을 코디 추천"',
    ),
    (
        '"Best dermatologist in Gangnam", "Best protein powder"',
        '"Best dermatologist in Gangnam", "Outfit ideas for a weekend date with my boyfriend"',
    ),
    (
        "e('\"가성비 프로틴 추천\" — 리뷰도 많고 판매량도 높은데 경쟁사만 나옵니다.',",
        "e('\"주말에 남친이랑 데이트할 때 입을 코디 추천\" — 리뷰도 많고 판매량도 높은데 경쟁사만 나옵니다.',",
    ),
    (
        '\'"Best value protein" — great reviews and sales, but AI only mentions competitors.\')',
        '\'"Weekend date outfit picks" — great reviews and sales, but AI only mentions competitors.\')',
    ),
    (
        "GPTO가 GEO 솔루션을, Brandots가 필요 시 브랜드 메시지 정리를 지원합니다.",
        "GPTO가 GEO 솔루션을, Brandots가 브랜드 메시지 정리를 지원합니다.",
    ),
    (
        "GPTO delivers GEO solutions, while Brandots optionally supports brand messaging clarity.",
        "GPTO delivers GEO solutions, while Brandots supports brand messaging clarity.",
    ),
    (
        "GEO만으로도 충분히 시작할 수 있습니다. 필요한 경우, Brandots가 브랜드",
        "GEO만으로도 충분히 시작할 수 있습니다. Brandots가 브랜드",
    ),
    (
        "You can start with GEO alone. If needed, Brandots helps clarify",
        "You can start with GEO alone. Brandots helps clarify",
    ),
]

for a, b in repls:
    c = s.count(a)
    if c != 1:
        raise SystemExit(f"Expected 1x {a[:50]!r} got {c}")
    s = s.replace(a, b, 1)

s = s[:start] + NEW_AE + s[end:]

le_sig = "LE=()=>{const{t:e}=Ct(),t=[{title:e(\"브랜드 현황 스코어 진단\""
ins = s.find(le_sig)
if ins < 0:
    raise SystemExit("LE= not found")
s = s[:ins] + HE + s[ins:]

s = s.replace("g.jsx(IE,{}),g.jsx(LE,{})", "g.jsx(IE,{}),g.jsx(HE,{}),g.jsx(LE,{})")

JS.write_text(s, encoding="utf-8")
print("OK: patched", JS)
