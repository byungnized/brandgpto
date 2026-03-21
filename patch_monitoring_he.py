# -*- coding: utf-8 -*-
"""Patch HE (monitoring) section: text for Ansan row 3 + horizontal scroll ~1.5 cards."""
import pathlib

JS = pathlib.Path(__file__).parent / "assets" / "index--9VqvNcB.js"
s = JS.read_text(encoding="utf-8")

OLD_IMG = (
    '{img:"./assets/monitoring-ansan-implant-card.png",a:"9%",b:"40%"}'
)
NEW_Q = (
    '{q:e("안산에 임플란트 잘하는 임플란트 전문 치과 알려줘",'
    '"Implant specialist dental clinics in Ansan"),a:"19%",b:"46%"}'
)
if OLD_IMG not in s:
    raise SystemExit("OLD_IMG not found")
s = s.replace(OLD_IMG, NEW_Q, 1)

OLD_GRID = (
    'g.jsx("div",{className:"grid gap-6 md:grid-cols-3 md:items-stretch",children:n.map((r,o)=>g.jsxs("div",{className:"group flex h-full flex-col rounded-xl border border-border bg-card p-8 transition-all duration-300 hover:border-primary/30 hover:shadow-glow",children:['
)
NEW_SCROLL = (
    'g.jsx("div",{className:"-mx-5 overflow-x-auto overflow-y-visible pb-3 scroll-smooth [-webkit-overflow-scrolling:touch] snap-x snap-mandatory md:-mx-8",children:g.jsx("div",{className:"flex w-max gap-4 px-5 md:gap-6 md:px-8",children:n.map((r,o)=>g.jsxs("div",{className:"group flex h-full w-[calc((100vw-2.5rem)/1.5)] shrink-0 snap-start flex-col rounded-xl border border-border bg-card p-6 transition-all duration-300 hover:border-primary/30 hover:shadow-glow md:p-8",children:['
)
if OLD_GRID not in s:
    raise SystemExit("OLD_GRID not found")
s = s.replace(OLD_GRID, NEW_SCROLL, 1)

# Add closing for inner flex wrapper: was `},o))})]})})` -> `},o))})})]})})`
OLD_TAIL = "},o))})]})})"
NEW_TAIL = "},o))})})]})})"
if s.count(OLD_TAIL) < 1:
    raise SystemExit("OLD_TAIL not found for HE")
# Only replace first occurrence in HE block — find HE start and replace first tail after it
he_start = s.find("HE=()=>{const{t:e}=Ct(),n=[")
le_marker = "},LE=()=>{const{t:e}=Ct(),t=[{title:e"
he_end = s.find(le_marker, he_start)
block = s[he_start:he_end]
idx = block.rfind(OLD_TAIL)
if idx < 0:
    raise SystemExit("OLD_TAIL not inside HE block")
block_new = block[:idx] + NEW_TAIL + block[idx + len(OLD_TAIL) :]
s = s[:he_start] + block_new + s[he_end:]

OLD_IMG_BRANCH = (
    'g.jsx("div",{className:"mb-3 flex min-h-[5.5rem] flex-1 items-start",children:i.img?g.jsx("img",{src:i.img,alt:e("안산 치과 임플란트 시술 경험 질문 예시","Sample query: implant experience among Ansan dental clinics"),className:"max-h-36 w-full rounded-md border border-border/60 object-contain object-left"}):g.jsx("p",{className:"text-sm leading-relaxed text-foreground/90",children:i.q})})'
)
NEW_P_ONLY = (
    'g.jsx("div",{className:"mb-3 flex min-h-[5.5rem] flex-1 items-start",children:g.jsx("p",{className:"text-sm leading-relaxed text-foreground/90",children:i.q})})'
)
if OLD_IMG_BRANCH not in s:
    raise SystemExit("OLD_IMG_BRANCH not found")
# Replace only within HE to avoid accidental matches
he_start = s.find("HE=()=>{const{t:e}=Ct(),n=[")
he_end = s.find(le_marker, he_start)
pre, mid, post = s[:he_start], s[he_start:he_end], s[he_end:]
if OLD_IMG_BRANCH not in mid:
    raise SystemExit("branch not in HE")
mid = mid.replace(OLD_IMG_BRANCH, NEW_P_ONLY, 1)
s = pre + mid + post

JS.write_text(s, encoding="utf-8")
print("OK patched", JS)
