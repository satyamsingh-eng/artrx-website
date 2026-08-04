# ArtRX Website Audit & Complete Context Analysis

**Source Website:** [artrx.co](https://artrx.co/)  
**Scrape & Analysis Date:** August 4, 2026  
**Audited By:** C3A Labs Intelligence Engine  
**Target Workspace:** `/Users/satyyy/Desktop/Dr. Sushma (THANVI) Personal Website/`

---

## 📌 Executive Summary

This document contains the complete, deep-scraped content, structural architecture, team profiles, medical partner testimonials, and design system extracted directly from [artrx.co](https://artrx.co/). 

The website serves as the primary digital home for **ArtRX**, a youth-led healthcare initiative bringing art therapy illustration pads and creative programs to hospitalized children and senior citizens in nursing homes throughout New York.

---

## 👩‍🎨 Team & Founder Profiles (Scraped Data)

### 1. Thanvi Suvva — Founder
- **Role:** Founder & Youth Director
- **Bio & Background:**
  - Rising junior with a deep passion for the intersection of art and medical science.
  - Sensitive to the healing impact that art has on pediatric hospital patients and long-term care seniors.
  - Leads ArtRX outreach across hospitals and nursing homes throughout **New York**.
  - **Academic & Research Achievements:**
    - Cancer researcher at **Weill Cornell Medical Center** studying potential therapeutics for cancer immunotherapy.
    - Research on limb regeneration under the mentorship of **Professor Ay Birol at Harvard University** (pending publication).
    - Participant in **SARAS** (Science and Research Awareness Series) at **Stony Brook University**.
    - Manager of the **Jericho High School** Boys' Badminton Team.
    - **Gold Key Winner** in the Scholastic Art & Writing Competition.

### 2. Jiley Diego — Team Member & Artist
- **Role:** Student & Artist (Science & Art Outreach)
- **Bio & Background:**
  - Student artist focused on the intersection of art, medicine, and scientific innovation (gene editing, regenerative medicine, biotechnology).
  - Believes creative thinking is essential to scientific progress, healthcare discovery, and emotional healing.
  - Drives community outreach to bridge science and art for therapeutic impact.

---

## 🏥 Medical Partners & Contact Directory (Scraped Data)

### Testimonial from Medical Partner
> **"ArtRX brings an innovative and compassionate approach to mental health support. Their workshops have helped our participants reduce anxiety and discover new ways to communicate emotions."**
> 
> — **Dr. Venugopal**, Gastroenterologist at *Stars Surgical Suites*

### Listed Contact Directory
1. **Varnitha Baddam** — Internal Medicine
   - *Email:* `varnithareddy@gmail.com`
2. **Rajendra Chalasani** — Lead Engineer
   - *Email:* `chalasanirajendra@gmail.com`

---

## 📄 Complete Page-by-Page Content Breakdown

### Page 1: Home Page (`https://artrx.co/`)
- **Title:** `Art Therapy Services for Mental Wellness | ArtRX`
- **Meta Description:** *Unlock the healing power of art therapy at ArtRX. Join workshops for emotional growth and creativity to enhance your well-being today!*
- **Main Hero Headline:** `ART RX`
- **Hero Subtitle:** *Help children facing difficult medical circumstances reconnect with moments of happiness and hold onto a sense of hope for the future.*
- **Core Mission Statement:**
  > "The goal is to provide children facing difficult circumstances, as well as senior citizens in nursing homes, with opportunities for creativity, self-expression, and emotional comfort through art. Illustration pads offer a simple but meaningful way for children to draw, color, and express emotions that may be difficult to put into words. For older adults, engaging in artistic activities can promote relaxation and stimulate memory. This idea stood out to me because it showed how even a simple activity like drawing can have a meaningful impact on a child's emotional well-being. Seeing the joy and confidence that creative expression can inspire sparked a passion in me to pursue a project that uses art to support children, with the hope of helping them find comfort, resilience, and happiness despite the difficulties they may be facing."

---

### Page 2: About the Founder Page (`https://artrx.co/about-the-founder`)
- **Title:** `Art Therapy for Mental Wellness | ArtRX`
- **Meta Description:** *Discover ArtRX's journey in art therapy. Empower your mental health through creativity. Join our workshops for healing and personal growth.*
- **Headings:** `About the Founder`, `Thanvi Suvva`, `Our Team`, `Jiley Diego`.
- **Full Text Content:** (Includes complete profiles for Thanvi Suvva and Jiley Diego detailed in the Team section above).

---

### Page 3: Gallery Page (`https://artrx.co/gallery`)
- **Title:** `Book Art Therapy Appointments | ArtRX` *(Note: Meta title has a mismatch bug on GoDaddy)*
- **Meta Description:** *Easily book your personalized art therapy sessions with our licensed therapists...*
- **Hero Heading:** `Gallery`
- **Sub-heading:** `ArtRX Pads`
- **Asset Count:** Contains 15 image assets showcasing sketchpads, art pads, and outreach sessions.

---

### Page 4: Our Partners Page (`https://artrx.co/our-partners`)
- **Title:** `Art Therapy for Hospitals | ArtRX`
- **Meta Description:** *Discover how ArtRX enhances patient care in hospitals through art therapy. Partner with us for workshops and creative health solutions today!*
- **Main Section:** `What Our Medical Partners Are Saying About ArtRX`
- **Testimonial:** Dr. Venugopal (Stars Surgical Suites).
- **Directory Section:** `Contact Directory` listing Dr. Varnitha Baddam (Internal Medicine) and Rajendra Chalasani (Lead Engineer).

---

### Page 5: Contact Us Page (`https://artrx.co/contact-us`)
- **Title:** `Contact Us for Art Therapy | ArtRX`
- **Meta Description:** *Reach out to ArtRX for personalized inquiries about our art therapy services, workshops, and wellness programs. Connect today!*
- **Headings:** `Contact Us`, `Reach Out To Join the Team`, `Connect with ArtRX for Support and Inquiries`.
- **Primary Inquiry Email:** `artrx39@gmail.com`
- **Form Fields:** Name (*), Email (*), Message (*).

---

## 🎨 Design System & Technical Audit Specs

| Element | Scraped Spec / Value | Rebuild Recommendation |
| :--- | :--- | :--- |
| **Heading Font** | `Instrument Serif`, Georgia, serif | Keep serif style for elegance, or offer rounded sans-serif (`Outfit`). |
| **Body Font** | `Arimo`, system-ui, sans-serif | Use `Inter` or `Plus Jakarta Sans` for clean readability. |
| **Primary Color** | `#383C3B` (Soft Charcoal) | Upgrade to Sage Green (`#2E7D32`) or Calming Teal (`#008080`). |
| **Background** | `#F4EFE6` (Soft Warm Off-White) | `#FAFAFA` with subtle glassmorphic contrast. |
| **CMS Platform** | GoDaddy Website Builder / Muse | Rebuild with clean, fast static HTML/CSS (zero slow tracking scripts). |

---

## 🔍 Key QA Audit Findings & Improvements for Rebuild

1. **Meta Title Bug on Gallery Page:**
   - *Current Bug on `artrx.co/gallery`:* Page title says "Book Art Therapy Appointments", which sounds like a commercial therapy practice rather than a non-profit youth initiative.
   - *Fix:* Re-title to "ArtRX Gallery — Impact & Art Therapy Kits".

2. **Inconsistent Branding / Color Palette:**
   - *Current Issue:* Plain gray/charcoal with no warm accents.
   - *Fix:* Introduce warm accent colors (Sage Green / Coral) to highlight pediatric and senior care impact.

3. **Lack of Interactive Filtering in Gallery:**
   - *Current Issue:* Static list of images with no category tags.
   - *Fix:* Add category filters ("Art Kits", "Pediatric Visits", "Senior Care").

4. **Missing Direct Hospital List & Call-to-Action:**
   - *Current Issue:* Only 1 doctor testimonial and no direct call-to-action for hospitals to request art kits.
   - *Fix:* Add a structured "Request Art Kits for Your Facility" dropdown in the contact form.
