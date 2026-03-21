# -*- coding: utf-8 -*-
"""Replace HE= block in bundle with syntax-valid column layout + image card."""
import pathlib

JS = pathlib.Path(__file__).parent / "assets" / "index--9VqvNcB.js"
s = JS.read_text(encoding="utf-8")

start = s.find("HE=()=>{const{t:e}=Ct(),n=[")
end = s.find("},LE=()=>{const{t:e}=Ct(),t=[{title:e", start)
if start < 0 or end < 0:
    raise SystemExit(f"markers missing start={start} end={end}")

NEW = (
    'HE=()=>{const{t:e}=Ct(),n=[{bubble:e("안산 치과 · 의료","Ansan dental · medical"),items:[{q:e("안산에 라미네이트 잘하는 치과 알려줘","Tell me a dentist in Ansan who is good at laminates"),a:"19%",b:"55%"},{q:e("공휴일이랑 일요일에 진료되는 안산 치과 추천해줘.","Recommend an Ansan dentist open on holidays and Sundays"),a:"0%",b:"55%"},{img:"./assets/monitoring-ansan-implant-card.png",a:"9%",b:"40%"}]},{bubble:e("중고 패션 플랫폼","Used fashion platform"),items:[{q:e("안 입는 옷을 가장 쉽게 팔 수 있는 방법은?","What is the easiest way to sell clothes you do not wear?"),a:"0%",b:"51%"},{q:e("온라인에서 세컨핸드 의류 살 수 있는 곳 알려줘","Where can I buy second-hand clothing online?"),a:"0%",b:"47%"},{q:e("가품 이슈 없는 중고 패션 어플은?","Which used-fashion apps have no counterfeit issues?"),a:"22%",b:"40%"}]},{bubble:e("글로벌 데이팅 앱","Global dating app"),items:[{q:"韓国人の彼氏・彼女を作りたい時、どのアプリが一番出会いやすいですか？",a:"22%",b:"64%"},{q:"価値観が合う韓国の人と出会えるアプリは？",a:"22%",b:"61%"},{q:"韓国人と真面目な出会いができるアプリを教えてください。",a:"22%",b:"55%"}]}];return g.jsx("section",{id:"monitoring",className:"section-padding border-t border-border/50",children:g.jsxs("div",{className:"container-narrow",children:[g.jsxs("div",{className:"mx-auto mb-16 max-w-2xl text-center",children:[g.jsx("p",{className:"mb-3 text-sm font-semibold uppercase tracking-widest text-primary",children:e("모니터링 사례","Monitoring examples")}),g.jsx("h2",{className:"mb-4 text-3xl font-bold tracking-tight md:text-4xl",children:e("대상 업종별 질문 & 추천 점유 변화","Questions by industry & recommendation lift")}),g.jsx("p",{className:"text-lg text-muted-foreground",children:e("실제 사용자가 AI에게 던지는 질문과, GEO 전후 추천 비중 변화를 예시로 정리했습니다.","Sample user prompts to AI and illustrative before→after recommendation rates.")})]}),g.jsx("div",{className:"grid gap-6 md:grid-cols-3 md:items-stretch",children:n.map((r,o)=>g.jsxs("div",{className:"group flex h-full flex-col rounded-xl border border-border bg-card p-8 transition-all duration-300 hover:border-primary/30 hover:shadow-glow",children:[g.jsx("div",{className:"mb-6 shrink-0 border-b border-border/60 pb-4 text-center",children:g.jsx("h3",{className:"text-base font-bold leading-snug tracking-tight text-foreground md:text-lg",children:r.bubble})}),g.jsx("div",{className:"flex flex-1 flex-col gap-4",children:r.items.map((i,s)=>g.jsxs("div",{className:"flex min-h-[10rem] flex-col rounded-lg border border-border/80 bg-muted/25 p-4 transition-colors group-hover:border-primary/20",children:[g.jsx("div",{className:"mb-3 flex min-h-[5.5rem] flex-1 items-start",children:i.img?g.jsx("img",{src:i.img,alt:e("안산 치과 임플란트 시술 경험 질문 예시","Sample query: implant experience among Ansan dental clinics"),className:"max-h-36 w-full rounded-md border border-border/60 object-contain object-left"}):g.jsx("p",{className:"text-sm leading-relaxed text-foreground/90",children:i.q})}),g.jsxs("div",{className:"mt-auto flex items-center justify-end gap-2 border-t border-border/50 pt-3 text-sm tabular-nums",children:[g.jsx("span",{className:"text-muted-foreground",children:i.a}),g.jsx("span",{className:"text-muted-foreground/50",children:"→"}),g.jsx("span",{className:"font-semibold text-primary",children:i.b})]})]},s))})]},o))})]})})}'
)

s = s[:start] + NEW + s[end:]
JS.write_text(s, encoding="utf-8")
print("OK HE block replaced, length", len(NEW))
