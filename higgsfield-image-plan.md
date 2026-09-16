# Cardworx Website: Higgsfield Image Plan (v2)

Every non-terminal image on the site, what it replaces, why it exists, and the exact prompt to generate it. Terminals stay as real manufacturer photos (never generated). The logo and the $0 badge stay as they are.

**What changed in v2**
1. **No text in any image.** Every screen and sign is generated blank. The words are placed in code on top of the photo (see Part 8), so they are always crisp, spelled right, and editable in seconds.
2. **Business types spread out.** The homepage now reads "anyone who takes cards": diner, boutique, salon, auto shop, jewelry, coffee bar, dental office, dispensary. No industry appears twice in the same section.
3. **New Industries section.** Eight tiles plus a catch-all, one photo each (Part 6).
4. **The four credit cards are dropped.** The 3D background cards are already painted in code with perfect chip, numbers and names, and photoreal reflections. Generating them would cost credits to get worse text. Only the two coins remain in Part 7.

---

## Part 1. The rules every image follows (the style bible)

Paste this block at the top of every prompt so everything looks like one photographer, one shoot.

**STYLE BIBLE (prefix for every prompt):**
> Ultra realistic editorial photograph, shot on a full frame camera with a 35mm or 50mm lens at f/2, shallow depth of field, natural skin texture with visible pores and slight imperfections, real fabric wrinkles, real fingerprints on glass and screens. Lighting: warm amber practical light from the scene (pendants, neon, window glow) mixed with a cool teal ambient fill in the shadows. Deep charcoal blacks, no crushed shadows. Modern South Florida small business setting. Diverse, everyday people, not models. No visible brand logos anywhere. Absolutely no text, letters, numbers or words anywhere in the image. Any screen is a plain dark glossy surface with a soft glow and no content. Any sign is blank. No glowing holograms, no floating icons, no futuristic UI overlays. It must look like a documentary photo, not a render.

**Why "no text":** AI image models still misspell and smear small type. Real HTML text over a blank screen is sharper than any render and can be changed without regenerating.

**Model:** GPT Image 2.5. **Cost:** every generation uses Higgsfield credits (about 490 on the Plus plan at last check). Exact credit cost is preflighted before anything is submitted.

---

## Part 2. Hero

### H1. Hero photo (screen text added in code)
- **File:** `assets/hero.jpg`   **Ratio:** 16:10
- **Business:** classic diner
- **Composition rule:** the terminal screen must face the camera at a mild angle (no more than about 20 degrees), fully visible, no hand, glare or reflection crossing it. The code overlay is aligned to that screen.
- **Prompt:**
> [STYLE BIBLE] Interior of a warm, busy classic South Florida diner at golden hour, chrome and red vinyl softly blurred. A smiling server in a black apron holds an unbranded modern handheld payment terminal toward a seated customer, who taps a dark credit card on the top of the device. The terminal screen faces the camera at a slight angle, a plain dark glossy rectangle with a faint glow and nothing on it. Focus on the hands, card and terminal. Candid, mid-action, genuine expressions.

### H2. Hero video (image-to-video from H1)
- **File:** `assets/hero.mp4`   5 seconds, loops
- **Prompt:**
> Subtle cinematic motion: the customer's hand slowly brings the card to the terminal and taps, the screen glow brightens softly, the server nods and smiles, gentle handheld camera drift, background diners move slightly, pendant lights flicker softly. The terminal screen stays blank. Slow, natural, no fast movement, seamless loop feel.

---

## Part 3. The six service panels

### S1. Dual Pricing
- **File:** `assets/svc-dual-pricing.jpg`   **Ratio:** 4:5   **Business:** boutique
- **Prompt:**
> [STYLE BIBLE] Overhead close-up of a marble boutique counter. A small blank clear acrylic countertop sign stands beside a neat stack of real US twenty dollar bills and one dark metal credit card. The edge of an unbranded terminal and a folded tissue-paper gift bag at the frame edge. Warm overhead light, teal reflection in the acrylic.

### S2. Card Processing
- **File:** `assets/svc-card-processing.jpg`   **Ratio:** 4:5   **Business:** salon
- **Prompt:**
> [STYLE BIBLE] A confident salon owner in her 40s stands at a sleek front desk in a bright modern hair salon, inserting a client's chip card into an unbranded countertop payment terminal. Styling chairs and mirrors softly blurred behind her, a client with fresh blowout smiling. Her hands and the terminal are sharp, the receipt is printing. Real, warm, professional.

### S3. Crypto Payments
- **File:** `assets/svc-crypto.jpg`   **Ratio:** 4:5   **Business:** coffee bar
- **Prompt:**
> [STYLE BIBLE] Close-up at a modern coffee bar counter. A customer holds a smartphone with its camera pointed at an unbranded countertop terminal whose screen shows only a large plain black and white QR code, nothing else. A small physical gold Bitcoin coin and a silver Ethereum coin rest on the counter beside a cortado. Steam from an espresso machine in the background, warm bar lighting, teal neon reflection on the counter.

### S4. Customer Financing
- **File:** `assets/svc-customer-financing.jpg`   **Ratio:** 4:5   **Business:** furniture showroom
- **Prompt:**
> [STYLE BIBLE] Inside a modern furniture showroom. A salesperson holds a tablet toward a young couple sitting on a grey sofa. The tablet screen shows only a large simple green checkmark on a dark background, no words. The couple lean in, genuinely smiling. Soft daylight from big windows, warm floor lamps, teal accent pillow. Focus on the couple's faces and the tablet.

### S5. Business Funding
- **File:** `assets/svc-business-funding.jpg`   **Ratio:** 4:5   **Business:** auto repair
- **Prompt:**
> [STYLE BIBLE] An auto repair shop owner in his 50s stands with arms crossed in a freshly expanded service bay: a brand new vehicle lift still wrapped in plastic, a technician in the background unboxing a tire machine, fresh epoxy floor reflecting warm shop lights, teal roll-up door open to Florida sun. Proud, calm expression. Documentary feel.

### S6. High Risk and Cannabis
- **File:** `assets/svc-high-risk.jpg`   **Ratio:** 4:5   **Business:** dispensary
- **Prompt:**
> [STYLE BIBLE] Interior of an upscale, clean, well-lit licensed cannabis dispensary. A budtender in a black polo behind a glass display counter completes a sale on an unbranded countertop terminal while a customer waits with a small unmarked paper bag. Glass jars blurred in the background with blank labels, wood and black metal fixtures, spot lighting. No cannabis leaf imagery, no smoke. Professional retail atmosphere.

---

## Part 4. Section images deeper on the page

### D1. Dual Pricing explainer photo (screen text can be added in code if needed)
- **File:** `assets/dual-pricing-register.jpg`   **Ratio:** 3:2   **Business:** mom and pop hardware store
- **Prompt:**
> [STYLE BIBLE] Medium close-up over a worn wooden hardware store counter. A customer holds a folded twenty dollar bill in one hand and a dark credit card in the other, looking at an unbranded terminal whose screen faces the camera, a plain dark glossy surface with a soft glow and nothing on it. The owner's hand rests on the counter, shelves of blurred hardware behind. Warm shop lighting, shallow focus on the screen and the two hands.

### D2. Dual Pricing countertop sign (text added in code)
- **File:** `assets/dual-pricing-sign.png`   **Ratio:** 4:5, then background removed
- **Composition rule:** shot nearly straight on, face of the sign fully visible, slight angle only.
- **Prompt:**
> Ultra realistic product photograph of a standing 5x7 inch clear acrylic countertop sign on a plain dark surface, shot nearly straight on with a very slight angle. The insert is a completely blank matte charcoal card with no printing of any kind. Subtle reflection in the acrylic, soft studio light with a faint teal edge highlight. Isolated on a plain dark background.

### F1. Equipment financing
- **File:** `assets/fin-equipment.jpg`   **Ratio:** 1:1   **Business:** restaurant kitchen
- **Prompt:**
> [STYLE BIBLE] A commercial kitchen at dawn. A chef runs her hand along a brand new stainless steel range, delivery straps still on the floor beside it. Warm light from the pass, cool light from a window. Focus on her hand and the new equipment.

### F2. Working capital
- **File:** `assets/fin-working-capital.jpg`   **Ratio:** 1:1   **Business:** retail stockroom
- **Prompt:**
> [STYLE BIBLE] A busy retail stockroom. A shop owner in her 30s checks a clipboard beside tall shelves freshly restocked with plain unmarked boxes, a delivery dolly still loaded behind her. Warm work lights, cool daylight from a loading door. Focus on her face and the full shelves. Momentum and confidence.

### F3. Expansion
- **File:** `assets/fin-expansion.jpg`   **Ratio:** 1:1
- **Prompt:**
> [STYLE BIBLE] A young business owner peeling protective film off the glass door of a brand new storefront, revealing a bright empty retail space inside ready for fixtures. Reflection of a palm-lined Florida street in the glass. Morning light. Hopeful, real.

### F4. Debt financing
- **File:** `assets/fin-debt.jpg`   **Ratio:** 1:1
- **Prompt:**
> [STYLE BIBLE] A relieved small business owner leaning back in her chair at a cluttered back-office desk, a closed laptop and a neat single folder in front of her, a stack of old paperwork pushed to the side. Late afternoon window light, warm lamp, genuine exhale of relief.

### A1. Agents and partners section
- **File:** `assets/partners.jpg`   **Ratio:** 4:3
- **Prompt:**
> [STYLE BIBLE] Outside a small Florida strip-mall storefront in warm late light. A well-dressed independent sales agent in his 30s shakes hands with a smiling shop owner in her 50s in front of her open door, blank awning above. His leather folio is under his arm. Palm trees and parked cars softly blurred. Candid, respectful, partnership energy.

### A2. Agent lifestyle
- **File:** `assets/agent-lifestyle.jpg`   **Ratio:** 4:3
- **Prompt:**
> [STYLE BIBLE] A sales agent sits at a sunny outdoor café table with a laptop open, angled slightly away from camera. The laptop screen shows only a dark interface with a single soft rising teal line chart, no words or numbers. A coffee and a phone beside the laptop. Relaxed, confident, looking off toward the street. Palm shadows across the table.

---

## Part 5. (removed) The four credit cards

Not generated. The background cards are painted in code with exact chip, numbers, names and wordmark, and already have studio reflections. Saves four generations plus four background removals.

---

## Part 6. Industries section (new)

Nine tiles: eight photos plus a text-only catch-all ("Don't see yours? If you take cards, we can help."). All the same size so no industry looks favored. Each tile shows the same moment, a card being tapped, in a different business, which is how the page says "we work with everyone."

All eight: **Ratio 4:3.**

### I1. Restaurants and diners
- **File:** `assets/ind-restaurants.jpg`
- **Prompt:**
> [STYLE BIBLE] A server at a lively bistro presents an unbranded handheld terminal tableside as a guest taps a card, plates and wine glasses in soft focus, pendant lights glowing warm, teal accent in the bar behind. Blank terminal screen.

### I2. Retail and boutiques
- **File:** `assets/ind-retail.jpg`
- **Prompt:**
> [STYLE BIBLE] A gift and home goods shop owner in her 60s rings up a customer at a wooden counter with an unbranded countertop terminal, wrapped parcel and candles beside it, shelves of ceramics blurred behind, window light. Blank terminal screen.

### I3. Salons and spas
- **File:** `assets/ind-salons.jpg`
- **Prompt:**
> [STYLE BIBLE] A barber in a modern barbershop holds an unbranded handheld terminal for a client in the chair who taps his phone to pay, fresh haircut, black leather chair, warm Edison bulbs, teal tiled wall. Blank terminal screen.

### I4. Auto repair and tire shops
- **File:** `assets/ind-auto.jpg`
- **Prompt:**
> [STYLE BIBLE] At an auto shop service counter, a mechanic in a grey work shirt hands car keys back to a customer who taps her card on an unbranded terminal, lifted car and tool chests softly blurred through the doorway, warm counter lamp, cool shop light. Blank terminal screen.

### I5. Jewelry and luxury goods
- **File:** `assets/ind-jewelry.jpg`
- **Prompt:**
> [STYLE BIBLE] A jeweler in a fine jewelry store presents a ring on a black velvet tray to a couple, an unbranded countertop terminal on the glass case beside it, spot lit cases sparkling in the background, warm amber light, teal reflection in the glass. Blank terminal screen.

### I6. Coffee and quick service
- **File:** `assets/ind-coffee.jpg`
- **Prompt:**
> [STYLE BIBLE] A barista slides an unbranded countertop terminal toward a customer who taps a card while holding a takeaway cup, espresso machine steaming, morning line blurred behind, warm wood counter, teal neon glow. Blank terminal screen.

### I7. Professional services
- **File:** `assets/ind-professional.jpg`
- **Prompt:**
> [STYLE BIBLE] A bright dental office front desk. A receptionist in scrubs turns an unbranded countertop terminal toward a patient who inserts a card, clean white counter, green plant, warm desk lamp, cool daylight from the waiting room. Blank terminal screen.

### I8. Cannabis and high risk
- **File:** `assets/ind-cannabis.jpg`
- **Prompt:**
> [STYLE BIBLE] Exterior evening shot of a clean modern licensed dispensary storefront with warm light spilling from the glass doors, a customer leaving with a small unmarked paper bag, blank sign above the door, palm trees, teal sky. No cannabis leaf imagery.

---

## Part 7. The 3D background: two crypto coins

Background removed after generation, then wrapped onto 3D coins that drift behind the page. Bitcoin and Ethereum only (both free to use).

### K1. Bitcoin coin
- **File:** `assets/coin-btc.png`   **Ratio:** 1:1
- **Prompt:**
> Ultra realistic product photograph of a physical gold Bitcoin collector coin, shot straight on, filling the frame, plain pure black background. Heavy machined brass-gold metal, the Bitcoin B symbol embossed in the center, fine reeded edge, subtle circuit-trace texture on the coin face, tiny scratches and real reflections. No lettering around the rim. Studio lighting with a warm key light and a cool teal rim.

### K2. Ethereum coin
- **File:** `assets/coin-eth.png`
- **Prompt:** same as K1 but: "brushed silver-platinum coin with the Ethereum diamond symbol embossed in the center."

---

## Part 8. How the text goes on in code

`index.html` now contains two overlay layers, hidden until the generated images are in place. Turn them on by changing the opening tag to `<html data-gen="1">`.

| Overlay | Sits on | What it shows | How it blends |
|---|---|---|---|
| `.ovl-screen` | the terminal screen in the hero (H1 / H2) | Cash price $42.00, Card price $43.68 | 3D rotated to the screen angle, `mix-blend-mode: screen`, soft glow, slow reflection sweep |
| `.ovl-sign` | the blank acrylic sign (D2) | "We offer two prices", Cash price / Card price, 3.99% service fee line | slight rotate to the insert, screen blend so it reads as printed |

Each overlay is positioned with CSS variables (`--x`, `--y`, `--w`, `--rx`, `--ry`, `--rz`). Once the real photo is in, aligning takes a minute of nudging those numbers. If a photo is ever swapped, retune the same numbers. Wording changes are plain text edits.

---

## Part 9. Summary count

| Group | Images | Notes |
|---|---|---|
| Hero | 1 photo + 1 video | video generated from the photo |
| Service panels | 6 | six different businesses |
| Dual Pricing section | 2 | blank screen + blank sign, text in code |
| Financing tiles | 4 | |
| Agents section | 2 | |
| Industries tiles | 8 | new section |
| Background coins | 2 | BTC and ETH; background removed |
| **Total** | **25 images + 1 video** | was 21 + 1; cards removed, industries added |

Kept as is: `logo-white.png`, `logo-dark.png`, `zero-fees-badge.png`, and all real terminal photos.

## Part 10. Order of work

1. Preflight the credit cost for the full batch and report the number.
2. Generate the hero first for approval, then Industries (the section that most defines the site's look), then services, then the rest.
3. Background removal on the sign and the two coins.
4. Align the two text overlays, flip `data-gen="1"`, wrap the coins onto the 3D background, hand over a new zip.
