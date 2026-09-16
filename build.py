#!/usr/bin/env python3
"""Builds every page of the site from site-master.html.
Sections in the master are delimited by '<!-- NAME -->' comment markers.
Run: python3 build.py   (index.html and the sub pages are regenerated)"""
import re
m=open('site-master.html').read()
head,rest=m.split('<body>',1)
chrome_end=rest.index('<!-- HERO -->')
chrome=rest[:chrome_end]                      # preloader, canvas, nav
tail_start=rest.index('<footer>')
footer_and_scripts=rest[tail_start:]
body=rest[chrome_end:tail_start]
parts=dict(re.findall(r'<!-- ([A-Z0-9 ]+?) -->\n(.*?)(?=\n<!-- [A-Z0-9 ]+? -->|\Z)',body,re.S))
NAV={'Solutions':'index.html#services','Industries':'index.html#industries','Dual Pricing':'dual-pricing.html','Savings':'savings.html','Terminals':'terminals.html','Financing':'financing.html','Agents':'agents.html','FAQ':'index.html#faq'}
PAGES={
 'index.html':dict(title='Cardworx Merchant Services | $0 Processing Fees, Cash Rewards, Wholesale Pricing',desc='Eliminate credit card processing fees with compliant Dual Pricing, earn monthly cash rewards, and get a free terminal. Wholesale merchant services in Boca Raton, FL.',
   sections=['HERO','SERVICES','INDUSTRIES','CALCULATOR','STATS','FAQ','CONTACT']),
 'terminals.html':dict(title='Terminals & POS | Clover, Valor, PAX, Dejavoo | Cardworx',desc='Free terminals with Dual Pricing. Clover, Valor PayTech, PAX, Dejavoo, Ingenico, SwipeSimple and virtual gateways at wholesale pricing.',
   sections=['TERMINALS','3D TERMINAL ASSEMBLY','CONTACT']),
 'savings.html':dict(title='Savings Calculator & Custom Pricing | Cardworx',desc='See what you give away in processing fees every year, and how Cardworx prices around the cards your business actually takes.',
   sections=['CALCULATOR','CUSTOM PRICING','STATS','CONTACT']),
 'dual-pricing.html':dict(title='Dual Pricing & Cash Discount | $0 Processing Fees | Cardworx',desc='Compliant Dual Pricing: post a cash price and a card price, eliminate your processing fees, and earn cash rewards every month.',
   sections=['DUAL PRICING','CALCULATOR','CONTACT']),
 'financing.html':dict(title='Business Financing & Customer Financing | Cardworx',desc='Equipment financing, expansion capital, working capital and debt financing for your business. Point of sale financing for your customers.',
   sections=['FINANCING','CONTACT']),
 'agents.html':dict(title='Become a Cardworx Agent | Residuals, Fast Onboarding',desc='Join the Cardworx agent program. Fast onboarding, residuals on every account, and a team that handles setup and support.',
   sections=['AGENTS','CONTACT']),
}
def nav(chrome):
    for k,v in NAV.items(): chrome=re.sub(r'<a href="#[a-z-]+">'+re.escape(k)+'</a>',f'<a href="{v}">{k}</a>',chrome)
    chrome=chrome.replace('<a class="logo" href="#top">','<a class="logo" href="index.html">').replace('href="#agents" class="btn btn-line">Become an agent','href="agents.html" class="btn btn-line">Become an agent')
    return chrome
for fn,cfg in PAGES.items():
    h=re.sub(r'<title>.*?</title>',f"<title>{cfg['title']}</title>",head,count=1,flags=re.S)
    h=re.sub(r'(<meta name="description" content=")[^"]*(")',lambda mo:mo.group(1)+cfg['desc']+mo.group(2),h,count=1)
    h=re.sub(r'(<link rel="canonical" href=")[^"]*(")',lambda mo:mo.group(1)+'https://www.cardworxusa.com/'+('' if fn=='index.html' else fn)+mo.group(2),h,count=1)
    secs=[parts[n] for n in cfg['sections']]
    if fn!='index.html': secs[0]=re.sub(r'<section ([^>]*?)class="([^"]*)"',r'<section \1class="\2 page-first"',secs[0],count=1) if 'class="' in secs[0].split('>')[0] else secs[0].replace('<section ','<section class="page-first" ',1)
    body='\n'.join(secs)
    # cross-page CTAs: agent buttons on home go to agents page; keep in-page anchors when the target exists
    ids=set(re.findall(r'id="([a-z0-9-]+)"',body))
    def fix(mo):
        tgt=mo.group(1)
        if tgt in ids: return mo.group(0)
        route={'services':'index.html#services','industries':'index.html#industries','dual':'dual-pricing.html','calc':'savings.html','terminals':'terminals.html','assemble':'terminals.html','financing':'financing.html','agents':'agents.html','faq':'index.html#faq','top':'index.html','merchant-form':'index.html#merchant-form','agent-form':'agents.html#agent-form'}
        return f'href="{route.get(tgt,"index.html")}"'
    body=re.sub(r'href="#([a-z0-9-]+)"',fix,body)
    foot=re.sub(r'href="#([a-z0-9-]+)"',fix,footer_and_scripts.split('<script',1)[0])+'<script'+footer_and_scripts.split('<script',1)[1]
    out=h+'<body>'+nav(chrome)+body+'\n'+foot
    open(fn,'w').write(out); print(fn,len(out))
