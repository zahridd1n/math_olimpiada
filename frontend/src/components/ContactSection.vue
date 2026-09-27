<template>
  <section class="editorial-section contact-editorial-section">
    <div class="container">
      <div class="contact-editorial-layout">
        <!-- Left Side: Editorial Details -->
        <div class="contact-details-block">
          <div class="header-kicker">
            <span class="editorial-label">Aloqa & Manzil</span>
            <span class="editorial-tag">[ 05 ]</span>
          </div>

          <h2 class="contact-headline">
            Savollaringiz bormi? <span class="serif-italic-gold">Biz bilan</span> <span class="serif-italic">bog'laning</span>
          </h2>

          <p class="contact-intro">
            Olimpiada shartlari, tayyorgarlik yoki ro'yxatdan o'tish bo'yicha har qanday savolingiz bo'lsa, mutaxassislarimiz yordam berishga tayyor.
          </p>

          <div class="contact-rows-list">
            <div class="contact-editorial-row">
              <span class="contact-type-label">TELEFON</span>
              <div class="contact-row-val">
                <a :href="contact.phoneLink" class="val-link font-mono">{{ contact.phone }}</a>
                <span class="editorial-tag">[ 09:00 – 19:00 ]</span>
              </div>
            </div>

            <div class="contact-editorial-row">
              <span class="contact-type-label">TELEGRAM KANALI</span>
              <div class="contact-row-val">
                <a :href="social.telegram" target="_blank" rel="noopener" class="val-link">
                  @hackathon_school
                </a>
                <span class="editorial-tag">[ Rasmiy yangiliklar ]</span>
              </div>
            </div>

            <div class="contact-editorial-row">
              <span class="contact-type-label">MANZIL</span>
              <div class="contact-row-val">
                <p class="val-text">{{ contact.address }}, {{ contact.addressLine2 }}</p>
                <span class="editorial-tag">[ Farg'ona shahri ]</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Right Side: Clean Location Panel -->
        <div class="location-brief-panel">
          <div class="brief-card">
            <div class="brief-top">
              <span class="editorial-tag">[ BOSH BINO ]</span>
              <span class="editorial-tag">Hackathon IT School</span>
            </div>
            
            <h3 class="brief-title">Zamonaviy ta'lim muhitiga tashrif buyuring</h3>
            <p class="brief-desc">
              O'quv xonalari, kompyuter laboratoriyalari va robototexnika ustaxonalarimiz bilan bevosita tanishish uchun maktabimizga istalgan vaqtda kelishingiz mumkin.
            </p>

            <div class="brief-cta">
              <a :href="social.telegram" target="_blank" rel="noopener" class="btn-editorial-outline">
                <span>Telegram orqali xabar yozish</span>
                <span>→</span>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { siteConfig } from '../config/site.js'
const contact = siteConfig.contact
const social = siteConfig.social
</script>

<style scoped>
.contact-editorial-section {
  background-color: var(--bg-section-2);
  position: relative;
}

.contact-editorial-layout {
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  gap: 70px;
  align-items: start;
}

.header-kicker {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 20px;
}

.contact-headline {
  font-size: clamp(2.2rem, 3.8vw, 3.2rem);
  font-weight: 700;
  line-height: 1.15;
  letter-spacing: -0.03em;
  color: #ffffff;
  margin-bottom: 18px;
}

.contact-intro {
  font-size: 1.05rem;
  line-height: 1.7;
  color: var(--text-secondary);
  margin-bottom: 40px;
}

/* Rows */
.contact-rows-list {
  display: flex;
  flex-direction: column;
  border-top: 1px solid var(--border-subtle);
}

.contact-editorial-row {
  display: grid;
  grid-template-columns: 150px 1fr;
  align-items: baseline;
  gap: 20px;
  padding: 22px 0;
  border-bottom: 1px solid var(--border-subtle);
}

.contact-type-label {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--text-dim);
}

.contact-row-val {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 8px;
}

.val-link {
  color: #ffffff;
  font-size: 1.05rem;
  font-weight: 600;
  transition: color 0.2s ease;
}

.val-link:hover {
  color: var(--gold);
}

.val-text {
  color: #ffffff;
  font-size: 0.98rem;
  margin: 0;
}

/* Brief panel */
.location-brief-panel {
  display: flex;
  justify-content: flex-end;
}

.brief-card {
  background: rgba(255, 255, 255, 0.025);
  border: 1px solid var(--border-medium);
  border-radius: 14px;
  padding: 36px;
  width: 100%;
}

.brief-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-bottom: 20px;
  border-bottom: 1px solid var(--border-subtle);
  margin-bottom: 20px;
}

.brief-title {
  font-size: 1.25rem;
  font-weight: 700;
  color: #ffffff;
  line-height: 1.35;
  margin-bottom: 14px;
}

.brief-desc {
  font-size: 0.95rem;
  line-height: 1.65;
  color: var(--text-secondary);
  margin-bottom: 28px;
}

.brief-cta .btn-editorial-outline {
  width: 100%;
  justify-content: center;
}

@media (max-width: 992px) {
  .contact-editorial-layout {
    grid-template-columns: 1fr;
    gap: 48px;
  }
}

@media (max-width: 600px) {
  .contact-editorial-row {
    grid-template-columns: 1fr;
    gap: 6px;
  }
}
</style>
