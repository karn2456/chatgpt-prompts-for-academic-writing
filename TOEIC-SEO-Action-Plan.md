# SEO Action Plan เจาะลึก — tciap.com
## เป้าหมาย: จาก Position 18.1 → Top 5 ใน 90 วัน
**อ้างอิงจาก: Search Console Data พ.ค. 2026 (Impressions 152, Clicks 0)**

---

## วิเคราะห์ปัญหาปัจจุบัน (Diagnosis)

### ข้อมูลจาก Search Console

```
สถานะ ณ พ.ค. 2026:
├── Impressions: 152 (+57% จากช่วงก่อน) → เว็บเริ่มถูก Index แต่...
├── Clicks: 0 → CTR = 0%
├── Avg. Position: 18.1 → หน้า 2 ของ Google
└── คำนิยาม: "เว็บมีศักยภาพแต่ยังมองไม่เห็นพอ"
```

### สาเหตุที่ Clicks = 0 แม้มี Impressions

| สาเหตุ | ความน่าจะเป็น | วิธีแก้ |
|--------|-------------|--------|
| Title Tag ไม่ดึงดูด | สูงมาก | Rewrite Titles ทุกหน้า |
| Position 18.1 ไกลเกินไป | สูงมาก | Push Top 10 ก่อน |
| AI Overview ดูดผู้ใช้ | สูง | AEO Optimization |
| Content ไม่ตรง Search Intent | กลาง | Intent Mapping |
| Technical Issues (Speed/Mobile) | กลาง | Technical Audit |

---

## Phase 1: Quick Fixes (วันที่ 1–7) ✅

### Day 1-2: Technical Audit

**เครื่องมือที่ต้องใช้:** Google Search Console + PageSpeed Insights + Screaming Frog Free

**Checklist Technical:**

```
✅ Core Web Vitals
   □ LCP (Largest Contentful Paint) < 2.5 วินาที
   □ FID (First Input Delay) < 100ms
   □ CLS (Cumulative Layout Shift) < 0.1

✅ Mobile-Friendliness
   □ ทดสอบทุกหน้าด้วย Google Mobile-Friendly Test
   □ Font ขนาดอ่านได้บน Mobile (ขั้นต่ำ 16px)
   □ ปุ่ม CTA ขนาดพอแตะได้ (ขั้นต่ำ 44x44px)

✅ Indexing
   □ ตรวจว่าทุกหน้าถูก Index (site:tciap.com ใน Google)
   □ XML Sitemap submit แล้วหรือยัง
   □ robots.txt ไม่ได้ Block หน้าสำคัญ

✅ HTTPS + Security
   □ SSL Certificate ยังไม่หมดอายุ
   □ ไม่มี Mixed Content (HTTP + HTTPS)
```

---

### Day 3-4: On-Page Title & Meta Overhaul

**Formula สำหรับ Title Tag ที่ดี:**
```
[Keyword หลัก] | [Benefit] | [Brand/Year]
ความยาว: 50-60 ตัวอักษร
```

**ก่อน → หลัง (ตัวอย่าง):**

| หน้า | Title เดิม (สมมติ) | Title ใหม่ (แนะนำ) |
|------|------------------|--------------------|
| Home | tciap.com | ติว TOEIC กรุงเทพ | ครู 25 ปี | tciap.com 2026 |
| คอร์สติว | คอร์สติว TOEIC | คอร์สติว TOEIC ออนไลน์ เริ่ม 990 บ | ผ่านชัวร์ |
| About | เกี่ยวกับเรา | ครู TOEIC 25 ปีประสบการณ์ | tciap.com |
| Blog | บทความ | เทคนิค TOEIC 2026 | Tips จากครูมืออาชีพ |

**Formula สำหรับ Meta Description:**
```
[ข้อดีหลัก 1] + [ข้อดีหลัก 2] + [CTA] (ความยาว 140-160 ตัวอักษร)

ตัวอย่าง:
"เรียนกับครู TOEIC 25 ปีที่มีผลลัพธ์พิสูจน์แล้ว คะแนนเฉลี่ยเพิ่ม 150 คะแนน
ใน 8 สัปดาห์ ทดลองเรียนฟรี 3 บทเรียน ไม่ต้องผูกมัด"
```

---

### Day 5-7: Schema Markup + Structured Data

**Schema ที่ต้องติดตั้งทันที:**

```json
1. Organization Schema (Homepage)
{
  "@type": "EducationalOrganization",
  "name": "tciap.com TOEIC Training",
  "description": "ติวสอบ TOEIC โดยครูประสบการณ์ 25+ ปี",
  "foundingDate": "[ปีก่อตั้ง]",
  "areaServed": "Thailand"
}

2. Course Schema (ทุกหน้าคอร์ส)
{
  "@type": "Course",
  "name": "[ชื่อคอร์ส]",
  "description": "[รายละเอียด]",
  "provider": {"@type": "Organization", "name": "tciap.com"},
  "offers": {
    "@type": "Offer",
    "price": "[ราคา]",
    "priceCurrency": "THB"
  }
}

3. FAQ Schema (ทุกหน้า Blog)
{
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "ค่าสอบ TOEIC 2026 เท่าไหร่?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "ค่าสอบ TOEIC (Listening & Reading) สำหรับบุคคลทั่วไปอยู่ที่ 1,800 บาท..."
      }
    }
  ]
}
```

---

## Phase 2: Content Optimization (วันที่ 8–30) 📝

### Keyword Research Matrix

**Priority 1: Low Competition + High Intent (โจมตีก่อน)**

| Keyword | Search Volume | Difficulty | Current Position | เป้าหมาย |
|---------|--------------|-----------|-----------------|---------|
| ติว TOEIC กรุงเทพ | Medium | Low-Mid | ไม่ทราบ | Top 3 |
| คอร์ส TOEIC ออนไลน์ ราคา | Medium | Low | ไม่ทราบ | Top 5 |
| TOEIC 700 เตรียมตัวอย่างไร | Medium | Low | ไม่ทราบ | Top 5 |
| ครู TOEIC กรุงเทพ | Low | Very Low | ไม่ทราบ | Top 3 |
| TOEIC score guarantee | Very Low | Very Low | ไม่ทราบ | Top 1 |

**Priority 2: Medium Competition (สร้าง Authority)**

| Keyword | Search Volume | Difficulty | Strategy |
|---------|--------------|-----------|---------|
| TOEIC คืออะไร | High | High | Long-form Guide |
| สมัครสอบ TOEIC | High | High | Process Guide + CTA |
| TOEIC 2026 | High | High | Evergreen + Update |
| ติว TOEIC ที่ไหนดี | Medium | Medium | Comparison + USP |

---

### Content Architecture (Pillar + Cluster Model)

```
PILLAR PAGE: "คู่มือ TOEIC 2026 ฉบับสมบูรณ์"
(Target: "TOEIC คืออะไร", "สอบ TOEIC 2026")
│
├── CLUSTER 1: การสอบ
│   ├── "ค่าสอบ TOEIC 2026 เท่าไหร่ สมัครยังไง"
│   ├── "ตารางสอบ TOEIC 2026 กรุงเทพและต่างจังหวัด"
│   └── "เอกสารที่ต้องนำไปสอบ TOEIC"
│
├── CLUSTER 2: การเตรียมสอบ
│   ├── "Timeline เตรียม TOEIC 30 วัน [Planner ฟรี]"
│   ├── "Timeline เตรียม TOEIC 60 วัน สำหรับมือใหม่"
│   └── "TOEIC Vocabulary 500 คำที่ออกสอบบ่อยสุด 2026"
│
├── CLUSTER 3: เทคนิค
│   ├── "เทคนิค TOEIC Listening ทุก Part อธิบายละเอียด"
│   ├── "เทคนิค TOEIC Reading Part 5-7 เจาะแต่ละ Type"
│   └── "ข้อผิดพลาดที่ทุกคนทำ TOEIC (จากครู 25 ปี)"
│
├── CLUSTER 4: คอร์สเรียน
│   ├── "คอร์สติว TOEIC ไหนดี 2026 เปรียบเทียบ"
│   ├── "เรียน TOEIC เองหรือเรียนกับครู ดีกว่ากัน?"
│   └── "คอร์ส TOEIC ออนไลน์ vs Onsite ต่างกันยังไง"
│
└── CLUSTER 5: Score & Career
    ├── "TOEIC Score ที่บริษัทไทยต้องการ 2026"
    ├── "TOEIC 650 vs 700 vs 785 ต่างกันยังไง"
    └── "TOEIC กับ IELTS ต่างกันยังไง ควรสอบอะไร"
```

---

### On-Page Optimization Checklist (ทุกบทความ)

```
✅ Keyword Optimization
   □ Primary Keyword ใน Title (ตำแหน่งแรก)
   □ Primary Keyword ใน H1
   □ Primary Keyword ใน Paragraph แรก (100 คำแรก)
   □ LSI Keywords กระจายทั่วบทความ
   □ Keyword ใน Image Alt Text

✅ Content Quality
   □ ความยาว: Pillar 2,500+ คำ | Cluster 1,200+ คำ
   □ มี H2, H3 ครอบคลุมทุก Subtopic
   □ มีรูปภาพหรือ Infographic อย่างน้อย 1 รูป
   □ มี Table หรือ List สำหรับ Featured Snippet
   □ ตอบ Search Intent ครบถ้วน

✅ Internal Linking
   □ Link ไป Pillar Page จากทุก Cluster
   □ Link ระหว่าง Cluster ที่เกี่ยวข้อง
   □ Link ไป CTA / Landing Page คอร์ส

✅ User Experience
   □ เวลาโหลดหน้า < 3 วินาที (Mobile)
   □ ย่อหน้าสั้น (ไม่เกิน 3-4 บรรทัด)
   □ มี Table of Contents สำหรับบทความยาว
   □ มี CTA อย่างน้อย 2 จุดต่อบทความ
```

---

## Phase 3: Authority Building (วันที่ 31–90) 🔗

### Link Building Strategy (เรียงตามลำดับความสำคัญ)

**Tier 1: Digital PR (Domain Authority สูง)**

| แหล่ง | แนวทาง | Timeline |
|------|--------|---------|
| Manager Online / ประชาชาติ | ส่ง Press Release "ครู TOEIC 25 ปี เปิด..." | สัปดาห์ 5-6 |
| Sanook Education | Guest Article เรื่อง TOEIC Trends 2026 | สัปดาห์ 6-7 |
| Kapook Education | Sponsored Content + Natural Backlink | สัปดาห์ 7-8 |

**Tier 2: Niche Education Sites**

| แหล่ง | แนวทาง |
|------|--------|
| Dek-D | Forum Response + Expert Q&A |
| Eduzones | Article Contribution |
| Pantip (ห้อง Education) | Q&A + แนบลิงก์ Resource |
| HRDC Thailand | Partner Page / Resource Link |

**Tier 3: Broken Link Building**

```
ขั้นตอน:
1. ใช้ Ahrefs/SEMrush หา Broken Links บนเว็บ TOEIC content
2. สร้าง Content ทดแทนที่ดีกว่า
3. ติดต่อเจ้าของเว็บเพื่อขอเปลี่ยน Link
```

**Tier 4: Resource Link (ฟรี + Passive)**

```
สร้าง Free Resources ที่คนอยากลิงก์มาให้:
□ "TOEIC Vocabulary Flashcard PDF 500 คำ" — ฟรี แลก Email
□ "TOEIC Score Calculator" — เครื่องมือออนไลน์ฟรี
□ "ตารางสอบ TOEIC 2026 ทุกรอบ" — Infographic ฟรี
□ "TOEIC Study Plan Template" — PDF ฟรี
```

---

### AEO (Answer Engine Optimization) — ตอบสนอง AI Overview

**หลักการ:** สร้าง Content ที่ Google AI ดึงไปแสดงใน AI Overview → ได้ Mention + Brand Traffic

**Format ที่ Google AI ชอบดึง:**

```
1. Concise Definition (50-100 คำ)
ตัวอย่าง:
"TOEIC (Test of English for International Communication) คือการทดสอบวัดระดับ
ทักษะภาษาอังกฤษเพื่อการสื่อสารในการทำงานระดับสากล พัฒนาโดย ETS ประเทศสหรัฐอเมริกา
คะแนนเต็ม 990 คะแนน แบ่งเป็น Listening 495 คะแนน และ Reading 495 คะแนน
ค่าสอบในประเทศไทย 1,800 บาท จัดสอบโดย CPA Thailand"

2. Step-by-Step Lists (สำหรับ How-to Queries)
ตัวอย่าง H2: "วิธีสมัครสอบ TOEIC 2026 ทำอย่างไร?"
ตามด้วย Numbered List 5-7 ขั้นตอนที่ชัดเจน

3. Comparison Tables (สำหรับ vs Queries)
"TOEIC vs IELTS" → ต้องมี Table เปรียบเทียบชัดเจน

4. Statistic + Source (สำหรับ Credibility)
ใส่สถิติที่มีแหล่งอ้างอิง → Google AI มักดึงตัวเลขจริง
```

---

## KPI Tracking Dashboard (90 วัน)

### เป้าหมาย Position ตาม Timeline

| Keyword | ปัจจุบัน | 30 วัน | 60 วัน | 90 วัน |
|---------|---------|--------|--------|--------|
| "ติว TOEIC กรุงเทพ" | ไม่ Top 20 | Top 15 | Top 10 | Top 5 |
| "คอร์ส TOEIC ออนไลน์" | ไม่ Top 20 | Top 12 | Top 8 | Top 5 |
| "TOEIC 700 เตรียมตัว" | ไม่ Top 20 | Top 10 | Top 5 | Top 3 |
| "TOEIC คืออะไร" | ~18.1 | Top 15 | Top 10 | Top 7 |
| "ครู TOEIC กรุงเทพ" | ไม่ทราบ | Top 5 | Top 3 | Top 1 |

### Metrics ที่ต้องดูทุกสัปดาห์

```
Search Console:
├── Total Impressions (เป้า: เพิ่ม 50%/เดือน)
├── Total Clicks (เป้า: จาก 0 → 50/วัน ใน 90 วัน)
├── Average CTR (เป้า: 3-5% เมื่อ Position Top 10)
└── Average Position (เป้า: < 10 สำหรับ 5 Keywords หลัก)

Google Analytics 4:
├── Organic Sessions
├── Bounce Rate (เป้า: < 60%)
├── Average Session Duration (เป้า: > 2 นาที)
└── Conversions (Form Submit / Line Click)
```

---

## เครื่องมือที่แนะนำ (Budget-Friendly)

| เครื่องมือ | การใช้งาน | ราคา |
|-----------|---------|------|
| Google Search Console | Tracking + เข้าใจ Query | ฟรี |
| Google Analytics 4 | Traffic Analysis | ฟรี |
| Google PageSpeed Insights | Core Web Vitals | ฟรี |
| Ubersuggest | Keyword Research | ฟรี (จำกัด) / $29/เดือน |
| Yoast SEO / RankMath | On-page (ถ้าใช้ WordPress) | ฟรี |
| Canva | สร้าง Infographic | ฟรี / $13/เดือน |
| Ahrefs Webmaster Tools | Backlink Check | ฟรี (จำกัด) |

---

## Checklist รายสัปดาห์ (SEO Maintenance)

```
ทุกสัปดาห์:
□ ดู Search Console: Clicks, Impressions, Position เปลี่ยนแปลงมั้ย?
□ ตรวจ Google Search: พิมพ์ Keywords หลัก ดูว่าเราอยู่ตรงไหน
□ เผยแพร่ Content อย่างน้อย 1 บทความ
□ ตอบ Comment / Question บน Social ที่เกี่ยวกับ TOEIC

ทุกเดือน:
□ อัปเดต Pillar Page ด้วยข้อมูลล่าสุด
□ ตรวจ Broken Links บนเว็บตัวเอง
□ ส่ง Link Building Outreach อย่างน้อย 5 Site
□ สรุป Top 10 Pages by Traffic → ดูว่า Optimize ต่อได้มั้ย
```

---

*แผนนี้ทบทวนทุก 30 วัน ปรับตาม Data จาก Search Console จริง*
