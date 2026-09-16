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
NAV={'Solutions':'index.html#services','Industries':'industries.html','Dual Pricing':'dual-pricing.html','Savings':'savings.html','Terminals':'terminals.html','Financing':'financing.html','Agents':'agents.html','FAQ':'faq.html'}
PAGES={
 'index.html':dict(title='Cardworx Merchant Services | $0 Processing Fees, Cash Rewards, Wholesale Pricing',desc='Eliminate credit card processing fees with compliant Dual Pricing, earn monthly cash rewards, and get a free terminal. Wholesale merchant services in Boca Raton, FL.',
   sections=['HERO','SERVICES','CALCULATOR','STATS','CONTACT']),
 'industries.html':dict(title='Industries We Serve | Restaurants, Retail, Salons, Auto & More | Cardworx',desc='Cardworx serves any business that takes cards: restaurants, retail, salons, auto repair, jewelry, coffee, professional services, cannabis and high risk.',sections=['INDUSTRIES','CONTACT']),
 'faq.html':dict(title='FAQ | Dual Pricing, Fees, Terminals & Funding | Cardworx',desc='Answers to common questions about Dual Pricing, $0 processing fees, cash rewards, free terminals, next day funding and the Cardworx agent program.',sections=['FAQ','CONTACT']),
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

SOLUTIONS=[
 ('dual-pricing.html','Dual Pricing & Cash Rewards','Dual Pricing','$0 processing fees. Cash back every month.','Post a cash price and a card price. Card payers cover the processing cost inside their price, your fee goes to $0, and Cardworx pays you cash rewards on top. Legal, compliant, and reversible if it ever stops fitting your customers.',
  [('$0 processing','Your effective rate on card sales goes to zero. Fees are collected inside the card price, not from you.'),('Monthly cash rewards','A share of the program comes back to you every month, turning checkout into a profit center.'),('Compliant signage included','We ship the terminal programmed for Dual Pricing and the signage that keeps you compliant.'),('Switch back anytime','If Dual Pricing is not right for your customers, moving to standard pricing is easy.')],
  ['DUAL PRICING','CALCULATOR','CONTACT'],'Dual Pricing & Cash Discount | $0 Processing Fees | Cardworx','Compliant Dual Pricing: post a cash price and a card price, eliminate your processing fees, and earn cash rewards every month.'),
 ('card-processing.html','Credit Card Processing','Card processing','In store, online and mobile. Wholesale rates, no middleman.','Cardworx is a wholesale merchant services company. You get EMV, contactless, online and mobile acceptance on leading hardware, next day funding, 24/7 live support in English and Spanish, and reporting you can actually use.',
  [('Every way to get paid','Countertop, handheld, mobile readers, virtual terminal and gateway. One account, one statement.'),('Next day funding','Money in your bank the next business day, not sitting in someone else\'s float.'),('24/7 live support','Real people, English and Spanish, any hour. Not a ticket queue.'),('Real reporting','Sales, deposits, chargebacks and card mix in one place, so you know what you paid and why.')],
  ['TERMINALS','CONTACT'],'Credit Card Processing | Wholesale Merchant Services | Cardworx','Accept cards in store, online and on mobile with wholesale pricing, next day funding, free terminals and 24/7 bilingual support.'),
 ('crypto-payments.html','Crypto Payments','Crypto payments','Reach 575 million crypto consumers. Get paid in dollars.','Customers pay with the wallet they already use. You receive US dollars, converted instantly at the moment of sale and deposited to your bank daily. No wallet to manage, no exposure to price swings, nothing new to learn at the register.',
  [('Instant conversion','Every crypto sale settles to USD at the time of the transaction. You never hold crypto.'),('Daily bank deposits','Funds arrive in your account on a daily schedule alongside your card deposits.'),('Wallet agnostic','Works with the major wallets and coins your customers actually carry.'),('Zero volatility','The customer takes the price risk, not you. Your price is your price.')],
  ['CONTACT'],'Crypto Payments for Businesses | Instant USD Conversion | Cardworx','Accept cryptocurrency from 575M+ consumers and receive US dollars with instant conversion and daily bank deposits.'),
 ('customer-financing.html','Customer Financing','Lending platform','Sell payment over price.','Point of sale financing lets your customers say yes to larger purchases. Retail, healthcare, home improvement, auto and services: when a customer can pay over time, the average ticket goes up and you get paid in full up front.',
  [('Bigger tickets','Customers buy what they want instead of what fits in one payment.'),('You get paid now','The lender funds you in full. The customer repays the lender.'),('Fast decisions','Applications take minutes at the counter or online, with instant decisions on most.'),('Broad approvals','Options across the credit spectrum, so more customers qualify.')],
  ['FINANCING','CONTACT'],'Customer Financing & Point of Sale Lending | Cardworx','Offer point of sale financing so customers can pay over time. Bigger tickets, funded in full up front.'),
 ('business-funding.html','Business Funding','Business financing','Capital for the business you\'re building.','Equipment, expansion, working capital and debt consolidation, with fast decisioning and rates built on deep industry knowledge. Funding structured around your card volume, so payments move with your sales.',
  [('Equipment','Machines, vehicles, kitchens and terminals. Finance the tools that make money.'),('Expansion','A second location, a build out, a bigger space.'),('Working capital','Inventory, payroll and cash flow gaps, covered in days.'),('Debt financing','Consolidate and restructure what you owe into something you can live with.')],
  ['FINANCING','CONTACT'],'Business Funding | Equipment, Expansion & Working Capital | Cardworx','Fast business financing for equipment, expansion, working capital and debt, structured around your card sales.'),
 ('high-risk.html','High Risk & Cannabis','High risk','Every business deserves a fair chance to succeed.','Dispensaries, CBD, nutraceuticals, travel, subscription, adult, firearms and other categories that mainstream processors decline. Cardworx specializes in placing high risk merchants with stable banking and honest pricing.',
  [('Licensed cannabis','Compliant payment solutions for dispensaries and delivery.'),('Stable banking','Placements built to last, not accounts that get shut off in ninety days.'),('Honest pricing','High risk does not have to mean getting gouged. Wholesale rates apply here too.'),('Chargeback tools','Monitoring and dispute support that keeps your account healthy.')],
  ['CONTACT'],'High Risk Merchant Accounts & Cannabis Dispensary Processing | Cardworx','Specialized payment processing for cannabis dispensaries and high risk businesses that other providers turn away.'),
]
def sol_section(eb,h1,lead,cards):
    cs=''.join(f'<div class="glass" data-reveal><b>{b}</b><p>{t}</p></div>' for b,t in cards)
    return f'''<section class="sol page-first" data-theme="teal">
  <div class="wrap">
    <div class="sol-head"><div data-reveal><span class="eb">{eb}</span><h1 class="h2">{h1}</h1></div><p class="lead" data-reveal>{lead}</p></div>
    <div class="sol-grid">{cs}</div>
    <div class="cp-cta" data-reveal><a href="#merchant-form" class="btn btn-teal">Get a quote</a><a href="tel:+18883846450" class="btn btn-line">(888) 384-6450</a></div>
  </div>
</section>'''
for fn,name,eb,h1,lead,cards,secs,title,desc in SOLUTIONS:
    PAGES[fn]=dict(title=title,desc=desc,sections=secs,intro=sol_section(eb,h1,lead,cards))

def nav(chrome):
    for k,v in NAV.items(): chrome=re.sub(r'<a href="#[a-z-]+">'+re.escape(k)+'</a>',f'<a href="{v}">{k}</a>',chrome)
    dd='<div class="dd"><a href="dual-pricing.html">Solutions <i></i></a><div class="menu">'+''.join(f'<a href="{fn}">{nm}</a>' for fn,nm,*_ in SOLUTIONS)+'</div></div>'
    chrome=chrome.replace('<a href="index.html#services">Solutions</a>',dd)
    chrome=chrome.replace('<a class="logo" href="#top">','<a class="logo" href="index.html">').replace('href="#agents" class="btn btn-line">Become an agent','href="agents.html" class="btn btn-line">Become an agent')
    return chrome
for fn,cfg in PAGES.items():
    h=re.sub(r'<title>.*?</title>',f"<title>{cfg['title']}</title>",head,count=1,flags=re.S)
    h=re.sub(r'(<meta name="description" content=")[^"]*(")',lambda mo:mo.group(1)+cfg['desc']+mo.group(2),h,count=1)
    h=re.sub(r'(<link rel="canonical" href=")[^"]*(")',lambda mo:mo.group(1)+'https://www.cardworxusa.com/'+('' if fn=='index.html' else fn)+mo.group(2),h,count=1)
    secs=[parts[n] for n in cfg['sections']]
    if cfg.get('intro'): secs=[cfg['intro']]+secs
    elif fn!='index.html': secs[0]=re.sub(r'<section ([^>]*?)class="([^"]*)"',r'<section \1class="\2 page-first"',secs[0],count=1) if 'class="' in secs[0].split('>')[0] else secs[0].replace('<section ','<section class="page-first" ',1)
    body='\n'.join(secs)
    # cross-page CTAs: agent buttons on home go to agents page; keep in-page anchors when the target exists
    ids=set(re.findall(r'id="([a-z0-9-]+)"',body))
    def fix(mo):
        tgt=mo.group(1)
        if tgt in ids: return mo.group(0)
        route={'services':'index.html#services','industries':'industries.html','dual':'dual-pricing.html','calc':'savings.html','terminals':'terminals.html','assemble':'terminals.html','financing':'financing.html','agents':'agents.html','faq':'faq.html','top':'index.html','merchant-form':'index.html#merchant-form','agent-form':'agents.html#agent-form'}
        return f'href="{route.get(tgt,"index.html")}"'
    body=re.sub(r'href="#([a-z0-9-]+)"',fix,body)
    foot=re.sub(r'href="#([a-z0-9-]+)"',fix,footer_and_scripts.split('<script',1)[0])+'<script'+footer_and_scripts.split('<script',1)[1]
    out=h+'<body>'+nav(chrome)+body+'\n'+foot
    open(fn,'w').write(out); print(fn,len(out))
